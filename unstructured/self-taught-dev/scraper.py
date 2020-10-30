# scraping tutorial https://www.youtube.com/watch?v=vIjXuYRLge8
from urllib.request import urlopen
from bs4 import BeautifulSoup

scrape_url = "https://planetdesert.com/collections/cactus"

request_page = urlopen(scrape_url)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

cactus_items = html_soup.find_all('div', class_="grid-product__content")

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)

for cactus in cactus_items:
    title = cactus.find('div', class_="grid-product__title").text
    price = cactus.find('div', class_="grid-product__price").text

    f.write(title + ',' + price)

f.close()