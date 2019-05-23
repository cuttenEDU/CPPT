$(document).ready(function () {
    $('.one-post').hover(function (event) {
        $(event.currentTarget).find('.one-post-shadow').animate({opacity:
'0.1'}, 100);
    }, function (event) {
        $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'},
100);
    });
    $(".himg").hover(function(event){
        $(event.currentTarget).animate({width: '338px'}, 100);
        }, function (event) {
        $(event.currentTarget).animate({width: '318px'},
100);
    });
});
