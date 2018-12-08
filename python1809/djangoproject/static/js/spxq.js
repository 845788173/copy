$(function(){
	$('#btn3').click(function(){
		var goodid=$(this).attr('goodid')
		var $that=$(this)
		$.get('/liqun/cartadd/',{goodid:goodid},function(response){
			console.log(response.number)
			if(response.status==-1){
				window.open('/liqun/login/',target="_self")
			}
			else if (response.status==1){
				console.log(1111)
				$that.prev().show().val(response.number)
			}
		})
	})
	$('#btn1').click(function(){
		var goodid=$(this).attr('goodid')
		var $that=$(this)
		$.get('/liqun/subcart/',{goodid: goodid},function (response) {
			if (response.status==1){
				let number=response.number
				$that.next().val(number)
			}

        })
	})


})

// $(function(){
// 				var log = $.cookie("log")
// 				var goodIndex = location.search.replace("?","");
// 				$.get({
// 					"url":"../json/floor.json",
// 					"success":function(res){
// 						//更新界面的回调函数
// 						callBack(res);
// 						onAA();
// 					}
// 				})
//
// 				function callBack(json2){
// 					$.each(json2,function(index2,data2){ //第几楼
// 						json1 = data2;
//
// 						$.each(json1,function(index1,data1){
// 							json = data1;
// 							//data 是json里面的每一个单独对象
// 							$.each(json,function(index,data){
// 								if(goodIndex==data.id){
// 									  var img = $(".mesimg")
// 									  $("<img/>").attr("src",data.img).appendTo(img)
// 									  $(".mesconcent").find("h1").html(data.concent);
// 									  $("#price").html("￥"+data.price);
// 									  $("#tit").html(">"+data.concent)
// 									  $(".blankli2").eq(0).find("img").attr("src",data.img1)
// 									  $(".blankli2").eq(1).find("img").attr("src",data.img2)
// 									  $(".blankli2").eq(2).find("img").attr("src",data.img3)
// 									  $(".blankli2").eq(3).find("img").attr("src",data.img4)
// 									  $(".blankli2").eq(4).find("img").attr("src",data.img5)
// 									  $(".blankli2").eq(0).find("p").html(data.concent1)
// 									  $(".blankli2").eq(1).find("p").html(data.concent2)
// 									  $(".blankli2").eq(2).find("p").html(data.concent3)
// 									  $(".blankli2").eq(3).find("p").html(data.concent4)
// 									  $(".blankli2").eq(4).find("p").html(data.concent5)
// 									  $(".proimg li").eq(0).find("img").eq(0).attr("src",data.img6)
// 									  var big = $("#bigArea")
// 									  $("<img/>").attr({
// 									  	"id":"bigImg",
// 									  	"src":data.img
// 									  }).css({
// 									  	"position": "absolute",
// 									  	"left": "0",
// 									  	"top": "0",
// 									  	"width": "500px",
// 									  	"height": "500px"
// 									  }).appendTo(big)
//
//
// 									   //  放大镜
//                 var _smallImg = $(".mesimg"); //小图
// 				var _smallArea = $("#smallArea"); //小区域
// 				var _bigImg = $("#bigImg"); //大图
// 				var _bigArea = $("#bigArea"); //大区域
// 				//bigImg.width / smallImg.width = bigArea.width/smallArea.width
// 				//smallArea.width = bigArea.width * smallImg.width / bigImg.width
// 				//计算小区域的宽高
// 				//width() == innnerWidth() == outerWidth()
// 				_smallArea.width( _bigArea.width() * _smallImg.width() / _bigImg.width() );
// 				_smallArea.height( _bigArea.height() * _smallImg.height() / _bigImg.height() );
//
// 				//放大系数/放大倍数
// 				var scale = _bigImg.width() / _smallImg.width();
// 				//scale = 4
//
// 				//mousemove
// 				_smallImg.mousemove(function(e){
// 					_smallArea.show();//显示小区域
// 					_bigArea.show();
// 					//clientX: 可视区域的x值
// 					//pageX: 距离窗口左边的x值
// 					var x = e.pageX - _smallImg.offset().left - _smallArea.width()/2;
// 					var y = e.pageY - _smallImg.offset().top - _smallArea.height()/2;
// 					//console.log(e.clientX);
// 					//console.log(e.pageX);
//
// 					//控制小区域范围在小图内
// 					if (x <= 0) { //不超出左边
// 						x = 0;
// 					}
// 					else if (x >= _smallImg.width()-_smallArea.width()) { //不超出右边
// 						x = _smallImg.width()-_smallArea.width();
// 					}
// 					if (y <= 0) { //不超出上边
// 						y = 0;
// 					}
// 					else if (y >= _smallImg.height()-_smallArea.height()) { //不超出下边
// 						y = _smallImg.height()-_smallArea.height();
// 					}
//
//
// 					//移动小区域
// 					_smallArea.css({left: x, top: y});
//
// 					//移动大图
// 					_bigImg.css({left: -x*scale, top: -y*scale});
//
// 				})
//
// 				//mouseleave
// 				_smallImg.mouseleave(function(){
// 					_smallArea.hide();//隐藏小区域
// 					_bigArea.hide();
// 				})
// 								}
// 							})
//
// 						})
// 					})
// 				}
//
// 				function onAA(){
//
// 				}
//           //  给下拉列表添加移入事件
//        $("#sel").mouseenter(function(){
//        	   $(this).parent().find("img").attr("src","../img/brandClassHideMore.png");
//        	   $(this).parent(".selected").css({
//        	   	  "height":52
//        	   })
//        })
//         $("#sel").mouseleave(function(){
//        	   $(this).parent().find("img").attr("src","../img/brandClassShowMore.png");
//        	   $(this).parent(".selected").css({
//        	   	  "height":25
//        	   })
//        })
//
//         //   给商品详情添加介绍切换事假
//         $(".introduce li").eq(0).addClass("intro")
//         $(".introduce li").click(function(){
//         	 $(this).addClass("intro").siblings().removeClass("intro")
//         	 if($(this).index()==1){
//         	 	  $(this).parents().find(".proimg li").eq(0).hide();
//         	 }else{
//         	 	  $(this).parents().find(".proimg li").eq(0).show();
//         	 }
//         })
//
//         // 给商品添加数量增减事假
// 			   var inp1 = document.getElementById("btn1");
// 			   var inp2 = document.getElementById("btn2");
// 			   var inp3 = document.getElementById("btn3");
// 			   var val = parseInt(inp2.value);
// 			   inp3.onclick=function(){
// 			      val+=1;
// 			      inp2.value= val;
// 		     }
// 			   inp1.onclick=function(){
// 			   	  if(val>1){
// 			   	  	val-=1;
// 			   	  	inp2.value= val;
// 			   	  }else{
// 			   	  	return val;
// 			   	  }
// 			   }
//
//
// 			   $("#buy").click(function(){
//
//
// 				// 	//要加入购物车的商品信息
// 				// 	var goodsId = location.search.replace("?","");
// 				// 	var goodsName = $("#goodname").html();
// 				// 	var goodsPrice = $("#price").html();
// 				// 	var goodsImg  = $(".mesimg").html();
// 				// 	var goodsber = $("#btn2").val()
// 				//
// 				//
// 				//
// 				// 	var sb= goodsPrice.slice(1)
// 				// 	var sp =goodsber
// 				// 	var goodsp = (sp*sb).toFixed(2)
// 				// 	//获取之前保存在cookie中的购物车信息
// 				// 	var log = $.cookie("log")
// 				// 	var arr = $.cookie(log+"_cart") ? JSON.parse( $.cookie(log+"_cart") ) : [];
// 				// 	//遍历查找是否之前的购物车cookie中存在即将添加的商品
// 				// 	var isExist = false; //表示是否存在该商品
// 				// 	for(var i=0; i<arr.length; i++) {
// 				// 		//如果存在该商品, 把数量增加
// 				// 		if (goodsName == arr[i].name) {
// 				// 			arr[i].ber=parseInt(goodsber)+parseInt(arr[i].ber);
// 				// 			isExist = true; //表示存在该商品
// 				// 		}
// 				// 	}
// 				//
// 				// 	//如果不存在, 则添加一个新商品
// 				// 	if (!isExist) {
// 				// 		//商品对象
// 				// 		var goods = {
// 				// 			id: goodsId,
// 				// 			img:goodsImg,
// 				// 			name: goodsName,
// 				// 			price: goodsPrice,
// 				// 			ber:goodsber,
// 				// 			sp:goodsp,
// 				// 			//num: 1//商品数量
// 				// 		}
// 				// 		arr.push(goods);
// 				// 	}
// 				//
// 				// 	var log = $.cookie("log")
// 				//
// 				// 	//保存到cookie中
// 				// 	$.cookie(log+"_cart", JSON.stringify(arr), {expires:30, path:"/"});
// 				// 	location.href="gouwuche.html"
// 				})
//     /// 判断是否登录
//         if($.cookie("log")){
//         	user=$.cookie("log")
//         	$("#us").html(user).css({
//         		"color":"blue"
//         	});
//         	$("#hi").parent("p").find("a").hide();
//         	$("<a/>").html("退出").attr("id","exit").css({
//         		"color":"blue"
//         	}).appendTo($("#hi").parent("p"))
//
//         	$("#exit").click(function(){
//         		$("#hi").parent("p").find("a").show();
//         		$(this).hide()
//         		$.cookie("log","",{expires:30, path:"/"})
//         		$("#us").html("")
//         	})
//         	$("#exit").mouseenter(function(){
//         		$(this).css({
//         			"color":"red"
//         		})
//         	})
//         	$("#exit").mouseleave(function(){
//         		$(this).css({
//         			"color":"blue"
//         		})
//         	})
//         }
// })
//
//
