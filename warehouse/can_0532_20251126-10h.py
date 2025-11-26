"""
Campbell's Soup Can #532
Produced: 2025-11-26 10:40:09
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken, missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import sys
import time

# ASCII art elements
quote = "I said to despair: 'I’ll haunt your auditions.’ It remained silent… then sent a bill.\n"
quote += "Bringing this up at therapy costs $150/session."

# Color and style codes
BG_BLUE = '\033[48;5;59m'  # Vibrant purple-blue
FG_WHITE = '\033[38;5;255m'
BLINK = '\033[5m'
RESET = '\033[0m'

def flickering_quote():
    sys.stdout.write("\033[H\033[2J")  # Clear screen and reset cursor
    while True:
        # Flicker effect with blinking and motion
        for i in range(5):
            # Alternate background/color states            sys.stdout.write(
                f"{BG_BLUE}┌───────────────────────┐\n"
                f"{BG_BLUE}│                     \"{quote} wholesome\"\n"
                f"{BG_BLUE}│                     {BLINK}🎭     {"}
                sys.stdout.flush()
                time.sleep(0.3)
            sys.stdout.write(clear_line)
            time.sleep(0.2)

try:
    flickering_quote()
except KeyboardInterrupt:
    sys.exit()