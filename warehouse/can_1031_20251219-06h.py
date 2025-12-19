"""
Campbell's Soup Can #1031
Produced: 2025-12-19 06:48:25
Worker: Mistral: Mistral 7B Instruct (free) (mistralai/mistral-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
from itertools import cycle

# Color definitions
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m'
}

# ASCII art frame
FRAME = [
    "╔═════════════════════════════════════════════════════════════════════════════════════════════════╗",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "║                                                                                 ║",
    "╚═════════════════════════════════════════════════════════════════════════════════════════════════╝"
]

# Woody Allen quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

def print_animated_frame(frame, quote, colors):
    color_cycle = cycle(colors)
    for i, line in enumerate(frame):
        if i == 4:  # The line where the quote will appear
            colored_line = next(color_cycle) + line + COLORS['reset']
            print(colored_line)
            print(f"║ {COLORS['yellow']}{' ' * 20}{quote}{' ' * 20}{COLORS['reset']} ║")
        else:
            colored_line = next(color_cycle) + line + COLORS['reset']
            print(colored_line)

def main():
    print("\033[2J\033[H")  # Clear screen
    print(f"{COLORS['cyan']}Woody Allen's Philosophical Wisdom{COLORS['reset']}\n\n")

    # Animate the frame with the quote
    for _ in range(3):
        print_animated_frame(FRAME, QUOTE, [COLORS['red'], COLORS['green'], COLORS['blue'], COLORS['magenta']])
        time.sleep(0.5)
        print("\033[2J\033[H")  # Clear screen

    # Final display
    print_animated_frame(FRAME, QUOTE, [COLORS['white']])
    print(f"\n{COLORS['magenta']}-- Woody Allen (probably){COLORS['reset']}")

if __name__ == "__main__":
    main()