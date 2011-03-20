#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        lsu.py
# Purpose:     Contains all parsing functions for Louisiana State University
#              Bookstore
#
# Author:      Andre Wiggins
#
# Created:     02/02/2011
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

import urllib2
import BeautifulSoup

def getTextbookSearchPage():
    url = r"http://lsu.bncollege.com/webapp/wcs/stores/servlet/BNCBHomePage?storeId=19057&catalogId=10001"
    data = ''
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT ' + 
                         '6.0; en-US; rv:1.9.0.11) Gecko/2009060215 ' + 
                         'Firefox/3.0.11 (.NET CLR 3.5.30729)'
                         }
    req = urllib2.Request(url, data, headers)
    
    res = urllib2.urlopen(req)
    html = res.read()
    print html
    print res.getcode(), res.geturl()
    soup = BeautifulSoup.BeautifulSoup(html)
    linkTags = soup.findAll('a')
    return linkTags

def main():
    print getTextbookSearchPage()

if __name__ == '__main__':
    main()