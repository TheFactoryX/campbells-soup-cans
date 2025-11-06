"""
Campbell's Soup Can #99
Produced: 2025-11-06 17:33:18
Worker: Meta: Llama 3.2 3B Instruct (free) (meta-llama/llama-3.2-3b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quotes(quotes):
    colors = {
        "woody": "\033[91m",  # red
        "dark": "\033[90m",  # gray
        "blue": "\033[94m",  # blue
        "green": "\033[92m",  # green
        "yellow": "\033[93m"  # yellow
    }

    for i, quote in enumerate(quotes, start=1):
        print(f"{colors['woody']} {i}. {colors['dark']}{quote}{colors['yellow']}")
        time.sleep(1)  # wait for 1 second

quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I'm like a chicken running around on the farm, and the farmer's running around in his head.",
    "The more I learn, the more I realize how much I don't know. It's like, what's the point of knowing, anyway?"
]

print_quotes(quotes)