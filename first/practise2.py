import requests as rts
import json
# URL
post_url = 'https://fanyi.baidu.com/sug'
kw = input('input a word\n')
data = {'kw': kw}
# UA伪装
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
# 请求发送
response = rts.post(url=post_url, data=data, headers=header)
# 获取响应数据
message_dict = response.json()
fileName = kw +'.json'
# fp = open(fileName, 'w', encoding='utf-8')
# json.dump(message_dict, fp=fp, ensure_ascii=False)
# fp.close()
print(message_dict)
print(f'Successful!!!')
