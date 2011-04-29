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