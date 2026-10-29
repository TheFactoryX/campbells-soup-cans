"""
Campbell's Soup Can #5181
Produced: 2026-10-29 00:57:32
Worker: Recursive: Flint (free) (recursive/flint-v1.0:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI color codes for a fun, neurotic vibe
BOX = "\033[93m"      # yellow for the box border
TEXT = "\033[96m"      # cyan for the quote
BOLD = "\033[1m"       # bold for emphasis
RESET = "\033[0m"      # reset all styles

quote = "I'm not afraid of death. I'm afraid of the awkward silence after I die."

# Split the quote into lines that fit nicely in the box
lines = [
    "I'm not afraid of death. I'm afraid",
    "of the awkward silence after I die."
]

width = 50  # width of the box interior

# Build the box frame
border = "+" + "-" * width + "+"
side = "|" + " " * width + "|"

print("\n")
print(BOX + BOLD + "  Woody Allen's Guide to Existential Dread  " + RESET)
print()

# Print the top border
print(BOX + border + RESET)

# Print the top side
print(BOX + side + RESET)

# Print the quote lines, centered and colored
for line in lines:
    centered = line.center(width)
    print(BOX + "|" + TEXT + BOLD + centered + RESET + BOX + "|")

# Print the bottom side and bottom border
print(BOX + side + RESET)
print(BOX + border + RESET)

print()
print(BOX + "  ... and that's the truth. (Probably.)" + RESET)
print()