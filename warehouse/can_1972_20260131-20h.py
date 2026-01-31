"""
Campbell's Soup Can #1972
Produced: 2026-01-31 20:41:51
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os, sys, random, time

def main():
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII art frame
    ascii_art = '''
  _________
 /         \
|   _______ |
|  /       \|
 |___________|
'''
    print(ascii_art)

    # Woody Allen style quote (one line)
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # Animate the quote – each character appears in a random foreground/background color
    for char in quote:
        fg = random.choice(['31','32','33','34','35','36','37'])  # red, green, yellow, blue, magenta, cyan, white
        bg = random.choice(['41','42','43','44','45','46','47']) # red, green, yellow, blue, magenta, cyan, white backgrounds
        styled = f"\033[{fg};{bg}m{char}\033[0m"
        print(styled, end='\r', flush=True)
        time.sleep(0.02)

    # Final newline and attribution
    print()
    print("\033[0m— Woody Allen (in his own head)")

if __name__ == "__main__":
    main()