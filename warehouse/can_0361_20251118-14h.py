"""
Campbell's Soup Can #361
Produced: 2025-11-18 14:36:21
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

import sys
import time
import os

# ANSI color codes
RESET = "\033[0m"
BLACK = "\033[30m"
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE  = "\033[34m"
MAGENTA = "\033[35m"
CYAN  = "\033[36m"
WHITE = "\033[37m"

# Bright variants
BRIGHT_RED   = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE  = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN  = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Clear screen helper
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Simple typewriter effect
def type_print(text, color=WHITE, speed=0.05):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

# ASCII art for a "brain"
brain_art = r"""
          _______
         /       \
        /  (  )  )\
       (   > <   ) )
        \__   __/
          | | |
          | | |
          |_|_|
"""

def main():
    clear_screen()
    # Print header
    header = f"{BRIGHT_MAGENTA}+-------------------------------------------+{RESET}"
    type_print(header, speed=0.01)
    quote_box = f"{BRIGHT_CYAN}│{RESET} "
    # Quote in Woody Allen style
    quote = (f"{BRIGHT_YELLOW}I’m not a philosopher, I’m a broken record replaying the same "
             f"melancholy soundtrack. I think, therefore I’m terrified of my own "
             f"thoughts. {BRIGHT_YELLOW}—{RESET}")
    # Wrap quote to width 47
    max_len = 47
    words = quote.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_len:
            current += (" " if current else "") + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    # Print quote inside box
    for line in lines:
        padded = line.ljust(max_len)
        type_print(quote_box + f"{BRIGHT_WHITE}{padded}{RESET} {quote_box}", speed=0.01)
    # Bottom border
    type_print(header, speed=0.01)
    # Spacer
    time.sleep(0.5)
    # Draw brain
    for line in brain_art.splitlines():
        type_print(line, color=BRIGHT_MAGENTA, speed=0.02)

if __name__ == "__main__":
    main()