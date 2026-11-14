"""
Campbell's Soup Can #5241
Produced: 2026-11-14 11:28:42
Worker: LiquidAI: LFM3-1.7B (free) (liquid/lfm-3-1.7b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Woody Allen-style philosophical quote.
Prints a single, witty, neurotic, existential line inside a colorful ASCII box.
"""

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Size of the box
BOX_WIDTH = 60

# One funny quote in Woody Allen's voice
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

# Build the decorative borders
top_border = f"{MAGENTA}╔{'═' * (BOX_WIDTH - 2)}╗{RESET}"
mid_border = f"{CYAN}║{'─' * (BOX_WIDTH - 2)}║{RESET}"
bottom_border = f"{RED}╚{'═' * (BOX_WIDTH - 2)}╝{RESET}"

# Output
print(top_border)
print(mid_border)
print(f"  {YELLOW}{QUOTE.strip()}{RESET}")
print(bottom_border)