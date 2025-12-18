"""
Campbell's Soup Can #1021
Produced: 2025-12-18 18:48:27
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import os

# ANSI escape codes
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BLINK = "\033[5m"
RESET = "\033[0m"
BOLD = "\033[1m"

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def print_centered(text, color=RESET, width=None):
    if not width:
        width = get_terminal_width()
    padding = (width - len(text.strip())) // 2
    print(" " * padding + color + text.strip() + RESET)

def main():
    quote = "I'm not scared of the afterlife - I just hope it doesn't have "\
            "the same seating arrangements as a middle school cafeteria."

    width = min(get_terminal_width(), 70)
    border = RED + "╔" + "═" * (width-2) + "╗" + RESET
    bottom_border = RED + "╚" + "═" * (width-2) + "╝" + RESET

    print("\n" * 2)
    print_centered(border, width=width)
    
    # Animation: Woody Allen-style hesitation
    sys.stdout.write(YELLOW + " " * ((width - 10)//2) + "Woody says..." + RESET)
    sys.stdout.flush()
    for _ in range(3):
        time.sleep(0.7)
        sys.stdout.write(BLINK + "." + RESET)
        sys.stdout.flush()
    time.sleep(1)
    print("\r" + " " * (width//2) + "\r")  # Clear line

    # Print quote with artistic formatting
    print_centered(RED + "║" + RESET, width=width)
    for line in [quote[:36], quote[36:]]:
        print_centered(
            RED + "║" + RESET + 
            YELLOW + BOLD + f" {line.center(width-4)} " + RESET + 
            RED + "║" + RESET, 
            width=width
        )
    print_centered(RED + "║" + RESET, width=width)
    print_centered(bottom_border, width=width)
    
    # Signature
    time.sleep(0.5)
    print_centered(CYAN + "~ a nervous existential crisis production ~" + RESET)
    print("\n" * 2)

if __name__ == "__main__":
    main()