$(function() {
	//动态获取商城公告信息
	$.get("json/boards_list.json",function(msg){
		var ulNode_boards = $("#boards_list");
		$.each(msg,function(){
			if(this._class == "boards_info"){
				var liNode = $("<li/>");
				$("<a href="+this.url+">"+this.info+"</a>").appendTo(liNode);
				liNode.appendTo(ulNode_boards);
			}
		});
	});
	
	//获取各楼层的信息
	$.get("json/floor.json", function(data) {
		//获取精品图片img
		var ulNode_groupImg = $("#groupImg");
		$.each(data.groupBout, function() {
			//				console.log(this)
			var liNode = $("<li/>");
			$("<i/>").appendTo(liNode);
			$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
			liNode.appendTo(ulNode_groupImg);
		})

		//获取广告图片
		var divNode = $(".banner");
		$.each(data.banner, function() {
			$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(divNode);
		})

		var divNode = $(".banner2");
		$.each(data.banner2, function() {
			$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(divNode);
		})

		//特色购
		var ulNode_spBuy = $("#spBuy_List");
		$.each(data.specialBuy, function() {
			//				console.log(this)
			var liNode = $("<li/>");
			$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
			liNode.appendTo(ulNode_spBuy);

			liNode.find("a").find("img").addClass(this._class)
		})

		//oneF
		$.each(data.floor_oneMoblie, function() {
			var divNOde_big = $(".floor_oneMoblie").find(".top").find(".big");
			$.each(this.big, function() {
				$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(divNOde_big);
			})

			var ulNode_mobList = $("#moblie_list")
			var x = 0;
			$.each(this.textImg, function() {
				var liNode = $("<li/>");

				if(x == 0) {
					liNode.addClass("tall");
				}
				if(x == 1) {
					liNode.addClass("tall");
				}
				x++;

				$("<a href=detailed.html?" + this.id + ">" + this.aText + "</a><p>" + this.pText + "</p><a href=detailed.html?" + this.id + "><img src=" + this.img + "></a>").appendTo(liNode);

				liNode.appendTo(ulNode_mobList)
				liNode.addClass("item");

			});

			var ulNode_logo = $(".floor_oneMoblie").find(".bottom").find(".boardsLogo_list");
			$.each(this.logoImg, function() {
				var liNode = $("<li/>");
				$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
				ulNode_logo.append(liNode);
			});
		});

		//twoF	
		$.each(data.floor_twoComputer, function() {

			var divNOde_big = $(".floor_twoComputer").find(".top").find(".big");
			$.each(this.big, function() {
				$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(divNOde_big);
			})

			var ulNode_comList = $("#computer_list")
			var x = 0;
			$.each(this.textImg, function() {
				var liNode = $("<li/>");

				if(x == 0) {
					liNode.addClass("tall");
				}
				if(x == 1) {
					liNode.addClass("tall");
				}
				x++;

				//				console.log(x++);
				$("<a href=" + this.url + ">" + this.aText + "</a><p>" + this.pText + "</p><a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
				liNode.appendTo(ulNode_comList)
				liNode.addClass("item");
			});

			var ulNode_logo = $(".floor_twoComputer").find(".bottom").find(".boardsLogo_list");
			$.each(this.logoImg, function() {
				var liNode = $("<li/>");
				$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
				ulNode_logo.append(liNode);
			});
		});

		//threeF
		$.each(data.floor_threeDigital, function() {

			var divNOde_big = $(".floor_threeDigital").find(".top").find(".big");
			$.each(this.big, function() {
				$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(divNOde_big);
			})

			var ulNode_digList = $("#digital_list")
			var x = 0;
			$.each(this.textImg, function() {
				var liNode = $("<li/>");

				if(x == 0) {
					liNode.addClass("tall");
				}
				if(x == 1) {
					liNode.addClass("tall");
				}
				x++;

				//				console.log(x++);
				$("<a href=" + this.url + ">" + this.aText + "</a><p>" + this.pText + "</p><a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
				liNode.appendTo(ulNode_digList)
				liNode.addClass("item");
			});

			var ulNode_logo = $(".floor_threeDigital").find(".bottom").find(".boardsLogo_list");
			$.each(this.logoImg, function() {
				var liNode = $("<li/>");
				$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
				ulNode_logo.append(liNode);
			});
		});

		//fourF
		$.each(data.floor_fourDiy, function() {

			var divNOde_big = $(".floor_fourDiy").find(".top").find(".big");
			$.each(this.big, function() {
				$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(divNOde_big);
			})

			var ulNode_diyList = $("#diy_list")
			var x = 0;
			$.each(this.textImg, function() {
				var liNode = $("<li/>");

				if(x == 0) {
					liNode.addClass("tall");
				}
				if(x == 1) {
					liNode.addClass("tall");
				}
				x++;

				//				console.log(x++);
				$("<a href=" + this.url + ">" + this.aText + "</a><p>" + this.pText + "</p><a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
				liNode.appendTo(ulNode_diyList)
				liNode.addClass("item");
			});

			var ulNode_logo = $(".floor_fourDiy").find(".bottom").find(".boardsLogo_list");
			$.each(this.logoImg, function() {
				var liNode = $("<li/>");
				$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
				ulNode_logo.append(liNode);
			});
		});
	})

	//===================================================
	//侧边栏移入移出显示二级菜单 
	$($(".sideNav_list")[0].childNodes).hover(function() {
//		console.log(this)
		$(this).find(".two_nav").show();
		$(this).css({
			"background": "#FFF",
			"color": "#333"
		});
		$(this).find("a").css("color", "#333")
	}, function() {
		$(this).find("div").hide();
		$(this).css({
			"background": "#2D2D2D",
			"color": "#FFF"
		});
		$(this).find("a").css("color", "#FFF")
	});

	//===================================================
	//顶部搜索框的隐藏出现
	$(window).on("scroll", function() {
		//console.log($(window).scrollTop());
		if($(window).scrollTop() > 500) {
			$(".topSearchBox").show();
		} else {
			$(".topSearchBox").hide();
		}
	})

	//=======================================================
	//首页的导航
	//1.====动态获取轮播图片获取数据
	$.get("json/lunbo.json", function(data) {
		//2.遍历数据，将图片显示在页面上
		for(var i = 0; i < data.length; i++) {
			var oImg = data[i];
			//创建节点
			$("#lunboImg_list").append("<li><a href=" + oImg.url + "><img src=" + oImg.img + "/></a></li>");
			$("#littleLogo").append("<li>" + (i + 1) + "</li>");
			//状态初始化
			if(i == 0) {
				$("#littleLogo li").addClass("active");
			}
		}
		//启动轮播
		lunboImg();
	});

	//=============轮播图方法
	function lunboImg() {
		var imgList = $("#lunboImg_list");
		var logoList = $("#littleLogo");
		var li1 = $("#lunboImg_list li");
		var li2 = $("#littleLogo li");

		var size = $("#lunboImg_list li").length;
		//console.log(size);
		//确定list 的width，并添加到样式
		var iWidth = $("#lunboImg_list li").width();
		var allWidth = iWidth * size;
		imgList.css("width", allWidth);

		//记录图片下标位置
		var i = 0;
		//启动定时器，移动图片
		var timer = setInterval(function() {
			i++;
			move();
		}, 3000)

		//=========移动动画方法
		function move() {
			//有缝轮播，当下标i>=#lunboImg_list li 的长度，动画回到第一张
			if(i >= size) {
				i = 0;
			} else if(i < 0) {
				i = size-1;
			}

			imgList.stop().animate({
				"left": -i * iWidth
			}, 500);
			
			//小图标选中状态
			li2.removeClass().eq(i).addClass("active");
		}

		//======上下页点击事件
		$("#pre").click(function() {
			i--;
			move();
		})

		$("#next").click(function() {
			i++;
			move();
		})

		//=====小图标移入事件
		li2.mouseenter(function() {
			i = $(this).index();
			move();
		});

		$(".center_img").hover(function() {
			clearInterval(timer);
		}, function() {
			clearInterval(timer);
			timer = setInterval(function() {
				i++;
				move();
			}, 3000)
		})

		//=====上下页按钮的隐藏切换效果
		$(".center_img").hover(function() {

			$(".pre_next").show();
			$(".pre_next").mouseenter(function() {
				$(this).css("background", "rgba(0,0,0,0.2)");
			})
		}, function() {
			$(".pre_next").hide();
			$(".pre_next").mouseleave(function() {
				$(this).css("background", "rgba(0,0,0,0)");
			})
		});
	}

	//=========================================================
	//楼层轮播图
	//1.====动态获取轮播图片获取数据
	$.get("json/floor.json", function(data) {
		//2.遍历数据，将图片显示在页面上
		var ulNode_floLunboList = $(".flo_lunboImgList");

		var lbX = 0;
		$.each(data.floorImg, function() {
			$.each(this, function() {
				var i = 0;
				$.each(this, function() {
					i++;
					//					console.log(this)
					var liNode = $("<li/>");
					$("<a href=" + this.url + "><img src=" + this.img + "/></a>").appendTo(liNode);
					liNode.appendTo(ulNode_floLunboList.eq(lbX));
					$(".flo_tubiaoList").eq(lbX).append("<li/>");

					if(i == 1) {
						$(".flo_tubiaoList").eq(lbX).find("li").eq(0).addClass("active");
					}
				});
				lb();
			});
			lbX++;
		});

		function lb() {

			var imgList = $(".flo_lunboImgList");

			var imgList1 = $(".flo_lunboImgList").eq(1);
			var logoList1 = $(".flo_tubiaoList").eq(1);
			var li1 = imgList1.find("li");
			var li2 = logoList1.find("li");

			var imgList2 = $(".flo_lunboImgList").eq(2);
			var logoList2 = $(".flo_tubiaoList").eq(2);
			var li2_2 = logoList2.find("li");

			var imgList3 = $(".flo_lunboImgList").eq(3);
			var logoList3 = $(".flo_tubiaoList").eq(3);
			var li2_3 = logoList3.find("li");

			var imgList0 = $(".flo_lunboImgList").eq(0);
			var logoList0 = $(".flo_tubiaoList").eq(0);
			var li2_0 = logoList0.find("li");

			var size = $(".flo_lunboImgList").eq(0).find("li").length;

			//确定list 的width，并添加到样式
			var iWidth = li1.width();
			var allWidth = iWidth * size + 3;
			imgList.css("width", allWidth);
			//记录图片下标位置
			var i = 0;

			var timer = setInterval(function() {
				i++;
				move();
			}, 3000);

			//=========移动
			function move() {
				//i>=#lunboImg_list li 的长度，动画回到第一张	
				if(i >= size) {
					i = 0;
				} else if(i < 0) {
					i =size-1;
				}

				//console.log(imgList);
				imgList0.stop().animate({
					"left": -i * iWidth
				}, 500);
				imgList1.stop().animate({
					"left": -i * iWidth
				}, 500);
				imgList2.stop().animate({
					"left": -i * iWidth
				}, 500);
				imgList3.stop().animate({
					"left": -i * iWidth
				}, 500);

				//小图标选中状态
				li2_0.removeClass().eq(i).addClass("active");
				li2.removeClass().eq(i).addClass("active");
				li2_2.removeClass().eq(i).addClass("active");
				li2_3.removeClass().eq(i).addClass("active");

			}

			//======上下页
			$("._pre").click(function() {
				i--;
				move();
			})

			$("._next").click(function() {
				i++;
				move();
			})

			//=====小图标移入事件
			li2.mouseenter(function() {
				i = $(this).index();
				move();
			});

			$(".floor_lunbo").hover(function() {
					clearInterval(timer);
				}, function() {
					clearInterval(timer);
					timer = setInterval(function() {
						i++;
						move();
					}, 3000)
				})
				
			//=====上下页按钮的隐藏切换效果
			$(".floor_lunbo").hover(function() {
				$(".pre_next").show();
				$(".pre_next").mouseenter(function() {
					$(this).css("background", "rgba(0,0,0,0.2)");
				})
			}, function() {
				$(".pre_next").hide();
				$(".pre_next").mouseleave(function() {
					$(this).css("background", "rgba(0,0,0,0)");
				})
			});

		}
	})

});