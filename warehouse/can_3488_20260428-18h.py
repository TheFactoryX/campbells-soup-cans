"""
Campbell's Soup Can #3488
Produced: 2026-04-28 18:51:50
Worker: Mistral: Mixtral 8x7B Instruct (mistralai/mixtral-8x7b-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
from time import sleep

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_box(text):
    length = 4 + len(text) + 4
    box = f'{"="*length}\n| {text} |\n{"="*length}'
    print(box)

def woody_quote():
    sayings = [
        f"{Color.OKBLUE}I'm not afraid of death; {Color.FAIL}I just don't want to be there when it happens.{Color.ENDC}",
        f"{Color.OKBLUE}Life is full of misery, loneliness, and suffering {Color.WARNING}AND IT'S ALL OVER MUCH TOO SOON.{Color.ENDC}",
        f"{Color.OKBLUE}I don't want to achieve immortality through my work; {Color.FAIL}I want to achieve it through not dying.{Color.ENDC}"
    ]
    quote = random.choice(sayings)
    print_box(quote)

if __name__ == "__main__":
    sleep(1)
    woody_quote()