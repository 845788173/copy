$(function () {

    // 全部类型（子分类）
    $('#all_type').click(function () {
        $('#all_type_container').toggle();  //切换显示和隐藏
        $('#all_type_icon').toggleClass('glyphicon-chevron-down').addClass("glyphicon-chevron-up");
        $('#all_sort_container').triggerHandler("click");  // 主动触发事件

        // if ($('#all_type_icon').hasClass('glyphicon-chevron-down')) {
        //     $('#all_type_icon').removeClass('glyphicon-chevron-down').addClass("glyphicon-chevron-up");
        // }
        // else {
        //     $('#all_type_icon').removeClass('glyphicon-chevron-up').addClass("glyphicon-chevron-down");
        // }
    });

    // 综合排序
    $('#all_sort').click(function () {
        $('#all_sort_container').toggle();  //切换显示和隐藏
        $('#all_sort_icon').toggleClass('glyphicon-chevron-down').addClass("glyphicon-chevron-up");
        $('#all_type_container').triggerHandler("click");  // 主动触发事件
    });

    // 点击‘全部类型’半透明层
    $('#all_type_container').click(function () {
        $(this).hide();
        $('#all_type_icon').removeClass('glyphicon-chevron-up').addClass("glyphicon-chevron-down");
    });

    // 点击‘综合排序’半透明层
    $('#all_sort_container').click(function () {
         $(this).hide();
         $('#all_sort_icon').removeClass('glyphicon-chevron-up').addClass("glyphicon-chevron-down");
    });


    //加入购物车
    $('.addtocart').click(function () {
        // 获取goodsid, num
        let num = $(this).prev().find('.num').text();
        let goodsid = $(this).attr('goodsid');

        // 添加购物车
        $.get('/axf/cartadd/', {goodsid:goodsid, num:num}, function (data) {
            // console.log(data)
            let obj = data;
            if (obj.status == 1) {
                alert("加入购物车成功！")
            }
            else {
                //未登录
                if (obj.status == 0) {
                    let res = confirm("您尚未登录，是否前往登录");
                    if (res){
                        location.href = "/axf/login/"
                    }
                }
                else {
                    alert(obj.msg)
                }
            }

        });

    });


    // +
    $('.add').click(function () {
        // index = $(this).index('.add');
        // num = $('.num').eq(index);

        let numNode = $(this).prev();
        numNode.html(parseInt(numNode.html()) + 1);

    });

    // -
    $('.reduce').click(function () {
        let numNode = $(this).next();
        if (parseInt(numNode.html()) > 1) {
            numNode.html(parseInt(numNode.html()) - 1);
        }
    });





});