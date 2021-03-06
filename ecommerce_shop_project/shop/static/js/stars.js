$(".clickable > span" ).on('click', function(event){
    event.preventDefault();
    var element = $(this);

    $.ajax({
        url : '/add_rating/' + $(this).attr("data-id") + '/' + $(this).attr("data-star"),
//        data: {data_star: data_star},
        type : 'POST',

        success : function(data){
            const spans = document.querySelectorAll(".ratings > span");
            spans.forEach(s => {
                console.log(s);
                s.classList.remove("empty-star");
                s.classList.remove("text-dark");
                s.classList.remove("hover");
            });
            const not_rated = document.querySelector(".not_rated");
            if (not_rated){
                not_rated.remove();
            }
            Array.from(spans).slice(data.stars).forEach(s => s.classList.add("empty-star"));
            console.log(data.stars);
//            element.html(' ' + data);
        }
    });
});


// You need these methods to add the CSRF token using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken')

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});