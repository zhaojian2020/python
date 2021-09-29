#coding=utf-8
import tushare
from sqlalchemy import create_engine


def set_ts_token():
    tushare.set_token('aebfd9d61005ae74f0e916f08840654489d2bc255ede21263ae95290')


def get_engine():
    return create_engine('mysql+pymysql://root:465021zj@localhost/stock?charset=utf8')
