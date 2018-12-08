$(function(){

            $.ajax( {
                // dataType: 'json',
                type: 'GET',
                url:'/api/v1/lunbo/',
                success: function (response) {
                    // console.log(response)
                    // var $p_name=$('<p></p>')
                    var $div1=$('.swiper-wrapper')
                    // console.log(response)
                    data=response["data"]
                    // console.log(data)
                    // console.log(data[0])
                    for (i=0;i<data.length;i++) {
                        // $li.attr('data-id',i)
                        var $div=$('<div class="swiper-slide"></div>')
                        var $img = $('<img>');
                        $img.attr('src',data[i]['image'])
                        // console.log(data[i])
                        $div.append($img)
                        $div1.append($div)
                    }
                    // $div1.append($div)
                }
            })

})