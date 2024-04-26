from random import choice
from bs4 import BeautifulSoup
import requests
from csv import DictWriter, DictReader

class Scraper:

    def __init__(self) -> None:
        self.url_to_scrape = "http://quotes.toscrape.com"
        self.current_response = requests.get(self.url_to_scrape)
        self.current_soup = BeautifulSoup(self.current_response.text, "html.parser")
        self.quotes_list = []
        self.tries_left = 4
        self._load_scraped_data()
        

    def _scrape_quotes(self):
        while self.current_soup.select("li.next"):            
            self._gather_quote_data_from_page(self.current_soup)
            modified_url = f"{self.url_to_scrape}{self.current_soup.select('li.next > a')[0]['href']}"
            self.current_response = requests.get(modified_url)
            self.current_soup = BeautifulSoup(self.current_response.text, "html.parser")
        self._gather_quote_data_from_page(self.current_soup)
    
    def _gather_quote_data_from_page(self, soup_var: BeautifulSoup):
        qd = soup_var.find_all(class_="quote")
        for i in qd:
            self.quotes_list.append({
                "qtext": i.select("span.text")[0].getText(),
                "qauthor": i.select("small.author")[0].getText(),
                "qhref": f"{self.url_to_scrape}{i.select('span > a')[0]['href']}"
            })
    
    def _get_hint(self, href):
        self.current_response = requests.get(href)
        self.current_soup = BeautifulSoup(self.current_response.text, "html.parser")
        return f"Author was born on {self.current_soup.select('span.author-born-date')[0].getText()} {self.current_soup.select('span.author-born-location')[0].getText()}"
    
    def _restart_game_prompt(self):
        restart_flag = input("\nGame over. Do you want to play again? y/n:")
        self.tries_left = 4
        if restart_flag.lower()[0] == 'y':
            self.start_game()
        else:
            print("GOODBYE HUMAN!")
    
    def _load_scraped_data(self):
        with open('quote_data.csv', 'r', encoding='utf-8') as f:
            csv_reader = DictReader(f)
            for i in csv_reader:
                self.quotes_list.append(i)
    
    def scrape_to_file(self):
        with open("quote_data.csv", "w", newline='', encoding='utf-8') as f:
            headers = ["qtext", "qauthor", "qhref"]
            csv_writer = DictWriter(f, fieldnames=headers)
            csv_writer.writeheader()
            self._scrape_quotes()
            for i in self.quotes_list:
                csv_writer.writerow(i)
    
    def start_game(self):  
        random_quote = choice(self.quotes_list)
        initials = random_quote['qauthor'].split(' ')  
        print(f"HELLO HUMAN! Here is your random quote: \n\t{random_quote['qtext']}\n Try to guess the author. You have {self.tries_left} tries in TOTAL.\n")   
        while self.tries_left > 0:
            if self.tries_left == 3:
                print(f"Your first hint is: {self._get_hint(random_quote['qhref'])}\n")
            if self.tries_left == 2:
                print(f"Your second hint is FIRST NAME INITIAL: {initials[0][0]}")
            if self.tries_left == 1:
                print(f"Your last hint is LAST NAME INITIAL: {initials[-1][0]}")
            author_input = input("Write your entry here: ")
            if author_input.lower() == random_quote['qauthor'].lower():
                print(f"You've guessed it!!! Congratulations.")    
                break          
            self.tries_left -= 1
        if not self.tries_left:
            print("Sorry, you ran out of guesses.")
        print(f"The author was: {random_quote['qauthor']}")
        self._restart_game_prompt()  

s = Scraper()
# ONLY RUN IF YOU NEED TO REGENERATE DATA
# s.scrape_to_file()
s.start_game()