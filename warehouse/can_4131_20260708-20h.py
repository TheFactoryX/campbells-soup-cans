"""
Campbell's Soup Can #4131
Produced: 2026-07-08 20:37:17
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import os
import time

# Configuration: ANSI Escape Codes for Colors
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    # Text Colors
    RED = '\033[31m'
    RED_BRIGHT = '\033[91m'
    GREEN = '\033[32m'
    GREEN_BRIGHT = '\033[92m'
    YELLOW = '\033[33m'
    YELLOW_BRIGHT = '\033[93m'
    CYAN = '\033[36m'
    CYAN_BRIGHT = '\033[96m'
    WHITE = '\033[37m'
    WHITE_BRIGHT = '\033[97m'
    # Background Colors (used for contrast if needed, but text focus here)
    BG_BLACK = '\033[40m'
    BG_WHITE = '\033[47m'

def clear_screen():
    """Clears the console to simulate a fresh "bit" starting."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_print(text, color=Colors.WHITE_BRIGHT, speed=0.04):
    """
    Prints text with a typewriter animation effect.
    Visually interesting and creates anticipation.
    """
    sys.stdout.write(color + BOLD)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Slight variation in speed to make it feel more human (or mad)
        time.sleep(speed * (1 if char.isalnum() else 0.1))
    sys.stdout.write(Colors.RESET + '\n')

def main():
    clear_screen()
    
    # --- ASCII Theater Introduction ---
    # A simple frame to represent the "screen"
    border = f"{Colors.CYAN_BRIGHT}╔{'═'*60}╗{Colors.RESET}"
    border_end = f"{Colors.CYAN_BRIGHT}╚{'═'*60}╝{Colors.RESET}"
    
    print(f"{border}")
    print(f"{Colors.CYAN_BRIGHT}║{' ' * 60}║{Colors.RESET}")
    print(f"{Colors.YELLOW}║{' ':^60}║{Colors.RESET}") # Empty title space
    print(f"{Colors.YELLOW}║{'Woody Allen - The Monologue (Live)':^60}║{Colors.RESET}")
    print(f"{Colors.CYAN_BRIGHT}║{' ' * 60}║{Colors.RESET}")
    print(f"{border}{Colors.RESET}")

    # --- The Quote ---
    # This quote captures his style: neurotic, self-aware, obsessed with mortality.
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "Life is a series of births, and... well, death. And also my Wi-Fi keeps "
        "dropping mid-thought. It's a tragic accident."
    )

    # Print quote with animation
    typewriter_print(quote, Colors.CYAN_BRIGHT, 0.03)

    # --- Visual End Note ---
    # Adding an "Office Desk" foot note, a classic Allen setting
    print("\n" + f"{Colors.GREEN_DIM if hasattr(Colors, 'GREEN_DIM') else Colors.GREEN}")
    print("  [Interior: Woody's cramped office. Entire day spent balancing spreadsheets]")
    print("   and realizing his life is just a financial audit he never signed up for...]")
    
    # Attribution
    print(f"{Colors.YELLOW}")
    print("                                                 - Woody Allen (in his head)")
    print(f"{border_end}")

if __name__ == "__main__":
    main()