#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : ALLEN
# @Time    : 2018/9/18 19:44
# @File    : models.py
# @Software: PyCharm
import os
import peewee
db_path = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    ),"house.db"
)
db = peewee.SqliteDatabase(db_path)
class HouseList(peewee.Model):
    house_title = peewee.CharField(max_length = "256")
    house_address = peewee.CharField(max_length="256")
    house_style = peewee.CharField(max_length="256")
    house_size = peewee.CharField(max_length="256")
    house_price = peewee.CharField(max_length="32")
    class Meta:
        database = db
if __name__ == "__main__":
    HouseList().create_table()