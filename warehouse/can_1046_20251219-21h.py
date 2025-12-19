"""
Campbell's Soup Can #1046
Produced: 2025-12-19 21:30:34
Worker: Meta: Llama 3.2 3B Instruct (free) (meta-llama/llama-3.2-3b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import sys
import time
from random import randint

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print a color
def print_color(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "end": "\033[0m"
    }
    print(colors[color] + text + colors["end"])

# Function to print a quote
def print_quote(quote):
    clear_screen()
    print_color("Philosophy Alert!", "red")
    print("\n\n" + "-" * 40)
    print_color(quote, "blue")
    print("\n\n" + "-" * 40)
    time.sleep(1) # Pause for 1 second

# List of quotes
quotes = [
    "I'm not worried about what other people think of me. I'm worried about what I think of myself.",
    "I'm not a vegetarian because I love animals. I'm a vegetarian because I hate plants.",
    "I'm reading a book on anti-gravity. It's impossible to put down."
]

# Select a random quote
random_quote = quotes[randint(0, len(quotes) - 1)]

# Print the quote
print_quote(random_quote)