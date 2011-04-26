#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        error.py
# Purpose:     Contains Request Handlers and functions to handle errors 
#              in requests
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
from google.appengine.ext.webapp import template

status_codes = {400: 'Bad Request',
                404: 'Not Found',
                500: 'Internal Server Error'} 

default_msgs = {400: 'The request has a syntax error. Please try again with correct syntax.',
                404: 'The requested page could not be found.',
                500: 'Sorry, an error occurred. Please try again later.'}

class ErrorHandler(webapp.RequestHandler):
    
    def get(self):
        requrl = self.request.url.rstrip('/')
        start = requrl.rfind('/error/') + len('/error/')
        code = int(requrl[start:start+3])
        msg = self.request.get('msg', default_msgs.get(code, "Error"))
        title = status_codes.get(code, "Error")
        
        values = {'title': title, 'msg': msg, 'code': code}
        html = template.render('../static/templates/error.html', values)
        
        self.error(code)
        self.response.out.write(html)