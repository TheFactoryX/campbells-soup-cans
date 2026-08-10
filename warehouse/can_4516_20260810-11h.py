"""
Campbell's Soup Can #4516
Produced: 2026-08-10 11:58:32
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI color codes
CYAN = "\x1b[1;36m"
YELLOW = "\x1b[1;33m"
MAGENTA = "\x1b[1;35m"
RESET = "\x1b[0m"
BOLD = "\x1b[1m"

def animated_print(text, delay=0.03):
    """
    Prints `text` character by character with a small delay for a typewriter effect.
    Preserves any trailing newline.
    """
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    # Add a newline only if the input didn't already end with one
    if not text.endswith("\n"):
        sys.stdout.write("\n")
        sys.stdout.flush()

# ------------------------------------------------------------
# The Woody‑Allen‑style philosophical quote (neurotic, funny,
# self‑deprecating, existential)
# ------------------------------------------------------------
quote1 = "Existential dread? That's just my anxiety level when I'm trying to"
quote2 = "decide whether to order dessert or just stare at the ceiling and"
quote3 = "wonder if anyone will remember my jokes after I'm gone."

# Visual settings
width = 78  # total width of the box (including the border characters)

# Build the decorative top and bottom lines
top_bottom = f"{MAGENTA}+{'=' * width}+{RESET}"

# Helper to format a line of the quote inside the box
def box_line(quote):
    content = f'"{quote}"'
    # Pad so the content fills the space exactly (width-4 accounts for the vertical bars and spaces)
    padded = content.ljust(width - 4)
    return f"{MAGENTA}|{RESET} {CYAN}{BOLD}{padded}{RESET} {MAGENTA}|{RESET}\n"

# A line of stars for extra visual flair
stars = f"{YELLOW}{'*' * width}{RESET}\n"

# ------------------------------------------------------------
# Print everything with an animated typewriter effect
# ------------------------------------------------------------
animated_print(stars)                 # star separator
animated_print(top_bottom)            # top of the box

# Print each line of the quote
for q in (quote1, quote2, quote3):
    animated_print(box_line(q))

animated_print(top_bottom)            # bottom of the box

# Author line (centered, with a subtle offset)
author_line = f"{YELLOW}{' ' * (width - 15)}— Woody-ish{RESET}\n"
animated_print(author_line)

# End with a playful newline
print()  # final newline for clean terminal output