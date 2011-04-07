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

from retailers import Retailers
from search import SearchPage, SearchRetailer
from book import BookPage, TextbookLookup, TextbookListingsLookup

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):

    def get(self):
        self.response.out.write("HI THERE")


application = webapp.WSGIApplication([('/retailers', Retailers),
                                      ('/search', SearchPage),
                                      ('/search/[a-z0-9\-]+', SearchRetailer),
                                      ('/book', BookPage),
                                      ('/textbook', TextbookLookup),
                                      ('/textbooklistings/[a-z0-9\-]+', 
                                       TextbookListingsLookup),
                                      ('/.*', MainPage)],
                                     debug=True)


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()