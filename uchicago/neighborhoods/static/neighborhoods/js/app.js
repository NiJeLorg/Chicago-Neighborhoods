/*!
 * app.js: Javascript that controls the Chicago Neighborhoods public pages
 */

function app() {}

app.init = function () {

    // set up listeners
    app.createListeners();

}

app.collapseNavbar = function () {
    if ($(".navbar").offset().top > 30) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
        $(".intro").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
        $(".intro").removeClass("top-nav-collapse");
    }    
}


app.createListeners = function () {
    $(window).scroll(app.collapseNavbar);
    $(document).ready(app.collapseNavbar);

    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });

    $('.navbar-collapse ul li a').click(function() {
        $(this).closest('.collapse').collapse('toggle');
    });

}













