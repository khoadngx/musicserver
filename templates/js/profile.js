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

$('#editprofile-btn').click(function () {
    $('#profile-name').removeAttr("disabled");
    $('#profile-dob').removeAttr("disabled");
    $('#profile-passwd').removeAttr("disabled");
    $('#profile-about').removeAttr("disabled");
});

$('#profile-name').change(function () {
    var name = this.value;
    if(name == ''){
        $('#profile-btn').addClass("disabled");
    } else {
        $('#profile-btn').removeClass("disabled");
    }
});

$('#profile-dob').change(function () {
    var dob = this.value;
    if(dob == ''){
        $('#profile-btn').addClass("disabled");
    } else {
        $('#profile-btn').removeClass("disabled");
    }
});

$('#profile-passwd').change(function () {
    var passwd = this.value;
    if(passwd == ''){
        $('#profile-btn').addClass("disabled");
    } else {
        $('#profile-btn').removeClass("disabled");
    }
});

$('#profile-about').change(function () {
    var about = this.value;
    if(about == ''){
        $('#profile-btn').addClass("disabled");
    } else {
        $('#profile-btn').removeClass("disabled");
    }
});

$('#profile-btn').click(function () {
    var usrname = $('#profile-usrname').val().trim();
    var name = $('#profile-name').val().trim();
    var passwd = $('#profile-passwd').val().trim();
    var dob = $('#profile-dob').val().trim();
    var about = $('#profile-about').val().trim();

    $.ajax({
        type: "PUT",
        url: 'http://127.0.0.1:8000/api/users/' + usrname + '/',
        data:{ 
            'usrname':usrname,
            'name': name,
            'passwd': passwd,
            'dob': dob,
            'about': about
        },
        dataType: 'json',
        success: function (data){
            if(data){
                location.reload(true);
            } else {
                alert('Sorry can\'t update profile!');
                location.reload(true);
            }
        },
        error: function () {
            alert('Something wrong!');
        }
    });
});

$('#unfollow-btn').click(function () {
    var follower = $('#follower').val().trim();
    var followed = $('#followed').val().trim();
    var deleteid = 0;

    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/follows/',
        dataType: 'json',
        success: function (data){
            if(data){
                for(var i=0; i < data.length; i++){
                    if(data[i].follower == follower && data[i].followed == followed){
                        deleteid = data[i].id;
                        break;
                    }
                }
                $.ajax({
                    type: "DELETE",
                    url: 'http://127.0.0.1:8000/api/follows/' + deleteid + '/',
                    dataType: 'json',
                    success: function (data){
                        if(data == null){
                            location.reload(true);
                        } else {
                            alert('Sorry can\'t unfollow this time!');
                            location.reload(true);
                        }
                    },
                    error: function () {
                        alert('Something wrong!');
                    }
                });
                location.reload(true);
            } else {
                alert('Sorry can\'t get the follow data this time!');
                location.reload(true);
            }
        },
        error: function () {
            alert('Something wrong!');
        }
    });
});

$('#follow-btn').click(function () {
    var follower = $('#follower').val().trim();
    var followed = $('#followed').val().trim();

    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/api/follows/',
        data: {
            'follower': follower,
            'followed': followed
        },
        dataType: 'json',
        success: function (data) {
            if (data) {
                location.reload(true);
            } else {
                alert('Sorry follow can\'t submit!');
                location.reload(true);
            }
        },
        error: function () {
            alert('Something wrong!');
        }
    });
});