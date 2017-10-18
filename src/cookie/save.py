#coding=utf-8
import urllib
import urllib2
import cookielib

#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
postdata = urllib.urlencode({'userName':'2471788627@qq.com','password':'zengjianrong'})
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com',postdata)
#保存cookie到文件
cookie.save(filename, ignore_discard = True, ignore_expires = True)