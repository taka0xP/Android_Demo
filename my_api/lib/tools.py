# -*- coding: utf-8 -*-
# @Time    : 2021-02-21 22:35
# @Author  : XU
# @File    : tools.py
# @Software: PyCharm
import os
import sys
sys.path.append(os.path.abspath(__file__).split("my_api")[0])
import pymysql
from my_api.config.setting import MYSQL_INFO


def my_db(sql):
    db = pymysql.connect(**MYSQL_INFO)
    try:
        with db.cursor() as cursor:
            cursor.execute(sql)
        if sql.strip()[0:6].upper() == 'SELECT':
            res = cursor.fetchall()
        else:
            cursor.commit()
            res = 'ok'
        return res
    except Exception as e:
        print(e)
        db.rollback()
