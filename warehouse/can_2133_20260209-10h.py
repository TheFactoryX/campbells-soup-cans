"""
Campbell's Soup Can #2133
Produced: 2026-02-09 10:16:40
Worker: Qwen: Qwen2.5-VL 7B Instruct (qwen/qwen-2.5-vl-7b-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
from termcolor import colored
from pyfiglet import figlet_format

# Function to display a colorful quote with a box around it
def display_quote(quote):
    print(colored(figlet_format("WOODY ALLEN", font="slant"), "blue"))
    print(colored(figlet_format("-" * 80, font="slant"), "green"))
    print(colored(quote, "cyan", attrs=['bold']))
    print(colored(figlet_format("-" * 80, font="slant"), "green"))
    print(colored(figlet_format("END", font="slant"), "magenta"))

# Woody Allen quote displayed in colorful ASCII art with a box around it
quote = "I'm not afraid of death; I just don't want to be there when it happens."
display_quote(quote)