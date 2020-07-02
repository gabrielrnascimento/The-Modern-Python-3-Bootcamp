import pyfiglet
import termcolor
import colorama

color_list = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
text = input("What would you like to print? ")
print("Choose one:")
for color in color_list:
    print(color)
color = input()
if color not in color_list:
    color = 'magenta'


colorama.init()
colored_text = termcolor.colored(pyfiglet.figlet_format(text), color=color)

print(colored_text)
