"""
Campbell's Soup Can #2759
Produced: 2026-03-14 09:48:59
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

def type_write(text, color, delay=0.05):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)

def main():
    quote = "I don't fear death; I just don't want to be there when it happens, especially if there's a line at the coffeeshop."
    padding = 2
    inner = " " * padding + quote + " " * padding
    width = len(inner)
    top_bottom = "+" + "-" * width + "+"
    # top border
    sys.stdout.write(CYAN + top_bottom + RESET + "\n")
    # left border + space
    sys.stdout.write(CYAN + "| " + RESET)
    # quoted text with typing effect
    type_write(quote, YELLOW, 0.07)
    # right border + space + newline
    sys.stdout.write(CYAN + " |" + RESET + "\n")
    # bottom border
    sys.stdout.write(CYAN + top_bottom + RESET + "\n")

if __name__ == "__main__":
    main()