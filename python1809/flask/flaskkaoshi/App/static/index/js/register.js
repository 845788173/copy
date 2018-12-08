$(function() {
//
    $('#exampleInputEmail1').blur(function () {
        checkUsername()
    });
//
//
    function checkUsername() {
        let $exampleInputEmail1=$('#exampleInputEmail1').val();
        if (/^[a-zA-Z_]\w{5,17}$/.test($exampleInputEmail1)){
            $('.user-tip').html('用户名合法').css('color','green')
            return true;
        }
        else{
            $('.user-tip').html('用户名不合法').css('color','red' )
            return false;
        }

    }
//
    $('#password').blur(function () {
        checkPassword()
    })
    function checkPassword() {
        let $Password=$('#password').val();
        if (/^.{8,20}$/.test($Password)){
            $('.password-tip').html('密码正确').css('color','green');
            return true;
        }
        else{
            $('.password-tip').html('密码错误').css('color','red');
            return false;
        }
    }
    // $('.submit').click(function () {
    //     if (checkPassword() && checkUsername()) {
    //         return true;
    //     }
    //     else {
    //         return false;
    //     }
    // })
//
//
//     console.log('#######')
//     $(      //页面加载完执行
//         $("#ajaxForm").on("submit",function () {    //表单提交时监听提交事件
//             console.log('#######')
//             $(this).ajaxSubmit(options);    //当前表单执行异步提交，optons 是配置提交时、提交后的相关选项
//             return false;   //  必须返回false，才能跳到想要的页面
//         })
//     )
//     //配置 options 选项
//     var options = {
//         url: "/api/v1/register/",       //提交地址：默认是form的action,如果申明,则会覆盖
//         type: "post",           //默认是form的method（get or post），如果申明，则会覆盖
//         success: successFun,    //提交成功后的回调函数，即成功后可以定页面跳到哪里
//         dataType: "json",       //接受服务端返回的类型
//         clearForm: true,        //成功提交后，清除所有表单元素的值
//         resetForm: true,        //成功提交后，重置所有表单元素的值
//         timeout: 3000           //设置请求时间，超过该时间后，自动退出请求，单位(毫秒)
//     }
//     //设置提交成功后返回的页面
//     function successFun(response,status) {
//         if (response.status == 200){
//             $('#msg').html('注册成功！')
//             console.log(response)
//             window.open('/static/home.html',target='_branch')
//         } else {
//             $('#msg').html(response.err)
//         }
//     }

        $('.submit').click(function () {

            console.log('删除动作')
            // console.log(response)
            let $user=$('.user-tip').prev().val()
            console.log($user)
            let $password=$('.password-tip').prev().val()
            console.log($password)
            let $email=$('.email-tip').prev().val()
            data_dict={username:$user,password: $password,email: $email}

            $.ajax({
                dataType: 'json',
                url:'/api/v1/register/',
                type: 'POST',
                data:data_dict,
                success: function (response) {
                    console.log(response)
                    if (response['status'] == 200 && (checkPassword() && checkUsername())) {
                        window.open('/static/home.html/', target = '_self');
                    }
                }
            })
        })
    })
