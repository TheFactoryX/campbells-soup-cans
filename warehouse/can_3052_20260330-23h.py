"""
Campbell's Soup Can #3052
Produced: 2026-03-30 23:51:57
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# -*- coding: utf-8 -*-
# One‑liner philosophical musing in true Woody Allen neurotic flair,
# printed with a splash of ANSI color and ASCII box art.
# -----------------------┐
# |  █  █  █  █  █  █   │
# |  I'm not afraid of  │# |  death; I just don't│
# |  want to be there    │
# |  when it happens.   │
#  █  █  █  █  █  █   ┘
# -----------------------┘

# ANSI colour codes (no external packages)
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
MAGENTA= "\033[95m"
RESET  = "\033[0m"

# The quotequote = "I'm not afraid of death; I just don't want to be there when it happens."

# Build a decorative frame
border_top    = f"{RED}╔{'─'*42}{RED}╗"
border_bottom = f"{RED}╚{'─'*42}{RED}╝"
quote_line    = f"{BLUE}{quote.center(42)}{RESET}"
quote_box     = f"{YELLOW}║{RESET} {quote_line} {YELLOW}║"

# Print the coloured ASCII “speech bubble”
print("\n" + border_top)
print(quote_box)
print(border_bottom + "\n")