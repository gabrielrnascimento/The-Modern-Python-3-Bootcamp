"""
Web Scraping Project

Introduction

In this project you'll be building a quotes guessing game. 
When run, your program will scrape a website for a collection of quotes. 
Pick one at random and display it. The player will have four chances to guess who said the quote. 
After every wrong guess they'll get a hint about the author's identity.
"""

import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"

# read scraped page as csv (written by csv_scrapper.py)
def read_quotes(filename):
    with open(filename, "r",encoding='utf-8') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

# choose a dictionary
def choose_quote(all_quotes):
    random_quote = choice(all_quotes)
    return random_quote

# check if user answer was equal to author's name
def check_answer(guess_count, author):
    answer = input(f"Who said this? Guesses remaining {guess_count}.\n")
    if answer.lower() == author.lower():
        return True
    return False

#gives a hint to the user regarding the number of guesses ramaining
def author_hint(guess_count, quote):
    if guess_count == 3:
        author_res = requests.get(quote['bio-link'])
        author_soup = BeautifulSoup(author_res.text, 'html.parser')
        born_date = author_soup.find(class_="author-born-date").get_text()
        born_location = author_soup.find(class_="author-born-location").get_text()
        print(f"Here's a hint: The author was born on {born_date} {born_location}")
    elif guess_count == 2:
        initials = " ".join([name[0] for name in quote['author'].split(" ")])
        print(f"Here's a hint: The author's initials are {initials}")
    elif guess_count == 1:
        first_name_letters = len(quote['author'].split(" ")[0])
        print(f"Here's a hint: There are {first_name_letters} letters in the author first name.")

def play_game():
    play = True
    while play:
        quote = choose_quote(all_quotes)
        print("Here's a quote:")
        print(quote['text'])
        guess_count = 4
        while guess_count > 0:
            if check_answer(guess_count,quote['author']):
                print("You Guessed Right! Congrats!")
                break
            guess_count -= 1
            author_hint(guess_count, quote)
        else:
            print("You have no more guesses, you lose!")
            print(f"The author was {quote['author']}!")
        replay = ''
        while replay.lower() not in ('y', 'yes', 'n', 'no'):
            replay = input("Do you want to play again? (y/n) ")
        if replay.lower() in ("y", 'yes'):
            play = True
        elif replay.lower() in ("n", 'no'):
            play = False
    print("Thanks for playing!")

all_quotes = read_quotes("quotes.csv")
play_game()