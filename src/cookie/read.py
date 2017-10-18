#coding=utf-8

'''
Created on 2017年6月16日

@author: Jianrong 
'''

import cookielib
import urllib2
from cookie.save import response

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard = True, ignore_expires = True)
#创建请求的request
request = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)
print response.read()