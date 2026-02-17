"""
Campbell's Soup Can #2277
Produced: 2026-02-17 11:07:06
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen‑style philosophical quote, printed in a colorful ASCII box

cyan   = "\033[96m"      # cyan for the border
magenta= "\033[95m"      # magenta for the text
reset  = "\033[0m"       # reset ANSI colors

# The quote (split on newline for easy padding)
quote = (
    "I’m not afraid of death; I just don’t want to be there when it happens…\n"
    "because the balcony is always full of strangers."
)

# Build the framed box
top    = f"{cyan}+" + "-" * 62 + f"+{reset}"
middle = f"{magenta}|{' '*62}|{reset}"
line1  = f"{magenta}|  I’m not afraid of death; I just don’t   |{reset}"
line2  = f"{magenta}|  want to be there when it happens…      |{reset}"
line3  = f"{magenta}|  because the balcony is always full of   |{reset}"
line4  = f"{magenta}|  strangers.                              |{reset}"
line5  = f"{magenta}|                                          |{reset}"
bottom = f"{cyan}+" + "-" * 62 + f"+{reset}"

# Print the box line by line
print(top)
print(middle)
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(bottom)