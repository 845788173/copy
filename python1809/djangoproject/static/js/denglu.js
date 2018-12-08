$(function(){
			
				$("#username").focus(function(){
					$(".tishi").hide();
					$(".itemd").show();
				})
				$("#yzm").blur(function(){
					var A = $("#yzm").val();
					var B = $("#yzmim").val();
					if(A==B){
						$(".tishi").hide();
					}else{
						$(".tishi").show();
						$(".tishi").html("验证码不正确");
					}
				})
				 // 给验证码添加颜色 
			    onload=function(){
			    	var spa = document.getElementById("yzmim")
			        var str=""
			        for(var i=0;i<4;i++){
			            var math=parseInt(Math.random()*10)%2;
			            if(math){
			                str+=parseInt(Math.random()*10);
			            }else{
			                str += String.fromCharCode(parseInt(Math.random()*26 + 65))
			            }
			        }
			        spa.value=str;
			        spa.style.color="rgb(" + parseInt(Math.random()*256) + "," + parseInt(Math.random()*256) + "," + parseInt(Math.random()*256) + ")"
			        
			    }
				//点击登录按钮
				$("#denglu").click(function(){
					
					//获取cookie中注册过的所有用户
					var users = $.cookie("users"); 
					if (users) {
						users = JSON.parse(users);
						
						//遍历查找是否有匹配的用户
						var isExist = false; //表示是否存在该用户
						for (var i=0; i<users.length; i++) {
							if ( $("#username").val() == users[i].name && $("#pass").val() == users[i].pwd ) {
								console.log('h')
								isExist = true; //表示存在该用户
					            $.cookie("log",users[i].name,{expires:30, path:"/"})
					            location.href="zhuye.html?"+users[i].name;
							}
						}
						
						if (!isExist) {
							$(".tishi").show();
							$(".tishi").html("用户名或密码错误")
							return;
						}
						
					}
					
					var A = $("#yzm").val();
					var B = $("#yzmim").val();
					if(A==B){
						
					}
					else{
						
						return;
					}
					
					
				})
				
			})