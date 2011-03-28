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

You can develop using whatever you want, but once you are done working on the 
module, if we could all have our files following the conventions we agree upon,
that would be great!

[PEP 8]: http://www.python.org/dev/peps/pep-0008/ "Python Conventions"
[PEP 257]: http://www.python.org/dev/peps/pep-0257/ "Python Docstrings"