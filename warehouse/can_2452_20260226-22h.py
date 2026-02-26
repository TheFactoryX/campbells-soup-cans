"""
Campbell's Soup Can #2452
Produced: 2026-02-26 22:53:25
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote(quote, author="Woody Allen", delay=0.03):
    # ANSI color codes
    colors = [
        "\033[31m",  # Red
        "\033[33m",  # Yellow
        "\033[32m",  # Green
        "\033[36m",  # Cyan
        "\033[35m",  # Magenta
        "\033[34m",  # Blue
    ]
    reset = "\033[0m"

    # Create a box around the quote
    max_len = max(len(quote), len(author)) + 6
    top_bottom = "─" * max_len
    print(f"\n┌{top_bottom}┐")
    print(f"│{quote.center(max_len)}│")
    print(f"└{top_bottom}┘")

    # Animate the author name with colors
    for char in author:
        color = colors[len(author) % len(colors)]
        sys.stdout.write(f"{color}{char}{reset}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Woody Allen style quote
quote = (
    "I don't want to achieve immortality through my work; "
    "I want to achieve it through not dying."
)

print_quote(quote)