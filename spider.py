import requests
from bs4 import BeautifulSoup
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
news = client['news']
item_info = news['item_info']
url_lists = news['url_lists']

# 以参考消息社会观察板块为抓取对象
urls = ['http://www.cankaoxiaoxi.com/china/shwx/{}.shtml'.format(i) for i in range(1,51)]

def get_single_links(url):
    try:
        wb_data = requests.get(url)
        print(wb_data.status_code)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        links = soup.select('.txt-list-a > li > a[href]')
        print(links)
        for link in links:
            print(link.get('href'))
            url_lists.insert_one({'links': link.get('href')})
    except:
        print("error")

def get_all_links():
    for url in urls:
        time.sleep(1)
        print(url)
        get_single_links(url)

def get_res(url):
    try:
        contentTxt = ""
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        contents = soup.select('.left_zw > p')
        if (len(contents) == 0):
            contents = soup.select('.inner > .fs-small > p')
        for content in contents:
            contentTxt += content.text
        data = {
            "link": url,
            "content": contentTxt
        }
        item_info.insert_one(data)
        print(data)
    except:
        print("error")



