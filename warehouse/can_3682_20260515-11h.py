"""
Campbell's Soup Can #3682
Produced: 2026-05-15 11:29:27
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3RED    = "\033[31m"
YELLOW = "\033[33m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"
RESET  = "\033[0m"

quote = "I'm not afraid of death; I just keep checking my watch to see if it's time for my final curtain call."

width = 60
top    = RED + "╔" + "═"*width + "╗" + RESET
middle = CYAN + "║" + " "*width + "║" + RESET
quote_line = f"{MAGENTA}║  {quote}{RESET}  ║"
bottom = RED + "╚" + "═"*width + "╝" + RESETprint(top)
print(middle)
print(quote_line)
print(middle)
print(bottom)