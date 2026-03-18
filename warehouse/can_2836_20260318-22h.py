"""
Campbell's Soup Can #2836
Produced: 2026-03-18 22:51:33
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# Woody Allen style quote (neurotic, existential, funny)
QUOTE = (
    "I'm not afraid of dying; I just don't want to be there when it happens "
    "and I wish the afterlife came with a better return policy."
)

def color(text, code):
    """Wrap text in ANSI color code."""
    return f"\033[{code}m{text}\033[0m"

def print_boxed(text, width=None, padding=2):
    """Print text inside a colored ASCII box."""
    lines = text.split("\n")
    if width is None:
        width = max(len(line) for line in lines) + 2 * padding
    top_bottom = "+" + "-" * (width - 2) + "+"
    side = "|"
    print(color(top_bottom, "96"))  # cyan border
    for line in lines:
        padded = line.center(width - 2 * padding)
        print(f"{color(side, '96')} {padded} {color(side, '96')}")
    print(color(top_bottom, "96"))

def typewriter_effect(s, delay=0.03):
    """Print string character by character with a slight pause."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline at the end

def main():
    # Simple "loading" animation
    sys.stdout.write("Reflecting on the void")
    for _ in range(3):
        time.sleep(0.4)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n")

    # Print the quote with a typewriter effect inside a box
    typewriter_effect(QUOTE, delay=0.04)

if __name__ == "__main__":
    main()