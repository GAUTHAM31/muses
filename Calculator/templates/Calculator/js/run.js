jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        console.log("cookie")
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});


$("#run").click(function(){
    console.log('clicked');
    $.ajax({
        url: 'run/',
        type: 'POST',
        data: {
            'title' : jsonInput.getValue()
        },
        // contentType: 'application/json',

        success: function(data) {
            array = data['list'];
            output.setValue("");
            for (var i = 0; i < array.length; i++)
            {
                console.log(array[i]);
                output.replaceRange(array[i]+"\n", CodeMirror.Pos(output.lastLine()))
            }

        //api
        api = "https://api.muses.com/api/"+data['api']
        api_code.setValue("");
        api_code.replaceRange(api+"\n", CodeMirror.Pos(api_code.lastLine()))


        },
        complete: function(){

        },
        error: function(req) {
           alert('Error: ' + req.status);
        }
    });
});
