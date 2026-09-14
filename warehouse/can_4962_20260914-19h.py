"""
Campbell's Soup Can #4962
Produced: 2026-09-14 19:22:22
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Colors
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# Define the width of the ASCII box
width = 100

# Build the box borders
border_top    = f"{CYAN}{BOLD}╔{'─'*width}{RESET}"
border_bottom = f"{CYAN}{BOLD}╚{'─'*width}{RESET}"
border_middle = f"{CYAN}║{' '*width}{RESET}"

# The Woody Allen‑style philosophical quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens – commitment overload."
quote_len = len(quote)

# Calculate the padding needed to fill the line to the proper width
padding = " " * (width - quote_len - 1)  # spaces after the quote before the closing box

# Assemble the line that contains the quote
quote_line = f"{CYAN}║ {quote}{padding}{RESET}║"

# Print everything
print(border_top)
print(quote_line)
print(border_bottom)