# -*- coding:utf-8 -*-
'''
Created on 2017年6月17日

@author: Jianrong
'''

import urllib2
import re
 
page = 1
url = 'https://www.qiushibaike.com/8hr/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    restr = r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>.*?'
    pattern = re.compile(restr, re.S)
    items = re.findall(pattern,content)
    print u"段子总数：",len(items)
    for item in items:
        print u"用户：" + item[0] + "\n" + u"内容：" + item[1] + "\n" + u"点赞数：",item[2] + "\n"
        '''
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
        '''
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason