"""
Campbell's Soup Can #1368
Produced: 2026-01-03 15:31:53
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import sys
import time

# ANSI escape codes for colors and styles
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
BLUE = "\033[34m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BRIGHT_WHITE = "\033[97m"

def print_with_typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote_part1 = "The universe is a vast, indifferent void filled with galaxies, black holes, "
    quote_part2 = "and the haunting realization that we're all just bipedal anxiety machines "
    quote_part3 = "worrying about whether we left the stove on."
    
    try:
        columns = os.get_terminal_size().columns
    except:
        columns = 80

    # Create ASCII art border
    border = CYAN + "╔" + "═" * (columns - 2) + "╗" + RESET
    empty_line = CYAN + "║" + " " * (columns - 2) + "║" + RESET
    bottom_border = CYAN + "╚" + "═" * (columns - 2) + "╝" + RESET

    # Create decorative elements
    top_deco = BRIGHT_WHITE + "✦" + DIM + "✦" + BRIGHT_WHITE + "✦" + RESET
    bottom_deco = DIM + "♢" + BRIGHT_WHITE + "♢" + DIM + "♢" + RESET
    
    print()
    print(BOLD + " " * ((columns - 3) // 2) + top_deco + RESET)
    print(border)
    print(empty_line)
    
    # Print quote lines centered with different colors
    for i, part in enumerate([quote_part1, quote_part2, quote_part3]):
        spaces = " " * ((columns - len(part) - 2) // 2)
        color = [BLUE, CYAN, YELLOW][i]
        line = CYAN + "║" + RESET + spaces + color + part + spaces + CYAN + "║" + RESET
        print_with_typing(line, delay=0.02 if i < 2 else 0.05)
    
    print(empty_line)
    print(bottom_border)
    print(BOLD + " " * ((columns - 3) // 2) + bottom_deco + RESET)
    print(RED + BOLD + " " * ((columns - 40) // 2) + "— Woody Allen, probably" + RESET)
    print()

if __name__ == "__main__":
    main()