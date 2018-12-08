$(function(){
	//给 所有的a标签添加移入事件
	$(".top").find("a").on("mouseover",function(){
		$(this).css({"color":"red"})
	}).on("mouseout",function(){
		$(this).css({"color":"black"})
	})
	$(".list>li").on("mouseover",function(){
		$(this).css({"color":"red"})
	}).on("mouseout",function(){
		$(this).css({"color":"black"})
	})
		$(".list").find("#li2").on("mouseover",function(){
		   $(this).find("#list2").show()
		   $("#list2").find("li").css({"color":"black"})
		   $("#list2").find("#lione").css({"color":"red"})
	}).on("mouseout",function(){$(this).find("#list2").hide()})
	
	//给二维码添加 添加图片事件
	$(".list").find("#img1").on("mouseover",function(){
		var Img = $("<img />").attr("src","/static/img/code_small.jpg").attr("id","img3");
		Img.css({"position":"absolute","top":25,"right":130})
		$("body").append(Img);
	}).on("mouseout",function(){$("#img3").remove()})
		
	 
	 //回到顶部
	 $("#btn").on("click",function(){
	 	   $("body").animate({
			        scrollTop:$(".top").offset().top			        
				},400);				
	})
	 var height = document.documentElement.clientHeight/2;
	$(".fix").css({
		"top":height+$("body").scrollTop()-$('.fix').height()/2,
		"right":10
	})
	//给body添加滚动事件 让fix 始终居中
	window.onscroll=function(){
		var height = document.documentElement.clientHeight/2;
		$(".fix").animate({
             "top":height+$("body").scrollTop()-$('.fix').height()/2,
             "right":10
		},10)
	}
    window.onresize=function(){
		var height = document.documentElement.clientHeight/2;
		$(".fix").animate({
             "top":height+$("body").scrollTop()-$('.fix').height()/2,
             "right":10
		},10)
	}
   // 给验证码添加颜色 
    onload=function(){
    	var spa = document.getElementById("yzm")
        var str=""
        for(var i=0;i<4;i++){
            var math=parseInt(Math.random()*10)%2;
            if(math){
                str+=parseInt(Math.random()*10);
            }else{
                str += String.fromCharCode(parseInt(Math.random()*26 + 65))
            }
        }
        spa.innerHTML=str;
        spa.style.color="rgb(" + parseInt(Math.random()*256) + "," + parseInt(Math.random()*256) + "," + parseInt(Math.random()*256) + ")"

    }
    
     $("#inp1").on("focus",function(){
	 	   var pNode = $("<p></p>").html(" 请输入邮箱/手机号").addClass("active").attr("id","pp")
	 	   $(".username").eq(0).append(pNode);
	 	   $(".ite").find(".IMG").eq(0).attr("src","/static/img/QQ图片20160925150151.png")
	 }).on("blur",function(){
	 	$(".active").remove();
	 	var pNode = $("<p></p>").addClass("active").attr("id","pp")
	 	$(".username").eq(0).append(pNode);	
	 	var a =  $("#inp1").val();
	 	var pat=/^[^\d]\w+$/;
	 	if(a.length>=6&&a.length<=20){
            if(pat.test(a)){
               $(".ite").find(".IMG").eq($(this).index()).attr("src","/static/img/QQ图片.png")
               $(".active").remove();
            }else{
                pNode.html("用户名只能包含数字、字母、下划线, 且不能以数字开头");
            }
        }else{
          pNode.html("用户名至少为6-20位")
        }
	 })
	 
	 $("#inp2").on("focus",function(){
	 	   var pNode = $("<p></p>").html("6-20位字符，可使用字母、数字或符号的组合，不建议使用纯数字，纯字母，纯符号").addClass("active1").attr("id","pp")
	 	   $(".username").eq(1).append(pNode);
	 	   $(".ite").find(".IMG").eq(1).attr("src","/static/img/QQ图片20160925150314.png")
	 }).on("blur",function(){
	 	$(".active1").remove();
	 	var pNode = $("<p></p>").addClass("active").attr("id","pp")
	 	$(".username").eq(1).append(pNode);
	 	var a =  $("#inp2").val();
	 	if(a.length>=6&&a.length<11){
	 		$(".ite").find(".IMG").eq(1).attr("src","/static/img/QQ图片.png")
            pNode.html("当前密码等级过低");
            $(".agre").show(); 
            $(".col li").eq(0).css({
            	"background":"orange"
            }).siblings().css({
            	"background":"#929292"
            })
	 	}
	 	if(a.length>=11&&a.length<15){
	 		$(".ite").find(".IMG").eq(1).attr("src","/static/img/QQ图片.png")
            pNode.html("当前密码等级中");
            $(".agre").show(); 
            $(".col li").eq(1).css({
            	"background":"orange"
            }).siblings().css({
            	"background":"#929292"
            })
	 	}
	 	if(a.length>=15&&a.length<=20){
	 		$(".ite").find(".IMG").eq(1).attr("src","/static/img/QQ图片.png")
            $(".active").remove();
            $(".agre").show(); 
            $(".col li").eq(2).css({
            	"background":"orange"
            }).siblings().css({
            	"background":"#929292"
            })
	 	}
	 	if(a.length>20||a.length<6){
            pNode.html("密码长度必须为6-20位")
	 	}
	 })
	 
	 //给li添加变色效果
	 $("#Hov .hover").on("mouseover",function(){
		$(this).css({"color":"red"})
	}).on("mouseout",function(){
		$(this).css({"color":"black"})
	})
	 
	 $("#inp3").on("focus",function(){
	 	   var pNode = $("<p></p>").html(" 请再次输入密码").addClass("active").attr("id","pp")
	 	   $(".username").eq(2).append(pNode);	
	 	   $(".ite").find(".IMG").eq(2).attr("src","/static/img/QQ图片20160925150314.png")
	 }).on("blur",function(){
	 	$(".active").remove();
	 	var pNode = $("<p></p>").addClass("active").attr("id","pp")
	 	$(".username").eq(2).append(pNode);	
	 	var a =  $("#inp2").val();
	 	var b =  $("#inp3").val();
	 	if(a!=""){	 		
	 		if(a==b){
	 		    $(".ite").find(".IMG").eq(2).attr("src","/static/img/QQ图片.png");
	 		    $(".active").remove();
		 	}else{
		 		pNode.html("两次密码不一致")
		 	}
	 	}else{
	 		$("#pp").eq(2).remove()
	 	}
	 	
	 })
	 
   
    $("#inp").click(function(){
    	//给输入框添加提示信息  判断正则
	 	var a =  $("#inp1").val();
	 	var pat=/^[^\d]\w+$/;
	 	if(a.length>=6&&a.length<=20){
            if(pat.test(a)){
             
            }else{
                return;
            }
        }else{
          return;
        }
	 
	
	 	var b =  $("#inp2").val();
	 	if(b.length>=6&&b.length<=20){
	 		
	 	}
	 	if(b.length>20||b.length<6){
            pNode.html("密码长度必须为6-20位");
            return;
	 	}
	 
	 	var c =  $("#inp3").val();
	 	if(b!=""&&c!=""){
	 	   if(b==c){
	 		
		 	}else{	 	
		 		return;
		 	}	
	 	}else{
	 		return;
	 	}
	 	
	 
	 var A = $("#inp4").val();
	 var B = $("#yzm").text();
	 if(A==B){
	 	
	 }else{
	 	return;
	 }
	 
	 if($(':checkbox').prop('checked')){
	 	
	 }else{
	 	return;
	 }
	
	//先获取之前保存在cookie中的用户
	var users = $.cookie("users") ? JSON.parse($.cookie("users")) : [];
	
	//遍历users数组, 判断是否存在该用户,如果存在则不能注册
	for(var i=0; i<users.length; i++) {
		if ( $("#inp1").val() == users[i].name ) {
			alert("该用户已经存在, 不能注册!");
			return;
		}
	}
	
	//需要注册的用户(需要保存到cookie中的用户)
	var user = {
		name: $("#inp1").val(), //用户名
		pwd: $("#inp2").val() //密码
	}
	users.push(user); //添加新用户
	
	//保存到cookie中
	$.cookie("users", JSON.stringify(users), {expires:30, path:"/"});
	     location.href="denglu.html"
    })
    
    
})
