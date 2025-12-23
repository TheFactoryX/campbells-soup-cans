"""
Campbell's Soup Can #1127
Produced: 2025-12-23 14:37:51
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import random
import sys

# ANSI escape codes
COLORS = [
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[33m",  # Yellow
    "\033[32m",  # Green
]
BORDER = "\033[1;37m"  # Bright White
AUTHOR = "\033[3;90m"  # Italic Grey
RESET = "\033[0m"

QUOTE = [
    "Life has no meaning except the temporary relief",
    "you get when your ex's new partner turns out", 
    "to be slightly less attractive than you imagined.",
]
AUTHOR_TEXT = "- Woody Allen's existential therapist"

def magic_typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(random.choice(COLORS) + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame():
    max_len = max(len(line) for line in QUOTE)
    width = max_len + 6
    
    # Top
    print(BORDER + "╔" + "═" * (width - 2) + "╗" + RESET)
    
    # Quote lines
    for line in QUOTE:
        padded_line = line.center(max_len)
        sys.stdout.write(BORDER + "║  " + RESET)
        magic_typewriter(padded_line, delay=0.04)
        sys.stdout.write(BORDER + "  ║" + RESET)
        print()
    
    # Bottom
    print(BORDER + "╚" + "═" * (width - 2) + "╝" + RESET)
    
    # Author
    time.sleep(0.5)
    print(AUTHOR + "\n" + AUTHOR_TEXT.center(width) + RESET)

if __name__ == "__main__":
    try:
        print("\n" * 2)
        draw_frame()
        print("\n" * 2)
    except KeyboardInterrupt:
        print("\n\n" + AUTHOR + "(Interrupted by existential dread)" + RESET)