$(function() {

	$(".btn").click(function() {
		//判断是否输入用户名和密码，并给出提示
		if($("._input").val() == "") {
			$(this).parent().find(".tipsBox").css("display", "block");
		} else if($(".pwd").val() == "") {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("请填写正确的密码");;
		}

		//获取cookie中注册过的所有用户
		var users = $.cookie("namePwd");
		if(users) {
			users = users.split("?");
			//遍历cookie数据
			for(var i = 0; i < users.length; i++) {
				var users1 = users[i].split(",");
				//遍历查找是否有匹配的用户
				if(users1[0] == $(".name").val() && users1[1] == $(".pwd").val()) {
					//表示存在该用户
					var isExist = true;

					//存储已登录的用户
					$.cookie('yideng', $(".name").val(), {
							expires: 7,
							path: "/"
					})
					//匹配成功跳转到首页
					setTimeout(function() {
						window.location.href = 'index.html';
					}, 1000)
				} else if(users1[0] == $(".name").val() && users1[1] != $(".pwd").val()) {
					$(".content").find(".tipsBox").css("display", "block").find("span").text("请填写正确的密码");
				} else{
					$(".content").find(".tipsBox").css("display", "block").find("span").text("请输入正确的用户名和密码");
				}
			}
		}

	})

})