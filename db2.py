#coding=utf-8
import pymysql

class DB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_stock_conn():
        return pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='82772e18b78ceb1b',
            db='stock',
            use_unicode=True,
            charset="utf8")


db = DB()


def get_stock_conn():
    return DB().get_stock_conn()
