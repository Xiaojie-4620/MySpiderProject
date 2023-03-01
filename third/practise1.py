# 使用bs4 中的 BeautifulSoup 对对象中的相关属性或者方法进行标签定位和数据提取
from bs4 import BeautifulSoup
import requests

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 实例化BeautifulSoup对象
soup = BeautifulSoup(html, 'lxml')
# `tagName` 获取网页中第一次出现的标签名内的信息 没有此类型标签则返回·None·
print(soup.a)  # OutPut: <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.div)
# soup.find('p') 等同于 soup.p
print(soup.find('p'))  # <p class="title"><b>The Dormouse's story</b></p>
# find 函数可以通过指定 class_ 参数查找相应class值的第一次出现的标签
print(soup.find('p', class_='story'))
# find_all 函数 找到soup对象中所有的对应的标签的内容 返回一个列表
print(soup.find_all('p'))
# select 是一个CSS选择器 返回值是一个列表
# print(soup.select('.sister'))
'''
获取标签之间文本数据:
.string 只能获取该标签下直系的文本内容 
get_text()和.text 二者都可以获取标签下的所有文本内容 
'''
print(soup.select('.sister')[0].string)   # Elsie

print(soup.find('p', class_='story').get_text())
'''
Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
'''
print(soup.find('p', class_='story').string)  # None
