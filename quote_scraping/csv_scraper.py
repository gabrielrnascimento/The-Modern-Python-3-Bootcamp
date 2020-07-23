import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter
from time import sleep


BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        print(f"Now Scrapping {BASE_URL}{url}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": f"http://quotes.toscrape.com{quote.find('a')['href']}"
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find('a')['href'] if next_btn else None
        # sleep(2)
    return all_quotes

def write_quotes(quotes):
    with open("quotes.csv", "w", newline='',encoding='utf-8') as file:
        headers = ['text', 'author', 'bio-link']
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in all_quotes:
            csv_writer.writerow(quote)

all_quotes = scrape_quotes()
write_quotes(all_quotes)