(function($) {
    $.fn.confirm = function() {
        $(this).click(function(event) {
            return confirm($(this).attr("title"));
        });
    };
    
    $('#confirm').confirm();
})(jQuery);
