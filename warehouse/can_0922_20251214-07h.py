"""
Campbell's Soup Can #922
Produced: 2025-12-14 07:30:31
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# ANSI escape codes for colors and styles
RESET   = '\033[0m'
BOLD    = '\033[1m'
CYAN    = '\033[36m'
YELLOW  = '\033[93m'

# The Woody‑Allen‑style quote (neurotic, funny, self‑deprecating, existential)
QUOTE = (
    "I keep telling myself that the only way "
    "to find meaning in this chaos is to write a joke about it, "
    "and then forget I'm still looking for meaning."
)

# Build a simple boxed display around the quote
border = '-' * len(QUOTE)
top    = '+' + border + '+'
middle = '|' + QUOTE + '|'
bottom = top

lines = [top, middle, bottom]

def typewriter(lines, per_char=0.02, line_pause=0.15):
    """Print lines with a typewriter effect, coloring borders and quote differently."""
    for line in lines:
        colour = YELLOW if '|' in line else CYAN  # borders cyan, quote yellow
        for char in line:
            sys.stdout.write(colour + char + RESET)
            sys.stdout.flush()
            time.sleep(per_char + random.uniform(-0.01, 0.01))
        sys.stdout.write('\n')
        time.sleep(line_pause)

def thinking_animation():
    """Brief ‘thinking’ animation to set the mood before the quote appears."""
    sys.stdout.write(BOLD + YELLOW + "Thinking" + RESET)
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.6)
    sys.stdout.write('\n\n')
    time.sleep(0.3)

def main():
    thinking_animation()
    typewriter(lines)

if __name__ == "__main__":
    main()
