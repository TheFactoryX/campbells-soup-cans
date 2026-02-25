"""
Campbell's Soup Can #2428
Produced: 2026-02-25 15:10:21
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

# Woody Allen‑style philosophical quote
quote = "I think the universe is a giant joke—and I'm the punchline."

def color(text, color_code):
    return f"{color_code}{text}{RESET}"

def boxed_print(text, border_color=MAGENTA, fill_color=GREEN):
    lines = text.split("\n")
    width = max(len(l) for l in lines) + 4
    top    = color(f"╔{'═'*width}╗", border_color)
    bottom = color(f"╚{'═'*width}╝", border_color)
    body   = ""
    for line in lines:
        padded = f" {line.ljust(width-2)} "
        body += color(f"║{padded}║\n", fill_color)
    sys.stdout.write(f"{top}\n{body}{bottom}\n")

boxed_print(quote)