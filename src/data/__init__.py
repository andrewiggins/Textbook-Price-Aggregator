#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/data/ package)
# Purpose:     Contains all data classes
#
# Author:      Andre Wiggins
#
# Created:     03/27/2011
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

import json

class Textbook(object):
    
    
    def __init__(self, isbn, isbn13, title='', author='', publisher='', date='',
                 edition='', imageurl='', synopsis='', language='', format=''):
        self.isbn = isbn
        self.isbn13 = isbn13
        self.title = title
        self.author = author
        self.publisher = publisher
        self.date = date
        self.edition = edition
        self.imageurl = imageurl
        self.synopsis = synopsis
        self.language = language
        self.format = format
    
    
    @staticmethod
    def from_dict(d):
        pass
    

class TextbookListing(object):
    pass


def main():
    pass


if __name__ == '__main__':
    from pprint import pprint
    
    t = Textbook(123456,7890,'Title','Author','Publisher','Date','Edition','ImageURL','Synopsis','Language','Format')
    pprint(t.__dict__)