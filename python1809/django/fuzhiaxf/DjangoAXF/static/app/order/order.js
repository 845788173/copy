$(function () {

    // 支付宝支付流程
    //  1,先跟支付宝签约，成为支付宝的商家
    //  2,创建应用，分配AppId,secret
    //  3,浏览商品 -> 点击‘加入购物车’将商品添加购物车 -> 在购物车页面点击'结算'
    //      -> 后台会生成订单 -> 进入订单页面点击'支付'按钮
    //      -> 调用支付宝的API(一般需要上传给支付宝这些数据：
    //          订单号，订单金额，商家id, 收款支付宝账号，回调url)
    //      -> 支付宝完成支付后，会通过调用‘回调url’来通知商家(一般会给商家发送：订单号,订单金额..)是否支付成功！
    //      -> 商家接收到支付结果后，可以修改对应订单的状态
    //      -> 支付结束

    //点击‘支付’按钮
    $('#pay').click(function () {

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