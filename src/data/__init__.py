#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/data/ package)
# Purpose:     Contains all data classes
#
# Author:      Andre Wiggins, Andrew Stewart
#
# Created:     03/27/2011
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

import json

class Textbook(object):
    
    attrs = ['title', 'author', 'publisher', 'date', 'edition', 'imageurl', 
             'synopsis', 'language', 'format','isbn', 'isbn13']
    
    def __init__(self, url, **kwargs):     
        self.url = url
        unusedattrs = Textbook.attrs[:]
        for key in kwargs:
            setattr(self, key, kwargs[key])
            if key in unusedattrs:
                unusedattrs.remove(key)
            
        for attr in unusedattrs:
            setattr(self, attr, '')
        

class TextbookListing(object):
    
    attrs = ['retailer', 'price', 'condition', 'isbn', 'isbn13']
    
    def __init__(self, url, **kwargs):
        self.url = url
        
        unusedattrs = Textbook.attrs[:]
        for key in kwargs:
            setattr(self, key, kwargs[key])
            if key in unusedattrs:
                unusedattrs.remove(key)
        

def main():
    from pprint import pprint
    
    tb_dict = {'title': 'Title','author': 'Author', 'publisher': 'Publisher', 
          'date': 'Date', 'edition': 'Edition', 'imageurl': 'ImageURL', 
          'synopsis': 'Synopsis', 'language': 'Language', 'format': 'Format',
          'isbn': '123456', 'isbn13': '7890'}
    tb = Textbook('url', **tb_dict)
    print json.dumps(tb.__dict__, sort_keys=True, indent=4)
    
    tl_dict = {'retailer': 'Retailer', 'price': 11.09, 'condition': 'Condition',
               'isbn': '12345', 'isbn13': '67890'}
    tl = TextbookListing('url', **tl_dict)
    pprint(tl.__dict__)


if __name__ == '__main__':
    main()