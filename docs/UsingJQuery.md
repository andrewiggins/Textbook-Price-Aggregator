Using jQuery
============

The following outlines the information learned by going through the 
[jQuery for Absolute Beginners Tutorial][tutorial].

Day 1 and 2
-----------
*Watch [Day 1] and [Day 2]*

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

####Display

*NOTE: the slide and fade functions do not remove an element, they just set the
css attribute `display` to `none`. You must remove it by calling [`remove()`][remove]
to fully remove it. Do this by passing in a second argument to the function. That
argument should be a function that calls [`remove()`][remove] on the tag. See
Day 13 code for example*

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

####Event

- [`.click(callback)`][click] - pass in a callback function for when the tag is 
                      clicked.

####Information

- [`.size()`][size] - returns the number of elements in an array. Note that selectors 
                      to `$` like `$('a')` return an array of `a` tags so [`.size()`][size]
                      on `$('a')` returns the number of 'a' tags in the DOM.

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
*Watch [Day 3]*

Use the [`.animate(attributes, speed)`][animate] function to animate a change in css 
attributes over a time. 

The `this` keyword references the tag that called the function when registered to
a tag's event.

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
*Watch [Day 4]*

Use the [`addClass('cssclass')`][addClass] and [`removeClass('cssclass')`][removeClass] 
functions to change a tag's css.
 
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
*Watch [Day 5]*

To create tags, or just add any html to a tag, [pass the desired html to the `$` function][jquery function 2] 
and call the [`.appendTo('tagselector')`][appendTo] passing in the tag you want to append the html to.

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
*Watch [Day 6]*

To have an event toggle a css class change call the [`.toggleClass('classname')`][toggleClass]
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

When animating an action on an event that has an on and off status, call the [`stop`][stop]
function so the events don't build up in the queue and delay each other. Try the 
[example code][Day 7] in your browser with and without calling [`stop`][stop].

###Example

    $(function() {
        $('#container img').animate({"opacity": .5});
        // set initial opacity to .5
        /* animate is a little more consistent across browsers when registering 
        opactiy than using the css function */
        
        $('#container img').hover(function() {
            $(this).stop().animate({"opacity": 1}); // put on one line if animating one property
        }, function (){
            $(this).stop().animate({"opacity": .5});
            /* stop() (stop animating) in case it is still in the process of doing 
            other animation b/c user is hovering on and off really quickly.*/
        });
    });

Day 8
-----
*Download [Day 8] code to run the example*

Today's lesson looks over a more in-depth example of the hover method. 
[Watch the video and download the code][Day 8] to see how it works.

One lesson learned here is when changing the position of a tag on an event like
[`hover`][hover] where there is an on/off status, do not run hover on the tag to be moved
because when the tag moves, it will initiate the [`hover`][hover] off action prematurely causing
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
            var org_size = $('p').css('font-size');
            // if only one paramter is provided, it returns the current value of the css value
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
*Watch [Day 10]*

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
instead of the tag you have the [mousemove] function on. [Watch and run the example][Day 11]
to understand

Day 12
------
*Download [Day 12] code to run the example*

Good review of how to do a hovering tooltip. Notable new things:

- Use the [Google Libraries API] to get jQuery. Faster load times and could possibly be cached from another
  website using it.
- Use the [`.append(html)`][append] function to append html to a tag.
- Use the [`.children(selector)`][children] function to select a child tag of a parent tag

Day 13
------
*Watch [Day 13] video to understand today's concepts*

Today goes over the first real AJAX function, [`ajax(settings)`][ajax], and it covers
basic form submitting using jQuery and AJAX. 

When submitting a form using AJAX instead of normal HTTP submission, be sure to
return false on the submit button click function so the page doesn't go to the
submission page. However, code the HTML of the page to work as if AJAX wasn't used
in case the user's browser does not support Javascript. Watch the video to see what
I am talking about. 

[`ajax()`][ajax] is called directly on [`$`][jquery function 1]. Then pass necessary 
settings to have the ajax work. Some common ones are outlined here:

- `url`: the URL of the AJAX request
- `type`: the method (usu. GET or POST, GET most likely for us) of the request
- `data`: any data used in the request (NOTE: this data is appended to the url and 
          sent as GET data, not POST (see [`param`][param] for turning a Javascript
          Object into a suitable HTTP Request string).
- `success`: the function to call on the success of the ajax request. The function 
             should take one parameter, which is the response of the request.
             
Also used often when dealing with form elements is the [`.val()`][val] function.
Read its [API page][val] for details on what it does. You can also use the following
to serialize a form's inputs into objects/strings to be submitted:

- [`.serialize()`][serialize] - Encode a set of form elements as a string for submission
- [`.serializeArray()`][serializeArray] - Encode a set of form elements as an array of names and values
             
###Example

    $(function() {
        $('#submit').click(function() {
            $('#container').append('<img src="img/loading.gif" alt="Currently Loading" id="loading" />');
            //the above creates the loading gif while the ajax runs
            
            var name = $('#name').val(); //Get the value of this input
            var email = $('#email').val();
            var comments = $('#comments').val();
            
            $.ajax({
                url: 'submit.php',
                type: 'POST',
                data: 'name=' + name + '&email=' + email + '&comments=' + comments,
                // the above mainly prepares the form data
                
                success: function(response) {
                    $('#response').remove('#response') // remove any previous response
                    $('#container').append('<p id="response">' + response + '</p>'); // add the new response
                    $('#loading').fadeOut(500, function(){ // fadeOut the loading gif
                        $(this).remove(); // fadeOut does not remove the element, just sets the css attr 'display' to 'none'
                    });
                }
            });
            
            return false; // if this click function runs, then the submit button does not need to submit itself
        });
    });

Day 14
------
*View [Day 14] video*

This lesson goes over how to utilize plugins and he goes through using the s3slider
plugin which creates a photo slideshow div in the html. Its a pretty cool plugin
and he goes through some CSS so check out the video if you want to see how it works

Day 15
------
*[Day 15] Part One video*

In part 1 of Day 15, the php to run the example is setup. No javascript is written.

In part 2 of Day 15, the javascript is written to change the style without having
to reload the page. What the AJAX of the script does is call a php script which sets
a cookie containing the style. It uses normal javascript to perform the changing
of css stylesheets. The javascript creates a page wide overlay div which darkens
the page while the ajax is working and the new css is loading. The verify_loaded_css
makes sure the css has loaded before removing the overlay div.

Some functions used/discussed:
 
- [`get`][get] - a shorthand for the [`ajax`][ajax] function. Use whichever you wish
                  however I believe for our purposes we will be using [`getJSON()`][getJSON]
- [`setTimeout(callback, milliseconds)`][setTimeout] - delays execution of javascript for the specified
                                           number of milliseconds then calls the callback
                                           function. Asychronous request still run.
                                           
Take note of the javascript object syntax used to define the verify_loaded_css object.

###Example

    $(function() {
        $('#container a').click(function() {
            $('<div id="overlay" />').appendTo('body').fadeIn('400'); //string or integer?

            $.ajax({
                type: 'GET',
                url: $(this).attr('href'), //this - the clicked tag
                data: 'js=1',

                success: function(response) {
                    $('#ss').attr('href', 'css/' + response + '.css');
                    verify_loaded_css.check(function() {
                        $('#overlay').fadeOut(400, function() {
                            $(this).remove();
                        });
                    });
                } // end success
            }); // ajax

            return false; // so the a tag doesn't reroute the user to switcher unless javascript is disabled
        }); // click

        // the following code allows us to wait to run code until the css page has loaded
        var verify_loaded_css = {
            init: function() {
                   $('<div id="test" />').appendTo('body');
            },
            
            check: function(runCallback) {
                if ($('#test').width() == 1) 
                    runCallback();
                else
                    setTimeout(function() {
                        verify_loaded_css.check(runCallback);
                    }, 300);
            }
        };
        
        verify_loaded_css.init();
    });

AJAX Overview
-------------

- [`.load`][load] function to load a part or whole webpage into a tag.
- Create a tag that has a `src` attribute and the browser will automatically fetch
  the required file
- Call [`.ajax`][ajax] to make a AJAX request

The following example uses [`getJSON()`][getJSON] to load a file `listings` and
output to the page. It uses [`each(data, function)`][each] to loop through both
the JSON array and JSON mapping.

###Example

Javascript:

    $(function () {
        $('#load').click(function() {
            $('<div id=overlay />').appendTo('body').hide().fadeIn(500);
            
            $.getJSON('listings', function(data) {
                output_json(data, 'div#json');
                
                $('#overlay').fadeOut(500, function() {
                    $(this).remove()
                });
            });
            
        }); // click
    }); // document ready
    
    function output_json(data, selector)
    {
        $(selector).append('<hr />');
        
        $.each(data, function(index, value) { // loop through array of mappings
            $('<dl id=' + index.toString() + ' />').appendTo(selector);
            
            $.each(value, function(key, value) { // loop through mapping
                var termhtml = '<dt>' + key + '</dt>\n';
                var defhtml = '<dd>' + value + '</dd>\n';
                $('dl#'+index).append(termhtml+defhtml);
            }); 
            
            $(selector).append('<hr/>');
        });
    }
    
JSON Data (`listings`):

    [{
        "condition": "Brand New",
        "isbn": "1584883936",
        "isbn13": "9781584883937",
        "price": 59.73,
        "retailer": "HalfDotCom",
        "url": "http://product.half.ebay.com/Galois-Theory-by-Ian-Stewart-2003-Paperback/2428211&tg=videtails&item=342098337890"
    }, {
        "condition": "Brand New",
        "isbn": "1584883936",
        "isbn13": "9781584883937",
        "price": 59.73,
        "retailer": "HalfDotCom",
        "url": "http://product.half.ebay.com/Galois-Theory-by-Ian-Stewart-2003-Paperback/2428211&tg=videtails&item=342097216122"
    }, {
        "condition": "Brand New",
        "isbn": "1584883936",
        "isbn13": "9781584883937",
        "price": 59.74,
        "retailer": "HalfDotCom",
        "url": "http://product.half.ebay.com/Galois-Theory-by-Ian-Stewart-2003-Paperback/2428211&tg=videtails&item=341567096920"
    }, {
        "condition": "Brand New",
        "isbn": "1584883936",
        "isbn13": "9781584883937",
        "price": 63.8,
        "retailer": "HalfDotCom",
        "url": "http://product.half.ebay.com/Galois-Theory-by-Ian-Stewart-2003-Paperback/2428211&tg=videtails&item=342072497170"
    }, {
        "condition": "Like New",
        "isbn": "1584883936",
        "isbn13": "9781584883937",
        "price": 55.25,
        "retailer": "HalfDotCom",
        "url": "http://product.half.ebay.com/Galois-Theory-by-Ian-Stewart-2003-Paperback/2428211&tg=videtails&item=341055437931"
    }]

Useful Functions
----------------

- [Ajax Helper Functions][ajax helpers]
- [Main AJAX Functions][ajax functions]. We will most likely use [`getJSON()`][getJSON].
- [`.each(data, function)`][each]

[addClass]: http://api.jquery.com/addClass "jQuery addClass"
[ajax functions]: http://api.jquery.com/category/ajax/shorthand-methods/ "jQuery AJAX Functions"
[ajax helpers]: http://api.jquery.com/category/ajax/helper-functions/ "jQuery Ajax Helpers"
[ajax]: http://api.jquery.com/jQuery.ajax/ "jQuery ajax"
[animate]: http://api.jquery.com/animate "jQuery animate"
[append]: http://api.jquery.com/append "jQuery append"
[appendTo]: http://api.jquery.com/appendTo "jQuery appendTo"
[attr]: http://api.jquery.com/attr "jQuery attr"
[attribute]: http://api.jquery.com/attribute-equals-selector/ "jQuery attribute Selector"
[children]: http://api.jquery.com/children "jQuery children"
[class selector]: http://api.jquery.com/class-selector/ "jQuery Class Selector"
[click]: http://api.jquery.com/click "jQuery click"
[css]: http://api.jquery.com/css/ "jQuery css"
[Day 1]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-video-series/ "Day 1"
[Day 2]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-2/ "Day 2"
[Day 3]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-3/ "Day 3"
[Day 4]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-4/ "Day 4"
[Day 5]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-5/ "Day 5"
[Day 6]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-6/ "Day 6"
[Day 7]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-7/ "Day 7"
[Day 8]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-8/ "Day 8"
[Day 9]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-9/ "Day 9"
[Day 10]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-10/ "Day 10"
[Day 11]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-11/ "Day 11"
[Day 12]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-12/ "Day 12"
[Day 13]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-13/ "Day 13"
[Day 14]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-14/ "Day 14"
[Day 15]: http://blog.themeforest.net/tutorials/jquery-for-absolute-beginners-day-15/ "Day 15"
[descendant selector]: http://api.jquery.com/descendant-selector/ "jQuery Descendant Selector"
[each]: http://api.jquery.com/each/ "jQuery each"
[element selector]: http://api.jquery.com/element-selector/ "jQuery Element Selector" 
[eq]: http://api.jquery.com/eq "jQuery eq Selector"
[even]: http://api.jquery.com/even-selector/ "jQuery even Selector"
[fading]: http://api.jquery.com/category/effects/fading/ "jQuery Fading Effect"
[first]: http://api.jquery.com/first-selector/ "jQuery first Selector"
[get]: http://api.jquery.com/jQuery.get/ "jQuery AJAX get"
[getJSON]: http://api.jquery.com/jQuery.getJSON/ "jQuery getJSON"
[Google Libraries API]: http://code.google.com/apis/libraries/ "Google Libraries API"
[hover]: http://api.jquery.com/hover "jQuery hover"
[id selector]: http://api.jquery.com/id-selector/ "jQuery ID Selector"
[jquery function 1]: http://api.jquery.com/jQuery/#jQuery1 "Main jQuery Function 1"
[jquery function 2]: http://api.jquery.com/jQuery/#jQuery2 "Main jQuery Function 2"
[jquery function 3]: http://api.jquery.com/jQuery/#jQuery3 "Main jQuery Function 3"
[last]: http://api.jquery.com/last-selector/ "jQuery last Selector"
[load]: http://api.jquery.com/load "jQuery load"
[mousemove]: http://api.jquery.com/mousemove "jQuery mousemove"
[nth-child]: http://api.jquery.com/nth-child-selector/ "jQuery nth-child Selector"
[param]: http://api.jquery.com/jQuery.param/ "jQuery param"
[parseFloat]: http://www.w3schools.com/jsref/jsref_parseFloat.asp "Javascript parseFloat"
[remove]: http://api.jquery.com/remove "jQuery remove"
[removeClass]: http://api.jquery.com/removeClass "jQuery removeClass"
[selectors]: http://api.jquery.com/category/selectors/ "jQuery Selectors"
[serialize]: http://api.jquery.com/serialize/ "jQuery serialize"
[serializeArray]: http://api.jquery.com/serializeArray/ "jQuery serializeArray"
[setTimeout]: http://www.w3schools.com/js/js_timing.asp "Javascript setTimeout"
[size]: http://api.jquery.com/size "jQuery size"
[slice]: http://api.jquery.com/slice "jQuery slice"
[sliding]: http://api.jquery.com/category/effects/sliding/ "jQuery Sliding Effects"
[stop]: http://api.jquery.com/stop "jQuery stop"
[toggleClass]: http://api.jquery.com/toggleClass "jQuery toggleClass"
[tutorial]: http://net.tutsplus.com/articles/web-roundups/jquery-for-absolute-beginners-video-series/ "jQuery for Absolute Beginners Tutorial"
[val]: http://api.jquery.com/val "jQuery val"
