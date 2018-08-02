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