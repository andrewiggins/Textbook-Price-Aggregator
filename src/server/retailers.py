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

import json
import pkgutil
import parsers.retailers
from google.appengine.ext import webapp


class Retailers(webapp.RequestHandler):
    
    @staticmethod
    def retailers():
        packages = pkgutil.walk_packages(parsers.retailers.__path__)
        return [info[1] for info in packages if not info[2]]
    
    def get(self):
        self.response.out.write(json.dumps(Retailers.retailers())) 