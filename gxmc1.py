#coding=utf-8
from common import db #数据库配置抽取
from common import ts #tushare配置相关的抽取
import tushare

ts.set_ts_token()
pro = tushare.pro_api()
data = ''
try:
	data = pro.stock_basic(fields='ts_code,symbol,name,area,industry,list_date,market,is_hs,list_status,exchange,delist_date,curr_type')
	#data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
except Exception as e: # e: py 2.7 写法， py 3写法是 Exception as e
    print (e)
#	exit(0)

#print type(data)
stock_conn = db.db.get_stock_conn() #创建conn
stock_cursor = stock_conn.cursor() #获取游标
stock_cursor.execute('truncate table stock_basic') #清表
stock_conn.commit() #提交变更

engine = ts.get_engine()
data.to_sql('stock_basic', engine, if_exists='append')
