$(function () {

    //首页顶部轮播
    new Swiper('#topSwiper', {
        loop: true, // 循环模式选项
        pagination: '.swiper-pagination'
    });

    // 必购数据轮播
    new Swiper('#swiperMenu', {
        slidesPerView: 3  // 每页显示数量
    });

});
