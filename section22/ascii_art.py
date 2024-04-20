import pyfiglet
from colorama import init
from termcolor import colored

permitted_colors = ["blue", "cyan", "red", "magenta", "green"]

init()
supplied_string = input("what message do you want to print? ")
supplied_color = input("\nwhat color? ")
if supplied_color not in permitted_colors:
    supplied_color = "blue"
f = pyfiglet.figlet_format(supplied_string, font="slant")
print(f"\n{colored(f, color=supplied_color)}")
