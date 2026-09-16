"""
Campbell's Soup Can #4972
Produced: 2026-09-16 16:56:47
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def c(text, code):
    """Wrap text in ANSI color codes."""
    return f"\033[{code}m{text}\033[0m"

quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."

top_border = c("╔═══════════════════════════════════════════════════════════════════════════╗", "31")
bottom_border = c("╚═══════════════════════════════════════════════════════════════════════════╝", "31")
side_border = c("║", "33")

print(top_border)
print(side_border + " " + c(quote, "36") + " " + side_border)
print(bottom_border)