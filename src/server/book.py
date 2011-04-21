#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        book.py
# Purpose:     Contains all Request Handlers pertaining to book request
#
# Author:      Andre Wiggins
#
# Created:     04/07/2011
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
import server
from google.appengine.ext import webapp
import parsers.retailers.halfdotcom as halfdotcom

class BookPage(webapp.RequestHandler):
    
    def get(self):
        self.response.out.write("BookPage")
    

class TextbookLookup(webapp.RequestHandler):
    
    def get(self):
        isbn = self.request.path.split('/')[-1]
        textbook = halfdotcom.lookup_isbn(isbn)
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(json.dumps(textbook.__dict__, indent=2, sort_keys=True))
    

class TextbookListingsLookup(webapp.RequestHandler):
    
    def get(self):
        retailer_name, isbn = self.request.path.split('/')[-2:]
        retailer = server.import_parser(retailer_name)
        
        jsonlistings = ''
        if retailer:
            listings = retailer.lookup_listings(isbn)
                 
            jsonlistings = '['
            for listing in listings:
                jsonlistings += json.dumps(listing.__dict__, indent=2, sort_keys=True)
                jsonlistings += ', '
            jsonlistings = jsonlistings[:-2] + ']'
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(jsonlistings)
        