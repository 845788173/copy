## 一、HttpRequest对象
- 概述

    服务器接受到客户端请求后，系统自动创建的对象(视图函数第一个参数)。


- 属性
    ```
    path 请求路径
    method 请求方法
    GET get请求参数
    POST post请求参数
    FILES 上传文件
    COOKIES cookie对象【会话技术】
    session session对象【会话技术】
    ```

- GET请求
    ```
    # 参数获取
    name = request.GET.get('name')
    ```

- POST请求
    ```
    # 参数获取
    name = request.POST.get('name')
    ```


## 二、HttpResponse对象
- 概述

    用于返回数据给客户端的。

- HttpResponse()
    ```
    response = HttpResponse('hello')
    response = HttpResponse('hello', status=200)
    ```

- render()
    ```
    response = render(request, 'index.html')
    response = render(request, 'index.html', status=301)
    ```

- redirect()
    ```
    response = redirect('/meituan/')
    ```

- JsonResponse()
    ```
    stu = {'name':'zhangsan', 'age':20}
    response = JsonResponse(stu)
    ```


## 三、会话技术
- 概述
    ```
    HTTP 无状态 [请求一次，返回对应响应，称为一次会话]

    会话技术: 实现状态保持

    为什么要使用会话保持?
        在一定时间段或操作中，跟踪请求者状态! [服务器就知道你是谁]
    ```
    > github HTTP，没操作都需要输入用户和密码 [服务器才知道你是谁]

- 会话技术
    ```
    cookie: 客户端会话技术
    session: 服务器会话技术(要依托cookie)
    token: 手动session
    ```


## 四、会话技术cookie


