Using jQuery
============

The following outlines the information learned by going through the 
[jQuery for Absolute Beginners Tutorial][tutorial].

Day 1 and 2
-----------

Embed code into the following to ensure it does not run until the page is 
completely loaded. See official documentation [here][jquery function 3]

    $(function() {
        //code here
    });
    
To find a tag in the DOM, use the [`$` "function"][jquery function 1]. It is jQuery's identifier.
It uses CSS syntax to find tags as follows: 

*To view all jQuery selector patterns, click [here][selectors]*

- [`$('a')`][element selector] - returns all `a` tags
- [`$('p a')`][descendant selector] - returns all `a` tags that is within a `p` tag
- [`$('.box')`][class selector] - returns all tags with a `class` of `box`
- [`$('#box')`][id selector] - returns all tags with an `id` of `box`
- [`$('ul#nav')`][id selector] - returns all `ul` tags with an `id` of `nav`. 
        This combines an element selector and an id selector.

Tags have the following functions:

Display

- [`.slideDown(speed)`, `slideUp(speed)`][sliding] - functions that hide/show a tag by
            sliding up/down the contents of the tag at the specified speed
    - `speed` can be a number in  milliseconds, 'slow', 'normal', or 'fast'
- [`.fadeIn(speed)`, `fadeOut(speed)`][fading] - functions that hide/show a tag by
            fading the contents of the tag in/out at the specified speed
    - `speed` same can be the same
- [`.css('attribute', 'value')`][css] - sets the css attribute to the specified value. 
            Should be used sparingly. All css should be in .css files and 
            instead use the `addClass('classname')` function to change the 
            css of a tag.

Event

- [`.click(callback)`][click] - pass in a callback function for when the tag is 
                      clicked.

Information

- [`.size()`][size] - returns the number of elements in an array. calls for tags to `$`
             like `$('a')` return an array of `a` tags

###Example

    $(function() {
        $('a').click(function() {
            $('.box').slideDown('normal');
            $('p a').css('color', 'blue');
            // fadeIn, fadeOut, slideUp, slideDown
        });
    });
    
Day 3
-----

Use the [`.animate(attributes, speed)`][animate] function to animate a change in css 
attributes over a time. 

###Example

    $(function() {
        $('#box').click(function() {
            
            //'this' keyword gets event's tag, which is #box in this case
            /*$(this).animate({
                "width": "50px", 
                "left": "50px"}, 4000);
            */ // they run at the same time. not exactly what we want
            // if animating more than property, put each on its own line
            
            $(this).animate({"left": "300px"}, 4000); // time for animation to occur
            $(this).animate({"width": "50px"}, 4000); // if animating on property, put on one line
        });
    });
    
Day 4
-----

Use the [`addClass('cssclass')`][addClass] and [`removeClass('cssclass')`][removeClass] 
functions to change a tags css.
 
 jQuery provides the following conventions to selecting tags:
 
 *To view all jQuery selector patterns, click [here][selectors]*
 
- [`$('li:first')`][first] - select first item in li tag
- [`$('li:last')`][last] - select last item in li tag
- [`$('li:even')`][even] - select the even items in the li tag  
- [`$('li:nth-child(4)')`][nth-child] - selects the 4th list item (1-based array)
- [`$('li:eq(4)')`][eq] - selects the item with index of 4 in a 0-based array
- [`$('li a[title=title]')`][attribute] - anchor tag under li tag with attribute title = title

Day 5
-----

To create tags, or just add any html to a tag, pass the desired html to the 
[`$` function][jquery function 2] and call the [`.appendTo('tagidentifier)`][appendTo] 
on the tag you want to append the html to.

To remove an tag, call [`.remove()`][remove] on the tag.

###Example

    $(function(){
        var i = $('ul#nav li').size();
        alert(i);
        
        $('a#add').click(function() {
            i++;
            $('<li>' + i + '</li>').appendTo('ul#nav'); //appendTo puts inside the tag
        });
        
        $('a#remove').click(function() {
            $('ul#nav li:last').remove();
            i--;
        });
    });
    
Day 6
-----

To have an event toggle a class change call the [`.toggleClass('classname')`][toggleClass]
within the event you want to toggle. See the example below.

###Example

    $(function() {
        $('a').click(function() {
            //$('#box').toggle());
            $('#box').toggleClass('border');
        });
    
        $('p').click(function() {
            $(this).toggleClass('highlight');
        });
    });

Day 7
-----
*Download [Day 7] code to run this example*

The [`.hover(on_callback, off_callback)`][hover] function performs an action when the 
mouse hovers on and/or off a tag. The first argument to [`hover`][hover] is a function 
to call when the mouse hovers on a tag. The second optional argument to [`hover`][hover]
is a function to call when the mouse hover off a tag.

When animating an action on an event that has a on and off status, call the [`stop`][stop]
function so the events don't build up in the queue and delay each other. Try the 
[example code][Day 7] in your browser with and without calling [`stop`][stop].

###Example

    $(function() {
        $('#container img').animate({"opacity": .5});
        // set initial opacity to .5
        // animate is a little more consistent across browsers when registering opactiy than using the css function
        
        $('#container img').hover(function() {
            $(this).stop().animate({"opacity": 1}); // put on one line if animating one property
        }, function (){
            $(this).stop().animate({"opacity": .5});
            // stop() (stop animating) in case it is still in the process of doing other animation b/c user is hovering on and off really quickly.
        });
    });

Day 8
-----
*Download [Day 8] code to run the example*

Today's lesson looks over a more in-depth example of the hover method. Watch the
video and download the code to see how it works.

One lesson learned here is when changing the position of a tag on an event like
[`hover`][hover] where there is an on/off status, do not run hover on the tag to be moved
as when the tag moves, it will initiate the [`hover`][hover] off action prematurely causing
a flicker effect. Watch the [video][Day 8] for illustrated example. 

Day 9
-----
*Download [Day 9] code to run the example*

Calling the [`.css(attribute)`][css] with one parameter returns the current value of that
attribute. 

The [`parseFloat(str, base)`][parseFloat] parses a string as a float in the given base.

The [`.slice(start, end)`][slice] function takes two agruments: `start` and
the optional `end`. Agruments may be negative meaning the index starts from the end.

Check the [exmaple code][Day 9] for a simple example using these functions

###Example

    $(function() {
        $('a').click(function () {
            var org_size = $('p').css('font-size'); // if only one paramter is provided, it returns the current value of the css value
            console.log(org_size);
            
            var unit_meas = org_size.slice(-2); // grab last 2 chars of size string which is the units
            console.log(unit_meas);
            
            var num = parseFloat(org_size, 10);
            console.log(num);
            
            if (this.id == 'larger') {
                $('p').css('font-size', num*1.4 + unit_meas);
            } else {
                $('p').css('font-size', num/1.4 + unit_meas);
            }
        
        });
    });
    
Day 10
------ 

Use the [`.load(url, callback)`][load] function to load the whole or part of a webpage into
a tag. See the example code below which loads `#movies` part of a webpage `data.html`
into a created div tag, and hides it and slides it down to show it.

###Example

    $(function () {
        $('a').click(function() {
            $('<div id="info" />').load('data.html #movies', function() {
                $(this).hide() // hidden so we can slide it down
                       .appendTo('#container')
                       .slideDown(1000);
            });
            
            return false; // so default action doesn't happen which is to send it to the data.html page
        });
    });

Day 11
------
*Download [Day 11] code to run the example*

Use the [`.attr('attribute name')`][attr] to get the value of an attribute of a tag
or to set it, passing the value you want to attribute to be as the second argument.

The [`.mousemove(callback)`][mousemove] function to run a function each time the
mouse moves on the tag. Be wary about placing something on the current mouse position.
It will flicker as the mouse will move to be on the tag you create on the mouse position
instead of the tag you have the [mousemove] function on. Watch and run the example
to understand

Useful Functions
----------------

- [Ajax Helper Functions][ajax helpers]
- [Main AJAX Functions][ajax functions]. We will most likely use [`.getJSON()`][getJSON].
- [`.each(function)`][each]

[tutorial]: http://net.tutsplus.com/articles/web-roundups/jquery-for-absolute-beginners-video-series/ "jQuery for Absolute Beginners Tutorial"

[Day 7]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-7/ "Day 7"
[Day 8]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-8/ "Day 8"
[Day 9]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-9/ "Day 9"
[Day 11]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-11/ "Day 11"

[jquery function 1]: http://api.jquery.com/jQuery/#jQuery1 "Main jQuery Function 1"
[jquery function 2]: http://api.jquery.com/jQuery/#jQuery2 "Main jQuery Function 2"
[jquery function 3]: http://api.jquery.com/jQuery/#jQuery3 "Main jQuery Function 3"

[slice]: http://api.jquery.com/slice "jQuery slice"
[load]: http://api.jquery.com/load "jQuery load"
[mousemove]: http://api.jquery.com/mousemove "jQuery mousemove"
[attr]: http://api.jquery.com/attr "jQuery attr"
[selectors]: http://api.jquery.com/category/selectors/ "jQuery Selectors"
[each]: http://api.jquery.com/each/ "jQuery each"
[ajax helpers]: http://api.jquery.com/category/ajax/helper-functions/ "jQuery Ajax Helpers"
[ajax functions]: http://api.jquery.com/category/ajax/shorthand-methods/ "jQuery AJAX Functions"
[getJSON]: http://api.jquery.com/jQuery.getJSON/ "jQuery getJSON"
[sliding]: http://api.jquery.com/category/effects/sliding/ "jQuery Sliding Effects"
[fading]: http://api.jquery.com/category/effects/fading/ "jQuery Fading Effect"
[css]: http://api.jquery.com/css/ "jQuery css"
[size]: http://api.jquery.com/size "jQuery size"
[click]: http://api.jquery.com/click "jQuery click"
[animate]: http://api.jquery.com/animate "jQuery animate"
[addClass]: http://api.jquery.com/addClass "jQuery addClass"
[removeClass]: http://api.jquery.com/removeClass "jQuery removeClass"
[appendTo]: http://api.jquery.com/appendTo "jQuery appendTo"
[remove]: http://api.jquery.com/remove "jQuery remove"
[toggleClass]: http://api.jquery.com/toggleClass "jQuery toggleClass"
[hover]: http://api.jquery.com/hover "jQuery hover"
[stop]: http://api.jquery.com/stop "jQuery stop"
[parseFloat]: http://www.w3schools.com/jsref/jsref_parseFloat.asp "Javascript parseFloat"

[first]: http://api.jquery.com/first-selector/ "jQuery first Selector"
[last]: http://api.jquery.com/last-selector/ "jQuery last Selector"
[even]: http://api.jquery.com/even-selector/ "jQuery even Selector"
[nth-child]: http://api.jquery.com/nth-child-selector/ "jQuery nth-child Selector"
[eq]: http://api.jquery.com/eq "jQuery eq Selector"
[attribute]: http://api.jquery.com/attribute-equals-selector/ "jQuery attribute Selector"

[element selector]: http://api.jquery.com/element-selector/ "jQuery Element Selector" 
[descendant selector]: http://api.jquery.com/descendant-selector/ "jQuery Descendant Selector"
[class selector]: http://api.jquery.com/class-selector/ "jQuery Class Selector"
[id selector]: http://api.jquery.com/id-selector/ "jQuery ID Selector"