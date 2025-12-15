"""
Campbell's Soup Can #947
Produced: 2025-12-15 10:46:19
Worker: Meta: Llama 3.2 3B Instruct (free) (meta-llama/llama-3.2-3b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
from random import choice

# ANSI escape codes
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'

def print_quote():
    quotes = [
        "I'm not saying I'm a pessimist, but I'm reading a book about the apocalypse.",
        "Life is like a pizza, even when it's bad, it's still pretty good.",
        "I'm not arguing, I'm just explaining why I'm right. There's a difference.",
        "The only thing I know for sure is that nothing is certain, except death and taxes.",
        "I'm not lazy, I'm just on energy-saving mode."
    ]
    quote = choice(quotes)
    print(f"{BLUE}{YELLOW}Thoughts on Life:{RESET} {quote}")
    time.sleep(1)
    print("\n")

def print_box(message):
    print(f"{GREEN}{'-' * 40}{RESET}")
    print(f"{BLUE}{message}{RESET}")
    print(f"{GREEN}{'-' * 40}{RESET}")

def print_link():
    links = [
        "https://en.wikipedia.org/wiki/Woody_Allen",
        "https://www.imdb.com/name/nm0000164/",
        "https://www.youtube.com/user/WoodyAllen"
    ]
    link = choice(links)
    print(f"{YELLOW}Learn more about Woody Allen at:{RESET} {link}")

def main():
    print_box("Woody Allen Quote Generator")
    print_quote()
    while True:
        command = input("Enter 'q' to quit or 'l' to print a link: ").lower()
        if command == 'q':
            break
        elif command == 'l':
            print_link()
        time.sleep(1)

if __name__ == "__main__":
    main()