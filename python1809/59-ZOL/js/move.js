/**
 * 
 * @param {Object} obj
 * @param {Object} attr
 * @param {Object} iTarget
 * @param {Object} fn
 */
function startMove(obj,attr,iTarget,fn){
	var json={};
	json[attr]=iTarget;
	startMoves(obj,json,fn);
}
/**
 * 
 * @param {Object} obj
 * @param {Object} json
 * @param {Object} fn
 */
function startMoves(obj,json,fn){
	
	//清除定时器
	clearInterval(obj.timer);
	
	//开启新的定时器
	obj.timer=setInterval(function(){
		//默认所有属性都到达了目标值，可以关闭定时器，停止动画
		var bStop = true ;
				
		//获取传入的要修改的属性
		for(var attr in json){
			// attr 属性名
			// iTarget 对应attr属性的值
			var iTarget = json[attr];
			
			var current = 0;
			if(attr == "opacity"){
				current = parseFloat(getStyleAtrr(obj,attr)*100);
				current = Math.round(current);//四舍五入
			}else{
				current = parseFloat(getStyleAtrr(obj,attr));
				current = Math.round(current);
			}
			//速度
			var iSpeed = (iTarget - current)/8;
			iSpeed = iSpeed>0?Math.ceil(iSpeed):Math.floor(iSpeed);
			
			//判断是否达到目标值
			if(current != iTarget){
				bStop = false;
			}
			
			//运动
			if(attr =="opacity"){
				obj.style.opacity = (current + iSpeed)/100;
				obj.style.filter = "alpha(opacity="+(current + iSpeed)+")";
			}else{
				obj.style[attr] = current + iSpeed +"px";
			}
		}
		//定时器是否该关闭
			if(bStop){
				clearInterval(obj.timer);
				
				//回调函数
				if(fn){
					fn();
				}
			}

		
	},30)
}




//封装获取某个属性值
				function getStyleAtrr(obj,attr){
					if(window.getComputedStyle){
						return window.getComputedStyle(obj,null)[attr];
					}
					return obj.currentStyle[attr];
				}