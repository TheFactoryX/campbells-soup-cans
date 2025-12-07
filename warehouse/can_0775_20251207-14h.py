"""
Campbell's Soup Can #775
Produced: 2025-12-07 14:31:40
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A fun, colorful Woody‑Allen‑style philosophical quote.
"""

import sys
import time

# ---------- Settings ----------
QUOTE = "I keep thinking the universe is a joke, but it gets a bit more absurd when I realize I am the punchline."
BOX_WIDTH = 120            # Width of the decorative box (must be > len(QUOTE)+2)
TYPE_DELAY = 0.035         # Delay between each character when typing

# ANSI color codes
COLORS = [41, 42, 43, 44, 45, 46, 47]  # Background colors: RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

# ---------- Utility functions ----------
def typewriter(text, delay=TYPE_DELAY):
    """Prints text one character at a time with cycling colors."""
    color_index = 0
    for ch in text:
        # Cycle background colors
        color_code = COLORS[color_index % len(COLORS)]
        sys.stdout.write(f"\033[{color_code}m{ch}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
        color_index += 1
    sys.stdout.write("\n")

def draw_box(content):
    """Draws a colored box around the given content string."""
    # Ensure the content fits inside the box
    if len(content) + 4 > BOX_WIDTH:
        raise ValueError("QUOTE too long for the box width.")
    # Top border
    top = f"\033[1;36m┌{'─' * (BOX_WIDTH-2)}┐\033[0m"
    # Bottom border
    bottom = f"\033[1;36m└{'─' * (BOX_WIDTH-2)}┘\033[0m"
    # Padding
    padding_space = ' ' * ((BOX_WIDTH - len(content) - 4) // 2)
    padded_content = f"│  {padding_space}{content}{padding_space}  │"
    # Print box
    print(top)
    print(padded_content)
    print(bottom)

def print_header():
    """Prints a colorful ASCII art header."""
    art = r"""
          \   /\
           )   \
          (      )
           \    /
            \__/   *  *  *  *
           /  \   *  *  *  *
          /    \
    """
    # Color the art teal
    colored_art = "\033[32m" + art + "\033[0m"
    print(colored_art)

# ---------- Main ----------
def main():
    print_header()
    time.sleep(0.6)          # Pause before typing
    draw_box(" ")
    typewriter(QUOTE)
    draw_box(" ")
    print("\033[1;33m[End of the cosmic sitcom.]\033[0m")

if __name__ == "__main__":
    main()