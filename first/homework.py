import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
kw = input('enter a city\n')
data_list = []
for i in range(1, 10):
    page = str(i)
    param = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': page,
        'pageSize': '10',
    }

    response = requests.post(url=url, params=param, headers=header)
    data_list.append(response.text)
    # fp = open('KFC.json', 'w', encoding='utf-8')
    # json.dump(list_data, fp=fp, ensure_ascii=False)
    # fp.close()
with open('message', 'w', encoding='utf-8') as fp:
    fp.write(data_list.__str__())
print('over!!!')