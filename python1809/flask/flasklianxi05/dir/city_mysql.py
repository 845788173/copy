import json
import pymysql
# import os
# import sqlite3
db=pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='7986805',database='python05',charset='utf8')
# db = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', database='python05', charset='utf8')
from App.settings import BASE_DIR

# temp=os.path.join(BASE_DIR,'test.db')
# db=sqlite3.connect(temp)

cursor=db.cursor()

with open('city.json','r')as fp:
    city_collection=json.load(fp)
    # print(city_collection)
    return_value=city_collection.get('returnValue')
    print(return_value)
    keys_letter=return_value.keys()
    # print(keys_letter)
    for key in keys_letter:
        db.begin()
        cursor.execute("INSERT INTO letter(name) VALUES ('{}')".format(key))
        db.commit()
        # SELECT * FROM letter WHERE name='A'
        db.begin()
        cursor.execute("SELECT * FROM letter WHERE name='{}'".format(key))
        db.commit()

        letter_result=cursor.fetchone()
        # print(letter_result)
        letter_id=letter_result[0]

        letter_cities=return_value.get(key)
        # print(letter_cities)
        for city in letter_cities:
            # print(city)
            id=city.get('id')
            parentId = city.get('parentId')
            regionName = city.get('regionName')
            cityCode = city.get('cityCode')
            pinYin = city.get('pinYin')

        # # INSERT INTO city VALUES(1, 0, '深圳', 23456, 'shenzhen', 3)
        db.begin()
        cursor.execute(
            "INSERT INTO city VALUES({}, {}, '{}', {}, '{}', {})".format(id, parentId, regionName, cityCode, pinYin,
                                                                         letter_id))
        db.commit()
