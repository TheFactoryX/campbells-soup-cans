"""
Campbell's Soup Can #2168
Produced: 2026-02-11 15:14:02
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

# ANSI escape codes
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_quote():
    os.system('' if os.name == 'nt' else 'clear')
    print(CLEAR)
    
    print(f"{YELLOW}       oO°Oo")
    print(f"      o      o")
    print(f"     O  WOODY O")
    print(f"      o      o")
    print(f"       oO°Oo{RESET}\n")
    
    quote = [
        f"{YELLOW}╭──────────────────────────────────────────────╮",
        f"│  {MAGENTA}I worry that the universe is expanding faster  {YELLOW}│",
        f"│  {MAGENTA}than my ability to find matching socks. But    {YELLOW}│",
        f"│  {MAGENTA}then I remember - we're all just flickering    {YELLOW}│",
        f"│  {MAGENTA}lights in God's existential fridge.{' ' * 6}{YELLOW}│",
        f"╰──────────────────────────────────────────────╯{RESET}"
    ]
    
    for line in quote:
        typewriter(line, delay=0.01)
    
    print(f"\n{BLUE}", end='')
    for _ in range(3):
        print("  ...and yet we persist", end='\r')
        time.sleep(0.7)
        print(" " * 20, end='\r')
        time.sleep(0.3)

if __name__ == "__main__":
    print_quote()