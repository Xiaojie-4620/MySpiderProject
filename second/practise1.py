import requests

if __name__ == '__main__':
    url = 'https://img.wxcha.com/m00/39/43/e6ae8ffa55fb94cb153dc68478f34487.jpg'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    # content 返回二进制形式的数据 \ text 字符串形式数据 \ json() 对象类型的数据
    img_data = requests.get(url=url).content
    with open('./photo.jpg', 'wb') as fp:
        fp.write(img_data)

    