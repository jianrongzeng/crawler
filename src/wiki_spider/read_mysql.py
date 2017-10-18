# coding=utf-8
'''
Created on 2017年6月26日

@author: Jianrong
'''
import pymysql


conn = pymysql.connect(host='localhost',
                    user='root',
                    password='root',
                    db='wiki_item',
                    charset='utf8mb4')
try:
    with conn.cursor() as cursor:
        sql = 'select item, url from urls'
        print cursor.execute(sql)
        print 'fetchmany(4):', cursor.fetchmany(4)
        print 'fetchmany(3):', cursor.fetchmany(3)
        print 'fetchall():', cursor.fetchall()
        
finally:
    conn.close()
