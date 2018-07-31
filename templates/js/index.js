$('#signin-btn').click(function () {
    var usrname = $('#signin-usrname').val().trim();
    var passwd = $('#signin-passwd').val().trim();

    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/users/' + usrname,
        dataType: 'json',
        success: function (data) {
            if (data != "" && data.passwd == passwd) {
                var usrss = data.usrname;
                $.ajax({
                    type: "GET",
                    url: '/signin',
                    data: {
                        'usrss': usrss,
                    },
                    dataType: 'json',
                    success: function (data) {
                        if (data.is_success) {
                            window.location.replace('http://127.0.0.1:8000/');
                        } else {
                            alert('Sign in failed, please try again!!!')
                            location.reload(true);
                        }
                    }
                });
            } else {
                $('#signin-alert').html("Incorrect username or password!!!");
            }
        },
        error: function () {
            $('#signin-alert').html("This user doesn't exist!!!");
        }
    });
});

$('#new-usrname').change(function () {
    var usrname = this.value;

    $.ajax({
        type: "GET",
        url: '/validate_usrname',
        data: {
            'usrname': usrname,
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                $('#create-alert').css('color', 'red');
                $('#create-alert').html("This username has already been taken!!!");
                $('#create-btn').addClass("disabled");
            } else {
                $('#create-alert').css('color', 'green');
                $('#create-alert').html("Available email address!!!");
                $('#create-btn').removeClass("disabled");
            }
        },
        error: function () {
            alert('Something wrong!');
        }
    });

});

$('#create-btn').click(function () {
    var usrname = $('#new-usrname').val().trim();
    var name = $('#new-name').val().trim();
    var passwd = $('#new-passwd').val().trim();
    var dob = $('#new-dob').val().trim();

    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/api/users/',
        data: {
            'usrname': usrname,
            'name': name,
            'passwd': passwd,
            'dob': dob,
        },
        dataType: 'json',
        success: function (data) {
            if (data != "") {
                // alert(data.name)
                var usrss = data.usrname;
                $.ajax({
                    type: "GET",
                    url: '/signin',
                    data: {
                        'usrss': usrss,
                    },
                    dataType: 'json',
                    success: function (data) {
                        if (data.is_success) {
                            window.location.replace('http://127.0.0.1:8000/');
                        } else {
                            alert('Sign in failed, please try again!!!');
                            location.reload(true);
                        }
                    }
                });
            } else {
                alert("Sorry we can't create accout for you, try again!!!");
                location.reload(true);
            }
        },
        error: function () {
            alert('Something wrong!');
        }
    });

});