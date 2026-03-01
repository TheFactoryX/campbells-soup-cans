"""
Campbell's Soup Can #2506
Produced: 2026-03-01 15:37:46
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
Woody Allen-style quote printer with colorful typewriter effect and a bordered box.
No external dependencies; uses ANSI escape codes for visuals.
"""

import sys
import time
import shutil

# ANSI escape sequences
CLEAR_SCREEN = "\033[2J"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
RESET = "\033[0m"

# Colors for the box and header
BOX_COLOR = "\033[36m"      # cyan
HEADER_COLOR = "\033[2;33m" # dim yellow

# Rainbow colors for the typing effect
RAINBOW = [
    "\033[31m", "\033[32m", "\033[33m", "\033[34m",
    "\033[35m", "\033[36m", "\033[37m",
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m", "\033[96m",
]

# The Woody‑Allen‑esque philosophical quote
QUOTE = "If eternity exists, I hope it has a good cancellation policy."


def move_cursor(row: int, col: int) -> None:
    """Move the terminal cursor to the given (1‑based) row and column."""
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()


def hide_cursor() -> None:
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()


def show_cursor() -> None:
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.flush()


def main() -> None:
    try:
        hide_cursor()

        # Get terminal dimensions, fall back to 80x24 if unavailable
        try:
            term_width, term_height = shutil.get_terminal_size()
        except:
            term_width, term_height = 80, 24

        # Clear screen and home cursor
        sys.stdout.write(CLEAR_SCREEN)
        sys.stdout.flush()

        # --- Box geometry -------------------------------------------------
        padding = 2
        interior_width = len(QUOTE) + 2 * padding
        box_width = interior_width + 2          # +2 for the borders
        box_height = 3                          # top, middle, bottom

        # Center the box vertically / horizontally
        start_row = max(1, (term_height - box_height) // 2)
        start_col = max(1, (term_width - box_width) // 2)

        # Place header two lines above the box (if possible)
        header = "Woody Allen once mused:"
        header_row = max(1, start_row - 2)
        header_col = max(1, (term_width - len(header)) // 2)

        # --- Draw header --------------------------------------------------
        move_cursor(header_row, header_col)
        sys.stdout.write(HEADER_COLOR + header + RESET)
        sys.stdout.flush()

        # --- Draw the box -------------------------------------------------
        # Top border
        move_cursor(start_row, start_col)
        sys.stdout.write(BOX_COLOR + "┌" + "─" * interior_width + "┐" + RESET)

        # Middle line (filled with spaces – will be overwritten by the quote)
        move_cursor(start_row + 1, start_col)
        sys.stdout.write(BOX_COLOR + "│" + RESET + " " * interior_width + BOX_COLOR + "│" + RESET)

        # Bottom border
        move_cursor(start_row + 2, start_col)
        sys.stdout.write(BOX_COLOR + "└" + "─" * interior_width + "┘" + RESET)
        sys.stdout.flush()

        # --- Prepare for typing the quote ---------------------------------
        quote_row = start_row + 1
        quote_col = start_col + 1 + padding   # after left border and left padding
        move_cursor(quote_row, quote_col)
        sys.stdout.flush()

        base_delay = 0.03  # seconds per character

        # Typewriter effect with rainbow colors
        for i, ch in enumerate(QUOTE):
            color = RAINBOW[i % len(RAINBOW)]
            sys.stdout.write(color + ch)
            sys.stdout.flush()
            time.sleep(base_delay)

            # Extra dramatic pauses at punctuation
            if ch in ",;:":
                time.sleep(base_delay * 2)
            elif ch in ".!?":
                time.sleep(base_delay * 4)

        # Reset color after the quote
        sys.stdout.write(RESET)
        sys.stdout.flush()

        # --- Move cursor to a safe place and show it ----------------------
        move_cursor(start_row + box_height + 2, 1)
        show_cursor()
        input("Press Enter to exit...")

    finally:
        # Ensure the cursor is visible even if something goes wrong
        show_cursor()


if __name__ == "__main__":
    main()