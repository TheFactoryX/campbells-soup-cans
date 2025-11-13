"""
Campbell's Soup Can #239
Produced: 2025-11-13 02:17:58
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import itertools

# ANSI colour codes
RESET  = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"

# Quote in Woody Allen style
QUOTE = (
    f"{BOLD}{CYAN}'I am not nervous about the abyss beyond my couch, "
    f"just that my existential dread may have already outlived the caffeine '
    f"boiling in my brain.'{RESET}"
)

def animated_spinner(duration: float = 2.0, frame_delay: float = 0.1):
    """Show a rotating spinner for a given duration."""
    spinner = itertools.cycle([f"{YELLOW}⠋{RESET}",
                               f"{YELLOW}⠙{RESET}",
                               f"{YELLOW}⠹{RESET}",
                               f"{YELLOW}⠸{RESET}",
                               f"{YELLOW}⠼{RESET}",
                               f"{YELLOW}⠴{RESET}",
                               f"{YELLOW}⠦{RESET}",
                               f"{YELLOW}⠧{RESET}",
                               f"{YELLOW}⠇{RESET}",
                               f"{YELLOW}⠏{RESET}"])
    steps = int(duration / frame_delay)
    for _ in range(steps):
        print(f"\r{next(spinner)} Shocking...{BOLD}{WHITE}...", end='', flush=True)
        time.sleep(frame_delay)
    print("\r" + " " * 30 + "\r", end='')   # clear line

def print_boxed_text(text: str):
    """Print the given text inside a colourful ASCII-art box."""
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    border = f"{MAGENTA}╭{'─' * (max_len + 2)}╮{RESET}"
    bottom = f"{MAGENTA}╰{'─' * (max_len + 2)}╯{RESET}"
    print(border)
    for line in lines:
        padded = line.ljust(max_len)
        print(f"{MAGENTA}│{RESET} {BOLD}{padded}{RESET} {MAGENTA}│{RESET}")
    print(bottom)

def main():
    # Step 1: simple breathing animation
    print(f"{GREEN}Preparing..." + f"{RESET}")
    animated_spinner(duration=3.0, frame_delay=0.12)

    # Step 2: Pause and then show the quote
    time.sleep(0.5)
    print_boxed_text(QUOTE)

    # Step 3: A little flourish at the end
    for _ in range(3):
        print(f"{CYAN}~{RESET}", end='', flush=True)
        time.sleep(0.2)
    print()

if __name__ == "__main__":
    main()