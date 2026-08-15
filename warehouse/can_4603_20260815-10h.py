"""
Campbell's Soup Can #4603
Produced: 2026-08-15 10:39:15
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time

# Woody Allen‑style philosophical quote
quote = ("I'm not afraid of death; I just don't want to be there when it happens.")

# ANSI color codes (bright variants for better visibility)
C_RESET = "\033[0m"
C_CYAN  = "\033[96m"
C_YELLOW= "\033[93m"
C_MAG   = "\033[95m"

def color(text, code):
    """Wrap text in the given ANSI color code."""
    return f"{code}{text}{C_RESET}"

def print_fancy_box():
    width = 84                     # total line width (including borders)
    top    = color("╔" + "═" * (width-2) + "╗", C_CYAN)
    middle = color("║" + " " * (width-2) + "║", C_CYAN)
    # Pad the quote so the box stays exactly `width` characters wide
    pad    = " " * (width - 4 - len(quote))
    quote_line = color(f"║ {quote}{pad} ║", C_YELLOW)
    bottom = color("╚" + "═" * (width-2) + "╝", C_CYAN)

    # Print with a tiny pause to give a “type‑writer” feel
    lines = [top, middle, quote_line, middle, bottom]
    for line in lines:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.05)

if __name__ == "__main__":
    print_fancy_box()