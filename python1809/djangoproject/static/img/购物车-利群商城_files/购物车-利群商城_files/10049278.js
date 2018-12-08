



















if(typeof doyoo=='undefined' || !doyoo){
var d_genId=function(){
    var id ='',ids='0123456789abcdef';
    for(var i=0;i<34;i++){ id+=ids.charAt(Math.floor(Math.random()*16));  }  return id;
};
var doyoo={
env:{
secure:false,
mon:'http://m8103.looyu.com/monitor',
chat:'http://looyuoms7614.looyu.com/chat',
file:'http://static.soperson.com/131221',
compId:20000590,
confId:10049278,
vId:d_genId(),
lang:'sc',
fixFlash:1,
subComp:0,
_mark:'1551f4dec0ca5c52c5b49e50b4a063ec6d5e933d04fbe77d040f95407d1441979d9d26f2c8f5e5d4'
}




};

if(typeof talk99Init == 'function'){
    talk99Init(doyoo);
}
if(!document.getElementById('doyoo_panel')){




document.write('<div id="doyoo_share" style="display:none;"></div>');
document.write('<lin'+'k rel="stylesheet" type="text/css" href="http://static.soperson.com/131221/talk99.css?150728"></li'+'nk>');
document.write('<scr'+'ipt type="text/javascript" src="http://static.soperson.com/131221/talk99.js?160907" charset="utf-8"></scr'+'ipt>');

}
}
