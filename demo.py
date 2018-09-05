# -*- coding:UTF-8 -*-
import requests


def test1():
    target = 'http://gitbook.cn/'
    req = requests.get(url=target)
    print(req.text)


# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests


def test2():
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, "lxml")
    texts = bf.find_all('div', class_='showtxt')
    f = open('filename.txt', 'rb')
    # f.write(texts[0])
    f.close()
    print(texts[0].text.replace('\xa0' * 8, '\n\n'))
    # for it in texts:
    #     print(it)

    # print(texts[0])
    # print.flush()


if __name__ == '__main__':
    test2()
