$(function() {

	chang();

	function chang() {

		//从cookie中获取购物车的所有商品,把数据转化为对象，反序列化
		var arr = $.cookie("cart");
		//		$('.cart_goods').html("");
		if(arr) {
			arr = JSON.parse(arr);
			//遍历数组, 显示所有商品的信息
			//			console.log(arr);
			var ulNode_cartBox = $(".cartBox").find(".cart_goods");
			for(var i = 0; i < arr.length; i++) {
				//=创建li节点

				//				if(arr[i]){

				var liNode_goodsBox = $("<li/>");
				liNode_goodsBox.addClass("goodsbox");

				//==<div class="cart_goods_msg">
				var divNode_goodsMsg = $("<div/>");
				divNode_goodsMsg.addClass("cart_goods_msg");
				$('<input type="checkbox" checked="checked" class="checkBox" />').appendTo(divNode_goodsMsg);
				$('<a href="#">' + arr[i].img + '</a>').appendTo(divNode_goodsMsg);

				//===<div class="inforbox">
				var divNode_inforBox = $("<div/>");
				divNode_inforBox.addClass("inforbox");
				$('<h3><a href="#">' + arr[i].name + '</a></h3>').appendTo(divNode_inforBox);
				$('<p>颜色：' + arr[i].colors + '</p>').appendTo(divNode_inforBox);
				$('<p>套装：' + arr[i].taocan + '</p>').appendTo(divNode_inforBox);
				divNode_inforBox.appendTo(divNode_goodsMsg);

				//<div class="sp_price">
				var divNode_spPrice = $("<div/>");
				divNode_spPrice.addClass("sp_price");
				$("<em>" + arr[i].price + "</em>").appendTo(divNode_spPrice);


				//<div class="sp_amount">
				var divNode_spAmount = $("<div/>");
				divNode_spAmount.addClass("sp_amount");
				var divNode_buyNum = $("<div/>");
				divNode_buyNum.addClass("buy_num");
				$('<span class="jian">-</span>').appendTo(divNode_buyNum);
				$('<input type="text" class="text_amount" value='+arr[i].num+' />').appendTo(divNode_buyNum);
				$('<span class="jia">+</span>').appendTo(divNode_buyNum);
				divNode_buyNum.appendTo(divNode_spAmount);

				//<div class="sp_youhui">
				var divNode_spYouhui = $("<div/>");
				divNode_spYouhui.addClass("sp_youhui");
				var divNode_buyYouhui = $("<div/>");
				divNode_buyYouhui.addClass("buy_youhui");

				divNode_buyYouhui.append(arr[i].youhui);
				divNode_buyYouhui.appendTo(divNode_spYouhui);

				//<div class="sp_total">
				var divNode_spTotal = $("<div/>");
				divNode_spTotal.addClass("sp_total");
				var allTotal = parseFloat(arr[i].price) * parseInt(arr[i].num);
				$('<em>' + allTotal + '<em/>').appendTo(divNode_spTotal);

				//<div class="sp_del">
				var divNode_spDel = $("<div/>");
				divNode_spDel.addClass("sp_del");
				var divNode_delBox = $("<div/>");
				divNode_delBox.addClass("del_box")
				$('<a href="#">移入收藏夹</a>').appendTo(divNode_delBox);
				$('<a href="#"class="del">删除</a>').appendTo(divNode_delBox);
				divNode_delBox.appendTo(divNode_spDel);

				divNode_goodsMsg.appendTo(liNode_goodsBox);
				divNode_spPrice.appendTo(liNode_goodsBox);
				divNode_spAmount.appendTo(liNode_goodsBox);
				divNode_spYouhui.appendTo(liNode_goodsBox);
				divNode_spTotal.appendTo(liNode_goodsBox);
				divNode_spDel.appendTo(liNode_goodsBox);

				ulNode_cartBox.append(liNode_goodsBox);

				console.log(arr[i].num)
					//				}
			}

		}

	}
	$(".jian").off().click(function() {
		var amount = parseInt($(this).next().val());

		if(amount <= 1) {
			amount = 1;
		} else {
			$(this).next().val(--amount);
			amount = parseInt($(this).next().val());
		}

		//查找当前li的下标
		x = $(this).closest('li').index();
		console.log(x)
		var arr = $.cookie("cart") ? JSON.parse($.cookie("cart")) : [];
		//获取当前的数量，重新覆盖cookie里的数量
		for(var i = 0; i < arr.length; i++) {
			if(i == x) {
				arr[i].num = amount
			}
		}
		$.cookie("cart", JSON.stringify(arr), {
			expires: 30,
			path: "/"
		});

		$('.total_cart_price').html(lookCart().numPrice)
		litPrice($(this));
	});

	$(".jia").off().click(function() {
		var amount = parseInt($(this).prev().val());

		$(this).prev().val(++amount);
		amount = parseInt($(this).prev().val());

		x = $(this).closest('li').index();
		console.log(x)
		var arr = $.cookie("cart") ? JSON.parse($.cookie("cart")) : [];
		for(var i = 0; i < arr.length; i++) {
			if(i == x) {
				arr[i].num = amount
			}
		}
		$.cookie("cart", JSON.stringify(arr), {
			expires: 30,
			path: "/"
		});

		$('.total_cart_price').html(lookCart().numPrice)
		litPrice($(this));
	})

	function lookCart() {
		//		kind num numPrice img 
		//		商品种类     总计
		var numPrice = 0;
		var arr = $.cookie("cart") ? JSON.parse($.cookie("cart")) : [];
		//遍历查找是否之前的购物车cookie中存在即将添加的商品

		for(var i = 0; i < arr.length; i++) {
			//如果存在该商品, 把数量增加
			numPrice += (parseInt(arr[i].price) * parseInt(arr[i].num));
		}
		//返回  总价
		return {
			"numPrice": numPrice
		}
	}
	$('.total_cart_price').html(lookCart().numPrice)
		//小计litPrice
	function litPrice(dh) {
		//console.log(dh.parent());
		if(dh) {
			var litPrice = (
				parseInt(dh.closest(".goodsbox").find(".sp_price").find("em").html()) *
				(parseInt(dh.parent().find("input").val()))
			);
			// console.log(litPrice);
			dh.closest(".goodsbox").find(".sp_total").find("em").html(litPrice);
		} else {
			for(var i = 0; i < $(".sp_price").length; i++) {
				var litPrice = (parseInt($(".sp_price").eq(i).find("em").html())) * (parseInt($(".sp_amount").eq(i).find("input").val()));
				//console.log(litPrice);
				$(".sp_total").eq(i).find("em").html(litPrice);
			}
		}
	}

	//全选
	$(".selectAll").click(function() {
		var isCheck = $(this).prop("checked");
		if(isCheck == true) {
			$(":checkbox").prop("checked", isCheck);
			$('.total_cart_price').html(lookCart().numPrice);
		} else {
			$(":checkbox").prop("checked", "");
			$('.total_cart_price').html(0.00);
		}
	});

//	$(".del_box").find(".del").off().click(function() {
//		//		$(this).closest().find(".goodsbox").
//
//		var arr = $.cookie("cart") ? JSON.parse($.cookie("cart")) : [];
//		//遍历查找是否之前的购物车cookie中存在即将添加的商品
//		x = $(this).closest('li').index();
//		for(var i = 0; i < arr.length; i++) {
//			//如果存在该商品, 把数量增加
//			if(i == x)
//				arr[i] = "";
//		}
//		$.cookie("cart", JSON.stringify(arr), {
//			expires: 30,
//			path: "/"
//		});
//		chang()
//	})

	$(".checkBox").click(function() {
		Check();
		//		parseInt($('.total_cart_price').html()-parseInt( $(this).closest(".goodsbox").find(".sp_total").find("em").html()));
		$('.total_cart_price').html(parseInt($('.total_cart_price').html()) - parseInt($(this).closest(".goodsbox").find(".sp_total").find("em").html()));
	})

	//判断是否全选
	Check();

	function Check() {
		var selAllcheck = $(".selectAll");
		var licheck = $(".checkBox");
		var flag = true;
		for(var i = 0; i < licheck.length; i++) {
			if(!licheck[i].checked) {
				flag = false;

			}
		}
		if(flag) {
			selAllcheck.prop("checked", true);
		} else {
			selAllcheck.prop("checked", false);
		}
	}

	//	var goodsList = $(".cart_goods").find("li");
	//	var inputAmount = $(this).find(".sp_amount").find(".text_amount")
	//	var unitPrice = 0;
	//	var amount = 0;
	//	var litPrice = 0;
	//
	//	$.each(goodsList, function() {
	//		unitPrice = parseFloat($(this).find(".sp_price").find("em").text());//单价
	//		amount = parseInt(inputAmount.val());//数量
	//		litPrice = parseInt(litPrice) +parseInt(unitPrice * amount);// 
	//	});
	//
	//	$(".shopCar_content").find(".sp_total").find("em").val(litPrice);
	//	$(".shopCar_content").find(".sp_total").find("em").val(litPrice);
	//
	//	$(".sp_amount").find(".jian").off().click(function() {
	//		$(this).next().val(parseInt($(this).next().val()) - 1);
	//		if(parseInt($(this).next().val()) <= 1) {
	//			$(this).next().val(1);
	//	}
	//		var money = $(".shopCar_content").find("em.total_cart_price");
	//		 money.val($(this).next().val(parseInt($(this).next().val()) - 1)*parseFloat($(".sp_price").find("em").text())

	//		var arr = $.cookie("cart") ? JSON.parse($.cookie("cart")) : [];
	//		var index = $(this).closest('li.goodsbox').index()
	//			//遍历查找是否之前的购物车cookie中存在即将添加的商品
	//		for(var i = 0; i < arr.length; i++) {
	//			if(i == index) {
	//				arr[i].num = $(this).parent().find('.text_amount').val();
	//			}
	//		}
	//		console.log(arr)
	//			//保存到cookie中
	//		$.cookie("cart", JSON.stringify(arr), {
	//			expires: 30,
	//			path: "/"
	//		});
	//		window.location.reload();
	//		chang();
	//		return false;
	//	});

})