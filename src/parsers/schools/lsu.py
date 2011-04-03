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


import sys
import string
import urllib
import urllib2
import traceback
import BeautifulSoup


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


def get_options(term, dept='', course=''):
    url = 'http://lsu.bncollege.com/webapp/wcs/stores/servlet/TextBookProcessDropdownsCmd?campusId=17548053&termId=%s&deptId=%s&courseId=%s&sectionId=&storeId=19057&catalogId=10001&langId=-1&dojo.transport=xmlhttp&dojo.preventCache=1301120964177'
    url = url % (term, dept, course)
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
            value = prepare_value(option['value'])
            options[option.string.lower()] = int(value)
    
    return options


def prepare_value(value):
    removechars = string.letters + string.punctuation
    removechars_table = dict((ord(char), None) for char in removechars)
    
    return value.translate(removechars_table)


def get_textbooks_html(sectionids):
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
    
    #if nextSibling div has no class, it is textbook div
    #    each tbListHolding is a textbook
    #elif nextSibling div has class tbListHolding, it is
    #    parse special data
    #else
    #    not sure, leave
    soup = BeautifulSoup.BeautifulSoup(get_textbooks_html(sectionids))
    form = soup.find('form', {'name': 'courseListForm'})
    class_tags = form.findAll('div', {'class': 'sectionHeading'})  
    
    for class_tag in class_tags:
        class_info = parse_class(str(class_tag))
        if class_info:
            print class_info
        
        
def parse_class(html):
    soup = BeautifulSoup.BeautifulSoup(html)
    
    if soup.find('div', {'class': 'optAccessories'}):
        return None
    
    li_tags = soup.find('ul').findAll('li')
    data_keys = ['semester', 'dept', 'course', 'section']
    class_info = {}
    for i in xrange(4):
        class_info[data_keys[i]] = li_tags[i].string
    
    return class_info
    

def test_classes():
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
    
    sectionids = [sections.values()[0], 46758415]


def main():
    sectionids = [46997808, 46758415]
    get_textbooks(sectionids)

if __name__ == '__main__':
    main()