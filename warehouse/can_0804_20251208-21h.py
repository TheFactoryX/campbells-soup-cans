"""
Campbell's Soup Can #804
Produced: 2025-12-08 21:28:15
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
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_ellipsis():
    print("\033[93m", end='')
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print("\033[0m")

def print_quote():
    quote = "I can't find meaning in life,\nbut I'm pretty sure my cat judges me\nfor not finding it faster."
    box_width = 50
    
    top_border = "\033[93m╔" + "═" * (box_width - 2) + "╗\033[0m"
    bottom_border = "\033[93m╚" + "═" * (box_width - 2) + "╝\033[0m"
    empty_line = "\033[93m║" + " " * (box_width - 2) + "║\033[0m"
    
    clear_screen()
    
    print("\n\n\033[3mPhilosophizing like Woody Allen", end=' ')
    animated_ellipsis()
    
    print(f"\n\n{top_border}")
    print(empty_line)
    for line in quote.split('\n'):
        padded = f"\033[97m{line.center(box_width - 4)}\033[0m"
        print(f"\033[93m║ \033[0m{padded} \033[93m║\033[0m")
    print(empty_line)
    print(bottom_border)
    print("\n\033[3m(Exit pursued by existential dread)\033[0m\n")

if __name__ == "__main__":
    print_quote()