# coding=utf-8
'''
Created on 2017年6月22日

@author: Jianrong
'''
import urllib2
from bs4 import BeautifulSoup
import pymysql


responce = urllib2.urlopen('https://baike.baidu.com/').read().decode('utf-8')
soup = BeautifulSoup(responce, 'html.parser')
urls = soup.find('dl', class_="today content show").find_all('a')
datas = []
for url in urls:
    item = url.find('div', class_="content_tit").get_text()
    datas.append({"item":item, "url":url['href']})
conn = pymysql.connect(host='localhost',
                    user='root',
                    password='root',
                    db='wiki_item',
                    charset='utf8mb4')
    # print data['item'].strip() + ':' + data['url']
try:
    with conn.cursor() as cursor:
        sql = "insert into urls(item, url)values(%s,%s)"
        for x in range(len(datas)):
            print datas[x]['item'].strip() + ':' + datas[x]['url']
            cursor.execute(sql, (datas[x]['item'], datas[x]['url']))
            conn.commit()
finally:
    conn.close()
    
    
