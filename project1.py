import requests
from bs4 import BeautifulSoup

web= requests.get("https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html")

soup=BeautifulSoup(web.content, "html.parser")

name=soup.find_all('a')

# Iterating over the list
for i in name:
    title = i.get("title")
    
    # Check if title is not None before printing
    if title:
        print(title)

pr=soup.find_all('p', class_="price_color")
for price in pr:
    print(price.text)