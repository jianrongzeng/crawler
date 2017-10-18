#coding=utf-8
'''
Created on 2017年6月19日

@author: Jianrong
'''

import urllib2
from bs4 import BeautifulSoup
import urlparse
import re
 
page = 1
url = 'https://www.qiushibaike.com/8hr/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    
    #要注意是herf还是href
    
    '''
    #find_all(name,attrs,string)
    #查找所有标签为a的节点
    soup.find_all('a')
    #查找所有标签为a，链接符合/view/123.htm形式的节点
    soup.find_all('a', href = '/view/123.htm') 
    soup.find_all('a', href = re.compile(r'/view/\d+'))
    #查找所有标签为div，class为abc，文字为python的节点
    soup.find_all('div', class_='abc', string='python')
    
    node.name #获取查找到的节点的名称
    node['href'] #获取节点的herf属性
    node.get_text() #获取节点的链接文字
    '''
    nodes = soup.find_all('div', class_="article block untagged mb15")
    for node in nodes:
        user = node.find('h2').get_text()
        link_node = node.find('a', href=re.compile(r'/article/'))
        full_link = urlparse.urljoin('https://www.qiushibaike.com/article/119190597', link_node['href'])
        content = node.find('div', class_="content").get_text()
        print 'user:%s\nlink:%s\ncontent:%s' % (user, full_link, content)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason