$(function () {

    // 前端 -> 发起ajax请求 -> 获取json数据  -> 解析json数据，并且渲染到页面中

    // 发起ajax请求
    // $.getJSON('/http://127.0.0.1:5000/students/')
    $.getJSON('/students/', function (response) {
        // console.log(response)

        // 遍历
        for (var i=0; i<response.length; i++){
            console.log(response[i])

            var str = response[i].name + '-' + response[i].age

            $('<li></li>').html(str).appendTo($('.studentlist'))
        }
    })
})