"""
Campbell's Soup Can #2358
Produced: 2026-02-21 16:47:44
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_wooden_quote():
    clear_screen()
    
    # Woody Allen ASCII art
    woody_art = """
           ,--./,-.
    |\\__/,|   '
   _._ ._.--~,
  ( `)_`---'(
  _`-'()) .---.
.'___ __)(   __`
|   '.__ `.'  |
|    |.'.'.__|
|    | '.__.'
|    |'._.'
'----'
"""
    
    # Print Woody Allen in a different color
    print("\033[1;35m" + woody_art + "\033[0m")
    
    # Quote with color emphasis
    quote = "\033[1;33mI'm not afraid of death; I just don't want to be there when it happens.\033[0m"
    sub_quote = "\033[0;36m— Woody Allen\033[0m"
    
    # Print a decorative border
    border = "\033[1;34m" + "─" * 80 + "\033[0m"
    print("\n" + border)
    print(f"\033[1;32m{'WOODY ALLEN ON LIFE:':^80}\033[0m")
    print(border)
    print()
    
    # Typewriter effect for the main quote
    typewriter_effect(f"\033[1;37m{quote:^80}\033[0m", 0.03)
    
    # Print a small animation before the author
    for i in range(3):
        sys.stdout.write("\033[1;36m.\033[0m")
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\n" + border)
    print(f"\033[0;36m{sub_quote:^80}\033[0m")
    print(border)
    
    # A small philosophical reflection
    time.sleep(1)
    reflection = "\033[0;97m\"Death is nature's way of telling you to slow down.\"\033[0m"
    typewriter_effect(f"\n{reflection:^80}\n", 0.05)
    
    # Clear screen after a few seconds
    time.sleep(5)
    clear_screen()

if __name__ == "__main__":
    print_wooden_quote()