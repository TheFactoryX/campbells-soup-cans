"""
Campbell's Soup Can #4497
Produced: 2026-08-09 10:52:28
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

# ANSI color codes
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
MAGENTA= '\033[35m'
CYAN   = '\033[36m'
RESET  = '\033[0m'

def rainbow(s):
    """Return *s* with each character colored in a rotating palette."""
    palette = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    return ''.join(palette[i % len(palette)] + ch for i, ch in enumerate(s))

# Woody Allen style existential joke
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Build a decorative frame
border = '*' * (len(quote) + 4)

# ----- Animated top border -------------------------------------------------
for _ in range(2):
    sys.stdout.write(rainbow('\n' + border + '\n'))
    time.sleep(0.15)                     # tiny pause for a blinking effect

# ----- Quote inside the box ------------------------------------------------
sys.stdout.write('* ' + quote + ' *\n')
sys.stdout.write(rainbow(border + '\n'))

# ----- A quick flashing star animation ------------------------------------
for _ in range(4):
    sys.stdout.write('\r' + ' ' * (len(border)//2) + BLUE + '★' + RESET)
    time.sleep(0.35)                     # blink four times

# ----- Print the punchline in a rainbow of colors -----------------------
print()
def colorful(txt):
    palette = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    return ''.join(palette[i % len(palette)] + ch for i, ch in enumerate(txt)) + RESET

print(colorful(quote))
print()