#coding=utf-8
'''
Created on 2017年6月19日

@author: Jianrong
'''


class HtmlOutputer(object):
    
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data) 

    
    def output(self):
        fout = open('output.html', 'w')
        
        fout.write("<html>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            #行开始标签
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            if 'summary' in data.keys():
                fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()    
    
 
'''   
datas = [{'url': 'http://baike.baidu.com/link?url=gnArCobC8jfbn2agxuYQlPMH1_OdDSHcXkGKfXl8Noag28uuESIzHCDV7h3WEkMyCHUPN-nqgTLGSghosRiN1q', 'summary': u'\nPython[1]\xa0\n\uff08\u82f1\u56fd\u53d1\u97f3\uff1a/\u02c8pa\u026a\u03b8\u0259n/ \u7f8e\u56fd\u53d1\u97f3\uff1a/\u02c8pa\u026a\u03b8\u0251\u02d0n/\uff09, \u662f\u4e00\u79cd\u9762\u5411\u5bf9\u8c61\u7684\u89e3\u91ca\u578b\u8ba1\u7b97\u673a\u7a0b\u5e8f\u8bbe\u8ba1\u8bed\u8a00\uff0c\u7531\u8377\u5170\u4ebaGuido van Rossum\u4e8e1989\u5e74\u53d1\u660e\uff0c\u7b2c\u4e00\u4e2a\u516c\u5f00\u53d1\u884c\u7248\u53d1\u884c\u4e8e1991\u5e74\u3002Python\u662f\u7eaf\u7cb9\u7684\u81ea\u7531\u8f6f\u4ef6\uff0c \u6e90\u4ee3\u7801\u548c\u89e3\u91ca\u5668CPython\u9075\u5faa GPL(GNU General Public License)\u534f\u8bae[2]\xa0\n\u3002Python\u8bed\u6cd5\u7b80\u6d01\u6e05\u6670\uff0c\u7279\u8272\u4e4b\u4e00\u662f\u5f3a\u5236\u7528\u7a7a\u767d\u7b26(white space)\u4f5c\u4e3a\u8bed\u53e5\u7f29\u8fdb\u3002Python\u5177\u6709\u4e30\u5bcc\u548c\u5f3a\u5927\u7684\u5e93\u3002\u5b83\u5e38\u88ab\u6635\u79f0\u4e3a\u80f6\u6c34\u8bed\u8a00\uff0c\u80fd\u591f\u628a\u7528\u5176\u4ed6\u8bed\u8a00\u5236\u4f5c\u7684\u5404\u79cd\u6a21\u5757\uff08\u5c24\u5176\u662fC/C++\uff09\u5f88\u8f7b\u677e\u5730\u8054\u7ed3\u5728\u4e00\u8d77\u3002\u5e38\u89c1\u7684\u4e00\u79cd\u5e94\u7528\u60c5\u5f62\u662f\uff0c\u4f7f\u7528Python\u5feb\u901f\u751f\u6210\u7a0b\u5e8f\u7684\u539f\u578b\uff08\u6709\u65f6\u751a\u81f3\u662f\u7a0b\u5e8f\u7684\u6700\u7ec8\u754c\u9762\uff09\uff0c\u7136\u540e\u5bf9\u5176\u4e2d[3]\xa0\n\u6709\u7279\u522b\u8981\u6c42\u7684\u90e8\u5206\uff0c\u7528\u66f4\u5408\u9002\u7684\u8bed\u8a00\u6539\u5199\uff0c\u6bd4\u59823D\u6e38\u620f\u4e2d\u7684\u56fe\u5f62\u6e32\u67d3\u6a21\u5757\uff0c\u6027\u80fd\u8981\u6c42\u7279\u522b\u9ad8\uff0c\u5c31\u53ef\u4ee5\u7528C/C++\u91cd\u5199\uff0c\u800c\u540e\u5c01\u88c5\u4e3aPython\u53ef\u4ee5\u8c03\u7528\u7684\u6269\u5c55\u7c7b\u5e93\u3002\u9700\u8981\u6ce8\u610f\u7684\u662f\u5728\u60a8\u4f7f\u7528\u6269\u5c55\u7c7b\u5e93\u65f6\u53ef\u80fd\u9700\u8981\u8003\u8651\u5e73\u53f0\u95ee\u9898\uff0c\u67d0\u4e9b\u53ef\u80fd\u4e0d\u63d0\u4f9b\u8de8\u5e73\u53f0\u7684\u5b9e\u73b0\u3002\n', 'title': u'Python'}, 
         {'url': u'http://baike.baidu.com/item/GPL', 'title': u'GPL'}, 
         {'url': u'http://baike.baidu.com/item/Zope', 'summary': u'\nZope\u662f\u4e00\u4e2a\u5f00\u653e\u6e90\u4ee3\u7801\u7684Web\u5e94\u7528\u670d\u52a1\u5668\uff0c\u5b98\u65b9\u7f51\u7ad9\u4f4d\u4e8e http://zope.org Zope\u76ee\u524d\u67092\u4e2a\u6bd4\u8f83\u72ec\u7acb\u7684\u7248\u672c\uff0cZope 2\u7cfb\u5217\u548cZope 3\u7cfb\u5217\u3002Zope 3\u662f\u6c72\u53d6\u4e86Zope 2\u7684\u6559\u8bad\uff0c\u5bf9Zope 2\u7684\u91cd\u5199\uff0c\u662f\u4e00\u4e2a\u91c7\u7528\u4e86\u73b0\u4ee3\u8bbe\u8ba1\u6a21\u5f0f\u7684\u3001\u57fa\u4e8e\u7ec4\u4ef6\u67b6\u6784\u7684\u5e94\u7528\u670d\u52a1\u5668\u3002\u6709\u4eba\u8bf4Zope 3\u5c31\u662f\u4e00\u4e2aPython\u7248\u672c\u7684\u8f7b\u91cf\u7ea7J2EE\u6846\u67b6\u3002 Zope 2\u7279\u522b\u9002\u5408\u811a\u672c\u5f00\u53d1\u4eba\u5458\uff0c\u76f4\u63a5\u901a\u8fc7\u6d4f\u89c8\u5668\u5c31\u53ef\u5feb\u901f\u6784\u5efa\u4e00\u4e2a\u5e94\u7528\u3002\n', 'title': u'zope'}, 
         {'url': u'http://baike.baidu.com/item/%E7%BC%96%E8%AF%91%E5%99%A8', 'summary': u'\n\u7b80\u5355\u8bb2\uff0c\u7f16\u8bd1\u5668\u5c31\u662f\u5c06\u201c\u4e00\u79cd\u8bed\u8a00\uff08\u901a\u5e38\u4e3a\u9ad8\u7ea7\u8bed\u8a00\uff09\u201d\u7ffb\u8bd1\u4e3a\u201c\u53e6\u4e00\u79cd\u8bed\u8a00\uff08\u901a\u5e38\u4e3a\u4f4e\u7ea7\u8bed\u8a00\uff09\u201d\u7684\u7a0b\u5e8f\u3002\u4e00\u4e2a\u73b0\u4ee3\u7f16\u8bd1\u5668\u7684\u4e3b\u8981\u5de5\u4f5c\u6d41\u7a0b\uff1a\u6e90\u4ee3\u7801 (source code) \u2192 \u9884\u5904\u7406\u5668 (preprocessor) \u2192 \u7f16\u8bd1\u5668 (compiler) \u2192  \u76ee\u6807\u4ee3\u7801 (object code) \u2192 \u94fe\u63a5\u5668 (Linker) \u2192 \u53ef\u6267\u884c\u7a0b\u5e8f (executables)\u9ad8\u7ea7\u8ba1\u7b97\u673a\u8bed\u8a00\u4fbf\u4e8e\u4eba\u7f16\u5199\uff0c\u9605\u8bfb\u4ea4\u6d41\uff0c\u7ef4\u62a4\u3002\u673a\u5668\u8bed\u8a00\u662f\u8ba1\u7b97\u673a\u80fd\u76f4\u63a5\u89e3\u8bfb\u3001\u8fd0\u884c\u7684\u3002\u7f16\u8bd1\u5668\u5c06\u6c47\u7f16\u6216\u9ad8\u7ea7\u8ba1\u7b97\u673a\u8bed\u8a00\u6e90\u7a0b\u5e8f\uff08Source program\uff09\u4f5c\u4e3a\u8f93\u5165\uff0c\u7ffb\u8bd1\u6210\u76ee\u6807\u8bed\u8a00\uff08Target language\uff09\u673a\u5668\u4ee3\u7801\u7684\u7b49\u4ef7\u7a0b\u5e8f\u3002\u6e90\u4ee3\u7801\u4e00\u822c\u4e3a\u9ad8\u7ea7\u8bed\u8a00 (High-level language)\uff0c \u5982Pascal\u3001C\u3001C++\u3001Java\u3001\u6c49\u8bed\u7f16\u7a0b\u7b49\u6216\u6c47\u7f16\u8bed\u8a00\uff0c\u800c\u76ee\u6807\u5219\u662f\u673a\u5668\u8bed\u8a00\u7684\u76ee\u6807\u4ee3\u7801\uff08Object code\uff09\uff0c\u6709\u65f6\u4e5f\u79f0\u4f5c\u673a\u5668\u4ee3\u7801\uff08Machine code\uff09\u3002\u5bf9\u4e8eC#\u3001VB\u7b49\u9ad8\u7ea7\u8bed\u8a00\u800c\u8a00\uff0c\u6b64\u65f6\u7f16\u8bd1\u5668\u5b8c\u6210\u7684\u529f\u80fd\u662f\u628a\u6e90\u7801\uff08SourceCode\uff09\u7f16\u8bd1\u6210\u901a\u7528\u4e2d\u95f4\u8bed\u8a00\uff08MSIL/CIL\uff09\u7684\u5b57\u8282\u7801\uff08ByteCode\uff09\u3002\u6700\u540e\u8fd0\u884c\u7684\u65f6\u5019\u901a\u8fc7\u901a\u7528\u8bed\u8a00\u8fd0\u884c\u5e93\u7684\u8f6c\u6362\uff0c\u7f16\u7a0b\u6700\u7ec8\u53ef\u4ee5\u88abCPU\u76f4\u63a5\u8ba1\u7b97\u7684\u673a\u5668\u7801\uff08NativeCode\uff09\u3002\n', 'title': u'\u7f16\u8bd1\u5668'}, 
         {'url': u'http://baike.baidu.com/item/%E7%9B%AE%E6%A0%87%E4%BB%A3%E7%A0%81', 'summary': u'\n\u76ee\u6807\u4ee3\u7801\uff08object code\uff09\u6307\u8ba1\u7b97\u673a\u79d1\u5b66\u4e2d\u7f16\u8bd1\u5668\u6216\u6c47\u7f16\u5668\u5904\u7406\u6e90\u4ee3\u7801\u540e\u6240\u751f\u6210\u7684\u4ee3\u7801\uff0c\u5b83\u4e00\u822c\u7531\u673a\u5668\u4ee3\u7801\u6216\u63a5\u8fd1\u4e8e\u673a\u5668\u8bed\u8a00\u7684\u4ee3\u7801\u7ec4\u6210\u3002\n', 'title': u'\u76ee\u6807\u4ee3\u7801'}, 
         {'url': u'http://baike.baidu.com/item/FORTRAN%E8%AF%AD%E8%A8%80', 'summary': u'\nFORTRAN\u8bed\u8a00\u662fFormula Translation\u7684\u7f29\u5199\uff0c\u610f\u4e3a\u201c\u516c\u5f0f\u7ffb\u8bd1\u201d\u3002\u5b83\u662f\u4e3a\u79d1\u5b66\u3001\u5de5\u7a0b\u95ee\u9898\u6216\u4f01\u4e8b\u4e1a\u7ba1\u7406\u4e2d\u7684\u90a3\u4e9b\u80fd\u591f\u7528\u6570\u5b66\u516c\u5f0f\u8868\u8fbe\u7684\u95ee\u9898\u800c\u8bbe\u8ba1\u7684\uff0c\u5176\u6570\u503c\u8ba1\u7b97\u7684\u529f\u80fd\u8f83\u5f3a\u3002\n', 'title': u'FORTRAN\u8bed\u8a00'}, 
         {'url': u'http://baike.baidu.com/item/%E6%95%B0%E6%8D%AE', 'summary': u'\n\u6570\u636e(data)\u662f\u4e8b\u5b9e\u6216\u89c2\u5bdf\u7684\u7ed3\u679c\uff0c\u662f\u5bf9\u5ba2\u89c2\u4e8b\u7269\u7684\u903b\u8f91\u5f52\u7eb3\uff0c\u662f\u7528\u4e8e\u8868\u793a\u5ba2\u89c2\u4e8b\u7269\u7684\u672a\u7ecf\u52a0\u5de5\u7684\u7684\u539f\u59cb\u7d20\u6750\u3002\u6570\u636e\u53ef\u4ee5\u662f\u8fde\u7eed\u7684\u503c\uff0c\u6bd4\u5982\u58f0\u97f3\u3001\u56fe\u50cf\uff0c\u79f0\u4e3a\u6a21\u62df\u6570\u636e\u3002\u4e5f\u53ef\u4ee5\u662f\u79bb\u6563\u7684\uff0c\u5982\u7b26\u53f7\u3001\u6587\u5b57\uff0c\u79f0\u4e3a\u6570\u5b57\u6570\u636e\u3002\u5728\u8ba1\u7b97\u673a\u7cfb\u7edf\u4e2d\uff0c\u6570\u636e\u4ee5\u4e8c\u8fdb\u5236\u4fe1\u606f\u5355\u51430,1\u7684\u5f62\u5f0f\u8868\u793a\u3002\n', 'title': u'\u6570\u636e'}, 
         {'url': u'http://baike.baidu.com/item/%E6%95%B0%E6%8D%AE?force=1', 'title': u'\u6570\u636e'}, {'url': u'http://baike.baidu.com/item/%E8%A1%A8%E8%BE%BE%E5%BC%8F', 'summary': u'\n\u8868\u8fbe\u5f0f\uff0c\u662f\u7531\u6570\u5b57\u3001\u7b97\u7b26\u3001\u6570\u5b57\u5206\u7ec4\u7b26\u53f7\uff08\u62ec\u53f7\uff09\u3001\u81ea\u7531\u53d8\u91cf\u548c\u7ea6\u675f\u53d8\u91cf\u7b49\u4ee5\u80fd\u6c42\u5f97\u6570\u503c\u7684\u6709\u610f\u4e49\u6392\u5217\u65b9\u6cd5\u6240\u5f97\u7684\u7ec4\u5408\u3002\u7ea6\u675f\u53d8\u91cf\u5728\u8868\u8fbe\u5f0f\u4e2d\u5df2\u88ab\u6307\u5b9a\u6570\u503c\uff0c\u800c\u81ea\u7531\u53d8\u91cf\u5219\u53ef\u4ee5\u5728\u8868\u8fbe\u5f0f\u4e4b\u5916\u53e6\u884c\u6307\u5b9a\u6570\u503c\u3002\n', 'title': u'\u8868\u8fbe\u5f0f'}, 
         {'url': u'http://baike.baidu.com/item/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86', 'summary': u'\n\u7f16\u8bd1\u539f\u7406\u662f\u8ba1\u7b97\u673a\u4e13\u4e1a\u7684\u4e00\u95e8\u91cd\u8981\u4e13\u4e1a\u8bfe\uff0c\u65e8\u5728\u4ecb\u7ecd\u7f16\u8bd1\u7a0b\u5e8f\u6784\u9020\u7684\u4e00\u822c\u539f\u7406\u548c\u57fa\u672c\u65b9\u6cd5\u3002\u5185\u5bb9\u5305\u62ec\u8bed\u8a00\u548c\u6587\u6cd5\u3001\u8bcd\u6cd5\u5206\u6790\u3001\u8bed\u6cd5\u5206\u6790\u3001\u8bed\u6cd5\u5236\u5bfc\u7ffb\u8bd1\u3001\u4e2d\u95f4\u4ee3\u7801\u751f\u6210\u3001\u5b58\u50a8\u7ba1\u7406\u3001\u4ee3\u7801\u4f18\u5316\u548c\u76ee\u6807\u4ee3\u7801\u751f\u6210\u3002 \u7f16\u8bd1\u539f\u7406\u662f\u8ba1\u7b97\u673a\u4e13\u4e1a\u8bbe\u7f6e\u7684\u4e00\u95e8\u91cd\u8981\u7684\u4e13\u4e1a\u8bfe\u7a0b\u3002\u867d\u7136\u53ea\u6709\u5c11\u6570\u4eba\u4ece\u4e8b\u7f16\u8bd1\u65b9\u9762\u7684\u5de5\u4f5c\uff0c\u4f46\u662f\u8fd9\u95e8\u8bfe\u5728\u7406\u8bba\u3001\u6280\u672f\u3001\u65b9\u6cd5\u4e0a\u90fd\u5bf9\u5b66\u751f\u63d0\u4f9b\u4e86\u7cfb\u7edf\u800c\u6709\u6548\u7684\u8bad\u7ec3\uff0c\u6709\u5229\u4e8e\u63d0\u9ad8\u8f6f\u4ef6\u4eba\u5458\u7684\u7d20\u8d28\u548c\u80fd\u529b\u3002 \u76ee\u524d\u5404\u4e2a\u5927\u5b66\u4f7f\u7528\u7684\u6559\u6750\u673a\u68b0\u5de5\u4e1a\u51fa\u7248\u793e\u3001\u56fd\u9632\u5de5\u4e1a\u51fa\u7248\u793e\u51fa\u7248\u7684\u300a\u7f16\u8bd1\u539f\u7406\u300b\u3002\n', 'title': u'\u7f16\u8bd1\u539f\u7406'}]
for data in datas:
    print data['title'], data['summary'].encode("utf-8"), data['url']
'''



