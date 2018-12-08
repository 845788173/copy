$(function () {

    // +
    $('.add').click(function () {

        //获取要修改的cartid
        let cartid = $(this).parents("li").attr('cartid');
        let that = this;

        $.post('/axf/cartnumadd/', {cartid: cartid}, function (data) {
            // console.log(data);
            let obj = data;
            if (obj.status == 1){
                // 在前端修改数量
                $(that).prev().html(obj.num);

                // 计算总价
                calculateTotalprice();

            }
            else {
                alert(obj.msg);
            }

        });

    });

    // -
    $('.reduce').click(function () {

        //获取要修改的cartid
        let cartid = $(this).parents("li").attr('cartid');
        let that = this;

        $.post('/axf/cartnumreduce/', {cartid: cartid}, function (data) {
            // console.log(data);
            let obj = data;
            if (obj.status == 1){
                // 在前端修改数量
                $(that).next().html(obj.num);

                // 计算总价
                calculateTotalprice();

            }
            else {
                alert(obj.msg);
            }

        });

    });

    // 删除
    $('.delbtn').click(function () {
        //获取要删除的商品的cartid
        let cartid = $(this).parents("li").attr('cartid');
        let that = this;

        $.post('/axf/cartdel/', {cartid: cartid}, function (data) {
            // console.log(data);
            let obj = data;
            if (obj.status == 1) {
                $(that).parents("li").remove();

                // 更新最新的‘全选’状态
                modifySelectallState();

            }
            else {
                alert(obj.msg);
            }
        });

    });

    // 勾选 / 取消勾选
    $('.select').click(function () {
        // 获取当前商品的cartid
        let cartid = $(this).parents('li').attr('cartid');
        let that = this;

        $.post('/axf/cartselect/', {cartid: cartid}, function (data) {
            let obj = data;
            if (obj.status == 1) {
                $(that).find('span').html(obj.select ? "√" : "");

                // 更新最新的‘全选’状态
                modifySelectallState();
            }
            else {
                alert(obj.msg);
            }
        });


    });

    // 全选 / 全不选
    $('#select-all').click(function () {
        // 获取当前的全选状态是否为全选
        let isAllSelect = $(this).find('span').html() ? 1 : 0;

        $.post('/axf/cartselectall/', {isAllSelect: isAllSelect}, function (data) {
            // console.log(data);
            let obj = data;
            if (obj.status == 1) {
                $('#select-all,.select').find('span').html(obj.selectall ? "√" : "");

                // 计算总价
                calculateTotalprice();
            }
        });
    });

    // 判断和修改‘全选’状态
    modifySelectallState();
    function modifySelectallState() {
        let flag = true;
        $('.select').each(function () {
            let gou = $(this).find('span').html();  // “√”  or “”
            flag = flag && Boolean(gou);
        });

        // 全选状态
        if (flag) {
            $('#select-all').find('span').html('√');
        }
        // 不全选状态
        else {
            $('#select-all').find('span').html('');
        }

        // 计算总价
        calculateTotalprice();
    }


    // 计算总价(=所有选中的商品总价)
    function calculateTotalprice() {
        let total = 0;

        $('.select').each(function () {
            let gou = $(this).find('span').html();
            if (gou) {
                let price = $(this).parents('li').find('.price').html();
                let num = $(this).parents('li').find('.num').html();
                total += parseFloat(price) * parseInt(num);
            }
        });

        //显示总价
        $('#total').html(total.toFixed(2));  //保留2位小数
    }


});