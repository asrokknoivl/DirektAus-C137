import requests
from bs4 import BeautifulSoup
import csv

class crawling_machine:
    def __init__(self):
        pass 

    def article_pass(self , link , title , url):
        title = title.lower()
        count = 0
        if len(title.split()) >= 5 and len(title.split()) < 21 and (link.startswith(url) or link.startswith('/')):
            for word in title.split():
                if len(word) > 1:
                    count = count + 1
            if  count >= 5 and self.is_clean(title) :
                return True
            return False

    def is_clean(self , title ):
        db = ['policy' , 'terms' , 'signin' , 'signup' , 'contact' , 'do not sell my into' , 'privacy',
              'authors' , 'service' , 'services' , 'cookies' , 'sign up' , 'sign in' , 'review' , 'reviews',
              'community' , 'subject' , 'sign' , 'facebook' , 'instagram' , 'twitter' , 'rss' , 'news',
              'do not follow']
        print(title.encode('cp1252').decode())
        for word in db:
            if word in title:
                return False
        return True

    def fix_link(self, url , link):
        if link.startswith('/'):
            link = url + link
        return link

    def auto_article_extractor(self , url , code , name):
        open('data/db.csv' , 'a').close()
        open('data/db_links.csv', 'a').close()
        articles = []
        links = []
        req = requests.get(url , headers={'User-Agent': 'Mozilla/5.0'}).text
        soup = BeautifulSoup(req , 'lxml')
        atags = soup.find_all('a')
        for atag in atags:
            link = atag.get('href')
            title = atag.get_text().strip()
            if self.article_pass(link , title , url):
                link = self.fix_link(url , link)
                article = [link , title , code , name]
                links.append(link)
                articles.append(article)
        self.filter_and_save(articles)
        self.save(articles , code)


    def get_old_data(self , code):
        with open(f'data/{code}.csv') as file:
            articles = file.read().split()
        return articles

    def filter_and_save(self , articles):
        filtered_articles = []
        old_articles = self.get_old_data('db_links')
        for article in articles:
            if article[0] in old_articles:
                continue
            filtered_articles.append(article)
        with open('data/db_links.csv' , 'a', newline='') as file:
            for artcl in filtered_articles:
                try:
                    file.write(artcl[0] + '\n')
                except:
                    pass
        with open('data/db.csv' , 'a' , newline='' ) as file:
            filew = csv.writer(file , delimiter='|')
            for artcl in filtered_articles:
                try:
                    filew.writerow(artcl)
                except :
                    pass

    def save(self , articles , code):
        with open(f'data/{code}.csv' , 'w' , newline= '') as file:
            filew = csv.writer(file)
            for article in articles:
                try:
                    filew.writerow(article)
                except :
                    pass


crwl = crawling_machine()
"""
crwl.auto_article_extractor('https://www.nature.com' , 'nature' , 'Nature.com')
crwl.auto_article_extractor('https://www.sciencedaily.com' , 'scdaily' , 'Science Daily')
crwl.auto_article_extractor('https://www.scientificamerican.com/' , 'scius' , 'Scientific American')
crwl.auto_article_extractor('https://www.aaas.org/news' , 'aaas' , 'The American Association for the Advancement of Science')
crwl.auto_article_extractor('https://www.sciencenews.org/' , 'sn' , 'Science News')
crwl.auto_article_extractor('https://www.nytimes.com/section/science' , 'nytimes' , 'The New York Times')
crwl.auto_article_extractor('https://science.howstuffworks.com/' , 'hsw' ,'HowStuffWorks') 
crwl.auto_article_extractor('https://www.sciencenewsforstudents.org/' , 'snfs' , 'Science News for Students')
crwl.auto_article_extractor('https://www.discovery.com/science' , 'discovery' , 'Discovery')
crwl.auto_article_extractor('https://www.livescience.com/' , 'LS' , 'Live Science')
crwl.auto_article_extractor('https://www.space.com/' , 'space' , 'Space.com')
crwl.auto_article_extractor('https://www.popsci.com/' , 'popsci' , 'Popular Science')
crwl.auto_article_extractor('https://www.smithsonianmag.com/' , 'SM' , 'Smithsonian Magazine')
crwl.auto_article_extractor('https://www.newscientist.com/' , 'NS' , 'New Scientist')
crwl.auto_article_extractor('https://www.sciencemag.org/' , 'AAASS' , 'AAAS-Science')
crwl.auto_article_extractor('https://www.redorbit.com/' , 'redorbit' , 'Redorbit')
crwl.auto_article_extractor("http://www.aps.dz/en/" , 'aps' , 'Algeria Press Service')
crwl.auto_article_extractor("https://www.elwatan.com" , 'elwatan' , 'El watan')
crwl.auto_article_extractor("https://www.liberte-algerie.com" , 'lib' , 'Liberté-Algerie')
crwl.auto_article_extractor("http://www.elmoudjahid.com" , 'mhjd' , 'El Moudjahid')
"""



crwl.auto_article_extractor("https://www.liberte-algerie.com" , 'lib' , 'Liberté-Algerie')





