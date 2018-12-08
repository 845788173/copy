# import json
# import os
# import sqlite3
#
# BASE_DIR=os.path.dirname(os.path.abspath(__file__))
# # 链接数据库
# temp = os.path.join(BASE_DIR, 'develop.db')
# db = sqlite3.connect(temp)
# # 游标
# cursor = db.cursor()
#
# with open('goods.json','r') as fp:
#     city_collection
#     for city in city_collection:
#             print(city)
#             # id = city.get('id')
#             # parentId = city.get('parentId')
#             # regionName = city.get('regionName')
#             # cityCode = city.get('cityCode')
#             # pinYin = city.get('pinYin')
#
#             # 插入 city 表
#             # INSERT INTO city VALUES(1, 0, '深圳', 23456, 'shenzhen', 3)
#             # cursor.execute("INSERT INTO city VALUES({}, {}, '{}', {}, '{}', {})".format(id, parentId, regionName, cityCode, pinYin, letter_id))
#             # db.commit()