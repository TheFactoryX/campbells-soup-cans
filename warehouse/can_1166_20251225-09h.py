"""
Campbell's Soup Can #1166
Produced: 2025-12-25 09:36:10
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (nvidia/nemotron-3-nano-30b-a3b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, os, sys

QUOTE = "I’m not afraid of death; I just don’t want to be there when it happens."

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def col(txt, code): return f"\033[{code}m{txt}\033[0m"

border_top    = col("╔══════════════════════════════╗", "93")
quote_line1   = col("║   " + QUOTE.split(';')[0].strip() + "   ║", "94")
quote_line2   = col("║   " + QUOTE.split(';')[1].strip() + "   ║", "92")
border_bottom = col("╚══════════════════════════════╝", "95")

for _ in range(6):
    clear()
    print(border_top)
    print(quote_line1)
    print(quote_line2)
    print(border_bottom)
    time.sleep(0.8)
    clear()