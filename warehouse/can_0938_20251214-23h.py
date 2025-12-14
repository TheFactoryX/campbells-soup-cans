"""
Campbell's Soup Can #938
Produced: 2025-12-14 23:29:42
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

# ANSI escape codes for colors and effects
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"
CURSOR_SHOW = "\033[?25h"
CURSOR_HIDE = "\033[?25l"

def main():
    quote = (
        "Life is absurd, but at least the\n"
        f"existential dread {RED}comes{RESET}{YELLOW} with free Wi-Fi."
    )
    
    # Create frame using box-drawing characters
    frame_width = 60
    top = RED + "╔" + "═" * (frame_width-2) + "╗" + RESET
    bottom = RED + "╚" + "═" * (frame_width-2) + "╝" + RESET
    
    print(CURSOR_HIDE)
    print("\n"*3)
    print(top)
    
    # Print empty lines with borders for vertical spacing
    empty_line = RED + "║" + " " * (frame_width-2) + "║" + RESET
    print(empty_line)
    
    # Type out quote with animation
    lines = quote.split("\n")
    for i, line in enumerate(lines):
        sys.stdout.write(RED + "║  " + RESET + YELLOW)
        sys.stdout.flush()
        
        for j, char in enumerate(line):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05 if char not in [" ", "\n"] else 0)
            
            # Random Woody Allen-style stutter
            if j % 15 == 0 and j > 0:
                time.sleep(0.2)
                sys.stdout.write(BLUE + "..." + RESET + YELLOW)
                sys.stdout.flush()
                time.sleep(0.2)
                
        remaining_space = frame_width - len(line) - 4
        sys.stdout.write(" " * remaining_space + RED + "  ║" + RESET)
        print()
        
    print(empty_line)
    print(bottom)
    
    # Add blinking cursor for dramatic effect
    for _ in range(5):
        sys.stdout.write("\033[3A")  # Move cursor up 3 lines
        sys.stdout.write("\033[47C")  # Move to end of first quote line
        sys.stdout.write(BOLD + RED + "|" + RESET)
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\033[47C")  # Move back
        sys.stdout.write(" ")
        sys.stdout.flush()
        time.sleep(0.4)
    
    print("\n"*3 + CURSOR_SHOW)

if __name__ == "__main__":
    main()