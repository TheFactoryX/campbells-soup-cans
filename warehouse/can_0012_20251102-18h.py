"""
Campbell's Soup Can #12
Produced: 2025-11-02 18:36:17
Worker: Microsoft: MAI DS R1 (free) (microsoft/mai-ds-r1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def typewriter(text, color, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    print("\033[2J\033[H", end="", flush=True)
    
    quote = ("Life is a cosmic sitcom where the laugh track is broken "
             "and I'm the punchline that forgot its timing. Frankly, "
             "death seems overrated - like WiFi in the afterlife.")
    author = "― Woody Allen"
    wrapped = textwrap.wrap(quote, width=50)
    
    # Top frame
    print(YELLOW + "▄" * 62 + RESET)
    print(YELLOW + "█" + RESET + "░" * 60 + YELLOW + "█" + RESET)
    
    # Quote box
    for i, line in enumerate(wrapped):
        padding = 60 - len(line)
        left_pad = padding // 2 * " "
        right_pad = (padding - padding // 2) * " "
        
        sys.stdout.write(YELLOW + "█" + RESET)
        typewriter("▓" + left_pad, CYAN, 0.005)
        typewriter(line, CYAN if i==1 else "\033[3m" + CYAN)
        typewriter(right_pad + "▓", CYAN, 0.005)
        print(YELLOW + "█" + RESET)
    
    # Author flourish
    sys.stdout.write(YELLOW + "█" + RESET)
    typewriter(" " * 38 + "✎ " + RED + author + " " * 4, "")
    print(YELLOW + "█" + RESET)
    
    # Bottom frame
    print(YELLOW + "█" + RESET + "░" * 60 + YELLOW + "█" + RESET)
    print(YELLOW + "▀" * 62 + RESET)
    print("\n" + " " * 24 + YELLOW + "⠸⣷⣄⠻⣿⠟⣡⣾" + RESET)

if __name__ == "__main__":
    main()