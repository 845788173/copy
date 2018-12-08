from app.ext import db

# 字母模型类
class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(4))
    # 城市列表
    l_cities = db.relationship('City', backref='letter', lazy=True)

# 城市模型类
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parentId = db.Column(db.Integer, default=0)
    regionName = db.Column(db.String(100))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(40))
    # 关系 【属于哪个字母下】
    c_letter = db.Column(db.Integer, db.ForeignKey(Letter.id))


# 用户模型类
class User(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    name = db.Column(db.String(40))
    # 密码
    password = db.Column(db.String(256))
    # 邮箱
    email = db.Column(db.String(20), unique=True)
    # 手机
    phone = db.Column(db.String(20), unique=True)
    # 令牌
    token = db.Column(db.String(256))
    # 是否删除
    isdelete = db.Column(db.Boolean, default=False)
    # 是否激活
    isactive = db.Column(db.Boolean, default=False)
    # 头像
    icon = db.Column(db.String(40), default='head.png')
    # 等级
    permissions = db.Column(db.Integer, default=1)



# 电影信息模型类
# insert into
# movies(backgroundpicture, flag, isdelete)
# values("i1/TB19_XCoLDH8KJjy1XcXXcpdXXa_.jpg",1,0);
class Movies(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 电影名
    showname = db.Column(db.String(256))
    # 电影名-英文
    shownameen = db.Column(db.String(256))
    # 导演
    director = db.Column(db.String(256))
    # 主演
    leadingRole = db.Column(db.String(256))
    # 电影分类
    type = db.Column(db.String(256))
    # 产地
    country = db.Column(db.String(256))
    # 语言
    language = db.Column(db.String(256))
    # 时长
    duration = db.Column(db.Integer)
    # 放映模式
    screeningmodel = db.Column(db.String(256))
    # 上映时间
    openday = db.Column(db.String(256))
    # 图片
    backgroundpicture = db.Column(db.String(256))
    # 标志位  0全部，   1热映，   2即将上映
    flag = db.Column(db.String(256))
    # 是否删除
    isdelete = db.Column(db.String(256))


# 影院模型类
class Cinemas(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 影院名称
    name = db.Column(db.String(256))
    # 城市
    city = db.Column(db.String(256))
    # 区域
    district = db.Column(db.String(256))
    # 详细地址
    address = db.Column(db.String(256))
    # 电话
    phone = db.Column(db.String(256))
    # 评分
    score = db.Column(db.Float)
    # 放映厅个数
    hallnum = db.Column(db.Integer)
    # 服务评分
    servicecharge = db.Column(db.Float)
    # 限制
    astrict = db.Column(db.Integer)
    # 标志位
    flag = db.Column(db.Integer, default=0)
    # 是否删除
    isdelete = db.Column(db.Boolean, default=False)





