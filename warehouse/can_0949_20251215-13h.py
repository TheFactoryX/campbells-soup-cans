"""
Campbell's Soup Can #949
Produced: 2025-12-15 13:08:30
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors and styles
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
FRAME = "\033[51m"

def type_with_effect(text, delay=0.03, color=WHITE):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Clear screen
    print("\033[H\033[J")
    
    # Woody Allen ASCII art
    ascii_art = f"""
    {RED}
       O
      /|\\    {WHITE}("Life is full of meaning...")
      / \\    {WHITE}("Wait, no - I meant misery...")
    {RESET}
    """
    print(ascii_art)
    time.sleep(1.2)
    
    # Decorative frame
    print(f"{FRAME}{' '*50}{RESET}")
    
    # Quote with typing effect
    type_with_effect(f"\n{BOLD}{YELLOW}\"I'm convinced there's an afterlife,", 0.04)
    type_with_effect(f"{UNDERLINE}But I'm pretty sure they use the same caterers", 0.03, CYAN)
    type_with_effect(f"{BOLD}{RED}as my cousin Harold's wedding.\"{RESET}\n", 0.05)
    
    # Signature
    time.sleep(0.5)
    type_with_effect(f"          {WHITE}- Woody Allen's Worries{RESET}", 0.05)
    
    # Funny closing line
    time.sleep(1)
    print(f"\n{CYAN}(This message will self-destruct in existential dread...){RESET}")

if __name__ == "__main__":
    main()