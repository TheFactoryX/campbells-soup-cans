"""
Campbell's Soup Can #1754
Produced: 2026-01-21 13:56:39
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os
import random
from itertools import cycle

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_allen_quote():
    # ANSI color codes
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'
    
    quotes = [
        "I've spent my entire life searching for meaning, only to realize I left my glasses at home.",
        "I tried to be a philosopher once, but I kept getting distracted by my own neurosis.",
        "Life is like a bagel - it's full of holes and sometimes you spread yourself too thin.",
        "I've come to the conclusion that life is just a series of unfortunate events punctuated by moments of mild amusement.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying... but I keep forgetting to not die."
    ]
    
    quote = random.choice(quotes)
    
    clear_screen()
    
    # Animated title with blinking effect
    title = "WOODY ALLEN ON EXISTENTIALISM"
    colors = [BLUE, RED, MAGENTA]
    color_cycle = cycle(colors)
    
    sys.stdout.write("\n")
    for _ in range(3):
        for char in title:
            sys.stdout.write(f"{BOLD}{next(color_cycle)}{char}{END}")
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write("\n")
        time.sleep(0.3)
    
    # ASCII art frame with decorative elements
    frame_top = "╔═════════════════════════════════════════════════════════════════════════════════╗"
    frame_bottom = "╚═════════════════════════════════════════════════════════════════════════════════╝"
    side_border = "║"
    
    # Print frame with decorative elements
    slow_print(YELLOW + frame_top, 0.01)
    
    # Print quote with color cycling
    quote_start = f"{YELLOW}{side_border} {END}"
    slow_print(quote_start, 0.01)
    
    quote_words = quote.split()
    color_cycle = cycle([RED, MAGENTA, CYAN, GREEN])
    for word in quote_words:
        color = next(color_cycle)
        sys.stdout.write(f"{BOLD}{color}{word}{END} ")
        sys.stdout.flush()
        time.sleep(0.1)
    
    slow_print(f"\n{YELLOW}{side_border}", 0.01)
    
    slow_print(YELLOW + frame_bottom, 0.01)
    
    # Animated comment
    time.sleep(1)
    comment = "- Woody Allen, probably while forgetting where he put his keys"
    for char in comment:
        if char == " ":
            sys.stdout.write(char)
        else:
            color = random.choice([GREEN, CYAN, YELLOW])
            sys.stdout.write(f"{color}{char}{END}")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    
    # Animated footer with typewriter effect
    time.sleep(1)
    footer_text = "Press any key to exit (but not too quickly, you might miss the moment)..."
    for i, char in enumerate(footer_text):
        if char == " ":
            sys.stdout.write(char)
        else:
            color = random.choice([CYAN, GREEN, YELLOW, MAGENTA])
            sys.stdout.write(f"{color}{char}{END}")
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Wait for key press
    input()

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

if __name__ == "__main__":
    woody_allen_quote()