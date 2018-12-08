$(function () {

    $('#login').click(function () {
        username = $('#username').val();
        password = $('#password').val();

        if (username && password){
            $('#password').val(md5(password))
        }
        else {
            $('#user-tip').html("用户名或密码不能为空");
            return false
        }

    });

});