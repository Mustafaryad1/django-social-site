(function () {
    var jquery_version = '2.1.4';
    var site_url = 'http://127.0.0.1:8000/'
    var static_url = site_url + 'static/'
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg) {
        //load css
        var css = jQuery('<link>');
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random() * 9999999999999999)
        });
        jQuery('head').append('css')
        // load html
        box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a> <h1>Select an image </h1>'
        jQuery('body').append(box_html);

        //    close event
        jQuery('#bookmarklet #close').click(function () {
            jQuery('#bookmarklet').remove();
        })
        // find images and display them
        jQuery.each(jQuery('img[src$="jpg"]'),function(index, image){
                if(jQuery(image).width() >=min_width && jQuery(image).height >=min_height){
                    image_url = jQuery(image).attr('src');
                    jQuery('#bookmarklet .images').append('<a href="#"><img src="'+ image_url +'"/></a> ')
                }
        });
        //    when an image has been selected open url with it
        jQuery('#bookmarklet .images a').click(function (e){
            select_image = jQuery(this).children('img').attr('src');
        //    hide bookmarklet
            jQuery('#bookmarklet').hide();
        //    open new window to submit the image
            window.open(site_url+'images/create/?url='
                +encodeURIComponent(select_image)
                + '&title=' +encodeURIComponent(jQuery('title').text()),
                '_blank');
        });
    };
    // check if jquery loaded
    if (typeof window.jquery != 'undefined') {
        bookmarklet();

    } else {
        // check conflicts
        var conflict = typeof window.$ != 'undefined';

        // create script and point to Google API
        var script = document.createElement('script');
        script.setAttribute('src', 'http://ajax.googleapis.com/ajax/libs/jquery') + jquery_version;
    }
}