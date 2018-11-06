import requests
from bs4 import BeautifulSoup
from lxml import html, etree
import pandas as pd
import time
import pymongo

def crawl(url):
# #content > div > div.article > ol > li:nth-child(18) > div > div.info > div.hd > a
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-of-type(1)')
    rates = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > div > span.rating_num')
    imgs = soup.select('#content > div > div.article > ol > li > div > div.pic > a > img')
    details = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a')

    for img, title, rate, detail in zip(imgs, titles, rates, details):
        data = {
            'img': img.get('src'),
            'title': title.get_text(),
            'rate': rate.get_text(),
            'details':detail.get('href')
        }
        print(data['title'], data['details'])


if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 25, 25)]
    for url in urls:
        crawl(url=url)

