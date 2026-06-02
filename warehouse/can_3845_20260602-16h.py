"""
Campbell's Soup Can #3845
Produced: 2026-06-02 16:54:44
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

# Woody Allen style philosophical quote with colorful ASCII box
quote = """I'm not afraid of death; I just don't want to be around when it happens."""

# ANSI colour codes (bright variants)
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
RESET   = "\033[0m"

# Build a simple bordered box (width = 50)
WIDTH = 50
border = "+" + "-" * WIDTH + "+"
box_lines = [border]

# Center each line of the quote inside the box
for line in quote.splitlines():
    box_lines.append("|" + line.center(WIDTH) + "|")

box_lines.append(border)

# Print each line with a cycling colour for visual fun
colours = [RED, GREEN, YELLOW, CYAN]
for idx, line in enumerate(box_lines):
    colour = colours[idx % len(colours)]
    print(colour + line + RESET)