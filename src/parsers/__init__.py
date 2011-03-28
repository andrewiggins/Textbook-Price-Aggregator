#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/parser/ directory)
# Purpose:     Contains general use parsing functions.
#
# Author:      Andre Wiggins
#
# Created:     03/21/2011
# Copyright:   (c) Andre Wiggins, Jacob Marsh, Andrew Stewart 2011
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


import BeautifulSoup


def parselinks(html):
    soup = BeautifulSoup.BeautifulSoup(html)
    linkTags = soup.findAll('a')
    links = {}
    for linkTag in linkTags:
        if linkTag.string:
            links[linkTag.string] = linkTag['href']
    return links