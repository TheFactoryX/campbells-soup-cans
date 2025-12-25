"""
Campbell's Soup Can #1178
Produced: 2025-12-25 21:30:46
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
import sys

def print_with_delay(text, delay=0.1, end='\n'):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)

def main():
    # ANSI escape codes for colors and styles
    bold_red = "\033[1;31m"
    bold_yellow = "\033[1;33m"
    bold_cyan = "\033[1;36m"
    reset = "\033[0m"
    
    # Clear screen
    print("\033[H\033[J")
    
    # Quote components
    frame = bold_red + "*" * 60 + reset
    quote = [
        bold_red + "Life has no meaning," + reset,
        bold_yellow + "it just yammers on endlessly" + reset,
        bold_cyan + "like one of my therapy sessions." + reset,
        bold_yellow + "And yet" + reset,
        bold_cyan + "I still worry" + reset,
        bold_red + "about being late" + reset,
        bold_cyan + "to the" + reset,
        bold_yellow + "meaningless thing." + reset
    ]
    
    # ASCII art
    iris = [
        bold_yellow + "           o           " + reset,
        bold_red +   "          /|\\          " + reset,
        bold_cyan +  "         / | \\         " + reset,
        bold_red +   "        /  |  \\        " + reset,
        bold_yellow + "   ____/___|___\\____   " + reset
    ]
    
    # Animation
    print()
    print(frame)
    for line in iris:
        print_with_delay(" " * 10 + line)
        time.sleep(0.3)
    print()
    print_with_delay(" " * 15 + bold_red + "« WOODY'S WISDOM »" + reset, 0.05)
    print("\n" + frame + "\n")
    
    # Print quote
    for i, part in enumerate(quote):
        print_with_delay(" " * (10 if i % 2 else 15) + part, 0.08)
        print()
    
    # Final flourish
    time.sleep(0.5)
    print("\n" + frame)
    print_with_delay("\n" + " " * 18 + bold_cyan + "└(^o^ )┘" + reset + bold_yellow + " (relax, it's temporary)" + reset + "\n", 0.05)

if __name__ == "__main__":
    main()