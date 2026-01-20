"""
Campbell's Soup Can #1733
Produced: 2026-01-20 13:56:58
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    
    # ANSI escape codes
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    quote = [
        "The universe is a vast meaningless void,",
        "and yet I still worry about",
        "what people think of my shoes."
    ]
    
    max_length = max(len(line) for line in quote)
    border = "─" * (max_length + 4)
    
    def typewriter(text, color, delay=0.03):
        for char in text:
            print(color + char + RESET, end='', flush=True)
            time.sleep(delay)
        print()
    
    print(f"\n{MAGENTA}❝{RESET}\n")
    
    # Thinking animation
    for _ in range(3):
        print(f"{CYAN}... Woody's thinking ...{RESET}", end='\r')
        time.sleep(0.5)
        print(" " * 25, end='\r')
        time.sleep(0.5)
    
    print(f"{CYAN}┌{border}┐{RESET}")
    for line in quote:
        padded_line = line.center(max_length)
        print(f"{CYAN}│{RESET}  {YELLOW}{BOLD}", end='')
        typewriter(padded_line, YELLOW)
        print(f"{CYAN}│{RESET}", end='')
    print(f"{CYAN}└{border}┘{RESET}")
    
    print(f"\n{MAGENTA}                ― Woody Allen (probably){RESET}\n")

if __name__ == "__main__":
    main()