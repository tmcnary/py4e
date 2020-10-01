from bs4 import BeautifulSoup
import urllib.request
import csv 
import random
import time
import os

with open('gov_newspapers.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ('name', 'state', 'newspaper', 'article headline', 'date', 'url', 'body text', 'negative', 'positive', 'neutral', 'composite'))
  writer.writeheader()
  news = {}
  for i in range(6):
    mo_url = "https://www.stltoday.com/search/?f=html&q=mike+parson&d1=2018-04-01&d2=2019-07-01&s=start_time&sd=desc&l=100&t=article&nsa=eedition&app%5B0%5D=editorial&o={}00".format(i)
    mo_search = urllib.request.urlopen(mo_url)
    parsed_mo = BeautifulSoup(mo_search.read())
    h3_tag = parsed_mo.find_all('h3', {'class' : 'tnt-headline'})
    for headline in range(len(h3_tag)):
      #time.sleep(2)
      try: 
        news['name'] = "Mike Parsons"
        news['state'] = 'MO'
        news['newspaper'] = 'St. Louis Post Dispatch'
        news['article headline'] = unicodedata.normalize('NFKD', h3_tag[headline].get_text()).strip()
        news['url'] = 'https://www.stltoday.com' + h3_tag[headline].find('a')['href']
        article = urllib.request.urlopen(news['url'])
        parsed_article = BeautifulSoup(article.read())
        news['date'] = parsed_article.find('time').get_text()
        news['body text'] = parsed_article.find('div', {'itemprop' : 'articleBody'}).get_text().strip()
        score = sia.polarity_scores(news['body text'])
        news['negative'] = score['neg']
        news['positive'] = score['pos']
        news['neutral'] = score['neu']
        news['composite'] = score['compound']
        writer.writerow(news)
      except urllib.error.HTTPError:
        pass
