"""
Campbell's Soup Can #186
Produced: 2025-11-10 15:34:20
Worker: Meta: Llama 4 Maverick (free) (meta-llama/llama-4-maverick:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
END_COLOR = "\033[0m"

def print_quote(quote):
    # Create a box around the quote
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    print(f"{BLUE}+{'-' * (max_len + 2)}+{END_COLOR}")
    for line in lines:
        print(f"{BLUE}|{END_COLOR} {line.ljust(max_len)} {BLUE}|{END_COLOR}")
    print(f"{BLUE}+{'-' * (max_len + 2)}+{END_COLOR}")

def animate_text(text, color):
    for char in text:
        sys.stdout.write(f"{color}{char}{END_COLOR}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def main():
    quote = f"I'm not afraid of death;\nI just don't want to be there when it happens."
    print(f"{YELLOW}{'=' * 40}{END_COLOR}")
    animate_text("Woody Allen's Wisdom", GREEN)
    print(f"{YELLOW}{'=' * 40}{END_COLOR}\n")
    print_quote(quote)
    print(f"\n{YELLOW}{'=' * 40}{END_COLOR}")
    animate_text("Ponder... ", RED)

if __name__ == "__main__":
    main()