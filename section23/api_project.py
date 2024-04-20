# make a joke generator from dad jokes websites
# add coloful ascii art title
# specify search term(pick one joke randomly from results)
# if there is no joke, let user know

from random import choice
from colorama import init
from termcolor import colored
from pyfiglet import figlet_format
import requests
init()

dad_joke_url = "https://www.icanhazdadjoke.com/search"
headers = {"Accept": "application/json"}
ascii_string = figlet_format("Dad Joke Generator 4444", font="slant")

print(colored(ascii_string, color="blue"))
search_term_input = input("Enter a search term for your dad joke: ")
params = {"term": search_term_input}

res_json = (requests.get(dad_joke_url, headers=headers, params=params)).json()

if res_json['results']:
    rand_joke = choice(res_json['results'])
    print(f"We have found {res_json['total_jokes']
                           } jokes about {search_term_input}. Here 's one: \n{rand_joke['joke']}")
else:
    print("Sorry, we didn't find any joke for that term.")
