"""
Campbell's Soup Can #2943
Produced: 2026-03-24 11:57:22
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
    border_bottom = fg_color + '+' + ('-')*size + '+'
    content = f'{fg_color}| {text} |\n{bg_color}' + ('~')*len(text)

    print(border_top)
    for _ in range(3):
        print(content)
        sleep(0.1)
    print(border_bottom)
    sleep(0.5)

quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "Eternity is really long, especially near the end.",
    "Existence is for those who have no imagination.",
    "I am at two with nature.",
    "My one regret in life is that I am unable to duplicate myself and meet myself. I would love to argue with me.",
    "To you I'm an atheist; to God, I'm the Loyal Opposition.",
]

print_box(random.choice(quotes))