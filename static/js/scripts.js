$(document).ready(function(){
   prepareDocument(); 
});


function prepareDocument (){
    statusBox;
}; 

// show loading-box if ajax-request takes some time 
function statusBox() {
	$('<div id="loading"><img src="/static/img/loading.gif" alt="" />Loading...</div>').prependTo("#main").ajaxStart(function () {
		$(this).show();
	})
	.ajaxStop(function () {
		$(this).hide();
	})
}

/*** ajax requests' processing ***/

// on item delete
function removeProcess(event, successFunction, url){
    var elem = $(event.target);
    elem.addClass("to-be-removed")
    var request_data = {"slug": elem.data("slug")};
    $.ajax({
        url : url,
        type : 'POST',
        data : request_data,
        dataType : 'json',
        success : successFunction,
        error : function (xhr, textStatus, errorThrown) {
            //log ajax errors
            console.log("There was an error processing ajax request: \n" +
            "\t -the text status is: ' " + textStatus + "'\n" +
            "\t -the error thrown is:' " + String(errorThrown) + "'" +
            "\t -the data sent  is: ' " + this.data + "'" +
            "\t -the method is: '" + this.type + "'");
        }
    });
}

function removeSuccess(json_response) {
    if (json_response.success == "True") {
        $(".to-be-removed").parent().parent().remove();    
    }
}

// on item edit
function editProcess(event, successFunction, url){
    var elem = $(event.target);
    var request_data = {"slug": elem.attr("data-slug")};
    console.log(request_data)
    $.ajax({
        url : url,
        type : 'POST',
        data : request_data,
        dataType : 'json',
        success : successFunction,
        error : function (xhr, textStatus, errorThrown) {
            //log ajax errors
            console.log("There was an error processing ajax request: \n" +
            "\t -the text status is: ' " + textStatus + "'\n" +
            "\t -the error thrown is:' " + String(errorThrown) + "'" +
            "\t -the data sent  is: ' " + this.data + "'" +
            "\t -the method is: '" + this.type + "'");
        }
    });
}

function editSuccess(json_response) {
    if (json_response.success == "True") {
        $("#item_form").empty();    
        $("#item_form").prepend(json_response.html).slideDown("slow");    
    }
}

/*** utility functions ***/

// ajax-csrf routine? required fo django csrf-protection
function prepareCsrf(){
    
    function getCookie(name) {
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
    
    var csrftoken = getCookie('csrftoken');
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
};