"""
Campbell's Soup Can #1595
Produced: 2026-01-14 05:49:29
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time
COLS = ['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m','\033[0m']
quote = "I’m not afraid of death; I just don’t want to be there when it happens, because then I’d miss the punchline."
def typewriterRainbow(s):
    for i,ch in enumerate(s):
        sys.stdout.write(COLS[i%len(COLS)] + ch)
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write('\033[0m\n')
print('*' * 55)
typewriterRainbow(quote)
print('*' * 55)