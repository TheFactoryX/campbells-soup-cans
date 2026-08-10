"""
Campbell's Soup Can #4526
Produced: 2026-08-10 23:50:44
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def typewriter(text, delay=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # ANSI color codes
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    quote = (
        f"{YELLOW}\"I don't believe in an afterlife, "
        f"but I do bring a spare pair of socks just in case.{RESET}"
    )

    width = len(quote) + 4
    top_bottom = f"{CYAN}{BOLD}┌{'─' * width}┐{RESET}"
    sides = f"{CYAN}{BOLD}│{' ' * width}│{RESET}"

    print(top_bottom)
    print(sides)
    # Print the quote with typewriter effect, centered inside the box
    sys.stdout.write(f"{CYAN}{BOLD}│ {RESET}")
    typewriter(quote, delay=0.05)
    sys.stdout.write(f"{CYAN}{BOLD} │{RESET}\n")
    print(sides)
    print(top_bottom)

if __name__ == "__main__":
    main()