"""
Campbell's Soup Can #4448
Produced: 2026-08-06 09:58:01
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import sys
import time

def sleep_print(text, delay=0.1):
    """Print characters one by one with a short delay for a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    # ANSI color codes
    reset = "\033[0m"
    green = "\033[32m"
    cyan = "\033[36m"
    yellow = "\033[33m"
    bold = "\033[1m"

    # A witty Woody Allen‑style philosophical quote (invented here)
    quote = "I don't fear death; I just don't want to be there when it arrives with a calculator."
    author = "— Woody Allen"

    # Intro line
    intro = f"{bold}{green}In the style of Woody Allen:{reset}"
    sleep_print(intro, 0.05)

    # Determine box width based on the longest line
    width = max(len(quote), len(author)) + 4   # 2 spaces padding each side

    # Top border
    top_border = f"{green}+{'-' * width}+{reset}"
    sleep_print(top_border, 0.05)

    # Quote line
    quote_line = (
        f"{cyan}|{yellow}  {quote}{' ' * (width - len(quote) - 4)}  {cyan}|{reset}"
    )
    sleep_print(quote_line, 0.05)

    # Author line
    author_line = (
        f"{cyan}|{yellow}  {author}{' ' * (width - len(author) - 4)}  {cyan}|{reset}"
    )
    sleep_print(author_line, 0.05)

    # Bottom border
    bottom_border = f"{green}+{'-' * width}+{reset}"
    sleep_print(bottom_border, 0.05)

if __name__ == "__main__":
    main()