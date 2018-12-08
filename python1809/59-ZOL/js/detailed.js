$(function() {

	//点击详情页商品的跳转
	$.get("json/detailed.json", function(data) {
		for(var i = 0; i < data.length; i++) {
			var id = getItem();
			if(id == data[i].id) {
				var obj = data[i];
				var Id = data[i].id;
				//=================商品展示图=====================
				var bigsrc = obj.bigImg[0].img;
				var bigsrcClass = obj.bigImg[0]._class;

				var divNode_bigImg = $(".bigImg");
				var divNode_bigArea = $("#bigArea");
				$("<img src=" + bigsrc + "/>").appendTo(divNode_bigImg); //添加大图图片
				$("<img src=" + bigsrc + "/>").addClass("_bigImg").appendTo(divNode_bigArea); //添加放大镜的大大图片

				//创建ul li img 获取图片
				var divNode_imgIist = $(".imgIist");
				var ulNode = $("<ul/>");
				ulNode.appendTo(divNode_imgIist);
				$.each(obj.smallImg, function() {
					$("<li><img src=" + this.img + "/></li>").appendTo(ulNode);
				});
				divNode_imgIist.find("li").eq(0).addClass("active"); //给第一个li添加默认样式

				//切换图片
				$(".imgIist ul li").click(function() {
					var i = $(this).index();
					$(".imgIist ul li").removeClass("active");
					$(this).addClass("active");
					$(".bigImg").find("img").attr("src", "img/detail/big_" + Id + (i + 1) + ".jpg");
					$("#bigArea").find("img").attr("src", "img/detail/big_" + Id + (i + 1) + ".jpg");

				});

				//放大镜
				var _smallImg = $("#smallImg");
				var _smallArea = $("#smallArea");
				var _bigImg = $("._bigImg");
				var _bigArea = $("#bigArea");

				//==计算小区域宽高
				//==smallArea/bigArea = smallImg/bigImg ( width() and height())
				_smallArea.width(_bigArea.width() * _smallImg.width() / _bigImg.width());
				_smallArea.height(_bigArea.height() * _smallImg.height() / _bigImg.height());

				var scale = _bigImg.width() / _smallImg.width(); //scale = 2

				//==mousemove
				_smallImg.mousemove(function(e) {
					//显示大小区域	
					_smallArea.show();
					_bigArea.show();
					//clientX
					//pageX :窗口左边的距离

					var x = e.pageX - _smallImg.offset().left - _smallArea.width() / 2;
					var y = e.pageY - _smallImg.offset().top - _smallArea.height() / 2;

					//控制范围
					if(x < 0) {
						x = 0;
					} else if(x >= _smallImg.width() - _smallArea.width()) {
						x = _smallImg.width() - _smallArea.width();
					}
					if(y <= 0) {
						y = 0;
					} else if(y >= _smallImg.height() - _smallArea.height()) {
						y = _smallImg.height() - _smallArea.height();
					}

					_smallArea.css({
						left: x,
						top: y
					})

					_bigImg.css({
						left: -x * 2,
						top: -y * 2
					})

				})

				//==mouseleave
				_smallImg.mouseleave(function() {
					//隐藏大小区域
					_smallArea.hide();
					_bigArea.hide();
				})

				//=================商品详细信息=====================
				var tittle = obj.msg[0].tittle;
				var subTittle = obj.msg[0].subTittle;
				var price = obj.msg[0].price;
				var class_price = obj.msg[0].class_price;
				var sale = obj.msg[0].sale;
				var gift = obj.msg[0].gift;
				var giftNum = obj.msg[0].giftNum;
				var class_num = obj.msg[0].class_num;
				var pingjiaNum = obj.msg[0].pingjiaNum;
				var chengjiao = obj.msg[0].chengjiao;
				var limit = obj.msg[0].limit;
				var youhui = obj.msg[0].youhui;

				$(".center_goodsMsg").find("h3").find("i").append(tittle);
				$("<span>" + subTittle + "</span>").appendTo($(".center_goodsMsg").find("h3"));
				$("<em  youhui = " + youhui + "/>").addClass(class_price).append(price).appendTo($(".goodsPrice"));
				$(".saleActivity").find("li").eq(0).append("<p>" + sale + "</p>");
				$(".gifts").append("<img src=" + gift + "></img>");
				$("<em/>").addClass(class_num).append(giftNum).appendTo($(".gifts"));
				$(".pingjia").find("a").eq(0).append("<i>" + pingjiaNum + "</i>");
				$(".pingjia").find("a").eq(1).append("<i>" + chengjiao + "</i>");
				$(".limit").append(limit);

				//商品颜色选择
				var ddNode_color = $(".skinInner").find(".color");
				var ulNode_color = $("<ul>");
				ulNode_color.appendTo(ddNode_color);
				$.each(obj.colors, function() {
					$("<li><span>" + this.info + "<span><i></i></li>").appendTo(ulNode_color);
				});
				ulNode_color.find("li").eq(0).addClass("active");
				ulNode_color.find("li").eq(0).find("i").addClass("active2");

				//颜色类别li点击事件
				$(".color").find("ul").find("li").click(function() {
					$(this).siblings().removeClass("active");
					$(this).siblings().find("i").removeClass("active2");
					$(this).addClass("active");
					$(this).find("i").addClass("active2");
				});

				//套餐选择
				var ddNode_taocan = $(".skinInner").find(".taocan");
				var ulNode_taocan = $("<ul>");
				ulNode_taocan.appendTo(ddNode_taocan);
				//套餐详情explain
				var divNode_explain = $("<div/>");
				divNode_explain.addClass("explain");
				divNode_explain.appendTo(ddNode_taocan)

				$.each(obj.taocan, function(index, res) {
					$("<li><span>" + this.tc + "<span><i></i></li>").appendTo(ulNode_taocan);
					if(index == 0) {
						divNode_explain.append(this.exp);
						ulNode_taocan.find("li").addClass("active");
						ulNode_taocan.find("li").find("i").addClass("active2");
					}

					//套餐选择 li点击事件
					$(".taocan").find("ul").find("li").click(function() {
						$(this).siblings().removeClass("active");
						$(this).siblings().find("i").removeClass("active2");
						$(this).addClass("active");
						$(this).find("i").addClass("active2");

						var i = $(this).index();
						divNode_explain.html(obj.taocan[i].exp);
						$(".priceNum").html(obj.taocan[i].price);
					});

				});


				var hotImg = obj.hotGoods.img;
				var hotTit = obj.hotGoods.title;
				var fuhao = obj.hotGoods.fuhao;
				var hotPrice = obj.hotGoods.price;
				//
				var ulNode_hot = $(".hotGoodsList");

				$.each(obj.hotGoods, function() {
					var liNode_hot = $("<li/>");
					//					console.log(this)
					$("<a href=detailed.html?" + this.id + "><span class=" + this.class_pic +
						"><img src=" + this.img + "/></span><span class=" + this.class_title +
						">" + this.title + "</span</a>").appendTo(liNode_hot);
					$("<p>" + this.fuhao + "<span>" + this.price + "</span></p>").appendTo(liNode_hot);
					liNode_hot.appendTo(ulNode_hot);
				});

			}

			function getItem() {
				var im = document.location.search;
				im = im.replace('?', '');
				return im;
			}

			//点击加入购物车
			$(".addToCartBtn").off().click(function() {
				alert("添加成功");
				var goodsImg = $(".imgIist").find("ul").find("li").eq(0).html();
				var goodsName = $(".center_goodsMsg").find("h3").find("i").html();
				var goodsColor = $(".center_goodsMsg").find(".color").find("li.active").find("span").text();
				var goodsTaocan = $(".center_goodsMsg").find(".taocan").find("li.active").find("span").text();
				var goodsPrice = $(".center_goodsMsg").find("em.priceNum").text();
				var goodsNumber = parseInt($(".center_goodsMsg").find("input.amount").val());
				var gooodsyouhui = $(".center_goodsMsg").find("em.priceNum").attr("youhui");
				var goodsId = getItem()
				console.log(goodsNumber)
					//获取之前保存在cookie中的购物车信息
				var arr = $.cookie("cart") ? JSON.parse($.cookie("cart")) : [];
				//遍历查找是否之前的购物车cookie中存在即将添加的商品

				var isExist = false; //表示是否存在该商品
				for(var i = 0; i < arr.length; i++) {
					//如果存在该商品, 把数量增加
					if(goodsId == arr[i].id && goodsColor == arr[i].colors && goodsTaocan == arr[i].taocan) {
						arr[i].num += goodsNumber;
						isExist = true; //表示存在该商品
					}

				}

				//如果不存在, 则添加一个新商品
				if(!isExist) {
					//商品对象
					var goods = {
						img: goodsImg,
						name: goodsName,
						colors: goodsColor,
						taocan: goodsTaocan,
						price: goodsPrice,
						num: goodsNumber,
						youhui: gooodsyouhui,
						id: goodsId
					}
					arr.push(goods);
				}

				//保存到cookie中
				$.cookie("cart", JSON.stringify(arr), {
					expires: 30,
					path: "/"
				});
				//console.log( $.cookie("cart") );
				
				return false;
			})

		}
	})

	//点击首页商品的跳转
	$.get("json/floor.json", function(data) {
		$.each(data.floor_oneMoblie[1], function() {
			$.each(data.floor_oneMoblie[1], function() {
				for(var i = 0; i < data.floor_oneMoblie[1].textImg.length; i++) {
					var id = getItem();
					if(id == data.floor_oneMoblie[1].textImg[i].id) {

						var obj = data.floor_oneMoblie[1].textImg[i];
						var Id = data.floor_oneMoblie[1].textImg[i].id;
						//=================商品展示图=====================
						var bigsrc = obj.bigImg[0].img;
						var bigsrcClass = obj.bigImg[0]._class;

						var divNode_bigImg = $(".bigImg");
						var divNode_bigArea = $("#bigArea");
						$("<img src=" + bigsrc + "/>").appendTo(divNode_bigImg); //添加大图图片
						$("<img src=" + bigsrc + "/>").addClass("_bigImg").appendTo(divNode_bigArea); //添加放大镜的大大图片

						//创建ul li img 获取图片
						var divNode_imgIist = $(".imgIist");
						var ulNode = $("<ul/>");
						ulNode.appendTo(divNode_imgIist);
						$.each(obj.smallImg, function() {
							$("<li><img src=" + this.img + "/></li>").appendTo(ulNode);
						});
						divNode_imgIist.find("li").eq(0).addClass("active"); //给第一个li添加默认样式

						//切换图片
						$(".imgIist ul li").click(function() {
							var i = $(this).index();
							$(".imgIist ul li").removeClass("active");
							$(this).addClass("active");
							$(".bigImg").find("img").attr("src", "img/detail/big_" + Id + (i + 1) + ".jpg");
							$("#bigArea").find("img").attr("src", "img/detail/big_" + Id + (i + 1) + ".jpg");

						});
						
						//放大镜
						var _smallImg = $("#smallImg");
						var _smallArea = $("#smallArea");
						var _bigImg = $("._bigImg");
						var _bigArea = $("#bigArea");

						//==计算小区域宽高
						//==smallArea/bigArea = smallImg/bigImg ( width() and height())
						_smallArea.width(_bigArea.width() * _smallImg.width() / _bigImg.width());
						_smallArea.height(_bigArea.height() * _smallImg.height() / _bigImg.height());

						var scale = _bigImg.width() / _smallImg.width(); //scale = 2

						//==mousemove
						_smallImg.mousemove(function(e) {
							//显示大小区域	
							_smallArea.show();
							_bigArea.show();

							var x = e.pageX - _smallImg.offset().left - _smallArea.width() / 2;
							var y = e.pageY - _smallImg.offset().top - _smallArea.height() / 2;

							//控制范围
							if(x < 0) {
								x = 0;
							} else if(x >= _smallImg.width() - _smallArea.width()) {
								x = _smallImg.width() - _smallArea.width();
							}
							if(y <= 0) {
								y = 0;
							} else if(y >= _smallImg.height() - _smallArea.height()) {
								y = _smallImg.height() - _smallArea.height();
							}

							_smallArea.css({
								left: x,
								top: y
							})

							_bigImg.css({
								left: -x * 2,
								top: -y * 2
							})

						})

						//==mouseleave
						_smallImg.mouseleave(function() {
							//隐藏大小区域
							_smallArea.hide();
							_bigArea.hide();
						})

						//=================商品详细信息=====================
						var tittle = obj.msg[0].tittle;
						var subTittle = obj.msg[0].subTittle;
						var price = obj.msg[0].price;
						var class_price = obj.msg[0].class_price;
						var sale = obj.msg[0].sale;
						var gift = obj.msg[0].gift;
						var giftNum = obj.msg[0].giftNum;
						var class_num = obj.msg[0].class_num;
						var pingjiaNum = obj.msg[0].pingjiaNum;
						var chengjiao = obj.msg[0].chengjiao;
						var limit = obj.msg[0].limit;
						var youhui = obj.msg[0].youhui;

						$(".center_goodsMsg").find("h3").find("i").append(tittle);
						$("<span>" + subTittle + "</span>").appendTo($(".center_goodsMsg").find("h3"));
						$("<em  youhui = " + youhui + "/>").addClass(class_price).append(price).appendTo($(".goodsPrice"));
						$(".saleActivity").find("li").eq(0).append("<p>" + sale + "</p>");
						$(".gifts").append("<img src=" + gift + "></img>");
						$("<em/>").addClass(class_num).append(giftNum).appendTo($(".gifts"));
						$(".pingjia").find("a").eq(0).append("<i>" + pingjiaNum + "</i>");
						$(".pingjia").find("a").eq(1).append("<i>" + chengjiao + "</i>");
						$(".limit").append(limit);

//						//商品颜色选择
//						var ddNode_color = $(".skinInner").find(".color");
//						var ulNode_color = $("<ul>");
//						ulNode_color.appendTo(ddNode_color);
//						$.each(obj.colors, function() {
//							$("<li><span>" + this.info + "<span><i></i></li>").appendTo(ulNode_color);
//						});
//						ulNode_color.find("li").eq(0).addClass("active");
//						ulNode_color.find("li").eq(0).find("i").addClass("active2");
//
//						//套餐选择
//						var ddNode_taocan = $(".skinInner").find(".taocan");
//						var ulNode_taocan = $("<ul>");
//						ulNode_taocan.appendTo(ddNode_taocan);
//						//套餐详情explain
//						var divNode_explain = $("<div/>");
//						divNode_explain.addClass("explain");
//						divNode_explain.appendTo(ddNode_taocan)
						
						
						//商品颜色选择
				var ddNode_color = $(".skinInner").find(".color");
				var ulNode_color = $("<ul>");
				ulNode_color.appendTo(ddNode_color);
				$.each(obj.colors, function() {
					$("<li><span>" + this.info + "<span><i></i></li>").appendTo(ulNode_color);
				});
				ulNode_color.find("li").eq(0).addClass("active");
				ulNode_color.find("li").eq(0).find("i").addClass("active2");

				//颜色类别li点击事件
				$(".color").find("ul").find("li").click(function() {
					$(this).siblings().removeClass("active");
					$(this).siblings().find("i").removeClass("active2");
					$(this).addClass("active");
					$(this).find("i").addClass("active2");
				});

				//套餐选择
				var ddNode_taocan = $(".skinInner").find(".taocan");
				var ulNode_taocan = $("<ul>");
				ulNode_taocan.appendTo(ddNode_taocan);
				//套餐详情explain
				var divNode_explain = $("<div/>");
				divNode_explain.addClass("explain");
				divNode_explain.appendTo(ddNode_taocan)

						
						
						
						
						
						
						
						
						

						$.each(obj.taocan, function(index, res) {
							$("<li><span>" + this.tc + "<span><i></i></li>").appendTo(ulNode_taocan);
							if(index == 0) {
								divNode_explain.append(this.exp);
								ulNode_taocan.find("li").addClass("active");
								ulNode_taocan.find("li").find("i").addClass("active2");
							}
						});

						//热门商品
						var hotImg = obj.hotGoods.img;
						var hotTit = obj.hotGoods.title;
						var fuhao = obj.hotGoods.fuhao;
						var hotPrice = obj.hotGoods.price;

						var ulNode_hot = $(".hotGoodsList");
						$.each(obj.hotGoods, function() {
							var liNode_hot = $("<li/>");
							$("<a href=detailed.html?" + this.id + "><span class=" + this.class_pic +
								"><img src=" + this.img + "/></span><span class=" + this.class_title +
								">" + this.title + "</span</a>").appendTo(liNode_hot);
							$("<p>" + this.fuhao + "<span>" + this.price + "</span></p>").appendTo(liNode_hot);
							liNode_hot.appendTo(ulNode_hot);
						});

					}

					function getItem() {
						var im = document.location.search;
						im = im.replace('?', '');
						return im;
					}

					//点击加入购物车
				

				}
			});
		});
	})






	//购买数量
	var amount = $(".amount");
	$(".jian").click(function() {
		amount.val(parseInt(amount.val()) - 1);
		if(parseInt(amount.val()) <= 1) {
			amount.val(1);
		}
	})

	$(".jia").click(function() {
		amount.val(parseInt(amount.val()) + 1);
		if(parseInt(amount.val()) >= $(".limit").html()) {
			amount.val(10);
		}
	})



	//查看所有商品
	$(".allGoods").find("dt").click(function() {
		$(this).next().css("display", "none");
		return false;
	})

	//品牌分类折叠
	$(".goodsBrand").find("dt").click(function() {

		if($(this).css("background-position") == "-23px -602px") {
			$(this).css("background-position", "-23px -570px");
		} else {

			$(this).css("background-position", "-23px -602px");
		}
		$(this).next().toggle();
		return false;
	})
});