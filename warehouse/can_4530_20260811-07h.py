"""
Campbell's Soup Can #4530
Produced: 2026-08-11 07:37:15
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI escape codes for colors
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def type_line(text, delay=0.05):
    """Print text character by character with a slight delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    # Box width (adjust as needed)
    WIDTH = 60

    # Build top and bottom border
    top_border = f"{CYAN}┌─{'─' * WIDTH}─┐{RESET}"
    bottom_border = f"{CYAN}└─{'─' * WIDTH}─┘{RESET}"

    print(top_border)

    # Woody‑Allen‑style philosophical quote, split into two lines
    lines = [
        f"{YELLOW}Life is a tragedy for those who think and a comedy for{RESET}",
        f"{YELLOW}those who feel—no wonder we're all so confused.{RESET}"
    ]

    for line in lines:
        # Print each line inside the box with a typing effect
        type_line(f"{CYAN}│{RESET} {line} {CYAN}│{RESET}")

    print(bottom_border)

    # Add attribution after a brief pause
    time.sleep(0.5)
    print(f"{CYAN}— Woody Allen{RESET}")

if __name__ == "__main__":
    main()