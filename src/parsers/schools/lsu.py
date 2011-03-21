#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        lsu.py
# Purpose:     Contains all parsing functions for Louisiana State University
#              Bookstore
#
# Author:      Andre Wiggins
#
# Created:     03/19/2011
# Copyright:   (c) Andre Wiggins, Jacob Marsh, Andrew Stewart 2011
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

import urllib
import urllib2
import cookielib
import BeautifulSoup
from pprint import pprint


def getAvailableClasses(path=None, data=None, cj=None, recursive=0):
    if not cj:
        cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    
    domain = r'http://lsu.bncollege.com'
    if not path:
        path = r'/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&storeId=19057&langId=-1'
    if not data:
        data = ''
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)'}
    req = urllib2.Request(domain + path, data, headers)
    
    res = opener.open(req)
    html = res.read()
    
    soup = BeautifulSoup.BeautifulSoup(html)
    select = soup.find('select', title="Select Term")
    if select:
        print select
        
    else:
        if recursive > 3:
            print 'Recursive Inf Loop'
            return None
        
        script = soup.find('script').string
        print script
        
        path = soup.find('form')['action']
        data = build_post_string(soup)
        print data
        
        return getAvailableClasses(path, data, cj, recursive+1)


def build_post_string(soup):
    postdata = {}
    inputs = soup.findAll('input')
    for input in inputs:
        postdata[input['name']] = input['value']
    return urllib.urlencode(postdata)


def getTextbooks(courses):
    pass


def main():
    getAvailableClasses()


if __name__ == '__main__':
    main()