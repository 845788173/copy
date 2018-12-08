$(function () {
    var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        effect: 'flip',
        grabCursor: true,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev'
    });

    $(".top").find("a").on("mouseover", function () {
        $(this).css({"color": "red"})
    }).on("mouseout", function () {
        $(this).css({"color": "black"})
    })
    $(".list>li").on("mouseover", function () {
        $(this).css({"color": "red"})
    }).on("mouseout", function () {
        $(this).css({"color": "black"})
    })
    $(".list").find("#li2").on("mouseover", function () {
        $(this).find("#list2").show()
        $("#list2").find("li").css({"color": "black"})
        $("#list2").find("#lione").css({"color": "red"})
    }).on("mouseout", function () {
        $(this).find("#list2").hide()
    })

    //给二维码添加 添加图片事件
    $(".list").find("#img1").on("mouseover", function () {
        var Img = $("<img />").attr("src", "static/img/code_small.jpg").attr("id", "img3");
        Img.css({"position": "absolute", "top": 25, "right": 130})
        $("body").append(Img);
    }).on("mouseout", function () {
        $("#img3").remove()
    })

    //给li添加变色效果
    $("#Hov .hover").on("mouseover", function () {
        $(this).css({"color": "red"})
    }).on("mouseout", function () {
        $(this).css({"color": "black"})
    })

    //  给导航添加变色效果
    $("#Lis>li").on("mouseover", function () {
        $(this).css({"color": "red"})
    }).on("mouseout", function () {
        $(this).css({"color": "black"})
    })
    //给第一个 添加固定颜色
    $("#Lis #shou").css({"color": "red"});

    //给所有的a标签添加下划线
    $(".lieb a").on("mouseover", function () {
        $(this).css({"text-decoration": "underline"})
    }).on("mouseout", function () {
        $(this).css({"text-decoration": "none"})
    })
    // 主页大轮播图
    //1, 获取数据
    // 			$.get("../json/zhuyelunbo.json", function(data){
    //
    // 				//console.log(data);
    //
    // 				//2, 显示数据到页面上
    // 				//遍历data数组, 将每个图片显示在页面上
    // 				for (var i=0; i<data.length; i++) {
    // 					var obj = data[i];
    // 					var img = obj.img; //img
    // 					var id = obj.id; //id
    //
    // 					//将创建的节点添加到页面上
    // 					$("#flash").append( "<li><img src=" + img +" /></li>" );
    // 					$("#flash2").append( "<li>" + (i+1) + "</li>" );
    //
    // 					//初始化把第一个li的样式变成选中状态
    // 					if (i == 0) {
    // 						$("#flash2 li").addClass("active");
    // 					}
    // 				}
    //
    // 				//开启自动轮播
    // 				lunbo();
    // 			})
    //
    //
    // 			//轮播图
    // 			function lunbo() {
    // 				//
    // 				var _list1 = $("#flash");
    // 				var _list2 = $("#flash2");
    // 				var _li1 = $("#flash li");
    // 				var _li2 = $("#flash2 li");
    //
    // 				//复制第1张图到最后
    // 				_li1.first().clone().appendTo(_list1);
    //
    // 				var size = $("#flash li").length;
    // 				//console.log(size); //9
    //
    // 				var i = 0; //即将显示的图片的下标
    //
    // 				//开启定时器, 自动轮播
    // 				var timer = setInterval(function(){
    // 					i++;
    // 					move();
    // 				}, 3000);
    //
    // 				//移动
    // 				function move(){
    //
    // 					//如果超出左边界
    // 					if (i < 0) {
    // 						_list1.css("left", -(size-1)*740); //瞬间移动到第5张图(i=4的图片)
    // 						i = size-2; //即将移动到第4张图(i=3的图)
    // 					}
    //
    // 					//如果超出右边界
    // 					if (i >= size) {
    // 						_list1.css("left", 0); //瞬间移动到第1张图(非动画)
    // 						i = 1; //即将移动到第2张图(i=1的图)
    // 					}
    //
    // 					//动画移动
    // 					_list1.stop().animate({left: -i*740}, 500);
    //
    // 					//更改按钮的选中状态
    // 					_li2.removeClass().eq(i).addClass("active");
    // 					if (i == size-1) {
    // 						_li2.removeClass().eq(0).addClass("active");
    // 					}
    // 				}
    //
    //
    // 				//按钮的移入事件
    // 				_li2.mouseenter(function(){
    // 					i = $(this).index();
    // 					move();
    // 				})
    //
    //
    // 				$(".tu").hover(
    // 					function(){ //mouseenter
    // 						clearInterval(timer); //停止定时器
    // 					},
    // 					function(){ //mouseleave
    // 						clearInterval(timer);
    // 						timer = setInterval(function(){
    // 							i++;
    // 							move();
    // 						}, 3000)
    //
    // 				})
    //
    // 			}
    //
    // 	//  大图下面的长轮播图
    // 	        var list1 = $("#Bigarea");
    // 			var li1 = $("#Bigarea li");
    //
    // 			//复制第1张图到最后
    // 			li1.eq(0).clone().appendTo(list1);
    // 			li1.eq(1).clone().appendTo(list1);
    // 			li1.eq(2).clone().appendTo(list1);
    // 			li1.eq(3).clone().appendTo(list1);
    //
    //
    // 			var size = $("#Bigarea li").length;
    // 			//console.log(size); //16
    //
    // 			var i = 0; //即将显示的图片的下标
    //
    // 			//开启定时器, 自动轮播
    // 			var timer = setInterval(function(){
    // 				i++;
    // 				move();
    // 			}, 800);
    //
    // 			//移动
    // 			function move(){
    //
    // 				//如果超出左边界
    // 				if (i < 0) {
    // 					list1.css("left", -3024); //瞬间移动到第5张图(i=4的图片)
    // 					i = 13; //即将移动到第4张图(i=3的图)
    // 				}
    //
    // 				//如果超出右边界
    // 				if (i >= size-4) {
    // 					list1.css("left", 0); //瞬间移动到第1张图(非动画)
    // 					i = 1; //即将移动到第2张图(i=1的图)
    // 				}
    //
    // 				//动画移动
    // 				list1.stop().animate({left: -(Math.ceil(i/4))*1008}, 500);
    //
    // 			}
    //
    // 			//上一页
    // 			$("#prev").click(function(){
    // 				i-=4;
    // 				move();
    // 			})
    //
    // 			//下一页
    // 			$("#next").click(function(){
    // 				i+=4;
    // 				move();
    // 			})
    //
    // 			$(".promarea").hover(
    // 				function(){ //mouseenter
    // 					clearInterval(timer); //停止时器
    // 				},
    // 				function(){ //mouseleave
    // 					clearInterval(timer);
    // 					timer = setInterval(function(){
    // 						i++;
    // 						move();
    // 					}, 3000)
    //
    // 			})

    //  给列表添加二级菜单
    $("#list li").mouseenter(function () {
        $(this).css({
            "background": "#b1191b"
        })
        $(this).find(".header-pop").show();
    })
    $("#list li").mouseleave(function () {
        $(this).css({
            "background": "#C81622"
        })
        $(this).find(".header-pop").hide();
    })

    //  添加用户名
    var URL = location.search.replace("?", "");
    if (URL) {
        user = URL;
        $("#us").html(user).css({
            "color": "blue"
        });
        $("#hi").parent("p").find("a").hide();
        $("<a/>").html("退出").attr("id", "exit").css({
            "color": "blue"
        }).appendTo($("#hi").parent("p"))

        $("#exit").click(function () {
            $("#hi").parent("p").find("a").show();
            $(this).hide()
            $.cookie("log", "", {expires: 30, path: "/"})
            $("#us").html("")
        })
        $("#exit").mouseenter(function () {
            $(this).css({
                "color": "red"
            })
        })
        $("#exit").mouseleave(function () {
            $(this).css({
                "color": "blue"
            })
        })
    }

})
