"""
Campbell's Soup Can #3025
Produced: 2026-03-29 09:53:45
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken, missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

defc(t, col):
    colors = {
        'reset': '\033[0m',
        'yellow': '\033[33m',
        'cyan': '\033[36m'
    }
    return colors.get(col, '') + t + colors['reset']

quote = ("I used to think the universe had a plan for me. "
         "Turns out it’s just a cosmic stand‑up comic who keeps forgetting the punchline.")

box = [
    "   ┌─────────────────────────────────────┐",
    "   │                                 │",
    f"   │{c(quote, 'yellow')}               │",
    "   │                                 │",
    "   └─────────────────────────────────────┘"
]

def animate(s, d=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(d)
    sys.stdout.write('\n')
    sys.stdout.flush()

for line in box:
    animate(line, 0.015)