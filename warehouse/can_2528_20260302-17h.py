"""
Campbell's Soup Can #2528
Produced: 2026-03-02 17:59:21
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# --- ANSI color helpers ---
RESET = '\033[0m'
CYAN  = '\033[36m'
MAGENTA = '\033[35m'
YELLOW = '\033[33m'
BRIGHT = '\033[1m'

def color(text, code): return f'{code}{text}{RESET}'

# --- The quote & styling ---
quote = "I’m not afraid of death; I just don’t want to be there when it happens."
WIDTH = 60
BORDER = '+' + '-' * (WIDTH - 2) + '+'

def center(s, width):
    pad = width - len(s)
    left, right = pad // 2, pad - pad // 2
    return ' ' * left + s + ' ' * right

top    = color(BORDER, CYAN)
mid    = '|' + ' ' * (WIDTH - 2) + '|'
quote_ln = color(color(center(quote, WIDTH - 2), MAGENTA), BRIGHT)
bottom = color(BORDER, CYAN)

# Simple “fade‑in” effect for visual fun
for line in [top, mid, quote_ln, mid, bottom]:
    print(line)
    sys.stdout.flush()
    time.sleep(0.12)

# Add a tiny sparkle of yellow stars around the box for extra flair
stars = color('*'*5, YELLOW)
print('\n' + stars + ' ' * ((WIDTH - len(stars)) // 2) + stars)