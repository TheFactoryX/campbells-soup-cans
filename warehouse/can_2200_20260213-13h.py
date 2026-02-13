"""
Campbell's Soup Can #2200
Produced: 2026-02-13 13:36:38
Worker: Aurora Alpha (openrouter/aurora-alpha)
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

# ANSI escape sequences for colors
RESET   = "\033[0m"
YELLOW  = "\033[1;33m"
CYAN    = "\033[1;36m"
MAGENTA = "\033[1;35m"
GREEN   = "\033[1;32m"

# The Woody‑Allen‑style quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

# Simple typing animation
def type_print(text, delay=0.03, color=YELLOW):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Build a nice box around the quote
def boxed_quote(quote):
    # Determine width (max line length)
    lines = quote.split("\n")
    width = max(len(line) for line in lines) + 4  # padding

    top    = f"{MAGENTA}╔{'═'*width}╗{RESET}"
    bottom = f"{MAGENTA}╚{'═'*width}╝{RESET}"
    middle = []
    for line in lines:
        padded = line.center(width - 2)
        middle.append(f"{MAGENTA}║{CYAN} {padded} {MAGENTA}║{RESET}")

    return "\n".join([top] + middle + [bottom])

def main():
    # Optional: a tiny ASCII art "thinking" face above the box
    art = f"{GREEN}   (¬‿¬)  {RESET}"
    print(art)

    # Show the box with a fade‑in effect (line by line)
    box = boxed_quote(QUOTE).split("\n")
    for line in box:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.1)

    # Finally, type out the quote inside the box for extra flair
    # (we overwrite the previous line with a typing animation)
    time.sleep(0.3)
    # Move cursor up one line (the bottom border) and erase it
    sys.stdout.write("\033[1A\033[2K")
    sys.stdout.flush()
    # Re‑print bottom border
    sys.stdout.write(box[-1] + "\n")
    sys.stdout.flush()
    # Move cursor up to the inner line (the text line)
    sys.stdout.write("\033[2A")
    sys.stdout.flush()
    # Type the quote
    type_print(QUOTE, delay=0.04, color=CYAN)

if __name__ == "__main__":
    main()