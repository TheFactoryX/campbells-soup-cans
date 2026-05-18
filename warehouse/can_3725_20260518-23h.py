"""
Campbell's Soup Can #3725
Produced: 2026-05-18 23:31:11
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A little neurotic, existential, and all‑in‑one colored Woody Allen quote.
"""

import sys
import time
import shutil

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
ITALIC  = "\033[3m"
FG_RED  = "\033[31m"
FG_CYAN = "\033[36m"
FG_YEL  = "\033[33m"
BG_DGRY = "\033[100m"

# The quote we will animate
QUOTE = (
    f"{FG_CYAN}{BOLD}I think when I ask myself what is the meaning of life, "
    f"I answer: {ITALIC}I just want to avoid running out of take‑out lunch{ITALIC}"
    f" before I die. {RESET}"
)

# A simple spinning cursor animation
SPINNER = "|/-\\"

def draw_box(text: str) -> str:
    """Return the text wrapped in an ASCII art box with colors."""
    lines = text.split('\n')
    width = max(len(line) for line in lines) + 4
    top = f"{FG_YEL}┌{'─' * (width-2)}┐{RESET}"
    bottom = f"{FG_YEL}└{'─' * (width-2)}┘{RESET}"
    boxed_lines = [
        f"{FG_YEL}│ {RESET}{line.ljust(width-4)}{FG_YEL} │{RESET}"
        for line in lines
    ]
    return "\n".join([top] + boxed_lines + [bottom])

def main():
    """Print the quote with a little animation."""

    # clear the screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # print header
    header = f"{FG_RED}{BOLD}Quirky Existential Couch Conversation:{RESET}"
    print(header)
    print()

    # animate the spinner while preparing the quote
    for _ in range(10):
        sys.stdout.write(f"\r{ITALIC}{SPINNER[_ % len(SPINNER)]} Preparing?{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write("\r                          \r")  # clear line

    # box the quote
    boxed = draw_box(QUOTE)
    print(boxed)

    # pause before exit
    time.sleep(2)

if __name__ == "__main__":
    main()