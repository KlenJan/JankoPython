from colorama import init
from termcolor import colored

init()

# print(dir(termcolor))

# print(help(termcolor))

colored_text = colored("Hello World", color="red",
                       on_color="on_blue", attrs=["blink"])
print(colored_text)
