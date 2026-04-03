"""
Campbell's Soup Can #3110
Produced: 2026-04-03 15:53:57
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

defc(t,c): return f"\033[{c}m{t}\033[0m"

border_top    = "╔═════════════════════════════════════════════════════════════════╗"
border_bottom = "╚════════════════════════════════════════════════════════════════╝"
mid_line1 = "║  \"I’m not afraid of death;\"                              ║"
mid_line2 = "║   I just don’t want to be around when it happens.\"      ║"

lines = [border_top, mid_line1, mid_line2, border_bottom]

for line in lines:
    for ch in line:
        sys.stdout.write(c(ch, 96))
        sys.stdout.flush()
        time.sleep(0.02)
    print()

print(c("\n — Woody Allen", 93))