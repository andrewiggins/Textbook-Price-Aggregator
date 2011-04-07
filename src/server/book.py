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

from google.appengine.ext import webapp

class BookPage(webapp.RequestHandler):
    
    def get(self):
        self.response.out.write("BookPage")
    

class TextbookLookup(webapp.RequestHandler):
    
    def get(self):
        self.response.out.write("TextbookLookup")
    

class TextbookListingsLookup(webapp.RequestHandler):
    
    def get(self):
        self.response.out.write("TextbookListingsLookup")