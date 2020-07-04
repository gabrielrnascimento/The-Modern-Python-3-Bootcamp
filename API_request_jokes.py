# Asks for a theme and get jokes about this theme on https://icanhazdadjoke.com

import requests
from termcolor import colored, cprint
import colorama
import pyfiglet

url = "https://icanhazdadjoke.com/search"

def header():
    colorama.init()
    header = colored(pyfiglet.figlet_format("DAD JOKES inc."), color="green")
    return print(header)

header()

joke_theme = input("Choose the joke theme: ")
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": joke_theme}
).json()

if response['total_jokes'] >= 1:
    if response['total_jokes'] == 1:
        print(f"I've got {response['total_jokes']} {joke_theme} joke, here it is: ")
        print(response['results'][0]['joke'])
    else:
        print(f"I've got {response['total_jokes']} {joke_theme} jokes, here's one: ")
        print(response['results'][0]['joke'])
        count = 0
        count += 1
        while count < len(response['results']):
            ask_another = input("Do you want another joke? (y/n) ")
            if ask_another.lower() == 'y':
                print(response['results'][count]['joke'])
                count += 1
            else:
                print("No more jokes for you")
                break
        else:
            print(f"There are no more {joke_theme} jokes")
else:
    print(f"Sorry, I don't have any jokes about {joke_theme}. Please try again.")
