"""
Campbell's Soup Can #4795
Produced: 2026-08-23 18:48:32
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def main():
    message_lines = [
        (YELLOW, "I'm not afraid of death,"),
        (GREEN, "but I'm terrified of life itself,"),
        (BLUE, "which is a wonderful oxymoron.")
    ]

    max_line_length = max(len(line) for color, line in message_lines)
    box_width = max_line_length + 4  # adding padding spaces

    top_bottom_border = f"{CYAN}+{'-' * (box_width - 2)}+ {RESET}"
    
    print(top_bottom_border)
    time.sleep(0.3)

    for color, line in message_lines:
        centered = line.center(max_line_length)
        print_line = f"{CYAN}|{RESET} {color}{centered} {CYAN}|{RESET}"
        print(print_line)
        time.sleep(0.2)

    print(top_bottom_border)
    time.sleep(0.3)
    print(f"\n{YELLOW}It's a beautiful paradox.{RESET}")

main()