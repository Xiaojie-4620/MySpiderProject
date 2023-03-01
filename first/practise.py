import requests as rts


if __name__ == "__main__":
    # UA伪装 将对应的User-Agent封装到一个字典中
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数
    key = input('enter a word')
    param = {'query': key}

    # 对指定的url发起的请求是携带参数的，并且请求过程中处理了参数
    response = rts.get(url=url, params=param, headers=headers)

    page = response.text
    fileName = key + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page)
    print(f'Successful!!!')
