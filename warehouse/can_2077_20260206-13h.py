"""
Campbell's Soup Can #2077
Produced: 2026-02-06 13:34:43
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

# A Woody Allen‑style philosophical nugget wrapped in a colorful ANSI box.
# Run this file directly – it needs no external libraries.

# ----------------------------------------------------------------------
# The quote (in true neurotic, existential, self‑deprecating Allen fashion)
# ----------------------------------------------------------------------
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# ----------------------------------------------------------------------
# ANSI colour codes (bright variants for a playful look)
# ----------------------------------------------------------------------
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

# ----------------------------------------------------------------------
# Build a small, bright ASCII‑art box around the quote
# ----------------------------------------------------------------------
top    = f"{CYAN}╔{'═'*38}╗{RESET}"
middle = f"{CYAN}║ {YELLOW}{quote}{RESET} {CYAN}║{RESET}"
bottom = f"{CYAN}╚{'═'*38}╝{RESET}"

# ----------------------------------------------------------------------
# Print the coloured box – only one philosophical quote appears here
# ----------------------------------------------------------------------
print(top)
print(middle)
print(bottom)