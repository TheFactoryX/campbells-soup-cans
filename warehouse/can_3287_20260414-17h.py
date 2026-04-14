"""
Campbell's Soup Can #3287
Produced: 2026-04-14 17:34:40
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
A little theatrical program that flashes a Woody‑Allen‑style philosophical quip
with a splash of color, animation, and a bit of existential dread.
"""

import time
import sys
import os

# ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED   = "\033[31m"
GREEN = "\033[32m"
YEL   = "\033[33m"
BLUE  = "\033[34m"
PURP  = "\033[35m"
CYAN  = "\033[36m"
WHITE = "\033[37m"

# A tiny spinner animation (used while "thinking")
SPINNER = ['|', '/', '-', '\\']

def clear_screen():
    """Clear the terminal screen in a cross‑platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')

def spin(seconds=1.5, label="Thinking"):
    """Spin for a given number of seconds, printing the label in a box."""
    end_time = time.time() + seconds
    idx = 0
    print(f"{CYAN}{BOLD}[{label}] {SPINNER[idx % len(SPINNER)]}{RESET}", end="", flush=True)
    while time.time() < end_time:
        time.sleep(0.1)
        idx += 1
        print(f"\r{CYAN}{BOLD}[{label}] {SPINNER[idx % len(SPINNER)]}{RESET}", end="", flush=True)
    print("\n")  # move to next line after spinning

def draw_box(text, color=WHITE, width=None):
    """Print text inside a colourful ASCII box."""
    lines = text.split('\n')
    if width is None:
        width = max(len(line) for line in lines) + 4  # padding
    top = f"{color}+{'-' * (width - 2)}+"
    print(top)
    for line in lines:
        print(f"| {line.ljust(width - 4)} |")
    print(top + RESET)

def main():
    clear_screen()
    quote = (
        f"{YEL}My philosophy? I spend as much time worrying about the meaning of life as I do "
        f"calculating how many times I have to drink coffee before my existential crisis reaches "
        f"a critical mass.{RESET}"
    )
    # Show "thinking" spinner
    spin(label="Contemplating")

    # Display the quote in a colourful box
    draw_box(quote, color=PURP)

    # A little animated confetti using time delays
    confetti_colors = [RED, GREEN, YEL, BLUE, PURP, CYAN]
    for i in range(10):
        for color in confetti_colors:
            sys.stdout.write(f"\r{color}•{RESET}")
            sys.stdout.flush()
            time.sleep(0.05)
    print("\n")

    # Final witty remark
    final = f"{BOLD}{GREEN}But remember: I’ve been told I’m as nervous as a hedgehog in a jazz club.{RESET}"
    print(final)

if __name__ == "__main__":
    main()