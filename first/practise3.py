# 爬取豆瓣电影排行榜
import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '1000',
}
response = requests.get(url=url, params=param, headers=header)
list_data = response.json()
name_list = []
for list in list_data:
    name_list.append(list['title'])
# fp = open('./douban.json', 'w', encoding='utf-8')
# json.dump(list_data, fp=fp, ensure_ascii=False)
# print('over')
print(name_list.__str__())
print(name_list.__len__())