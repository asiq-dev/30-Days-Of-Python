import requests

from bs4 import BeautifulSoup


price_selector = ".price_color"
title_selector = ".product_pod h3 a"

data = requests.get("https://books.toscrape.com/").content

soup = BeautifulSoup(data, "html.parser")

# print(soup)


prices = soup.select(price_selector)
titles = soup.select(title_selector)


with open("books.csv", "w" , encoding="utf-8") as book_file:
    for price, title in zip(prices, titles):
       book_file.write(f" {title['title']},{price.string}\n ")
