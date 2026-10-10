"""
Campbell's Soup Can #5090
Produced: 2026-10-10 18:36:57
Worker: TheDrummer: Skyfall 36B V2 (thedrummer/skyfall-36b-v2)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def print_colorized_text(text, color_code):
    print(f"\033[1;{color_code}m{text}\033[0m")

def print_boxed_text(text, width):
    print_colorized_text("┌" + "─" * width + "┐", 33)
    print_colorized_text(f"│{' ' * width}│", 33)
    print_colorized_text(f"│{text[:width]:^{width}}│", 33)
    print_colorized_text(f"│{' ' * width}│", 33)
    print_colorized_text("└" + "─" * width + "┘", 33)

def print_woody_quote(quote):
    quote_lines = quote.split("\n")
    max_width = max(len(line) for line in quote_lines)
    loading_colors = [32, 33, 31, 36, 35, 34]

    print("\n")
    for i in range(3, 0, -1):
        for color in loading_colors:
            print_colorized_text("   Loading...", color)
            time.sleep(0.1)
            sys.stdout.write("\033[F")  # Move cursor up one line
            sys.stdout.write("\033[K")  # Clear line

    for line in quote_lines:
        print_boxed_text(line, max_width)
        time.sleep(0.5)

    print("\n")

def main():
    woody_quotes = [
        "The talent for being happy is appreciating and ^{letting the small}\\_ joys and '
        "\t\t pleasures of the present moment which come your way,"
        "for they occur 5 times a day...\n",
        "Sex: shared fantasizing and masturbating while sitting in a gifted-eyes \\_source of wonder!\n",
        "If you want to make God laugh, \[...\]\ntell him your future plans\n",
    ]
    quote = random.choice(woody_quotes)
    print_woody_quote(quote)

if __name__ == "__main__":
    main()