var cart = {
    //防止多次点击
    doing: false,
    //获取当前数量
    nowQuantity: function (id) {
        try {
            qty = 0;
            $('.pqty_' + id).each(function () {
                qty += parseInt($(this).val());
            });
            return qty;
        }
        catch (e) {
            alert('请输入数字类型');
        }
    },
    //减少数量
    reduceQuantity: function (id, minQty) {
        nowQty = this.nowQuantity(id);
        nowQty = nowQty - 1;
        this.changeQuantity(id, nowQty, minQty, 0);
    },
    //添加数量
    addQuantity: function (id, maxQty) {
        nowQty = this.nowQuantity(id);
        nowQty = nowQty + 1;
        this.changeQuantity(id, nowQty, 0, maxQty);
    },
    //更改数量
    changeQuantity: function (id, qty, minQty, maxQty) {
        if (this.doing) { alert('操作中，请稍等'); return; };
        if (qty > 0 && minQty > 0 && qty < minQty) {
            alert('此商品最少购买' + minQty + '个');
            return;
        }
        if (qty > 0 && maxQty > 0 && qty > maxQty) {
            alert('此商品最多购买' + maxQty + '个');
            return;
        }
        this.doing = true;
        $.getJSON('/Cart/ChangeCartProductCount', { cartProductId: id, qty: qty, t: new Date() }, function (data) {
            if (data.Success == 1) {
                document.location.reload();
            }
            else {
                alert(data.Result);
            }
            cart.doing = false;
        });
    },
    //计算购物车总价格
    chargeSum: function () {
        totalCount = 0, totalPrice = 0;
        idStr = "";
        $('.supplier_title').each(function () {
            if ($(this).attr("checked")) {
                totalCount += parseFloat($(this).attr('data-qty'));
                totalPrice += parseFloat($(this).attr('data-price'));
                idStr += $(this).attr('data-id');
            }
        });
        $('#check_allacount').html("￥" + parseFloat(totalPrice).toFixed(2));
        $('#check_acount').html(totalCount);
        $('#select_id').val(idStr);
    },
    //去结算页
    goReceiver: function () {
        if ($('#select_id').val() == "") {
            alert('请至少选择一个供应商');
            return;
        }
        else {
            $.get('/Ajax/SetCartProductId', { 'str': $('#select_id').val(), 't': new Date() }, function (data) {
                if (data == "")
                    document.location.href = "/Cart/GoReceiver";
                else
                    alert(data);
            });
        }
    }
};