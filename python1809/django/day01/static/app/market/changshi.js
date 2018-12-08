$(function(){
    $('#all_type').click(function(){
        $('#all_type_container').toggle();
        $('#all_type_icon').toggleClass('glyphicon-chevron-down').addClass("glyphicon-chevron-up")
        $('#all_sort_container').triggerHandler('click')
    })
    $('all_sort_con').click(function(){
        $(this).hide();
    })
    $('.addtocart').click(function(){
        let num=$(this).prev().find('.num').text()
        let goodsid=$(this).attr('goodsid')
        $.get('/axf/addcart/',{goodsid:goodsid,num:num},function(data){
            let obj=data;
            if (obj.status==1) {
                alert('jiarugouwuchechenggong')
            }
            else{
                if(obj.status==0){
                    let res=confirm('nihaishangweidengru,qingqianwangdengru');
                    if(res){
                        location.href='/'
                    }
                }
            }

        })
    })
})