$(function(){
					
	// 首页右侧小轮播图
	            var _list1 = $("#xiao2");
				var _list2 = $("#xiao");
				var _li1 = $("#xiao2 li");
				var _li2 = $("#xiao li");
				
				//复制第1张图到最后
				_li1.first().clone().appendTo(_list1);				
				
				var size = $("#xiao2 li").length;
				//console.log(size); //5
				
				var i = 0; //即将显示的图片的下标
				
				//开启定时器, 自动轮播
				var timer1 = setInterval(function(){
					i++;
					move();
				}, 3000);
				
				//移动
				function move(){
					
					//如果超出左边界
					if (i < 0) {
						_list1.css("left", -(size-1)*251); //瞬间移动到第5张图(i=4的图片)
						i = size-2; //即将移动到第4张图(i=3的图)
					}
					
					//如果超出右边界
					if (i >= size) {
						_list1.css("left", 0); //瞬间移动到第1张图(非动画)
						i = 1; //即将移动到第2张图(i=1的图)
					}
					
					//动画移动
					_list1.stop().animate({left: -i*251}, 500);
					
					//更改按钮的选中状态
					_li2.removeClass().eq(i).addClass("act");
					if (i == size-1) {
						_li2.removeClass().eq(0).addClass("act");
					}
				}
				
				
				//按钮的移入事件
				_li2.mouseenter(function(){
					i = $(this).index();
					move();
				})				
				
				$(".messbott").hover(
					function(){ //mouseenter
						clearInterval(timer1); //停止定时器
					},
					function(){ //mouseleave
						clearInterval(timer1);
						timer1 = setInterval(function(){
							i++;
							move();
						}, 3000)
						
				})	
})
