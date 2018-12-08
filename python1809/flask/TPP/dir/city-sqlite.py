import json
import os
import sqlite3
from app.settings import BASE_DIR

# 链接数据库
temp = os.path.join(BASE_DIR, 'develop.db')
db = sqlite3.connect(temp)
# 游标
cursor = db.cursor()

# 打开文件
with open('city.json','r') as fp:
    # 加载
    city_collection = json.load(fp)
    returnValue = city_collection.get('returnValue')

    '''
    "F" : [
      {
        "cityCode" : 450600,
        "id" : 360,
        "parentId" : 0,
        "pinYin" : "FANGCHENGGANG",
        "regionName" : "防城港"
      },
      ....
    ]
    '''

    # 获取所有的key
    keys_letter = returnValue.keys()
    print(keys_letter)


    # 遍历，插入数据库
    for letter in keys_letter:
        # 插入letter表
        # INSERT INTO letter(name) VALUES('B')

        cursor.execute("INSERT INTO letter(name) VALUES('{}')".format(letter))
        db.commit()

        # 字母 对应 表中 id 【因为在插入城市时，指定关系是属于哪个字母下的，这需要字母的id】
        # SELECT * FROM letter WHERE name='A'
        cursor.execute("SELECT * FROM letter WHERE name='{}'".format(letter))
        db.commit()

        # 取出数据
        letter_result = cursor.fetchone()
        letter_id = letter_result[0]

        # 字母key  对应 城市列表
        letter_cities = returnValue.get(letter)
        print(letter_cities)

        # 遍历城市列表
        for city in letter_cities:
            id = city.get('id')
            parentId = city.get('parentId')
            regionName = city.get('regionName')
            cityCode = city.get('cityCode')
            pinYin = city.get('pinYin')

            # 插入 city 表
            # INSERT INTO city VALUES(1, 0, '深圳', 23456, 'shenzhen', 3)
            cursor.execute("INSERT INTO city VALUES({}, {}, '{}', {}, '{}', {})".format(id, parentId, regionName, cityCode, pinYin, letter_id))
            db.commit()