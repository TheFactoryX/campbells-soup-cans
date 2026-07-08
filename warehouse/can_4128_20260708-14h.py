"""
Campbell's Soup Can #4128
Produced: 2026-07-08 14:40:33
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

quote = "I don't want to achieve immortality through my work; I want to achieve it by avoiding taxes and eating dessert first."
width = 70

def typewriter(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def print_boxed(text):
    border = CYAN + "#" * width + RESET
    print(border)
    for i, line in enumerate(text.split("\n")):
        line = line.center(width - 2)
        inner = f"{YELLOW}#{RESET} {GREEN}{line}{YELLOW}#{RESET}"
        print(inner)
    print(border)

# Print the boxed, colorful quote with a tiny typing animation
print_boxed(quote)
typewriter(quote, delay=0.02)