"""
Campbell's Soup Can #1228
Produced: 2025-12-28 05:41:10
Worker: Nous: Hermes 3 405B Instruct (free) (nousresearch/hermes-3-llama-3.1-405b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    author = "Woody Allen"

    # Print the quote with a typewriter effect
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

    # Print the author and a separator with colors
    print(f"\n\x1b[32m{author}\x1b[0m")
    print("\x1b[34m" + "-" * len(quote) + "\x1b[0m")

def main():
    print_quote()

if __name__ == "__main__":
    main()