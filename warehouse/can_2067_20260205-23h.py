"""
Campbell's Soup Can #2067
Produced: 2026-02-05 23:40:39
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

COLORS = {
    'yellow': '\033[93m',
    'cyan': '\033[36m',
    'reset': '\033[0m',
    'blink': '\033[5m'
}

QUOTE = "Life is absurdly meaningless,\nbut did you remember to unplug the iron?"
AUTHOR = "- Woody Allen's Anxiety"

def type_effect(text, color, delay=0.04):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(COLORS['reset'])

def main():
    # Clear screen
    print("\033[2J\033[H", end='')
    
    # Calculate box dimensions
    lines = QUOTE.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max_len + 6
    
    # Create ASCII box elements
    top = COLORS['yellow'] + "╔" + "~" * (box_width-2) + "╗" + COLORS['reset']
    bottom = COLORS['yellow'] + "╚" + "~" * (box_width-2) + "╝" + COLORS['reset']
    empty = COLORS['yellow'] + "║" + " " * (box_width-2) + "║" + COLORS['reset']
    
    # Print animated box
    print(top)
    print(empty)
    for line in lines:
        sys.stdout.write(COLORS['yellow'] + "║  ")
        padded = line.center(max_len)
        type_effect(padded, COLORS['yellow'])
        sys.stdout.write(COLORS['yellow'] + "  ║\n")
    print(empty)
    print(bottom)
    
    # Print author with blink effect
    time.sleep(0.5)
    sys.stdout.write("\n" + " " * ((box_width - len(AUTHOR))//2))
    type_effect(AUTHOR, COLORS['cyan'] + COLORS['blink'], 0.08)
    
    # Finishing touch
    time.sleep(1)
    print("\n\n" + COLORS['reset'] + " "*(box_width//2) + "(ツ)")

if __name__ == "__main__":
    main()