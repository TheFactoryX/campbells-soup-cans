"""
Campbell's Soup Can #4607
Produced: 2026-08-15 14:39:01
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

def typewriter(text, delay=0.05):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delta)
    print()  # newline after finished

def main():
    plain_quote = (
        "I'm terrified of commitment; I can't even decide whether to commit to a sandwich or to existential dread."
    )
    # Colored version of the quote (bright yellow)
    colored_quote = f"\033[1;33m{plain_quote}\033[0m"

    # Box width based on visible text length (plus two spaces for padding)
    width = len(plain_quote) + 4

    top_bottom = f"\033[1;36m+{'-' * width}+\033[0m"
    side = f"\033[1;36m|\033[0m"

    print(top_bottom)
    print(f"{side} {colored_quote} {side}")
    print(top_bottom)

    # Playful blinking cursor after the quote
    for _ in range(3):
        sys.stdout.write("\033[1;32m_\033[0m")  # green blinking underscore
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b \b")  # erase underscore
        sys.stdout.flush()
        time.sleep(0.5)
    print()  # final newline

if __name__ == "__main__":
    main()