$(function() {
	$("input").focus(function() {
		$(this).css("border", "1px solid #c00")
	})

	$("input").blur(function() {
		$(this).css("border", "1px solid #ccc")
	})

	//======手机号码验证
	var phone = false;
	var code = false;
	var pwd1 = false;
	var pwd2 = false;
	$(".number").blur(function() {
		reg = /^[1-3]{3}\d{8}$/
		var phonenum = $(this).val()
		if(phonenum == "") {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("请填写手机号码");
			$(this).parent().find(".right_tips").css("display", "none")
		} else if(!reg.test(phonenum)) {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("请填写有效的11位手机号码");
			$(this).parent().find(".right_tips").css("display", "none")
		} else if($.cookie("namePwd")) {
			str = $.cookie("namePwd").split("?")
			for(var i = 0; i < str.length; i++) {
				console.log(str[i])
				var str1 = str[i].split(",");

				if(str1[0] == $(".number").val()) {
					$(this).parent().find(".tipsBox").css("display", "block").find("span").text("此用户已注册");
					$(this).parent().find(".right_tips").css("display", "none");
					phone = false;

				} else {
					$(this).parent().find(".tipsBox").css("display", "none")
					$(this).parent().find(".right_tips").css("display", "block");
					phone = true;
				}
			}
		} else {
			$(this).parent().find(".tipsBox").css("display", "none")
			$(this).parent().find(".right_tips").css("display", "block");
			phone = true;
		}
	});

	//图片验证码
	var code = "";
	
	//随机获取验证码是函数
	function getcode() {
		$.get("json/captcha.json", function(data) {
			//定义一个数组，存放json的数据
			var arr = [];
			//随机产生一个0-9的的数字
			var Id = parseInt(Math.random() * 10); 
			//遍历数据存放到数组中
			$.each(data, function() {
				arr.push({
					Img: this.img,
					Val: this.val
				});
			})
			$(".captcha").css('background', "url(" + arr[Id].Img + ")");
			code = arr[Id].Val;
		})
	}
	getcode();
	
	//点击验证码图片，或换一张，验证码改变
	$(".captcha,.chang ,.rgt_btn ").click(function() {
		getcode();
		return false;
	});

	$(".code").blur(function() {
		if($(this).val() == "") {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("请填写图片验证码");
			$(this).parent().find(".right_tips").css("display", "none")
		} else if($(this).val() != code) {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("请填写正确的图片验证码");
			$(this).parent().find(".right_tips").css("display", "none")
		} else {
			$(this).parent().find(".tipsBox").css("display", "none");
			$(this).parent().find(".right_tips").css("display", "block");
			code = true;
		}
	});

	//密码
	$(".pwd_first").blur(function() {
		var reg = /^[a-zA-Z0-9]{6,16}$/
		var pwd = $(this).val()
		if(pwd == "") {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("请输入密码");
			$(this).parent().find(".right_tips").css("display", "none")
		} else if(!reg.test(pwd)) {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("6-16位字符，可使用字母、数字组合");
			$(this).parent().find(".right_tips").css("display", "none")
		} else if(/^[0-9]{6,16}$/.test(pwd)) {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("密码不能全是数字");
			$(this).parent().find(".right_tips").css("display", "none")
		} else {
			$(this).parent().find(".tipsBox").css("display", "none")
			$(this).parent().find(".right_tips").css("display", "block");
			pwd1 = true;
		}
	})

	//再次输入密码
	$(".pwd_again").blur(function() {
		if($(this).val() == "") {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("请填写确认密码");
			$(this).parent().find(".right_tips").css("display", "none");
		} else if($(this).val() != $(".pwd_first").val()) {
			$(this).parent().find(".tipsBox").css("display", "block").find("span").text("两次填写的密码不一致");
			$(this).parent().find(".right_tips").css("display", "none")
		} else {
			$(this).parent().find(".tipsBox").css("display", "none")
			$(this).parent().find(".right_tips").css("display", "block");
			pwd2 = true;
		}
	})

	//注册按钮
	$(".rgt_btn").click(function() {

		var rgts = true;
		//复选框没勾选，弹出提示框
		if(!$(".check").is(":checked")) {
			alert("请先阅读用户协议");
			rgts = false;
			return;
		}

		$(".rgt_btn").val("正在注册...");
		setTimeout(function() {
			$(".rgt_btn").val("注册")
		}, 1000)

		if(phone == false || code == false || pwd1 == false || pwd2 == false) {
			setTimeout(function() {
				alert("注册失败！请填写完整信息")
			}, 1500)
		} else {
			alert("注册成功");
			var str = null;

			//注册成功，存储cookie
			//cookie存在，添加数据
			if($.cookie("namePwd")) {
				str = $.cookie("namePwd");
				str += "?" + $(".number").val() + "," + $(".pwd_first").val();
			} else {
				str = $(".number").val() + "," + $(".pwd_first").val();
			}
			$.cookie("namePwd", str, {expires: 7,path: "/"});

			//注册成功，跳转到登陆界面
			setTimeout(function() {
				window.location.href = 'login.html';
			}, 1500)

		}
	})

})