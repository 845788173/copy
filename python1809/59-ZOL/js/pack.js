	
//	各层head导航切换   这是个问题  
/**
 * 导航切换
 */
function headNav(){
		$('.one_way_head').eq(0).find('li').mouseenter(function(){
			$(this).parent().find('li').removeClass('f1_favor');
			$(this).addClass('f1_favor');
		})
		$('.one_way_head').eq(1).find('li').mouseenter(function(){
			$(this).parent().find('li').removeClass('f2_favor');
			$(this).addClass('f2_favor');
		})
		$('.one_way_head').eq(2).find('li').mouseenter(function(){
			$(this).parent().find('li').removeClass('f3_favor');
			$(this).addClass('f3_favor');
		})
		$('.one_way_head').eq(3).find('li').mouseenter(function(){
			$(this).parent().find('li').removeClass('f4_favor');
			$(this).addClass('f4_favor');
		})
}
//	百叶窗也得这样。。。
/**
 * 百叶窗
 */
function shutter(){
	$('.window_shade').eq(0).find('h2').mouseenter(function(){
		$('.window_shade').eq(0).find('dl').stop().slideUp(700);
		$(this).parent().find('dl').stop().slideDown(700);
	})	
	$('.window_shade').eq(1).find('h2').mouseenter(function(){
		$('.window_shade').eq(1).find('dl').stop().slideUp(700);
		$(this).parent().find('dl').stop().slideDown(700);
	})
	$('.window_shade').eq(2).find('h2').mouseenter(function(){
		$('.window_shade').eq(2).find('dl').stop().slideUp(700);
		$(this).parent().find('dl').stop().slideDown(700);
	})	
	$('.window_shade').eq(3).find('h2').mouseenter(function(){
		$('.window_shade').eq(3).find('dl').stop().slideUp(700);
		$(this).parent().find('dl').stop().slideDown(700);
	})	
			
		
}
//	各层楼的轮播 
//	.tbCarousel有多个 然后0 1 3.. 为上下轮播      
/**
 * 楼层中的轮播
 */
//function flCarousel(){
//	var fl_length = $('.tbCarousel').find('ul').length;
//	for(var i=0; i<fl_length; i++){
//		var ele = $('.tbCarousel').find('ul')[i];
//		if(i%2){
//			lCarousel(ele);
//		}
//		else{
//			tCarousel(ele);
//		}
//	}
//}


//   太乱了0.0

	//		搜索栏下边的推荐修改样式
	function  r_choose(){
		var recommend = $('#recommend').find('a');
		recommend.slice(0,4).css('color','#D93600');
		recommend.slice(4).css('color','#666');
	}
	
	

	//移入menu的li上显示对应的详情
	function submenu(){
		$('.menu').find('li').hover(function(){
			if($(this).index()<2){
				$(this).find('.sub_menu').css("top",($(this).height()*-$(this).index()))
			}
			else if($(this).index()<4){
				$(this).find('.sub_menu').css("top",(this.offsetHeight*-$(this).index()))
			}
			else if($(this).index()==4){
				$(this).find('.sub_menu').css("top",-$(this).find('.sub_menu').height() + (this.offsetHeight*4)	  )
			}
			else{
				$(this).find('.sub_menu').css("top",-$(this).find('.sub_menu').height() + this.offsetHeight )
			}
			
			$(this).find('.sub_menu').show();
		},function(){
			$(this).find('.sub_menu').hide();
		})
	}
	
	//透明轮播
	function mian_animate(){
		var i = 0;
		var timer = setInterval(function(){
				i++;
				move();
		},3000)
		$('.carousel').find('a').hover(function(){
			$('.carouselArea .btn').show();
		//移入自身的时候也显示
			$('.carouselArea .btn').mouseenter(function(){
				$('.carouselArea .btn').show();
			})
		},function(){
			$('.carouselArea .btn').hide();
		})
		//鼠标移入时改变
		$('.small_Slider').find('li').hover(function(){
			clearInterval(timer);
			i = $(this).index();
			move();
		},function(){
			timer = setInterval(function(){
				i++;
				move();
			},3000)
		});
		//点击按钮  上一页
		$('.carouselArea .btn').click(function(){
			clearInterval(timer);
			timer = setInterval(function(){
				i++;
				move();
			},3000)
		});
		$('.carouselArea .prev').click(function(){
			var size = $('.carouselArea .carousel').find('li').length;
			i--;
			if(i == -1){
				i=size-1;
			}
			move();
		});
		$('.carouselArea .next').click(function(){
			i++;
			move();
			
		});
		
		//	轮播
		function move(){
			var size = $('.carouselArea .carousel').find('li').length;
			if(i>=size){
				i=0;
			}
			$('.carouselArea .carousel').find('li').stop().animate({
				"opacity":0
			},500).removeClass('active');
			$('.carouselArea .carousel').find('li').eq(i).stop().animate({
				"opacity":1
			},500).addClass('active');
			$('.small_Slider').find('li').removeClass('cur').eq(i).addClass('cur');
		}
	
	}
//	上下轮播
//ele为js节点
	function tCarousel(ele){
	 	var x = 0;
	 	for(var i=0;i<3;i++){
	 		$(ele).find('li').eq(i).clone(true).appendTo($(ele));
	 	}
	 	
	 	var h = $(ele).find('li').height();
		var Cartimer = null;
			clearInterval(Cartimer);
			move();
			
			$(ele).parent().find('span').click(function(){
				clearInterval(Cartimer);
				var size = $(ele).find('li').length;
				if($(this).index()==1){
					x--;
					if(x<=0){
						x = size - 3;
						$(ele).css("top",(-h*(size-2)));
					}
					var y = -h*x;
					startMoves(ele,{top:y})

					move();
				}else{
					x++;
					if(x >= size-2){
						x = 1;
						$(ele).css("top",0);
					}
					var y = -h*x;
					startMoves(ele,{top:y})
					move();
				}
			})
			function move(){

				Cartimer = setInterval(function(){
					x++;
					var size = $(ele).find('li').length;
					if(x >= size-2){
						x = 1;
						$(ele).css("top",0);
					}
					var y = -h*x;
					startMoves(ele,{top:y})
				},3000);
			} 
	}
	
	//	左右轮播
//ele为js节点
	function lCarousel(ele){
	 	var x = 0;
//	 	for(var i=0;i<3;i++){
	 		$(ele).find('li').eq(0).clone(true).appendTo($(ele));
//	 	}
	 	
	 	var h = $(ele).find('li').width();
		var Cartimer = null;
			clearInterval(Cartimer);
			move();
			
			$(ele).parent().find('span').click(function(){
				clearInterval(Cartimer);
				var size = $(ele).find('li').length;
				if($(this).index()==1){
					x--;
					if(x<0){
						x = size - 2;
						$(ele).css("left",(-h*(size-1)));
					}
					var y = -h*x;
					startMoves(ele,{left:y})

					move();
				}else{
					x++;
					if(x >= size){
						x = 1;
						$(ele).css("left",0);
					}
					var y = -h*x;
					startMoves(ele,{left:y})
					move();
				}
			})
			function move(){
				Cartimer = setInterval(function(){
					x++;
					var size = $(ele).find('li').length;
					if(x >= size){
						x = 1;
						$(ele).css("left",0);
					}
					var y = -h*x;
					startMoves(ele,{left:y})
				},3000);
			} 
	}