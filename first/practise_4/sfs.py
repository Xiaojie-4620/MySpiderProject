import requests
import json

if __name__ == "__main__":
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=ed9f2964df024b22af19a6e5fdd0f411'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    response = requests.post(url=url, headers=header)
    page = response.text
    # print(page)
    # with open('xinxi', 'w', encoding='utf-8') as fp:
    #    fp.write(page)
    # fp.close()
    fp = open('xinxi.json', 'w', encoding='utf-8')
    json.dump(page, fp=fp, ensure_ascii=False)
    print('Over')