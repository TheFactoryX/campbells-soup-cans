"""
Campbell's Soup Can #2746
Produced: 2026-03-13 18:14:13
Worker: DeepSeek: DeepSeek V3.2 Speciale (deepseek/deepseek-v3.2-speciale)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen style philosophical quote printer.
Displays a quote with a typewriter effect inside a colored box.
"""

import sys
import time

# ---------- ANSI escape codes ----------
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BRIGHT_RED = "\033[31;1m"
BRIGHT_YELLOW = "\033[33;1m"
BRIGHT_CYAN = "\033[36;1m"

# Border color
BORDER_COLOR = BRIGHT_YELLOW

# ---------- Helper functions ----------
def clear_screen():
    """Clear terminal and move cursor to home position."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def slow_write(text, delay=0.04, color=None):
    """
    Print text character by character with a delay.
    If a color is given, set it before writing and do NOT reset afterwards.
    """
    if color:
        sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    # Do not reset here; caller manages color changes.

# ---------- Quote definition ----------
# Each line is a list of (text, color_code) segments.
line1 = [
    ("I've been searching for the meaning of life,", CYAN),
]

line2 = [
    ("but so far all I've found are ", CYAN),
    ("takeout menus", YELLOW),
    (" and ", CYAN),
    ("existential dread", BRIGHT_RED),
    (".", CYAN),
]

lines = [line1, line2]

# Compute visible lengths (ignore color codes).
line_lengths = [sum(len(text) for text, _ in line) for line in lines]
max_len = max(line_lengths)  # width of the box interior (without margins)

# ---------- Main ----------
def main():
    try:
        hide_cursor()
        clear_screen()

        # Draw top border
        top_border = BORDER_COLOR + "┌" + "─" * (max_len + 2) + "┐" + RESET
        sys.stdout.write(top_border + "\n")
        sys.stdout.flush()

        # Print each line with typewriter effect inside the box
        for i, line_segments in enumerate(lines):
            # Left border + left margin space
            sys.stdout.write(BORDER_COLOR + "│" + RESET + " ")
            sys.stdout.flush()

            # Write each colored segment slowly
            for text, color in line_segments:
                slow_write(text, delay=0.04, color=color)

            # Fill remaining space and add right border
            filler_len = max_len - line_lengths[i]   # spaces to align
            sys.stdout.write(RESET)                     # reset text color
            sys.stdout.write(" " * (filler_len + 1))    # filler + right margin space
            sys.stdout.write(BORDER_COLOR + "│" + RESET + "\n")
            sys.stdout.flush()

        # Draw bottom border
        bottom_border = BORDER_COLOR + "└" + "─" * (max_len + 2) + "┘" + RESET
        sys.stdout.write(bottom_border + "\n")
        sys.stdout.flush()

        # Signature
        signature = "– Woody Allen (probably)"
        sys.stdout.write("\n")
        slow_write(signature, delay=0.04, color=DIM)
        sys.stdout.write("\n")

    except KeyboardInterrupt:
        # If user interrupts, we still want to show the cursor
        pass
    finally:
        show_cursor()

if __name__ == "__main__":
    main()