$(function(){
		//给楼层添加数据   	         
				$.get({
					"url":"../json/floor.json",
					"success":function(res){					
						//更新界面的回调函数
						callBack(res);
						onAA();
					}
				})
				
				function callBack(json2){
					$.each(json2,function(index2,data2){ //第几楼
						//console.log(data2)
						var floor = $(".floorright").eq(index2);
						json1 = data2;
						
						$.each(json1,function(index1,data1){
							//console.log(data1)
							var ulNode1 = floor.find('.floorpro').eq(index1);
							json = data1;
							//data 是json里面的每一个单独对象
							$.each(json,function(index,data){
								var liNode = $("<div/>").attr("class","floor_pro");
								var aNode = $('<a/>').attr("href","spxq.html?"+data.id);
								aNode.appendTo(liNode);
								$("<img/>").attr("src",data.img).appendTo(aNode);
								$("<p/>").text(data.concent).attr("class","concent").appendTo(liNode);
								$("<p/>").text("利群价：￥"+data.price).attr("class","price").appendTo(liNode)
								ulNode1.append(liNode);
							})
						})
					})
				} 
				// 给商品添加切换效果
				function onAA(){
					$(".floorpro:first-child").show();
	    	    	$(".floorTop ul li:first-child").addClass("bor"); 	    	
					$(".floorTop li").mouseover(function(){ 
						var index = $(this).index();
						$(this).parents(".floorright").find(".floorpro").eq(index).show().siblings().hide();  
	    	    	    $(this).find(".jiao").show().parent().siblings().find(".jiao").hide();
	    	    	    $(this).removeClass("bor").addClass("bor").siblings().removeClass("bor");
					})
				}
				
				// 楼梯效果
				/*
					思路：
						1、给window绑定scroll事件
							1）当滚动到一定距离时，显示导航条
							2）当滚动到楼层对应位置时，高亮显示导航条对应楼层
						2、点击导航条，滚动到相应的楼层
						3、返回顶部
				 */
				var liNode = $(".Nav .flashli");
				$(window).scroll(function(){
//					console.log($(this).scrollTop());
					
					var currentTop = $(this).scrollTop()
					//显示楼梯
					if( currentTop>=500 ){
						$(".Nav").show();
					}else {
						$(".Nav").hide();
					}
					$(".floor").each(function(index,ele){				
					//   	currentTop>$(this).offset().top + $(this).outerHeight
						//判断当前的div是否在页面中出现
						//判断对应的楼层
						if(currentTop>=$(this).offset().top-150 &&  currentTop<= $(this).offset().top + $(this).outerHeight()/2){
							//第0个div 对应0 li
							//1          1
						      $(".Nav .flashli").find("img").eq(index+1).hide().parent().siblings().find("img").show();
					          $(".Nav .flashli").find(".hover").eq(index+1).show().parent().siblings().find(".hover").hide();
						}
					})
				})
		    //  给小楼层添加点击事件移动楼层
				liNode.click(function(){				
					//找到滑块的滑动距离
					//等对应楼层offset（）。top
					
					//对应楼层   $('#main div')。eq（this。index（））
					
					//偏移量  offset（）。top
					if($(this).index()==0){
						 $(".Nav .flashli").find("img").eq($(this).index()).hide().parent().siblings().find("img").show();
					     $(".Nav .flashli").find(".hover").eq($(this).index()).show().parent().siblings().find(".hover").hide();
					}else{
						$("body").animate({
						scrollTop:$(".floor").eq( $( this).index()-1).offset().top
						
						//liNode.find("span").addClass("hover");
					});	
                         $(".Nav .flashli").find("img").eq($(this).index()).hide().parent().siblings().find("img").show();
					     $(".Nav .flashli").find(".hover").eq($(this).index()).show().parent().siblings().find(".hover").hide();
					}
									
					
				
				})
				//   给回到顶部添加事件
				$(".last").on("click",function(){				
					$("body").animate({
						scrollTop:$(".top").offset().top
					});
				}).on("mouseover",function(){
					$(this).find("img").hide();
					$(this).find(".hover").show()
				}).on("mouseout",function(){
					$(this).find("img").show();
					$(this).find(".hover").hide()
				})
				//  给所有小小楼层添加移入移除事件
				liNode.on("mouseover",function(){
					liNode.find("img").eq($(this).index()).hide();
					liNode.find(".hover").eq($(this).index()).show()
				}).on("mouseout",function(){
					liNode.find("img").eq($(this).index()).show();
					liNode.find(".hover").eq($(this).index()).hide()
				})
				
       //  给最左侧的图 添加移入换图事件
             $(".smaFlash li:first-child").css({
             	"background":"white"
             })
             $(".bigFlash li:first-child").show();
             
             $(".smaFlash li").mouseenter(function(){
             	  $(this).css({
             	  	"background":"white"
             	  	}).siblings().css({
             	  		"background":"#CEB9BE"
             	  	})
             	  var index = $(this).index();
             	  $(this).parents(".floorF").find(".bigFlash").find("li").eq(index).show().siblings().hide();
             })
             
            
             
})
