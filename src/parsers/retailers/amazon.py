#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        amazon.py
# Purpose:     wrapper for using AWS offered by Amazon 
#
# Author(s):   Russell Jacob Marsh
#
# Created:     04/25/2011
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

from lib import ecs

class AmazonReq:
    def __init__(self):
        ecs.setLicenseKey('AKIAIHF4ICHMS5ME3LMQ')
        ecs.setSecretKey('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')
        ecs.setLocale('us')

    def lookupISBN(self, isbn):
        book = ecs.ItemSearch(isbn)
        return book
        
    def lookupTitle(self, title):
        book = ecs.ItemSearch(title, SearchIndex='Books')
        return book

if __name__ == "__main__":
  req = AmazonReq()
  book = req.lookupISBN("0393327795")
  for i in book:
    print i.Title
