"""
Campbell's Soup Can #4014
Produced: 2026-06-25 22:46:11
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A single‑file, self‑contained Python program that prints
a short, neurotic, Woody‑Allen‑style philosophical quote
with a little animation and colors.
"""

import sys
import time
import textwrap

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
RED     = "\033[31m"
GREEN   = "\033[32m"
MAGENTA = "\033[35m"

# Quote to display
QUOTE = (
    "I fear death, but I only wish I'd never "
    "had to order a movie ticket at 3 a.m. in the middle "
    "of night. The absurdity of life is heightened by "
    "the fact that I know I’m just a nervous tumor in a "
    "brain that thinks it's a genius."
)

# Text styling: a box made of ASCII art with a fun border
def print_box(text, padding=1, width=80):
    lines = textwrap.wrap(text, width - 4 - padding*2)
    top = f"+{'-' * (width - 2)}+"
    bottom = top
    print(f"{BOLD}{CYAN}{top}{RESET}")
    for _ in range(padding):
        print(f"|{' ' * (width - 2)}|")
    for line in lines:
        print(
            f"|{' ' * padding}{line:<{width - 4 - padding*2}}{' ' * padding}|"
        )
    for _ in range(padding):
        print(f"|{' ' * (width - 2)}|")
    print(f"{BOLD}{CYAN}{bottom}{RESET}")

# Animated printing of the quote, letter‑by‑letter
def typewriter(text, delay=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != '\n':
            time.sleep(delay)
    print()  # finish with newline

def show_quote():
    # Clear the screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Title
    title = f"{BOLD}{MAGENTA}The Existential Pavlovian Phone Call{RESET}"
    print(f"{title:^{80}}")
    print()

    # Animated quote
    typewriter(f"{BOLD}{YELLOW}{QUOTE}{RESET}", delay=0.06)

    print()
    # Final punchline in a box
    final = f"{RED}“You’re a stupid, neurotic, lonely, and feeling bad human.”{RESET}"
    print_box(final, padding=1, width=80)

if __name__ == "__main__":
    show_quote()
    # Pause so that the user can read the result before the script exits
    try:
        time.sleep(4)
    except KeyboardInterrupt:
        pass
