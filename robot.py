# _*_ coding: utf-8 _*_

import urllib,re,Mysqldb

def getHtml():
    html = urllib.urlopen('http://www.quanshu.net/book/9/9055/').read()
    text = html.decode('gb2312').encode('utf-8')
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a>'
    return re.findall(reg,text)

def getContent(url):
    html = urllib.urlopen(html = urllib.urlopen('http://www.quanshu.net/book/9/9055/' + url).read()
    text = html.decode("gbk").encode("utf-8")
    print text

for i in getHtml():
    print i[0]
    print i[1]
    getContent(i[0])
    mysql = Mysqldb.connect()

更新测试