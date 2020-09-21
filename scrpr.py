import newspaper
from newspaper import article
import requests
from bs4 import BeautifulSoup as bs
from lxml import html

def scrape_AAAS():
    url = 'https://www.aaas.org/news'
    req = requests.get(url)
    soup = bs(req.text , 'lxml')
    articles = soup.find_all("div" , class_ = "aa-teaser-card__body")
    for article in articles:
        base = article.h4.a
        link = url + base.get('href')
        title = base.get_text()
        print(link , title)

def scrape_how_stuff_works():
    pass

def scrape_nature():
    pass

