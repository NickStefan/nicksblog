var jPM = {};

$(function() {

    jPM = $.jPanelMenu({

        menu : '#menu',
        trigger : '.menu-trigger',
        animated: false,
        beforeOpen : ( function() {

            if (matchMedia('only screen and (min-width: 992px)').matches) {
                $('.sidebar').css("left", "250px");
            }

        }),
        beforeClose : ( function() {

            $('.sidebar').css("left", "0");
            $('.writer-icon, .side-writer-icon').removeClass("fadeOutUp");
        })
    });

    jPM.on();
    $('.menu-trigger').click(function(){});

    $('.select-posts, .select-categories').on('click', function () {

        $('.home-page-posts').toggleClass("hide");
        $('.home-page-categories').toggleClass("hide");

        $('.select-posts').toggleClass("active");
        $('.select-categories').toggleClass("active");

        $('.home-footer').toggleClass("hide");
    });

    $('.writer-icon').on('click', function () {
        $(this).addClass("fadeOutUp");

    });

    var fullHeight = $(window).height();

    $('.hero-image-404').css("height", fullHeight );

    $('.postbody').each(function(){
        var mdown = $(this).html();
        var stack = [];
        var mdown = mdown.split('').map(function(v,k,c){
            if (v === '`') {
                stack.push('`');
            }
            if (k === c.length - 4 && stack.length % 6 !== 0) {
                return v + '```';
            }
            return v;
        }).join('');
        $(this).html(marked(mdown));
    });
    $('code').wrap('<pre></pre>');

    hljs.initHighlightingOnLoad();

});