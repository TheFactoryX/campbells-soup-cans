"""
Campbell's Soup Can #1431
Produced: 2026-01-06 14:41:56
Worker: Mistral: Mistral 7B Instruct (free) (mistralai/mistral-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# ANSI color codes
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}

# ASCII art frame
FRAME = [
    "╔══════════════════════════════════════════════════════════╗",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "║                                                           ║",
    "╚══════════════════════════════════════════════════════════╝"
]

# Woody Allen style quotes
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "The heart wants what it wants, but the brain knows better. Unfortunately, the heart has a better PR team.",
    "I'm at two with nature. I don't trust it.",
    "I'm not a pessimist, I'm a realist with a pessimistic outlook.",
    "I'm not afraid of dying. I just don't want to be there when it happens.",
    "I'm not a vegetarian because I love animals. I'm a vegetarian because I hate plants.",
    "I'm not a psycho. I'm a psychoanalyst. There's a big difference.",
    "I'm not a sex maniac. I'm a sex fanatic. There's a big difference."
]

def print_frame():
    for line in FRAME:
        print(line)

def print_quote(quote, color):
    print(f"\n{color}║ {quote.center(60)}{COLORS['reset']} ║\n")

def animate_quote(quote, color):
    for char in quote:
        print(f"{color}{char}{COLORS['reset']}", end='', flush=True)
        time.sleep(0.05)
    print()

def main():
    print("\033[2J\033[H")  # Clear screen
    random_color = random.choice(list(COLORS.keys()))
    random_quote = random.choice(QUOTES)

    print_frame()
    print_quote("A WOODY ALLEN STYLE PHILOSOPHICAL QUOTE", "yellow")
    print_frame()

    print(f"\n{COLORS[random_color]}")
    animate_quote(random_quote, COLORS[random_color])
    print(f"{COLORS['reset']}\n")

    print_frame()
    print_quote("THANK YOU FOR YOUR ATTENTION", "cyan")
    print_frame()

if __name__ == "__main__":
    main()