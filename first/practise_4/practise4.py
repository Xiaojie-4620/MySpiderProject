import requests
import json

if __name__ == "__main__":
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/allQyxx/allQyxx.jsp'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    param = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'xkType': '2',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }
    response = requests.post(url=url,data=param, headers=header)
    page = response.text
    print(page)
    # print(page_text)
    # fp = open('./xi.json', 'w', encoding='utf-8')
    # json.dump(page, fp=fp, ensure_ascii=False)
    # fp.close()
    print('Over')