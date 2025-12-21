"""
Campbell's Soup Can #1080
Produced: 2025-12-21 11:28:01
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
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

# ANSI color codes
COLOR_ITA = "\033[3m"
COLOR_BOLD = "\033[1m"
COLOR_YELLOW = "\033[93m"
COLOR_CYAN = "\033[96m"
COLOR_RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    # ASCII art glasses (Woody Allen style)
    print(f"{COLOR_CYAN}       .--------.")
    print("      /   \\   /   \\")
    print("     |  o  | |  o  |")
    print("      \\____/ \\____/")
    print("      '------------'{COLOR_RESET}\n")
    
    time.sleep(0.5)
    
    # Quote with decorations
    typing_effect(f"{COLOR_CYAN}┌───────────────────────────────────────┐")
    typing_effect(f"│  {COLOR_RESET}{COLOR_BOLD}THE EXISTENTIAL WAITING ROOM{COLOR_RESET}{COLOR_CYAN}  │")
    typing_effect(f"├───────────────────────────────────────┤{COLOR_RESET}")
    
    time.sleep(0.3)
    typing_effect(f"{COLOR_CYAN}│{COLOR_RESET}                                             {COLOR_CYAN}│{COLOR_RESET}")
    
    quote_parts = [
        (f"  {COLOR_BOLD}I don't fear death;{COLOR_RESET}", 0.06),
        (f"{COLOR_BOLD}I just resent{COLOR_RESET} ", 0.07),
        (f"{COLOR_YELLOW}{COLOR_BOLD}having an appointment{COLOR_RESET}", 0.09),
        (f"  \n  in a calendar I never agreed to.\n", 0.06),
        (f"{COLOR_ITA}    (And knowing my luck,", 0.08),
        (f"    they'll probably reschedule.{COLOR_RESET})", 0.1)
    ]
    
    for text, delay in quote_parts:
        typing_effect(f"{COLOR_CYAN}│{COLOR_RESET}   {text}", delay)
        time.sleep(0.15)
    
    typing_effect(f"{COLOR_CYAN}│{COLOR_RESET}                                             {COLOR_CYAN}│{COLOR_RESET}")
    typing_effect(f"{COLOR_CYAN}└───────────────────────────────────────┘{COLOR_RESET}")
    
    time.sleep(0.5)
    typing_effect(f"\n{COLOR_YELLOW}         [ the cosmic receptionist rolls her eyes ]{COLOR_RESET}\n")

if __name__ == "__main__":
    main()