Python Style Rules
==================

So here is a list of some Python conventions that I think we should follow for 
final submission. (See official document on python conventions, [PEP 8]. The
following styles are from that document.)

Python Code Style
-----------------

1. **Import** - Import modules on separate lines (just like in C/C++ you can't 
   #include multiple things on the same #include statement)
2. **Indentation** - Use *4 spaces* for indentation (Notepad++ has a really easy 
   built-in function that changes all tabs to the specified number of spaces)
3. **Documentation** - Use standard python docstrings, [PEP 257]

Python Naming Conventions
-------------------------
1. **Modules** - lowercase\_with\_underscores (No capital letters) (Use 
   underscores sparingly, only if it improves readability)
2. **Classes** - CapWords (Each word in name begins with a capital letter)
3. **Function/Method/Variable Names**: lowercase\_with\_underscores (Same as 
   modules, only use underscores if it improves readability)

File Conventions
-----------------------

### Test Code ###

Put all and any top-level test code under the following block of code:

`if __name__ == '__main__':`

It only runs the test code if the module is run as a top-level module and does
not run the code if the module is imported.

### Header ###

Example Header:

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

Notes:

1. First line is the shebang.
2. Put the name of the file for "Name".
3. For "Purpose", put a one sentence description of the purpose of the module.
4. For "Author(s)" list anyone who has edited the file. So if you have not 
   edited a file e.g. file1, your name will not be listed in file1's header. 
   Andrew helped me with the above file so I put his name in the header, this 
   way we know who has done what, etc.
5. Put the date the file was created for "Created".
6. For copyright, we will list everyone's name in alphabetical order and the 
   year (2011)
7. For license, just copy and paste the above.

Please fill out what you can of the header. I'll keep an eye out and try to 
make all the headers consistent.

You can develop using whatever you want, but once you are done working on the 
module, if we could all have our files following the conventions we agree upon,
that would be great!

[PEP 8]: http://www.python.org/dev/peps/pep-0008/ "Python Conventions"
[PEP 257]: http://www.python.org/dev/peps/pep-0257/ "Python Docstrings"