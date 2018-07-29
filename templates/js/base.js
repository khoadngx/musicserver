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
      }
    });
  });