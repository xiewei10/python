#!/usr/bin/env python3
# coding = utf-8
__author__ = "谢威"

import re
import urllib.request
import urllib



# 打开网页 获取网页源代码
def openURL(url):
    req = urllib.request.Request(url)
    # 伪装一下
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    response = urllib.request.urlopen(req)
    data = response.read().decode("gbk","ignore")
    return  data


#获取种子
def getSeeds(url):
    url = 'http://www.ygdy8.net'+str(url)
    patten = re.compile('<tbody>.*?<tr>.*?<a href="(.*?)">',re.S)
    results = re.findall(patten,openURL(url))
    for x in results:
        return x



# 获取下一步的网页
def getNextLink(url):
    # 正则匹配
    patten = re.compile('<b>.*?<a href="(.*?)" class="ulink">(.*?)</a>.*?</b>',re.S)
    data = openURL(url)
    # 获取电影名字和下一页的链接 会以列表形式返回
    html = re.findall(patten,data)
    i = 0
    for x in html:
        #名字
        name = x[1]

        #获取种子
        seeds = getSeeds(x[0])

        #这里写入文件
        try:
            with open('/Users/xiewei/Desktop/movieSeeds.txt','a') as f:
                f.write('\n\n\n'+"电影名字: "+name+'\n'+"种子: "+seeds)
                print("正在写入%s部电影"%str(i))
        except TypeError:
            print("链接有问题 跳过...")
            continue

        i += 1


url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html'

j = 0
for i in  range(1,3):
    url = 'http://www.ygdy8.net/html/gndy/dyzz/'+"list_23_"+str(i)+'.html'
    print('开始搜索...........')
    getNextLink(url)
    j+=1
    print('第%s页电影保存完毕'%str(j))

