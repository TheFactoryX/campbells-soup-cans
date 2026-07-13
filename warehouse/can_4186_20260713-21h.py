"""
Campbell's Soup Can #4186
Produced: 2026-07-13 21:12:37
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# Woody Allen style philosophical quote
quote = "I’m not scared of death; I just don’t want to be there when it happens."

# ANSI escape codes
ESC = '\x1b'
RESET = ESC + '[0m'
GREEN = ESC + '[92m'
YELLOW = ESC + '[93m'
MAGENTA = ESC + '[95m'

def draw_frame(text):
    """Prints the given text inside a colorful ASCII box."""
    width = len(text) + 6
    top = GREEN + '+' + '-' * width + '+' + RESET
    middle = GREEN + '| ' + YELLOW + text + YELLOW + ' |' + GREEN + RESET
    print(top)
    print(middle)
    print(top)

# Typewriter effect for a playful reveal
for ch in quote:
    sys.stdout.write(MAGENTA + ch + RESET)
    sys.stdout.flush()
    time.sleep(0.02)
sys.stdout.write('\n')

# Display the quote inside the decorative frame
draw_frame(quote)