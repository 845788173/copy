$(function () {

    //点击‘确认收货’按钮
    $('.confirm').click(function () {

        // 将后台状态改变
        $.post('/axf/orderstatuschange/', {oid: $(this).attr('oid'), status: 2}, function (data) {
            let obj = data;
            if (obj.status == 1) {
                // 如果修改成功，则跳转到‘我的’页面
                location.href = "/axf/mine/";
            }
            else {
                alert(obj.msg);
            }
        });

    })

});