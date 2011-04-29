/**
 * This javascript file contains javascript methods pertaining to the getting,
 * processing, and outputing of SWAT Textbooks data.
 * 
 * Requires the util file: util.js
 */


/**
 * Requires the util file: util.js
 */
textbooklistings = {

    attrs: [],

    /**
     * Defines the order of conditions for when they are compared.
     */
    condition_order: { 'Brand New': 0, 
                       'Like New': 1, 
                       'Very Good': 2, 
                       'Good': 3, 
                       'Acceptable': 4},

    /**
     * The mapping of `textbooklistings` attributes to there comparing functions.
     * Only those attributes with special comparing functions that the default
     * comparator will not work correctly on, are defined.
     */
    cmp_mapping: {
        'condition': function(cond1, cond2) {
            var cond1_value = textbooklistings.condition_order[cond1];
            var cond2_value = textbooklistings.condition_order[cond2];
            
            return cond1_value - cond2_value;
        }
    },
    
    /**
     * Returns a function that will take two `textbooklisting` objects and compare
     * them on the attributes passed in as `attr`. This function automatically
     * handles the pasing in fo the cmp_mapping for the attributes with special
     * comparators.
     * 
     * @param attrs the attributes to compare two `textbooklisting` objects on.
     */
    cmp_factory: function(attrs) {
        this.attrs = util.get_attrs(attrs);
        
        return function(obj1, obj2) {
            return util.cmp_objs(obj1, obj2, textbooklistings.attrs, textbooklistings.cmp_mapping);
        };
    }
};

output = {

    textbook: function (textbook, container, highlight) {
        if (typeof(highlight) == 'undefined' || highlight == '')
            highlight = 'highlight';
        
        $(container).click( function() {
            window.location = $(this).find('a').attr('href');
            return false;
        }).addClass('clickable');

        imgdiv = $('<div />').addClass('cell')
                             .appendTo(container);
        
        $('<img />').addClass('bookimage top')
                    .attr('src', textbook.imageurl)
                    .appendTo(imgdiv);
        
        linkdiv = $('<div />').hover(function() {
            $(this).addClass(highlight);
        }, function() {
            $(this).removeClass(highlight);
        }).addClass('cell top')
          .appendTo(container);        
        
        $('<a />').attr('href', textbook.url)
                  .append(textbook.title)
                  .appendTo(linkdiv);
    }

};