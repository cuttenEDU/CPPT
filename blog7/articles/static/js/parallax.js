$(document).ready(function () {
    var yPosition;
    var scrolled = 0;
    var $parallaxElements = $('.imgs img');
    var logo = $("#himg");
    console.log(logo)

    $(window).scroll(function () {
        scrolled = $(window).scrollTop();
        for (var i = 0; i < $parallaxElements.length; i++) {
            yPosition = (scrolled * 0.15 * (i + 1));
            $parallaxElements.eq(i).css({top: yPosition});
        }
        yPosition = (scrolled * 0.5);
        logo.css({top: yPosition});
        console.log('trying')
    });
});
