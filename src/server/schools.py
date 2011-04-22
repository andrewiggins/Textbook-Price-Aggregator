#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        schools.py
# Purpose:     Contains all Request Handlers that pertain to school information
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


class CourseSearchPage(webapp.RequestHandler):
    '''Handles request to /coursesearch/school for a search of school courses'''
    
    def get(self):
        self.response.out.write("CourseSearchPage")
    

class CourseLookup(webapp.RequestHandler):
    '''Handles request to /course/school for specified course lookup'''
    
    def get(self):
        self.response.out.write("CourseLookup")
