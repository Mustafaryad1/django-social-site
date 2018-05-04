(function (){
    if(window.myBookmarklet !== undefinded) {
        myBookmarklet();
    }
    else {
        documnet.body.appendChild(document.createElement('script')).src='http://127.0.0.1:8000/'
    }

})