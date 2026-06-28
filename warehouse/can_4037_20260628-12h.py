"""
Campbell's Soup Can #4037
Produced: 2026-06-28 12:46:33
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

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"

def slow_print(text, delay=0.03):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the string

def main():
    quote = (
        "I'm convinced the universe is just a giant therapist's couch, "
        "and I keep forgetting to pay the copay."
    )
    width = len(quote) + 4  # padding inside the box
    top_border = "╔" + "═" * width + "╗"
    bottom_border = "╚" + "═" * width + "╝"
    empty_line = "║" + " " * width + "║"
    quote_line = f"║  {quote}  ║"

    # Optional silly ASCII neurotic face
    face = [
        "   (_/)",
        "  (='.'=)",
        "   (\")_(\")",
    ]

    # Print top border with color
    slow_print(CYAN + BOLD + top_border + RESET, delay=0.005)
    slow_print(CYAN + BOLD + empty_line + RESET, delay=0.005)

    # Print face (in magenta) slowly
    for line in face:
        slow_print(MAGENTA + line + RESET, delay=0.007)

    slow_print(CYAN + BOLD + empty_line + RESET, delay=0.005)

    # Print the quote in yellow with typing effect
    slow_print(YELLOW + BOLD + quote_line + RESET, delay=0.04)

    slow_print(CYAN + BOLD + empty_line + RESET, delay=0.005)
    slow_print(CYAN + BOLD + bottom_border + RESET, delay=0.005)

if __name__ == "__main__":
    main()