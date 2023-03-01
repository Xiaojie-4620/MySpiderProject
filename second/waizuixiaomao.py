import re
import requests
import os


def save(path, img):
    with open(path, 'wb') as fp:
        fp.write(img)

url = 'https://www.kalvin.cn/gl/71470.html'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
# 创建一个文件夹 保存爬取到的图片
if not os.path.exists('./myPhotos1'):
    os.mkdir('./myPhotos1')
# 使用通用爬虫获取页面信息
response = requests.get(url=url, headers=header).text
# 使用聚焦爬虫将页面中的图片进行解析\爬取
# ex = '<div class="bd">.*?<li class=""><a href="(.*?)".*?</a></li>.*?</div>'
# ex = '<li class="">.*?<a href="(.*?)".*?</a></li>'
ex = '.*?<img src="(.*?)">.*?'
src_list = re.findall(ex, response, re.S)
print(src_list)
# for src in src_list:
#     print(src[0:70])
#
for src in src_list:
    src_1 = src[0:70]
    img_data = requests.get(url=src_1, headers=header).content
    # 生成图片名称
    img_name = src_1.split('/')[-1]
    # 图片存储的路径
    img_path = './myPhotos1/' + img_name
    # 存储图片
    save(img_path, img_data)
print(f'Successful Save')

