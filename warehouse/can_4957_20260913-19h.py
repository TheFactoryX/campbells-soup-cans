"""
Campbell's Soup Can #4957
Produced: 2026-09-13 19:27:33
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, os

# Enable ANSI escape sequences on Windows terminals
os.system('')

# ANSI color codes
RED   = '\033[91m'
GREEN = '\033[92m'
YELLOW= '\033[93m'
BLUE  = '\033[94m'
MAGENTA= '\033[95m'
CYAN  = '\033[96m'
RESET = '\033[0m'
BOLD  = '\033[1m'

colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Typing effect with cycling colors
for i, ch in enumerate(quote):
    sys.stdout.write('\r' + colors[i % len(colors)] + quote[:i+1] + RESET)
    sys.stdout.flush()
    time.sleep(0.05)

sys.stdout.write('\n\n')  # finish the line

# Draw a colorful box around the quote
width = len(quote) + 4
top_bottom   = BOLD + CYAN + '+' + '-' * width + '+' + RESET
empty_line   = BOLD + CYAN + '|' + ' ' * width + '|' + RESET
quote_line   = BOLD + YELLOW + '|  ' + quote + '  |' + RESET

print(top_bottom)
print(empty_line)
print(quote_line)
print(empty_line)
print(top_bottom)

# A tiny neurotic Woody‑Allen‑style face
face = r"""
   \   /   
    .-.
   '(   )'
    '-'
"""
print(MAGENTA + face + RESET)