#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/parsers/schools directory)
# Purpose:     Contains useful classes and functions for all schools.
#
# Author:      Andre Wiggins
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


class Course():


    def __init__(self, dept, num, section=''):
        self.dept = dept
        self.num = num
        self.section = section

        if self.section:
            self.__title = "%s%s%s%s" % (dept.upper(),num,'s',section)
        else:
            self.__title = "%s%s" % (dept.upper(),num)


    def __cmp__(self, other):
        if self.dept.upper() < other.dept.upper():
            return -1
        elif self.dept.upper() > other.dept.upper():
            return 1
        else:
            if self.num < other.num:
                return -1
            elif self.num > other.num:
                return 1
            else:
                if self.section and other.section:
                    if self.section < other.section:
                        return -1
                    elif self.section > other.section:
                        return 1
                    else:
                        return 0
                else:
                    return 0


    def compare_attr(self, other, attr):
        if getattr(self, attr) < getattr(other, attr):
            return -1;
        elif getattr(self, attr) > getattr(other, attr):
            return 1;
        else:
            return 0;
            
            
    def __str__(self):
        return self.__title
    
    def __dict__(self):
        keys = [attr for attr in dir(self) if not attr.startswith('__')]
        values = [getattr(self, attr) for attr in keys]
        
        return dict(zip(keys,values))


class CourseList(list):
    
    
    def sort_courses(self, attr):
        for i in xrange(1, len(self)):
            for k in xrange(i, 0, -1):
                if self[k].compare_attr(self[k-1], attr) < 0:
                    self[k], self[k-1] = self[k-1], self[k]
                else:
                    break

    
    def find_class(self, **kwargs):
        toremove = CourseList()
        for course in self:
            for key, value in kwargs.items():
                if getattr(course, key) != value:
                    toremove.append(course)
        
        results = CourseList()
        for course in self:
            if course not in toremove:
                results.append(course)
        
        return results