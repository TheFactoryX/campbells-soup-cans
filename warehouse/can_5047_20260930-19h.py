"""
Campbell's Soup Can #5047
Produced: 2026-09-30 19:20:57
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

def color(text, code):
    """Wrap text with ANSI color code."""
    return f"\033[{code}m{text}\033[0m"

def slow_print(text, delay=0.03):
    """Print text character by character without adding a newline."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Clear screen and move cursor to top‑left
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Woody Allen‑style quote (original)
    quote = "I'm convinced that the meaning of life is to find a good Wi‑Fi signal before the existential dread kicks in."

    # Simple ASCII face (neurotic vibe)
    face = [
        color("   _____", 36),
        color("  | o o |", 36),
        color("  |  >  |   < Woody Allen's worried face", 36),
        color("  |  '-'  |", 36),
        color("   \\_____/", 36)
    ]

    # Box dimensions
    width = len(quote) + 4          # extra spaces inside the box
    top    = color("╔" + "═" * width + "╗", 93)
    bottom = color("╚" + "═" * width + "╝", 93)
    side   = color("║", 93)

    # Print face
    for line in face:
        print(line)
    print()  # blank line before the box

    # Print top border
    print(top)
    # Print left border, then slowly type the quote, then right border
    sys.stdout.write(side + " ")
    sys.stdout.flush()
    slow_print(quote, delay=0.04)  # typing speed
    sys.stdout.write(" " + side + "\n")
    # Print bottom border
    print(bottom)

    # Optional: a little neurotic footnote
    time.sleep(0.5)
    print(color("\nP.S. If you’re reading this, the Wi‑Fi worked… for now.", 90))

if __name__ == "__main__":
    main()