"""
Campbell's Soup Can #2580
Produced: 2026-03-05 09:00:30
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys

def print_quote():
    # Woody Allen style quote
    quote = [
        "I don't want to achieve immortality through my work;",
        "I want to achieve it through not dying."
    ]

    # ANSI escape codes for colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    # Create a frame for the quote
    frame = f"""
    {BLUE}┌─────────────────────────────────────────┐{RESET}
    {BLUE}│{RESET} {RED}{BOLD}Woody Allen's Philosophy on Immortality{RESET} {BLUE}│{RESET}
    {BLUE}├─────────────────────────────────────────┤{RESET}
    """

    # Print frame with animation
    print(frame, end="")
    sys.stdout.flush()
    time.sleep(0.5)

    # Print each line of the quote with animation
    for i, line in enumerate(quote):
        line_with_padding = f"│{RESET} {YELLOW}{' ' * (37 - len(line) // 2)}{line}{' ' * (37 - len(line) // 2)}{BLUE}│{RESET}"
        print(line_with_padding)
        sys.stdout.flush()
        time.sleep(0.3)

    # Print bottom of frame
    print(f"{BLUE}└─────────────────────────────────────────┘{RESET}")

    # Attribution with animation
    attribution = f"{GREEN}— Woody Allen{RESET}"
    print(f"\n{attribution}")
    sys.stdout.flush()
    time.sleep(0.5)

    # Fun animation: make the quote "breathe"
    for _ in range(2):
        for color in [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]:
            print(f"\033[1A\033[K{BLUE}│{RESET} {color}{BOLD}I don't want to achieve immortality through my work;{RESET} {BLUE}│{RESET}")
            print(f"\033[1A\033[K{BLUE}│{RESET} {color}{BOLD}I want to achieve it through not dying.{RESET} {BLUE}│{RESET}")
            sys.stdout.flush()
            time.sleep(0.2)

    # Final attribution
    print(f"\n{MAGENTA}— Still Woody Allen{RESET}")
    print(f"{YELLOW}Life is full of misery, loneliness, and suffering - and it's all over much too soon.{RESET}")

if __name__ == "__main__":
    print_quote()