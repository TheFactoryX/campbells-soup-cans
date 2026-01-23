"""
Campbell's Soup Can #1805
Produced: 2026-01-23 22:35:10
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

# ANSI escape codes for colors and styles
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.05, color=RESET):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_quote():
    clear_screen()
    
    # ASCII art of a neurotic thinker
    print(f"{CYAN}")
    print(r"    o O O   ")
    print(r"   o        ")
    print(r"  ___       ")
    print(r" // \\\\     ")
    print(r" || ||      ")
    print(r" \\\\_//     ")
    print(f"{RESET}")
    
    # Fancy quote box
    print(f"{YELLOW}╔{'═'*60}╗{RESET}")
    print(f"{YELLOW}║{RESET}", end="")
    typewriter_effect(
        f"{ITALIC}I'm haunted by the idea that someday I'll understand life, ", 
        color=YELLOW
    )
    print(f"{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}", end="")
    typewriter_effect(
        f"{ITALIC}and then immediately forget it while looking for my glasses.", 
        color=YELLOW
    )
    print(f"{YELLOW}╚{'═'*60}╝{RESET}")
    
    time.sleep(1)
    print(f"\n\n{RED}{BOLD}        - Woody Allen (probably){RESET}")
    print(f"{MAGENTA}\n* This quote has been certified {BOLD}92% accurate{RESET}{MAGENTA} by unreliable sources *{RESET}")

if __name__ == "__main__":
    display_quote()