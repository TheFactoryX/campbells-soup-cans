"""
Campbell's Soup Can #2615
Produced: 2026-03-07 06:58:53
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen style philosophical quote with colorful ASCII art

quote = "I'm not scared of death; I just don't want to be there when it happens."
reset  = "\033[0m"
magenta = "\033[35m"
yellow  = "\033[93m"

border_top    = f"{magenta}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{reset}"
border_mid    = f"{magenta}┃                                        ┃{reset}"
border_bottom = f"{magenta}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{reset}"
quote_line    = f"{yellow}┃ {quote}                     ┃{reset}"
attribution   = f"{magenta}┃ — Woody Allen (in his mind)           ┃{reset}"

print(border_top)
print(border_mid)
print(quote_line)
print(border_mid)
print(attribution)
print(border_bottom)