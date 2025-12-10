"""
Campbell's Soup Can #841
Produced: 2025-12-10 14:42:33
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
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
COLOR_YELLOW = "\033[93m"
COLOR_GREEN = "\033[92m"
COLOR_CYAN = "\033[96m"
COLOR_RESET = "\033[0m"

def typing_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"\n{COLOR_YELLOW}        ★ ☆ ✰ ✦ ✧ ✩ ✪ {COLOR_RESET}")
    print(f"{COLOR_CYAN}          ___")
    print("         (O O)")
    print("         ( - )")
    print("        /|Ψ|\\")
    print(f"       oo   oo{COLOR_RESET}")
    print(f"{COLOR_YELLOW}       ✩ ✪ ✧ ✦ ✰ ☆ ★ {COLOR_RESET}\n")
    
    quote = (
        f"{COLOR_GREEN}╔══════════════════════════════════════════════╗\n"
        f"║ {COLOR_RESET}I worry that my plants are judging me.        {COLOR_GREEN}║\n"
        f"║ {COLOR_RESET}They've seen me binge-watch entire series     {COLOR_GREEN}║\n"
        f"║ {COLOR_RESET}while promising I'd 'start tomorrow.'         {COLOR_GREEN}║\n"
        f"║ {COLOR_RESET}Now they won't grow - it's either the soil,   {COLOR_GREEN}║\n"
        f"║ {COLOR_RESET}or silent botanical disappointment.          {COLOR_GREEN}║\n"
        f"╚══════════════════════════════════════════════╝{COLOR_RESET}"
    )
    
    typing_print(quote, 0.02)
    print(f"\n{COLOR_CYAN}       (I should probably water them...){COLOR_RESET}\n")

if __name__ == "__main__":
    main()