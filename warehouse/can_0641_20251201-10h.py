"""
Campbell's Soup Can #641
Produced: 2025-12-01 10:43:14
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

def print_slowly(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def main():
    quote = "Existential dread is like a bad toupee - the more you try to ignore it, the more everyone can see it's all you think about."
    author = "- Woody Allen's Nervous Cousin"

    try:
        # Clear screen
        print("\033[H\033[J")
        
        # Print animated ASCII shark (because why not)
        print("\033[36m")
        shark = [
            "         █████████         ",
            "       ███        ███      ",
            "     ███    \033[33m▄▄▄▄▄▄▄▄\033[36m   ███   ",
            "   ███    \033[33m▀▀▀███▀▀▀\033[36m     ███ ",
            " ███    \033[91m☠\033[36m               ███",
            "███  \033[1;37mEXISTENTIAL\033[0;36m    ███",
            "███    \033[1;37mSHARK\033[0;36m        ███",
            " ███                     ███",
            "   ███                   ███",
            "     ███               ███",
            "       ███           ███",
            "         █████████████",
            ""
        ]
        for line in shark:
            print(line)
            time.sleep(0.1)
        
        # Print quote in a box
        print("\033[0m")  # Reset
        print()
        print("\033[44;1;37m" + " " * 70 + "\033[0m")
        print("\033[44;1;37m" + " " * 70 + "\033[0m")
        
        # Quote text with typewriter effect
        print("\033[44;1;37m  ", end="")
        print_slowly("\033[33m✦ \033[1;36m" + quote + "\033[0m")
        print("\033[44;1;37m  \033[33m" + author.center(66) + "\033[0m")
        
        print("\033[44;1;37m" + " " * 70 + "\033[0m")
        print("\033[44;1;37m" + " " * 70 + "\033[0m")
        
        # Flashing cursor at end
        print("\n\033[35mAnd yet we persist...\033[0m", end=" ")
        while True:
            print("\033[5m▋\033[0m", end="")
            sys.stdout.flush()
            time.sleep(0.5)
            print("\b \b", end="")
            sys.stdout.flush()
            time.sleep(0.3)
            
    except KeyboardInterrupt:
        print("\n\n\033[31mAlright, I'll stop contemplating mortality for now...\033[0m\n")

if __name__ == "__main__":
    main()