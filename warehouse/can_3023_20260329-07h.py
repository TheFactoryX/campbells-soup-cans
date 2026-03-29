"""
Campbell's Soup Can #3023
Produced: 2026-03-29 07:19:00
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody_quote.py
import time
import sys

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_slowly(text, delay=0.05):
    """Print text slowly to create a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_quote(quote):
    """Animate the quote with colors and effects"""
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    for i, line in enumerate(quote.split('\n')):
        color = colors[i % len(colors)]
        print(f"{color}{line}{RESET}")
        time.sleep(0.5)

def draw_box(text):
    """Draw a box around the text"""
    width = max(len(line) for line in text.split('\n'))
    border = "+" + "-" * (width + 2) + "+"
    print(BOLD + border + RESET)
    for line in text.split('\n'):
        print(BOLD + "|" + " " + line.ljust(width) + " " + "|" + RESET)
    print(BOLD + border + RESET)

def main():
    quote = (
        "I took a speed-reading course and read War and Peace in twenty minutes.\n"
        "It involves Russia.\n"
        "\n"
        "I don't want to achieve immortality through my work;\n"
        "I want to achieve it through not dying.\n"
        "\n"
        "Life is full of misery, loneliness, and suffering - and it's all over\n"
        "much too soon.\n"
    )

    print_slowly("Fetching a Woody Allen quote...\n", 0.1)
    time.sleep(1)

    print_slowly("Here's something to ponder:\n", 0.05)
    time.sleep(1)

    draw_box(quote)

    print()
    print_slowly("Woody Allen: Master of existential neurosis and self-deprecating humor", 0.03)
    print()

if __name__ == "__main__":
    main()