"""
Campbell's Soup Can #845
Produced: 2025-12-10 18:46:16
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_print(text, color_code):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.04 if char not in ',.!?' else 0.2)
    print()

def main():
    clear_screen()
    
    quote = [
        "I keep wondering if the universe has a purpose -",
        "and if so, how much longer it plans to wait",
        "before revealing it to me personally,",
        "because frankly I'm losing patience.",
        "           -- Woody Allen's Brain"
    ]
    
    box_top =    "\033[33m/¯¯\\" + "¯"*(max(len(line) for line in quote)+2) + "¯\\\033[0m"
    box_bottom = "\033[33m\\__/" + "_"*(max(len(line) for line in quote)+2) + "_/\033[0m"
    
    print("\n\n")
    print(f"{' '*(os.get_terminal_size().columns//2 - len(box_top)//2)}\033[1;31m{box_top}\033[0m")
    
    for line in quote:
        padding = ' '*(max(len(line) for line in quote) - len(line) + 4)
        print(f"{' '*(os.get_terminal_size().columns//2 - len(box_top)//2)}\033[33m| \033[0m", end='')
        woody_print(f"\033[93m{line}{padding}", "1;93")
        print(f"{' '*(os.get_terminal_size().columns//2 - len(box_top)//2)}\033[33m |\033[0m")
    
    print(f"{' '*(os.get_terminal_size().columns//2 - len(box_bottom)//2)}\033[1;31m{box_bottom}\033[0m")
    
    print("\n\n\033[36m(There's a 50% chance this program has already forgotten why it ran.)\033[0m\n")

if __name__ == "__main__":
    main()