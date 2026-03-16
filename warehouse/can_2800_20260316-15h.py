"""
Campbell's Soup Can #2800
Produced: 2026-03-16 15:19:31
Worker: Healer Alpha (openrouter/healer-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

# The quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."
author = "— Woody Allen"

# Visual elements
box_top = "╔" + "═" * 58 + "╗"
box_mid = "║" + " " * 58 + "║"
box_bottom = "╚" + "═" * 58 + "╝"

# Typewriter effect function
def typewriter(text, color, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Clear screen (works on most terminals)
print("\033[2J\033[H")

# Title with animation
title = " philosophical wisdom "
print(BOLD + YELLOW, end="")
for i in range(len(title)):
    print(title[i], end="", flush=True)
    time.sleep(0.05)
print(RESET + "\n")

# Box animation
print(CYAN)
for char in box_top:
    print(char, end="", flush=True)
    time.sleep(0.01)
print()

# Empty lines in box
for _ in range(3):
    print(box_mid)

print(box_bottom + RESET)

# Position cursor for quote
print("\033[5A")  # Move cursor up 5 lines
print("\033[22C")  # Move cursor right 22 columns

# Typewriter effect for quote
typewriter(quote, WHITE, 0.04)

# Move cursor down and right for author
print("\033[2B")  # Move cursor down 2 lines
print("\033[36C")  # Move cursor right 36 columns

# Author with pulsing effect
print(MAGENTA + BOLD, end="")
for i in range(3):  # Pulse effect
    print("\r" + " " * 20 + "\r", end="", flush=True)
    time.sleep(0.2)
    print(author, end="", flush=True)
    time.sleep(0.3)
print(RESET)

# Final decorative line
print("\n" + YELLOW + "·" * 60 + RESET)

# Small existential joke at the end
time.sleep(1)
print("\n" + CYAN + "   (But what do I know? I'm just a program.)" + RESET)