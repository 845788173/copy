$(function () {

    //点击‘支付’按钮
    $('.pay').click(function () {

        // 模拟支付成功
        // 支付成功后，将后台状态改变
        $.post('/axf/orderstatuschange/', {oid: $(this).attr('oid'), status: 1}, function (data) {
            let obj = data;
            if (obj.status == 1) {
                // 如果支付成功，则跳转到‘我的’页面
                location.href = "/axf/mine/";
            }
            else {
                alert(obj.msg);
            }
        });

    })

});