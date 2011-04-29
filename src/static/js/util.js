util = {
    
    /**
     * Formats a string or number to currency so only two decimal places are 
     * returned, rounding the number if more decimal places are provided.
     * @param amount the amount to format
     * @param unit (optional, default='') string to apply to the front of the 
     * amount as the unit symbol
     * @return the amount formated as currency
     */
    format_currency: function (amount, unit) {
        unit = (typeof(unit) == 'undefined') ? '' : unit;
        
        var num = parseFloat(amount);
        if(isNaN(num)) 
            num = 0.00;
        
        var minus = '';
        if(num < 0) 
            minus = '-';
        
        num = Math.abs(num);
        num = parseInt((num + .005) * 100);
        num = num / 100;
        
        s = new String(num);
        if(s.indexOf('.') < 0) 
            s += '.00';
        if(s.indexOf('.') == (s.length - 2))
            s += '0';
        s = unit + minus + s;
        return s;
    },
        
    /**
     * Returns the correct comparing function for an attribute if it exist
     * in the compare functions mapping. If it does not exist the default
     * compare function is used (util.cmp).
     * 
     * @param attr the attribute to find the comparator of
     * @param cmp_mapping a mapping of attribute names to the corresponding
     * comparing function
     * @return the correct comparator for the attribute `attr 
     */
    get_cmp: function (attr, cmp_mapping) {
        if (typeof(cmp_mapping) != 'undefined')
            return (typeof(cmp_mapping[attr]) != 'undefined') ? cmp_mapping[attr] : this.cmp;
        else
            return this.cmp;
    },

    /**
     * Compares two objects assuming one is undefined such that
     * defined < undefined so defined objects come first
     */
    cmp_undefined: function (a1, a2) {
        var is_a1_undef = (typeof(a1) == 'undefined');
        var is_a2_undef = (typeof(a2) == 'undefined');
        
        if (is_a1_undef && is_a2_undef)
            return 0;
        else if (is_a1_undef)
            return 1;
        else if (is_a2_undef)
            return -1;
        else
            throw "cmp_undefined called with 2 defined objects";
    },
    
    /**
     * The main function of the comparing utils. Returns a function that takes two 
     * objects and compares them on the attributes named in the passed in 
     * list, `attrs`
     * 
     * Example usage:
     * array = [object1, object2, ... ];
     * array.sort(util.cmp_factory(['attribute1', 'attribute2']));
     * 
     * @param attrs the attributes to compare objects on. (can be a list for
     * multiple attributes or a string for a single attribute)
     * @return a function that takes two objects and compares them on the 
     * specified attributes
     */
    attrs: [],
	cmp_factory: function (attrs) {
		this.attrs = this.get_attrs(attrs);
		
		return function(obj1, obj2) {
			return util.cmp_objs(obj1, obj2, util.attrs);
		};
	},

	/**
     * Prepares the `attrs` parameter of cmp_factory for use in cmp_objs.
     */
	get_attrs: function (attrs) {
	    if (typeof(attrs) == 'string')
            attrs = [attrs];
        else if (typeof(attrs) == 'undefined')
            attrs = [];
        else
            attrs = attrs;
	    
	    return attrs;
	},
	
	/**
     * The default comparator of two objects
     */
	cmp: function(a1, a2) {
	    if (a1 > a2)
            return 1;
        else if (a1 < a2)
            return -1;
        else
            return 0;
	},
	
	/**
     * The function that does the majority of the work for the util comparing 
     * functions.
     * 
     * @param obj1 the first object to compare
     * @param obj2 the second object ot compare
     * @param attrs the attributes to compare the objects on. Can be a list of
     * attribute, a string (a single attribute) or undefined, in which case it
     * will directly compare the two objects.
     * @param cmp_mapping (optional) a object that maps attribute names to 
     * their corresponding comparing function. Only objects that have special
     * comparing functions (such as the `condition` attribute of `textbooklistings`)
     * need to be specified in cmp_mapping. If an attribute name is not specified
     * in the cmp_mapping, then the default comparator is used.
     * @return positive number if obj1 > obj2, negative number if obj1 < obj2, or
     *  0 if obj2 == obj2
     */
	cmp_objs: function (obj1, obj2, attrs, cmp_mapping) 
	{
		var n = (attrs.length > 0) ? attrs.length : 1;
	    
	    for (var i = 0; i < n; i++) 
	    {
	        var a1 = (attrs.length == 0) ? obj1 : obj1[attrs[i]];
	    	var a2 = (attrs.length == 0) ? obj2 : obj2[attrs[i]];
	        
	        if ((typeof(a1) == 'undefined') || (typeof(a2) == 'undefined')) 
	        	var result = this.cmp_undefined(a1, a2);
	        else 
	            var result = this.get_cmp(attrs[i], cmp_mapping)(a1, a2);
	        
	        if ((result != 0) || (i == n-1))
                return result;
            else
                continue;
	        
	    }
	},

	/**
     * Test the comparing functions of the util library.
     */
	test_cmp: function () {
	    var obj1 = {'a': 1, 'b':2, 'c': 3, 'd':4}; 
	    var obj2 = {'a': 2, 'b':1, 'c': 3}; 
	    var obj3 = {'a':3, 'b': 0, 'c':5}; 
	    var a = [obj2, obj1, obj3];

	    var ans = [[obj1, obj2, obj3],
                   [obj3, obj2, obj1],
                   [obj1, obj2, obj3],
                   [obj1, obj3, obj2]];
	    
	    var tests = [['a'],
	                 'b',
	                 ['d', 'a'],
	                 ['d', 'b']];
	    
	    for (var i = 0; i < ans.length; i++) 
	    {
	        a.sort(util.cmp_factory(tests[i]));
	        if (!this.arrayobjs_equal(ans[i], a)) 
	            throw "Failed Test " + i.toString();
	        else
	            console.debug('Pass Test ' + i.toString());
	    }
	},
	
	/**
     * Compares two arrays of objects. Used in test_cmp.
     */
	arrayobjs_equal: function (arr1, arr2) {
	    var pass = true;
	    for (var i = 0; i < arr1.length; i++)
	    {
	        arr1_obj = arr1[i];
	        arr2_obj = arr2[i];
	        for (key in arr1_obj)
	            if (arr1_obj[key] != arr2_obj[key]) {
	                pass = false;
	                break;
	            }
            
            if (!pass)
                break;
	    }   
	    
	    return pass;
	}
};