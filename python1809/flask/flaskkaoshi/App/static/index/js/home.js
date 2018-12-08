$(function() {
	// var swiper = new Swiper('.swiper-container', {
	// 	pagination: '.swiper-pagination',
	// 	paginationClickable: true,
	// 	nextButton: '.swiper-button-next',
	// 	prevButton: '.swiper-button-prev',
	// 	spaceBetween: 30,
	// 	effect: 'fade'
	// });
    console.log(111)
    var swiper = new Swiper('.swiper-container', {

        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        paginationClickable: true,
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: true,
        loop:true,
        observer: true, //修改swiper自己或子元素时，自动初始化swiper
        observeParents: true,//修改swiper的父元素时，自动初始化swiper

    });


})