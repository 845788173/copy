$(function () {
    var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        direction: 'vertical'
    });


    // 获取数据
    $.getJSON('/api/v1/wheel/', function (response) {
        console.log(response)
        if (response.status ==200){
            var wheels = response.data

            for (var i=0; i<response.count; i++){
                var temp = response.data[i].img
                var $img = $('<img>').attr('src', temp)
                $('<div class="swiper-slide"></div>').append($img).appendTo('.swiper-wrapper')
            }
        } else {
            console.log('获取数据失败')
        }
    })
})