#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        vendors.py
# Purpose:     Contains all Request Handlers pertaining to retailers
#
# Author:      Andre Wiggins, Andrew Stewart
#
# Created:     04/7/2011
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

import server
from google.appengine.ext import webapp
from parsers.retailers import available_retailers


class Retailers(webapp.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(server.getjson(available_retailers()))
