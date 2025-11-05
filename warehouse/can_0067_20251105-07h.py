"""
Campbell's Soup Can #67
Produced: 2025-11-05 07:30:41
Worker: Microsoft: MAI DS R1 (free) (microsoft/mai-ds-r1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

ANSI_COLORS = ['\033[95m', '\033[96m', '\033[93m', '\033[92m', '\033[94m']
RESET = '\033[0m'
W = '\033[1m'  # White bold text

quote = [
    "  Life is like a poorly written sitcom - the laugh track",
    "  is suspiciously absent, the plot makes no sense, and", 
    "  I'm just here waiting for the cancellation notice."
]
author = "- Neurotic Screenwriter's Existential Crisis"

max_len = max(len(line) for line in [s.strip() for s in quote])
padding = 8
art = r'''
    ╔═════════════════════╗
    ║       .- - .        ║
    ║     :       :       ║
    ║   ==           ==   ║
    ║      : .-. :        ║
    ║       (   )         ║
    ║        :-:          ║
    ╚═════════════════════╝'''
art_lines = art.split('\n')[1:]

def glow_print(text, color, delay=0.03, width=50):
    spaces = ' ' * ((width - len(text)) // 2)
    for c in spaces + text:
        sys.stdout.write(f"{color}{c}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Animated ASCII art
for i, line in enumerate(art_lines):
    sys.stdout.write(ANSI_COLORS[i%3] + line + RESET + '\n')
    time.sleep(0.1)

# Typewriter effect with scrolling box
box_top = f"╔{'═'*(max_len+padding)}╗"
box_bottom = f"╚{'═'*(max_len+padding)}╝"

glow_print(box_top, ANSI_COLORS[0], 0.01)
for line in quote:
    padded = f"║{line.center(max_len+padding)}║"
    sys.stdout.write(ANSI_COLORS[1] + '║' + RESET)
    for c in line.center(max_len+padding):
        sys.stdout.write(f"{W}{c}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write(ANSI_COLORS[1] + '║' + RESET + '\n')
glow_print(box_bottom, ANSI_COLORS[0], 0.01)

# Dancing author line
for i in range(8):
    spaces = ' ' * (i%4)
    sys.stdout.write(f"\033[1A{ANSI_COLORS[i%5]}{spaces}{author}{RESET}\n")
    time.sleep(0.2)

print("\n" + " "*15 + "🎬 Cut! Let's try that scene again... 🍿")