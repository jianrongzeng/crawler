#coding=utf-8
'''
Created on 2017年6月21日

@author: Jianrong
'''

import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #href="/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6"
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        #url
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        if title_node is not None:
            res_data['title'] = title_node.get_text()
            print res_data['title']
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        if summary_node is not None:
            res_data['summary'] = summary_node.get_text()
            print "summary:" + res_data['summary']
        return res_data
        
    
    
    def parse(self,page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    

'''      
hp = HtmlParser()
url = 'http://baike.baidu.com/link?url=Pf6rsrTCCDuY77qIAA9CxakV-l2u4wPs6kXfh5_FEf2KgPupiOWSVzDz1nD3rOkRsnQtSDO5XGkGszVk-REUd_'
html_cont = urllib2.urlopen(url).read()
hp.parse(url, html_cont)
'''



