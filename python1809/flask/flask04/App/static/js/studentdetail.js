$(function () {
     console.log(window.location.href)
      var herf=window.location.href;
      var id=herf.split('=')[1]
    console.log(id)
    $.getJSON('/api/students/' + id +'/' ,function(data){
        // console.log(data)
        // var herf=window.location.href;
        // console.log(window.location.herf)

        // console.log(window.location.herf)

        $('#student_info_name').html(data['name']);
        $('#student_info_age').html(data['age']);
    })
    $('#student_delete').click(function(data){

        console.log('删除动作')
        console.log(data)
        $.ajax('/api/students/' +id +'/',{
            dataType:'json',
            type:'DELETE',
            success:function (data) {
                console.log(data)
                if(data['msg']==='deletesuccess'){
                    window.open('/static/html/studentlist.html/',target='_self');
                }
            }
        })
    })

})