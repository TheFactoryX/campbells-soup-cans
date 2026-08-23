"""
Campbell's Soup Can #4778
Produced: 2026-08-23 01:59:39
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time

# ---------- ANSI color helpers ----------
COL = {
    'reset': '\033[0m',
    'red'  : '\033[31m',
    'green': '\033[32m',
    'yellow':'\033[33m',
    'blue' : '\033[34m',
    'magenta':'\033[35m',
    'cyan' : '\033[36m',
    'white':'\033[37m'
}
def color(text, name):
    return f"{COL.get(name, '')}{text}{COL['reset']}"

# ---------- Simple typewriter ----------
def typewriter(s, delay=0.04):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

# ---------- The quote ----------
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Build a colored box around it
top    = "╔" + "═"* (len(quote) + 4) + "╗"
middle = "║ " + " " + quote + " " + " ║"
bottom = "╚" + "═"* (len(quote) + 4) + "╝"

# ---------- Visual presentation ----------
typewriter(color("   ╔═════════════════════════════════════╗", 'magenta'));   time.sleep(0.1)
typewriter(color(top, 'magenta'));                                   time.sleep(0.1)
typewriter(color(middle, 'yellow'));                                 time.sleep(0.05)
typewriter(color(bottom, 'magenta'));                                time.sleep(0.1)
typewriter("");                                                          # blank line

typewriter(color("   A classic Woody Allen thought for the day…", 'cyan')); time.sleep(0.3)
typewriter(color('“' + quote + '”', 'green'));                           time.sleep(0.2)
typewriter(color("- neurotic, existential, ever‑present.", 'blue'));    time.sleep(0.2)
typewriter("")  # final blank line

# Optional extra flourish
typewriter(color(r"""
   ╭────╮
   │🧠│   <-- Your brain after philosophy
   ╰────╯
""", 'white'))  # no delay needed for the static art