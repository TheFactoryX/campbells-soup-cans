"""
Campbell's Soup Can #4812
Produced: 2026-08-24 15:00:00
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A neurotic, colorful Woody Allen-style philosophical quote."""

# ANSI color codes for playful formatting
RESET = "\033[0m"
CYAN  = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"

# The Woody-approved philosophical gem (plain string, no ANSI codes inside)
quote = ("I'm not afraid of death. I just don't want to be there when it happens, "
         "because I'd feel terrible about missing my own eulogy "
         "and having to listen to people pretend they liked me.")

# Banner width (wide enough to hold the quote with room to breathe)
W = 200

# Compute centered padding on the plain quote length
pad = (W - 2 - len(quote)) // 2
left_pad = " " * pad
right_pad = " " * (W - 2 - len(quote) - pad)

# Helper to wrap text in color, always resetting at the end
def c(text, color_code):
    return f"{color_code}{text}{RESET}"

# Top border of the "comedy club"
print(c("┌" + "─" * (W - 2) + "┐", CYAN))
# Empty space inside the top border
print(c("│" + " " * (W - 2) + "│", CYAN))
# The quote, centered like a neurotic thought in a gilded cage
print(c("│ " + left_pad + quote + right_pad + " │", YELLOW))
# Empty space inside the bottom border
print(c("│" + " " * (W - 2) + "│", CYAN))
# Bottom border
print(c("└" + "─" * (W - 2) + "┘", CYAN))

# Woody's neurotic signature footer
print()
print(c("Neurotically yours,", MAGENTA))
print(c("   " + "_" * 40, BOLD + CYAN))
print(c("   - A Python script desperately seeking meaning", RESET))