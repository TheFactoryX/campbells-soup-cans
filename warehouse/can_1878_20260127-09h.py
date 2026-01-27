"""
Campbell's Soup Can #1878
Produced: 2026-01-27 09:48:15
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# terminals don't all support blinking (like Windows CMD), but it works in most modern Linux/macOS terminals
def blink(quote, color='\033[1;33m', delay=0.2, loops=3):
    for _ in range(loops):
        for col in [color, '\033[1;31m', '\033[1;32m']:
            sys.stdout.write(f"\r  \033[?5l {col}quote\033[0m  ")
            sys.stdout.flush()
            time.sleep(delay)

# Main content
print("\033[1;35m+------------------------------------------+")
print("\033[1;33m| \033[1;37mWoody Allen's Existential Update \033[1;32m|\033[0m")
print("\033[1;35m+------------------------------------------+\033[0m\n")

quote = "\033[1;34m« I'm not afraid of death; I'm just terrified of the \033[1;35mquestion mark\033[0m\n  that follows me home, asking questions I can't answer over a glass of wine and \033[1;36m5000 unread emails.\033[0m »"

# Typewriter effect for dramatic reveal
for word in quote.split():
    print(word, flush=True, end=' ')
    time.sleep(0.05)

# Blink "EXISTENTIAL" in the quote for added Allen-ness
blink("EXISTENTIAL", color='\033[1;31m')

# Final punchline
print("\n\033[1;37m\nP.S. This quote is 100% free of intellectual property because I paid my tax dollars in existential dread.\033[0m")