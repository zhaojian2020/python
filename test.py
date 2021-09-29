#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pysnowball as ball
import json
import time #引入time类库
import pymysql
from common import db

ball.set_token('xq_a_token=737318e45e37283c174e6861710dab688eebe737;')

stock_conn = db.get_stock_conn()
stock_cursor = stock_conn.cursor()
 
stock_cursor.execute("select ts_code,list_date from stock_basic") #获取所有
basic_rows = stock_cursor.fetchall() #获取所有的股票

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = stock_conn.cursor()    
# SQL 查询语句
sql = "INSERT INTO `stock`.`stock_daily_qff` (`volume`, `high`, `name`, `chg`, `navps`, `symbol`, `percent`, `pb`, `current`, `amount`, `last_close`, `low`, `time`, `turnover_rate`, `volume_ratio`, `open`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"

for basic_row in basic_rows: #遍历
	ts_code = basic_row[0] #股票代码
	ts_code = ts_code[7:9] + ts_code[0:6]
#	    list_date = int(basic_row[1]) # 上市时间，转化成数字，方便计算
	#gl = ball.industry(ts_code) #所属概念 dl = gl['industry']['concept'] ,['ind_name']
	ss = ball.quotecc(ts_code)#每日数据（开盘、每股净资产、量比等）
	ss = ss['data']['quote']
	ii ={}
	ii['symbol'] = ss['symbol']
	ii['name'] = ss['name']
	ii['time'] = ss['time']
	ii['open'] = ss['open']
	ii['current'] = ss['current']
	ii['high'] = ss['high']
	ii['low'] = ss['low']
	ii['volume'] = ss['volume']
	ii['volume_ratio'] = ss['volume_ratio']
	ii['amount'] = ss['amount']
	ii['last_close'] = ss['last_close']
	ii['pb'] = ss['pb']
	ii['navps'] = ss['navps']
	ii['turnover_rate'] = ss['turnover_rate']
	ii['chg'] = ss['chg']
	ii['percent'] = ss['percent']
#	ii = json.dumps(ii,encoding='UTF-8', ensure_ascii=False)
	tup = []
	for i in ii.values():
		tup.append(i)
	tup = tuple(tup)

	# 执行SQL语句
	cursor.execute(sql,tup)
	stock_conn.commit()
	# 关闭数据库连接
	#dbb.close()
