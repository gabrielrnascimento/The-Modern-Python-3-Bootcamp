# Asks for a theme and get jokes about this theme on https://icanhazdadjoke.com

import requests

url = "https://icanhazdadjoke.com/search"

joke_theme = input("Choose the joke theme: ")
response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": joke_theme}
    )


data = response.json()

print(f"We have {data['total_jokes']} {joke_theme} joke(s), here's one: ")
print(data['results'][0]['joke'])
count = 0
count += 1
while count < len(data['results']):
    ask_another = input("Do you want another joke? (y/n) ")
    if ask_another.lower() == 'y':
        print(data['results'][count]['joke'])
        count += 1
    else:
        print("No more jokes for you")
        break
else:
    print(f"There are no more {joke_theme} jokes")
