from multiprocessing import Pool
from homework1 import news, get_res, get_all_links, item_info, url_lists

# print(item_info.count())
# print(url_lists.count())

get_all_links()
allLinks = []
for data in url_lists.find():
    allLinks.append(data['links'])
print(len(allLinks))
if __name__ == '__main__':
    pool = Pool()
    pool.map(get_res, allLinks)
