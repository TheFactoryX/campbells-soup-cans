"""
Campbell's Soup Can #3291
Produced: 2026-04-14 23:04:53
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
┌───────────────────────────────────────────────────────────────────────┐
│                       🐍  Woody‑Allen Style  Quote Bot  🐍               │
│  (Made with pure Python, ANSI colors and a touch of neurotic flair.)  │
└───────────────────────────────────────────────────────────────────────┘
"""

import sys
import time
import random

# ANSI color codes
RESET = "\033[0m"
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
BLUE  = "\033[34m"
MAGENTA="\033[35m"
CYAN  = "\033[36m"
BOLD  = "\033[1m"

# Quote in Woody Allen's signature neurotic style
QUOTE = "If you think you are too small to make a difference, try sleeping with a mosquito. 🌍"

# ASCII art banner with random colors
BANNER_LINES = [
    "  ____          _           _                     _   ",
    " |  _ \\ ___  __| | ___   __| | ___  _ __   ___  | |_ ",
    " | |_) / _ \\/ _` |/ _ \\ / _` |/ _ \\| '_ \\ / _ \\ | __|",
    " |  __/  __/ (_| | (_) | (_| | (_) | | | |  __/ | |_ ",
    " |_|   \\___|\\__,_|\\___/ \\__,_|\\___/|_| |_|\\___|  \\__|",
]

def random_color():
    return random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])

def print_banner():
    for line in BANNER_LINES:
        print(random_color() + line + RESET)
        time.sleep(0.05)

def typing_effect(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # new line

def main():
    print_banner()
    print()
    print(BOLD + YELLOW + "Here comes something existential…" + RESET)
    time.sleep(1.2)
    typing_effect(QUOTE, 0.06)
    print()
    print(GREEN + BOLD + "— Woody (something like) Allen" + RESET)

if __name__ == "__main__":
    main()
