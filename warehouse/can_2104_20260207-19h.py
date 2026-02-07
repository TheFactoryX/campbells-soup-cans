"""
Campbell's Soup Can #2104
Produced: 2026-02-07 19:36:38
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# ANSI color codes
RED = "\033[31;1m"
YELLOW = "\033[33;1m"
GREEN = "\033[32;1m"
CYAN = "\033[36;1m"
MAGENTA = "\033[35;1m"
PINK = "\033[95;1m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_coffee_cup():
    cup = f"""
        {PINK}( ){YELLOW}☕{PINK}( )
        {GREEN}.------.
       {YELLOW}/        \\
      {CYAN}|   Hot   |
      {MAGENTA}|  Liquid |
       {YELLOW}\\________/
    {RESET}"""
    print(cup)

def typewriter(text, color, delay=0.08):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    display_coffee_cup()
    time.sleep(1)

    quote = [
        "Existential crisis aside,",
        "I find it deeply unsettling", 
        "that the universe expands",
        "but my pants don't fit anymore.",
        "",
        f"{YELLOW}― Woody Allen via Python (2024){RESET}"
    ]

    for i, line in enumerate(quote):
        if i < 4:
            typewriter(f"   {RED}✽ {CYAN}{line}", CYAN)
        elif i == 4:
            print()
        else:
            print(f"\n   {line}")
        time.sleep(0.5 if i < 4 else 1.5)

    print(f"\n{GREEN}┌{'─'*45}┐")
    print(f"│ {RED}💭 The meaning of life is somewhere between 💭 {GREEN}│")
    print(f"│ {RED}   genetic predisposition and elastic waistbands   {GREEN}│")
    print(f"└{'─'*45}┘{RESET}")

if __name__ == "__main__":
    main()