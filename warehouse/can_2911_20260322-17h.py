"""
Campbell's Soup Can #2911
Produced: 2026-03-22 17:42:39
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_black": "\033[40m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m",
}
RESET = COLORS["reset"]

def type_print(text, delay=0.03, color=COLORS["yellow"]):
    """Print text character by character with a slight delay."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the whole line

def print_boxed_quote(quote):
    """Print a quote inside a colorful ASCII box."""
    # Prepare lines (quote may contain newlines)
    lines = quote.split("\n")
    max_len = max(len(line) for line in lines)
    width = max_len + 4  # padding for borders and spaces

    top = COLORS["cyan"] + "╔" + "═" * (width - 2) + "╗" + RESET
    bottom = COLORS["cyan"] + "╚" + "═" * (width - 2) + "╝" + RESET    print(top)
    for line in lines:
        padded = line.ljust(width - 4)
        # Print border sides
        sys.stdout.write(COLORS["cyan"] + "║ " + RESET)
        # Type the content slowly
        for ch in padded:
            sys.stdout.write(COLORS["yellow"] + ch + RESET)
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(COLORS["cyan"] + " ║" + RESET)
        print()
    print(bottom)

def main():
    # Original Woody Allen‑style quote
    quote = (
        "I spend so much time worrying about the meaning of life "
        "that I forget to actually live it—turns out, the meaning "
        "was the snack break all along."
    )
    print_boxed_quote(quote)

if __name__ == "__main__":
    main()