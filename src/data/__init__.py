#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/data/ package)
# Purpose:     Contains all data classes
#
# Author(s):   Andre Wiggins, Andrew Stewart
#
# Created:     03/27/2011
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

from textbook import Textbook, TextbookListing
from course import Course


def cmp_factory(attr):
    '''Return a function that compares two objects on attr'''
    f = lambda obj1, obj2: getattr(obj1, attr).__cmp__(getattr(obj2, attr))
    return f  


def main():
    pass

if __name__ == '__main__':
    main()