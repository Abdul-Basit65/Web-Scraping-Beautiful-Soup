import requests
from bs4 import BeautifulSoup

web = requests.get("https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html")

soup = BeautifulSoup(web.content, "html.parser")

# Find all product containers
products = soup.find_all('article', class_='product_pod')

# Iterating over each product to print its name and price
for product in products:
    title = product.h3.a.get("title")  # Get the title from the 'a' tag inside 'h3'
    price = product.find('p', class_="price_color").text  # Get the price

    # Print the title and price
    print(f"Product: {title}\nPrice: {price}\n")
