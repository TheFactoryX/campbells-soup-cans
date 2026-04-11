"""
Campbell's Soup Can #3233
Produced: 2026-04-11 07:17:12
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

# A single-file, colorfully animated Woody‑Allen style philosophical joke
# See: https://en.wikipedia.org/wiki/Woody_Allen

import sys
import time
import math

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
BLINK = "\033[5m"

# 256‑color palette (red, yellow, green, cyan, blue, magenta)
COLO = [
    "\033[38;5;196m",   # bright red
    "\033[38;5;226m",   # bright yellow
    "\033[38;5;46m",    # bright green
    "\033[38;5;51m",    # bright cyan
    "\033[38;5;21m",    # bright blue
    "\033[38;5;201m",   # bright magenta
]

# The witty quote, split into two parts
QUOTE = (
    f"{ITALIC}{BLINK}I kept listening to my heart and it said, "
    f"{BOLD}\"If you want meaning, refuse death. That means living in constant anxiety, "
    f"so I'm avoiding life entirely.\"{RESET}"
)

# Helper: simple spinner animation
def spinner(frames=12, delay=0.05, duration=3):
    for _ in range(int(duration / delay)):
        for i in range(frames):
            sys.stdout.write(f"\r{COLO[i % len(COLO)]}◕{RESET}")
            sys.stdout.flush()
            time.sleep(delay)

# ASCII art border
def art_border(text):
    lines = text.splitlines()
    width = max(len(line) for line in lines)
    top_bottom = ("─" * (width + 4))
    art = f"{COLO[3]}┌{top_bottom}┐{RESET}\n"
    for line in lines:
        art += f"{COLO[3]}│  {line.ljust(width)}  │{RESET}\n"
    art += f"{COLO[3]}└{top_bottom}┘{RESET}"
    return art

# Main routine
def main():
    # Clear terminal for a clean start
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Show a spinning circle while the 'thoughts' settle
    spinner()

    # Print the quote inside a colorful box
    boxed = art_border(QUOTE)
    print(boxed)

    # A final twist: a subtle animation of the quote flipping vertically
    lines = QUOTE.splitlines()
    for _ in range(3):
        for line in reversed(lines):
            sys.stdout.write(f"\r{line}")
            sys.stdout.flush()
            time.sleep(0.07)
        sys.stdout.write("\r" + " " * 80 + "\r")
        sys.stdout.flush()

    # Farewell message
    farewell = f"{COLO[4]}Thanks for sharing my existential dread!{RESET}"
    time.sleep(0.5)
    print(f"\n{farewell}\n")

if __name__ == "__main__":
    main()