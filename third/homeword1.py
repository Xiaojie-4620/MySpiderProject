# 爬取三国演义小说所有的章节标题和章节内容
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page = requests.get(url=url, headers=header)
    page.encoding = page.apparent_encoding
    page_text = page.text
    soup = BeautifulSoup(page_text, 'lxml')
    chapter_data = soup.select(".book-mulu li")
    # print(chapter_data)
    fp = open('./chapter_name', 'w', encoding='utf-8')
    for li in chapter_data:
        title = li.a.string
        fp.write(title + '\n')

    print('over!!!!')
