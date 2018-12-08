$(function(){
	
	//判断是否存在已登录的用户
	if($.cookie("yideng")){
		$('<span>你好，<a href="#">'+$.cookie("yideng")+'</a></span>').appendTo($('.header_login_info'));
		$('<span class="esc"><a href="index.html">退出</a></span>').appendTo($('.header_login_info'));
	}else{
		$('<span>Hi~欢迎来到ZOL商城，请<a href="login.html">登录</a></span>').appendTo($('.header_login_info'));
		$('<span class="last"><a href="register.html">免费注册</a></span>').appendTo($('.header_login_info'));
		
		$(".topNav").find(".header_cart").click(function(){
			window.location.href = 'login.html';
		});
		
		$(".sideBar").find(".header_cart").click(function(){
			window.location.href = 'login.html';
		})
	}
	//退出，清除cookie
	$(".esc").click(function(){
		$.cookie("yideng","",{expires:7,path:"/"})
		window.location.reload();
	});
	
	//header_menu 头部导航，鼠标移入移出事件
	$(".header .header_right_menu ul li").hover(function() {
		$(this).css("background", "#fff")
		$(this).find("div").show();
	}, function() {
		$(this).find("div").hide();
		$(this).css("background", "")
	});
	
	//头部热门搜索动态获取数据
	var ulNode_hot = $("#hot_search"); 
	$.get("json/hot_search.json", function(data) {
		$.each(data, function() {
			if(this._class == "hot_sec") {
				var liNode = $("<li/>"); //创建li节点
				$("<a href=" + this.url + ">" + this.goods + "</a>").appendTo(liNode);
				liNode.appendTo(ulNode_hot);
			}
		});
	});
	
	
	//侧边栏的显示隐藏
	$(".top_tabBox div").hover(function() {
		$(this).css("background-color", "#F33");
		$(this).find(".side_ico").css({
			"background": "#fff",
			"color": "#FF3333"
		});
		$(this).find(".over").stop().show().animate({
			"left": "-70px"
		}, 300);
	}, function() {
		$(this).css("background-color", "#2D2D2D");
		$(this).find(".side_ico").css({
			"color": "#fff",
			"background": "#FF3333"
		});
		$(this).find(".over").stop().hide().css({
			"left": '37px'
		});
	});

	$(".side_back").hover(function() {
		$(this).css("background-color", "#F33");
	}, function() {
		$(this).css("background-color", "#2D2D2D");
	})

	//回到顶部
	$(".side_back").click(function() {
		$("html,body").scrollTop(0);
	})
	
	
	
	
});
