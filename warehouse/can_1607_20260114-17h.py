"""
Campbell's Soup Can #1607
Produced: 2026-01-14 17:43:37
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

def print_box(text, fg_color='\033[38;5;202m', bg_color='\033[48;5;235m'):
    size = 40 + len(text)
    border_top = fg_color + '+' + bg_color*size + '+'
    border_bottom = fg_color + '+' + ('-' * size) + '+'
    interior = fg_color + '| ' + text + ' ' * (size - len(text) - 2) + ' |'
    
    print(border_top)
    for _ in range(2):
        print(interior)
        sleep(0.05)
    print(border_bottom)
    
    sleep(1)
    for _ in range(2):
        print('\033[F' * 4)
        sleep(0.05)

quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "Eternity is really long, especially near the end.",
    "My one regret in life is that I am not someone else.",
    "There are two types of people in this world: those who believe there are two types of people and those who don't.",
    "I am at two with nature.",
]

print_box(random.choice(quotes))