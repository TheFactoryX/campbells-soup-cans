"""
Campbell's Soup Can #3289
Produced: 2026-04-14 21:07:41
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, colorful, animated Woody‑Allen‑style quote printer.
Run it directly: python3 this_file.py
"""

import sys
import time
import shutil

# ANSI colour codes
RESET = "\033[0m"
FG_CYAN = "\033[96m"
FG_YELLOW = "\033[93m"
FG_MAGENTA = "\033[95m"
FG_GREEN = "\033[92m"
BG_BLACK = "\033[40m"

# The quote – neurotic, funny, existential
QUOTE = (
    "I think the only thing I'm really good at is "
    "overthinking the fact that I'm overthinking."
)

# Fancy box drawing characters
TL, TR, BL, BR, H, V = "╔", "╗", "╚", "╝", "═", "║"

def get_terminal_width():
    """Return the width of the terminal (fallback to 80)."""
    try:
        columns = shutil.get_terminal_size().columns
    except Exception:
        columns = 80
    return columns

def wrap_text(text, width):
    """Wrap text to the given width without breaking words."""
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 > width:
            lines.append(current.rstrip())
            current = ""
        current += w + " "
    if current:
        lines.append(current.rstrip())
    return lines

def typewriter_print(line, colour=FG_CYAN, delay=0.03):
    """Print a line with a typewriter effect."""
    for ch in line:
        sys.stdout.write(colour + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    term_width = get_terminal_width()
    box_width = min(70, term_width - 4)          # leave some margin
    inner_width = box_width - 2                  # border takes 2 chars

    # Prepare wrapped quote lines
    wrapped = wrap_text(QUOTE, inner_width - 2)  # -2 for a little padding

    # Print top border
    sys.stdout.write(FG_MAGENTA + TL + H * box_width + TR + RESET + "\n")

    # Empty line above text
    sys.stdout.write(FG_MAGENTA + V + " " * box_width + V + RESET + "\n")

    # Print each line of the quote centred
    for line in wrapped:
        padded = line.center(inner_width)
        sys.stdout.write(FG_MAGENTA + V + " " + FG_GREEN)
        typewriter_print(padded, colour=FG_GREEN, delay=0.02)
        sys.stdout.write(FG_MAGENTA + " " + V + RESET + "\n")

    # Empty line below text
    sys.stdout.write(FG_MAGENTA + V + " " * box_width + V + RESET + "\n")
    # Print bottom border
    sys.stdout.write(FG_MAGENTA + BL + H * box_width + BR + RESET + "\n")

    # A little pause before exiting
    time.sleep(0.5)

if __name__ == "__main__":
    main()