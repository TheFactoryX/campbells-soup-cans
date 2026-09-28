"""
Campbell's Soup Can #5037
Produced: 2026-09-28 06:55:16
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
import random

def color_text(text, color_code):
    """Return text wrapped in ANSI color code."""
    return f"\033[{color_code}m{text}\033[0m"

def main():
    # Original Woody Allen‑style quote
    quote = "I'm not afraid of the unknown; I just don't want it to show up uninvited and steal my socks."

    # Build a simple box around the quote
    inner_width = len(quote) + 2          # space on each side inside the box
    top_bottom = "+" + "-" * inner_width + "+"
    middle = f"| {quote} |"

    # A tiny doodle to give it personality
    doodle = [
        "   .-.",
        "  (   )",
        "   '-'"
    ]

    # Collect all lines to display
    lines = doodle + [""] + [top_bottom, middle, top_bottom]

    # Print each line with a slight delay and random color
    for line in lines:
        if line == "":
            print()  # blank line for spacing
            time.sleep(0.1)
            continue
        # Choose a bright color (91-97) for each line
        color = random.choice([91, 92, 93, 94, 95, 96, 97])
        sys.stdout.write(color_text(line, color) + "\n")
        sys.stdout.flush()
        time.sleep(0.2)  # pause between lines for a gentle animation effect

    # Ensure colors are reset at the end
    sys.stdout.write("\033[0m\n")

if __name__ == "__main__":
    main()