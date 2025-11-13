"""
Campbell's Soup Can #252
Produced: 2025-11-13 15:33:21
Worker: OpenAI: GPT-5 Nano (openai/gpt-5-nano)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

def main():
    quote = "Life is a cosmic joke, and I'm the straight man who forgot the setup, the punchline, and why we're laughing in the first place."
    # Wrap the quote to fit nicely in a box
    wrap_width = 60
    lines = textwrap.wrap(quote, width=wrap_width)
    w = max((len(line) for line in lines), default=0)

    # ASCII box border with colors (ANSI)
    COLOR = "\033[96m"  # bright cyan
    RESET = "\033[0m"

    top = "┌" + "─" * (w + 2) + "┐"
    bottom = "└" + "─" * (w + 2) + "┘"

    # Print top border
    print(COLOR + top + RESET)

    # Typewriter-style printing for each content line
    delay = 0.035  # seconds per character
    for line in lines:
        # Start the line with left border
        sys.stdout.write(COLOR + "│ " + RESET)
        sys.stdout.flush()
        # Print content characters with a bit of animation
        for ch in line.ljust(w):
            sys.stdout.write(COLOR + ch + RESET)
            sys.stdout.flush()
            time.sleep(delay)
        # Pad remaining spaces if line shorter than width
        remaining = w - len(line)
        for _ in range(remaining):
            sys.stdout.write(COLOR + " " + RESET)
            sys.stdout.flush()
            time.sleep(delay / 2)
        # End the line with right border
        sys.stdout.write(COLOR + " │" + RESET + "\n")
        sys.stdout.flush()

    # Print bottom border
    print(COLOR + bottom + RESET)

if __name__ == "__main__":
    main()