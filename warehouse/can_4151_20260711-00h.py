"""
Campbell's Soup Can #4151
Produced: 2026-07-11 00:12:53
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful, color‑fancy print of a Woody‑Allen–style philosophical quip,
with a small typing animation and a decorated border.
"""

import sys
import time

# ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

# The quote itself (Woody Allen‑ish, neurotic, self‑deprecating)
QUOTE = ("I think the cosmos is testing me: "
         "first, by making me fall into existential dread, "
         "then by giving me a sarcastic shrug to answer with.")

# Styling for the border and text
BORDER_CHAR = "─"
TOP_LEFT = "┌"
TOP_RIGHT = "┐"
 ய் = "⎵"  # blank space, just for visual padding
BOTTOM_LEFT = "└"
BOTTOM_RIGHT = "┘"

# Compose the text block
lines = QUOTE.splitlines()
max_len = max(len(line) for line in lines)
pad = 2  # spaces on each side inside the box

# Build the full block with a top and bottom border
border_line = CYAN + TOP_LEFT + BORDER_CHAR * (max_len + pad * 2) + TOP_RIGHT + RESET
bottom_line = CYAN + BOTTOM_LEFT + BORDER_CHAR * (max_len + pad * 2) + BOTTOM_RIGHT + RESET

# Prepare the lines with padding
padded_lines = [CYAN + "│" + RESET + " " * pad + BOLD + line.ljust(max_len) + RESET + " " * pad + CYAN + "│" + RESET
                for line in lines]

# Print the box with typing animation
def type_print(text, delay=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

# Clear screen (optional)
print("\033[H\033[J", end="")

# Print top border
type_print(border_line + "\n")

# Print content lines
for pline in padded_lines:
    type_print(pline + "\n")

# Print bottom border
type_print(bottom_line + "\n")

# Small pause before exit
time.sleep(2)