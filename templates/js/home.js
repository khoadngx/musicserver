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
                alert('Update failed!');
                location.reload(true);
            }
        },
        error: function () {
            alert('Something wrong!');
        }
    });
});

$('#createpl-btn').click(function () {
    var name = $('#createpl-name').val().trim();
    var owned = $('#createpl-owned').val().trim();

    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/api/playlists/',
        data: {
            'name': name,
            'owned': owned,
        },
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log(data);
                location.reload(true);
            } else {
                alert("Sorry we can't create playlist this time!!!");
                location.reload(true);
            }
        },
        error: function () {
            alert('Something wrong!');
        }
    });

});