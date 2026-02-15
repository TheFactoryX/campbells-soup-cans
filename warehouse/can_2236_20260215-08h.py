"""
Campbell's Soup Can #2236
Produced: 2026-02-15 08:50:29
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
quote = "I'm not scared of death—I just don't want to be there when it happens."
width = len(quote) + 4

C_BLUE = "\033[94m"
C_WHITE = "\033[97m"
C_RESET = "\033[0m"

top    = C_BLUE + "╔" + "═" * width + "╗" + C_RESET
bottom = C_BLUE + "╚" + "═" * width + "╝" + C_RESET
middle = C_BLUE + "║ " + C_WHITE + quote + " " + C_BLUE + "║" + C_RESET

print(top)
print(middle)
print(bottom)