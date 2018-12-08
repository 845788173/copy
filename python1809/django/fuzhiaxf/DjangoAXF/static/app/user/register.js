$(function () {

    // 前端做本地校验
    /*
    flag1 = false;  // 用户名
    flag2 = false;  // 密码
    flag3 = false;  // 确认密码
    flag4 = false;  // 邮箱

    // 检测用户名
    $('#username').blur(function () {

        let value = $(this).val();
        if (/^[a-zA-Z_]\w{5,17}$/.test(value)){
            $("#user-tip").html("用户名合法").css("color",'green');
            flag1 = true;
        }
        else {
            $("#user-tip").html("用户名不合法").css("color",'red');
            flag1 = false;
        }
    });

    // 密码
    $('#password').blur(function () {
         let value = $(this).val();
         if (/^.{8,20}$/.test(value)) {
             $("#password-tip").html("");
             flag2 = true;
         }
         else {
             $("#password-tip").html("密码不合法").css("color",'red');
             flag2 = false;
         }
    });

    // 确认密码
    $('#repassword').blur(function () {
         let value = $(this).val();
         if (value == $('#password').val()) {
             $("#repassword-tip").html("");
             flag3 = true;
         }
         else {
             $("#repassword-tip").html("两次密码不一致").css("color",'red');
             flag3 = false;
         }
    });

    // 邮箱
    $('#email').blur(function () {
         let value = $(this).val();
         if (/^\w+@\w+(\.\w+)+$/.test(value)) {
             $("#email-tip").html("");
             flag4 = true;
         }
         else {
             $("#email-tip").html("邮箱不合法").css("color",'red');
             flag4 = false;
         }
    });


    // 注册
    $('#register').click(function () {

        // 如果所有输入框都合法
        if (flag1 && flag2 && flag3 && flag4) {
            window.alert("输入都合法");
            return false;
        }
        else {
            window.alert("输入不合法");
            return false;
        }
    });

    */



    // 检测用户名
    $('#username').blur(function () {
        checkUser()
    });
    function checkUser(){
        let value = $('#username').val();
        if (/^[a-zA-Z_]\w{5,17}$/.test(value)){
            $("#user-tip").html("用户名合法").css("color",'green');
            return true;
        }
        else {
            $("#user-tip").html("用户名不合法").css("color",'red');
            return false;
        }
    }

    // 密码
    $('#password').blur(function () {
         checkPasswd()
    });
    function checkPasswd(){
        let value = $('#password').val();
        if (/^.{8,20}$/.test(value)) {
            $("#password-tip").html("");
            return true;
        }
        else {
            $("#password-tip").html("密码不合法").css("color",'red');
            return false;
        }
    }

    // 确认密码
    $('#repassword').blur(function () {
         checkRepasswd();
    });
    function checkRepasswd(){
        let value = $('#repassword').val();
        if (value == $('#password').val()) {
            $("#repassword-tip").html("");
            return true;
        }
        else {
            $("#repassword-tip").html("两次密码不一致").css("color",'red');
            return false;
        }
    }

    // 邮箱
    $('#email').blur(function () {
         checkEmail()
    });
    function checkEmail(){
        let value = $('#email').val();
        if (/^\w+@\w+(\.\w+)+$/.test(value)) {
             $("#email-tip").html("");
             return true;
        }
        else {
             $("#email-tip").html("邮箱不合法").css("color",'red');
             return false;
        }
    }


    // 注册
    $('#register').click(function () {

        // 如果所有输入框都合法
        if (checkUser() && checkPasswd() && checkRepasswd() && checkEmail()) {
            // window.alert("输入都合法");
            // return false;

            // 提交表单前加密
            $('#password').val(md5($('#password').val()))

        }
        else {
            // window.alert("输入不合法");
            return false;
        }
    });






});


