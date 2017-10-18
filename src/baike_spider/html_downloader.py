#coding=utf-8
'''
Created on 2017年6月19日

@author: Jianrong
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        responce = urllib2.urlopen(url)
        if responce.getcode() != 200:
            return None
        return responce.read()