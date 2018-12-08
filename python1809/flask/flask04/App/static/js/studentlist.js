$(function(){
    $.getJSON('/api/students/',function (data) {
        console.log(data);
        var $student_list_container=$('#student_list_container')
        var student_list=data['data']
        for (var i=0;i<student_list.length;i++){
            console.log(student_list[i]);
            var $p_name=$('<p></p>')
            // var $a=$('<a></a>')
            // $a.attr('href','/api/students/' + student_list[i]['id'] +'/');
            // $a.append($p_name)
            $p_name.html(student_list[i]['name']);
            var $li=$('<li></li>');

            $li.append($p_name);
            $li.attr('data-id',i);

            $li.click(function(){
                var studentid = student_list[$(this).attr('data-id')]['id']
                // window.open('/static/html/studentdetail.html?id= '+student_list[$(this).attr('data-id')]['id'],target='_self')
                // console.log(studentid)
                window.open('/static/html/studentdetail.html?id=' + studentid)
            })
            $student_list_container.append($li);
        }

    })



})