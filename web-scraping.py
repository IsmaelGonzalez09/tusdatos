import requests
from bs4 import BeautifulSoup
import json


def web_scraping(url):

    soup = BeautifulSoup(url.text, 'html.parser')
    data_tablets = soup.find_all(class_="col-sm-4 col-lg-4 col-md-4")

    res = []
    for i in data_tablets:
        name = i.find('a')['title']
        price = i.find('h4', attrs={'class': 'pull-right price'}).text
        description = i.find('p', attrs={'class': 'description'}).text
        reviews = i.find('p', attrs={'class': 'pull-right'}).text
        data = {'name':name, 'price':price, 'description': description, 'reviews':reviews}
        res.append(data)

    return res

url1 = requests.get('https://webscraper.io/test-sites/e-commerce/scroll/computers')
url2 = requests.get('https://webscraper.io/test-sites/e-commerce/scroll/phones')

res1 = web_scraping(url1)
res2 = web_scraping(url2)
with open('web-s-computers.json', 'w', encoding='latin-1') as f:
    json.dump(res1, f, indent=8, ensure_ascii=False)
with open('web-s-phones.json', 'w', encoding='latin-1') as f:
    json.dump(res2, f, indent=8, ensure_ascii=False)