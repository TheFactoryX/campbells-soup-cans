"""
Campbell's Soup Can #116
Produced: 2025-11-07 12:59:16
Worker: OpenAI: gpt-oss-20b (openai/gpt-oss-20b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A playful, colored, single-file Python program that prints a Woody‑Allen‑style
philosophical quote with a typewriter effect inside a framed box.
"""

import sys
import time

# ----- ANSI colour codes -----
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"

# ----- The quote -----
quote = (
    f"{CYAN}I’m not afraid of pointlessness; I’m probably terrified of doing nothing… "
    f"so I keep asking why.{RESET}"
)

# ----- Frame dimensions -----
inner_width = len(quote) + 4  # 2 spaces padding on each side
top_border = "╔" + "═" * inner_width + "╗"
bottom_border = "╚" + "═" * inner_width + "╝"
empty_line = "║" + " " * inner_width + "║"

# ----- Print frame and typewriter effect -----
print(top_border)
print(empty_line)  # empty line above the quote

# Typewriter effect
current = ""
for ch in quote:
    current += ch
    # Overwrite the line with the current text
    sys.stdout.write("\r" + "║  " + current.ljust(len(quote)) + "  ║")
    sys.stdout.flush()
    time.sleep(0.05)  # tweak for animation speed
sys.stdout.write("\n")  # move to next line after the quote

print(empty_line)  # empty line below the quote
print(bottom_border)

# End of program
