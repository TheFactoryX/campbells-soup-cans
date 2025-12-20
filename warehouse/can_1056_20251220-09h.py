"""
Campbell's Soup Can #1056
Produced: 2025-12-20 09:31:51
Worker: Meta: Llama 3.1 405B Instruct (free) (meta-llama/llama-3.1-405b-instruct:free)
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
    # Create a "typewriter" effect
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def print_boxed_quote(quote):
    lines = quote.splitlines()
    max_len = max(len(line) for line in lines)
    border = "—" * (max_len + 4)

    print(YELLOW + border + END_COLOR)
    for line in lines:
        padding = " " * ((max_len - len(line)) // 2)
        print(YELLOW + "| " + padding + line + padding + " |" + END_COLOR)
    print(YELLOW + border + END_COLOR)

def main():
    quote = """
Life is like a restaurant:
the food is overpriced,
the service is terrible,
but you still have to tip... 
your entire existence.
"""

    print("\n" * 5)
    print(RED + "PHILOSOPHICAL QUOTE OF THE DAY" + END_COLOR)
    print("\n" * 2)

    print_boxed_quote(quote)

    print("\n" * 2)
    print(GREEN + "— A wise (and slightly neurotic) philosopher" + END_COLOR)
    print("\n" * 5)

if __name__ == "__main__":
    main()