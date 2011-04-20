#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        lsu.py
# Purpose:     Contains all parsing functions for Louisiana State University
#              Bookstore
#
# Author(s):   Andre Wiggins
#
# Created:     03/19/2011
# Copyright:   (c) Jacob Marsh, Andrew Stewart, Andre Wiggins 2011
# License:
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#-------------------------------------------------------------------------------


import string
import urllib
import urllib2
import traceback
import BeautifulSoup
import data


def get_terms():
    url = 'http://lsu.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&storeId=19057&langId=-1'
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.HTTPError:
        traceback.print_exc()
        print 'URL: %s' % url
        return {}
    soup = BeautifulSoup.BeautifulSoup(html)
    
    options = {}
    for option in soup.find('select').findAll('option'):
        if option['value']:
            options[option.string] = int(option['value'])
    
    return options


def get_options(term, dept='', course='', recur_count=0):
    url = 'http://lsu.bncollege.com/webapp/wcs/stores/servlet/TextBookProcessDropdownsCmd?campusId=17548053&termId=%s&deptId=%s&courseId=%s&sectionId=&storeId=19057&catalogId=10001&langId=-1&dojo.transport=xmlhttp&dojo.preventCache=1301120964177'
    url = url % tuple(map(urllib.quote, map(str, [term, dept, course])))
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.HTTPError as httperr:
        if httperr.getcode() == 403 and recur_count < 3:
            print "err: %s \nrecur_count: %s" % (str(httperr), recur_count)
            return get_options(term, dept, course, recur_count+1)
        else:
            print httperr.getcode()
            traceback.print_exc()
            print 'URL: %s' % url
            return {}
    soup = BeautifulSoup.BeautifulSoup(html)
    
    options = {}
    for option in soup.find('select').findAll('option'):
        if option['value']:
            value = prepare_value(option['value'])
            options[option.string.lower()] = int(value)
    
    return options


def prepare_value(value):
    removechars = string.letters + string.punctuation
    removechars_table = dict((ord(char), None) for char in removechars)
    
    return value.translate(removechars_table)


def get_textbooks_html(sectionids):
    #return open(r"C:\Users\Andre\Downloads\TBListView.htm").read()
    
    url = 'http://lsu.bncollege.com/webapp/wcs/stores/servlet/TBListView'
    data = {'storeId': 19057,
            'langId': -1,
            'catalogId': 10001,
            'savedListAdded': True,
            'viewName': 'TBWizardView',
            'mcEnabled': 'N',
            'numberOfCourseAlready': 0,
            'viewTextbooks.x': 62,
            'viewTextbooks.y': 18,
            'sectionList': 'newSectionNumber'}
    for i in xrange(len(sectionids)):
        data['section_'+str(i+1)] = sectionids[i]
    
    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    
    try:
        html = urllib2.urlopen(req).read()
    except urllib2.HTTPError:
        traceback.print_exc()
        print 'URL: %s' % url
        return ''
    
    return html 


def get_textbooks(sectionids):
    #should it take Course objects?
    
    #if nextSibling div has no class, it is textbook div
    #    each tbListHolding is a textbook
    #elif nextSibling div has class tbListHolding, it is
    #    parse special data
    #else
    #    not sure, leave
    soup = BeautifulSoup.BeautifulSoup(get_textbooks_html(sectionids))
    form = soup.find('form', {'name': 'courseListForm'})
    course_tags = form.findAll('div', {'class': 'sectionHeading'}) 
    
    for course_tag in course_tags:
        course_info = parse_class(str(course_tag))
        if course_info:
            print course_info
            
            book_tags = course_tag.nextSibling
            while str(type(book_tags)) != str(BeautifulSoup.Tag):
                book_tags = book_tags.nextSibling
            
            course_info.textbooks = []
            for book_tag in book_tags.findAll('div', {'class':'tbListHolding'}):
                course_info.textbooks.append(parse_book(str(book_tag)))
            
        
def parse_book(html):
    #FALL 2011 BIOL 1001s001
    #FALL 2011 AAAS 2000s001
    #SPRING 2011 ENGL 2025s002
    soup = BeautifulSoup.BeautifulSoup(html)
    book_info = {}
    
    heading, content = soup.findAll('div')[1:3]
    title, status = [li.findAll(text=True)[0] for li in heading.findAll('li')[1:]]
    book_info['title'] = urllib.unquote(title.strip())
    book_info['status'] = urllib.unquote(status.strip())
    print book_info['title'], book_info['status'] 
        
    text = [s.strip() for s in content.findAll(text=True) if s.strip() and s.find(':') == -1]
    book_info.update(zip(('author', 'edition', 'publisher', 'isbn13'), text[:4]))
    book_info['year'] = book_info['edition']
    print book_info['author'], book_info['edition'], book_info['publisher'], book_info['isbn13']
    
    listings = [s for s in text[6:] if s != 'if available']
    print listings
        
def parse_class(html):
    soup = BeautifulSoup.BeautifulSoup(html)
    
    if soup.find('div', {'class': 'optAccessories'}):
        return None
    
    li_tags = soup.find('ul').findAll('li')
    data_keys = ['semester', 'dept', 'course', 'section']
    class_info = {}
    for i in xrange(4):
        class_info[data_keys[i]] = li_tags[i].string
    
    ci = class_info
    return data.Course(ci['semester'], ci['dept'], ci['course'], ci['section'])
    

def test_options():
    terms = get_terms()
    term = terms.values()[0]
    print terms
    
    depts = get_options(term=term) 
    dept = depts.values()[0]
    print depts
    
    courses = get_options(term=term, dept=dept) 
    course = courses.values()[0]
    print courses
    
    print term, dept, course
    
    sections = get_options(term=term, dept=dept, course=course)
    print sections
    return sections


def test_get_available_courses(term, termid):
    """Return a list of courses that have textbooks listed for that semester."""
    courses = []
    depts = get_options(termid) 
    for dept, deptid in depts.items():
        nums = get_options(termid, deptid)
        for num, numid in nums.items():
            sections = get_options(termid, deptid, numid)
            for section, sectionid in sections.items():
                courses.append(data.Course(term, dept, num, section, sectionid))
    
    return courses


def main():
    sectionids = [46997808, 47221180, 45123192]
    get_textbooks(sectionids)
    

if __name__ == '__main__':
    main()