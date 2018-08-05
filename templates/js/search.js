$('#signout-btn').click(function() {
    $.ajax({
        type: "GET",
        url: '/signout',
        data:{
            'check': 1,
        },
        dataType: 'json',
        success: function (data){
            if(data.is_success){
                window.location.replace('http://127.0.0.1:8000/');
            } else {
                alert('Log out failed!')
                location.reload(true);
            }
        },
        error: function () {
            alert('Something wrong!');
        }
    });
});

$('#search-btn').click(function() {
    var keyword = $('#search-keyword').val().trim();
    if(keyword == ''){
        alert('please enter keyword!');
    } else {
        window.location.replace('http://127.0.0.1:8000/search/' + keyword);
    }
});