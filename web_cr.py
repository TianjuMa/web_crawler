import requests
from bs4 import BeautifulSoup
# from lxml import html, etree
# import pandas as pd
import time
from MyDBManager import *

db_manager = MyDBManager()


def saveToDB(data):
    # print(data)
    # for key in data.items():
    #     print(key)
        # db_manager.insert(item)
    db_manager.insert(data)


def crawl(url):
    wb_data = requests.get(url)
    time.sleep(0.2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-of-type(1)')
    rates = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > div > span.rating_num')
    imgs = soup.select('#content > div > div.article > ol > li > div > div.pic > a > img')
    details = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a')

    for img, title, rate, detail in zip(imgs, titles, rates, details):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'rate': rate.get_text(),
            'details': fetchShortComment(detail.get('href'))
        }
        # print(data)

        saveToDB(data)


def fetchShortComment(url='https://movie.douban.com/subject/1307914/'):
    wb_data = requests.get(url)
    # time.sleep(2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    all_short_page_url = soup.select('#comments-section > div.mod-hd > h2 > span > a')

    return all_short_comments(all_short_page_url[0].get('href'))


def all_short_comments(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    comments = soup.select('#comments > div > div.comment > p > span')

    return [comment.get_text() for comment in comments]


if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        crawl(url=url)
