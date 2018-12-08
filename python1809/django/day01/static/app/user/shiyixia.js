
$(function(){
    $('#login').click(function(){
        username=$('#username').val();
        password=$('#password').val();
        if (username&&password){
            $('#password').val(md5(password))
        }
        else{
            $('#user-tip').html('yonghuminghuomimabunengweikong')
        }

    })
})