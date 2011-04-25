#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/server/ package)
# Purpose:     Contains all code for serving webpages to clients
#
# Author(s):   Andre Wiggins
#
# Created:     04/02/2011
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

from google.appengine.dist import use_library
use_library('django', '1.2')

from book import BookPage, TextbookListingsLookup, TextbookLookup
from error import ErrorHandler
from retailers import Retailers
from schools import CourseLookup, CourseSearchPage
from search import SearchResultsPage, SearchRetailer

from django.utils import simplejson
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import parsers.schools
import parsers.retailers

class HomePage(webapp.RequestHandler):

    def get(self):
        path = '../static/templates/base.html'
        template_values = {}
        self.response.out.write(template.render(path, template_values, True))


def getjson(obj):
    return simplejson.dumps(obj, indent=2, sort_keys=True, 
                            default=lambda obj1: obj1.__dict__)


def main():
    run_wsgi_app(app)

isbn = '(?:[0-9Xx]+)'
opt_isbn = '(?:/'+isbn+')*' #optional ISBN
name = '(?:[a-z0-9\-]+)'
app = webapp.WSGIApplication([('/?', HomePage),
                              ('/retailers/?', Retailers),
                              ('/searchresults/?', SearchResultsPage),
                              ('/search/'+name, SearchRetailer),
                              ('/book'+opt_isbn+'/?', BookPage),
                              ('/textbook/'+isbn+'/?', TextbookLookup),
                              ('/textbooklistings/'+name+'/'+isbn+'/?', 
                               TextbookListingsLookup),
                              ('/coursesearch/'+name+'/?', CourseSearchPage),
                              ('/course/'+name+'/?', CourseLookup),
                              ('/.*', ErrorHandler)],
                              debug=True)


if __name__ == "__main__":
    main()