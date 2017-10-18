#coding=utf-8
'''
Created on 2017年6月19日

@author: Jianrong
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer
import urllib2

'''
爬虫总调度程序
以一个入口url作为参数来爬取相关页面
'''


class SpiderMain(object):
    def __init__(self):
        #初始化各个对象
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except urllib2.HTTPError, e:
                print 'craw failed!'
                print e.code
                print e.reason
        self.outputer.output()
            
            

#main函数
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/link?url=gnArCobC8jfbn2agxuYQlPMH1_OdDSHcXkGKfXl8Noag28uuESIzHCDV7h3WEkMyCHUPN-nqgTLGSghosRiN1q"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)