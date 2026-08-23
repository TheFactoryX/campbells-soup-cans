"""
Campbell's Soup Can #4798
Produced: 2026-08-23 21:35:39
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

# ANSI color codes
RESET = "\033[0m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
MAGENTA = "\033[1;35m"

def clear_screen():
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

def slow_print(text, delay=0.05):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    clear_screen()

    # Title
    slow_print(f"{YELLOW}=== Woody's Existential Café ==={RESET}\n", 0.07)

    # The quote, broken for visual balance
    quote_lines = [
        "I don't want to be remembered for my achievements; I just want to be...",
        "...remembered for the way I made everyone feel slightly uncomfortable...",
        "...about their own mortality."
    ]

    # Determine box size based on the longest line
    max_line_len = max(len(line) for line in quote_lines)
    inner_width = max_line_len                 # width for the text part
    box_width = inner_width + 6                # add borders and padding

    top_border = f"{CYAN}╔{'═' * (box_width - 2)}╗{RESET}"
    bottom_border = f"{CYAN}╚{'═' * (box_width - 2)}╝{RESET}"

    # Print top border
    slow_print(top_border)

    # Print each line of the quote inside the box
    for line in quote_lines:
        padded = line.ljust(inner_width)
        middle = f"{CYAN}║{YELLOW}  {padded}  {CYAN}║{RESET}"
        slow_print(middle)

    # Print bottom border
    slow_print(bottom_border)

    # A quirky postscript
    postscript = (
        f"\n{GREEN}☕ Woody's P.S.: If you're still thinking about this, "
        f"maybe order a coffee. It might have more caffeine than your life. {RESET}"
    )
    slow_print(postscript, delay=0.04)

if __name__ == "__main__":
    main()