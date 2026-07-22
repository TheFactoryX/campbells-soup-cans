"""
Campbell's Soup Can #4287
Produced: 2026-07-22 06:42:01
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# -*- coding: utf-8 -*-
# A Woody Allen style philosophical quote with visual flair

# Define the quote
quote = "I'm not anxious about dying, I'm just anxious about not dying."

# ANSI escape codes for colors
BLUE = '\033[34m'
YELLOW = '\033[33m'
RESET = '\033[0m'

# Calculate the width of the box (quote length + 2 for quotes)
box_width = len(quote) + 2

# Create the box borders
top_border = f"{BLUE}+{('-' * box_width)}+ {RESET}"
middle_line = f'{YELLOW}| "{quote}" |{RESET}'
bottom_border = f"{BLUE}+{('-' * box_width)}+ {RESET}"

# Print the box with the quote
print(top_border)
print(middle_line)
print(bottom_border)