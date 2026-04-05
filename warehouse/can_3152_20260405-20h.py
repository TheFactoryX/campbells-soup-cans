"""
Campbell's Soup Can #3152
Produced: 2026-04-05 20:49:59
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

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
RESET = "\033[0m"
BOLD = "\033[1m"

def typewriter(text, delay=0.03):
    """Print text character by character with a slight delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after finished

def colorful_box(lines, width=None):
    """Print a box around given lines with random colors."""
    if width is None:
        width = max(len(line) for line in lines) + 4  # padding
    top = f"{random.choice(COLORS)}╔{'═' * (width - 2)}╗{RESET}"
    bottom = f"{random.choice(COLORS)}╚{'═' * (width - 2)}╝{RESET}"
    print(top)
    for line in lines:
        padded = line.ljust(width - 4)
        color = random.choice(COLORS)
        print(f"{color}║  {padded}  ║{RESET}")
    print(bottom)

def main():
    quote = (
        "I'm not afraid of death; I just don't want to be the punchline "
        "of the universe's cruel joke."
    )
    # Prepare lines for the box
    quoted = f'"{quote}"'
    # Optional Woody Allen‑style flourish
    footer = "- Woody Allen (probably)"
    box_lines = [quoted, footer]
    # Print with a little typewriter effect inside the box
    # We'll print the box statically, then animate the quote inside.
    colorful_box(["", ""], width=len(quoted) + 6)  # dummy to get width
    # Recalculate width properly
    width = len(quoted) + 6
    # Redraw box with proper width
    colorful_box(["", ""], width=width)  # clear previous dummy
    # Actually draw the box with content
    print()
    colorful_box([quoted, footer], width=width)
    # Typewriter effect for the quote only (inside the box)
    # We'll re‑print the quote line with typewriter inside the same box space.
    # Simpler: just typewriter the quote before boxing.
    print()  # space
    typewriter(quoted, delay=0.05)
    time.sleep(0.2)
    typewriter(footer, delay=0.05)

if __name__ == "__main__":
    main()