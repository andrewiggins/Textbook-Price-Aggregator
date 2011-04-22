#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/parsers/schools directory)
# Purpose:     Contains useful classes and functions for all schools.
#
# Author(s):   Andre Wiggins
#
# Created:     02/02/2011
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

import os
import pkgutil


def available_schools():
    packages = pkgutil.walk_packages([__file__[:__file__.rfind(os.sep)]])
    return [pkginfo[1] for pkginfo in packages if not pkginfo[2]]


def main():
    print available_schools()
    

if __name__ == "__main__":
    main()