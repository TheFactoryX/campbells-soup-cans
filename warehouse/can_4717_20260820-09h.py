"""
Campbell's Soup Can #4717
Produced: 2026-08-20 09:50:00
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

# ANSI color codes
RESET   = "\033[0m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
GREEN   = "\033[92m"

def type_print(text, delay=0.05, color=RESET):
    """Print text character‑by‑character with a typewriter effect."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

def draw_box(width, height, border_color=CYAN, fill_color=YELLOW):
    """Draw a simple ASCII box with optional inner fill (empty)."""
    # Top border
    type_print("┌" + "─" * (width - 2) + "┘", color=border_color)
    # Empty inner lines
    for _ in range(height - 2):
        type_print("│" + " " * (width - 2) + "│", color=fill_color)
    # Bottom border
    type_print("└" + "─" * (width - 2) + "┘", color=border_color)

def main():
    quote = (
        "I pondered the meaning of life, then realized I left the oven on."
    )
    # Box dimensions: quote length + padding
    padding = 4
    box_width = len(quote) + padding
    box_height = 3  # top, quote line, bottom

    # Animate the box drawing
    draw_box(box_width, box_height, border_color=CYAN, fill_color=YELLOW)

    # Position cursor to print the quote inside the box (line 2, column 2)
    # Move up one line and right padding spaces
    sys.stdout.write(f"\033[{box_height - 1}A\033[{padding}C")
    sys.stdout.flush()
    type_print(quote, delay=0.07, color=MAGENTA)

    # Reset cursor position after quote (optional)
    sys.stdout.write(f"\033[{box_height - 1}B\033[{padding}D")
    sys.stdout.flush()

if __name__ == "__main__":
    main()