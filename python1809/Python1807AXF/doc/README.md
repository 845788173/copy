## 一、项目结构
- 首页
- 闪购超市
- 购物车
    ```
    订单系统
    支付系统
    评价系统
    物流系统
    ...
    ```
- 我的
    ```
    用户系统
    ```

## 二、布局
- 百分比布局
    相对于父元素.


- rem
    相对于body节点 字体大小的比例。

## 三、基础模板
`base.html`头部、尾部是一致的，先完成基本结构，以及相关文件导入;

`首页home.html、闪购超市maket.html、购物车cart.html、我的mine.html` 四个页面都是继承自基础模板;

## 四、首页 -- 轮播图
- 数据分析
    ```
    insert into axf_wheel(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg","酸奶女王","21870"),("http://img01.bqstatic.com//upload/activity/2017031710450787.jpg@90Q.jpg","优选圣女果","21869"),("http://img01.bqstatic.com//upload/activity/2017030714522982.jpg@90Q.jpg","伊利酸奶大放价","21862"),("http://img01.bqstatic.com//upload/activity/2017032116081698.jpg@90Q.jpg","鲜货直供－窝夫小子","21770"),("http://img01.bqstatic.com//upload/activity/2017032117283348.jpg@90Q.jpg","鲜货直供－狼博森食品","21874");


    img 商品图片地址
    name 商品名称
    trackid 商品id
    ```

- 模型类
