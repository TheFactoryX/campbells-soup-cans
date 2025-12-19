"""
Campbell's Soup Can #1033
Produced: 2025-12-19 08:45:08
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
    *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
    *                                                                         *
    *             "I am two with nature, like a split personality."           *
    *                          - (Probably) Woody Allen                      *
    *                                                                         *
    *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
    
    A dramatic, neurotic, and colorful Python monologue.
"""

import sys
import time
import random

# --- ANSI Colors & Formatting (Pure Python, No Dependencies) ---
class Style:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    ITALIC  = "\033[3m" # Not widely supported, but we try
    UNDER   = "\033[4m"
    
    # Foreground
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
    GRAY    = "\033[90m"
    
    # Backgrounds
    BG_RED  = "\033[41m"
    BG_CYAN = "\033[46m"

# --- The Script ---
def type_effect(text, color, speed=0.04):
    """Prints text character by character for dramatic effect."""
    print(color, end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print(Style.RESET)

def slide_in(lines, color):
    """Slides text in from the right."""
    width = 60
    for i in range(width, -1, -1):
        # Move cursor up to overwrite previous frame
        sys.stdout.write("\033[F" * (len(lines) + 2)) 
        sys.stdout.write("\033[K") # Clear line
        
        for line in lines:
            padding = " " * i
            print(f"{color}{padding}{line}{Style.RESET}")
        time.sleep(0.02)

def draw_curtains():
    """Animates opening curtains."""
    rows = 10
    for step in range(20):
        sys.stdout.write("\033[H") # Home cursor
        print(f"{Style.BOLD}{Style.YELLOW}THEATER OF THE MIND{Style.RESET}\n")
        
        left_space = " " * step
        right_space = " " * (39 - step)
        
        for _ in range(rows):
            # Red curtains
            print(f"{Style.BG_RED}{left_space}      {right_space}{Style.RESET}")
        
        sys.stdout.flush()
        time.sleep(0.05)

def main():
    # 1. Clear Screen & Initial Setup
    print("\033[H\033[J", end="") # Clear screen
    
    # 2. The Dramatic Entrance (ASCII Art + Animation)
    # We create a little "stage" with colors
    stage_header = [
        "   _____________________________________________________________________  ",
        "  |                                                                     | ",
        "  |    " + Style.CYAN + "Existentialist Cabaret" + Style.RESET + "                                         | ",
        "  |_____________________________________________________________________| "
    ]
    
    # Animate the text sliding in
    slide_in(stage_header, Style.GRAY)
    time.sleep(0.5)
    
    # 3. The Quote (The Core Content)
    quote_part_1 = "I'm not afraid of death;"
    quote_part_2 = "I just don't want to be there"
    quote_part_3 = "when it happens."
    
    # The Woody Allen persona animation (The cursor and the neurotic typing)
    print("\n" * 2)
    print(f"{Style.GRAY}({Style.RED}*{Style.GRAY}){Style.WHITE} Neurotic Philosopher: {Style.RESET}", end="")
    
    # Type out the quote with specific timing and color shifts
    time.sleep(0.5)
    
    type_effect(quote_part_1, Style.BOLD + Style.YELLOW, 0.06)
    time.sleep(0.2)
    
    # Dramatic pause
    print(f"{Style.GRAY}({Style.RED}*{Style.GRAY}){Style.WHITE} Neurotic Philosopher: {Style.RESET}", end="")
    type_effect(quote_part_2, Style.MAGENTA, 0.05)
    time.sleep(0.4)
    
    # The punchline
    print(f"{Style.GRAY}({Style.RED}*{Style.GRAY}){Style.WHITE} Neurotic Philosopher: {Style.RESET}", end="")
    type_effect(quote_part_3, Style.RED + Style.BOLD, 0.08)
    
    # 4. The Neurotic Elaboration (The Footer)
    time.sleep(1.0)
    print("\n" + Style.GRAY)
    print("   " + "_" * 55)
    print(f"  | {Style.RESET}He sighs, adjusting his thick-rimmed glasses. He looks at the{Style.GRAY}  |")
    print(f"  | {Style.RESET}void. The void looks back. It asks for a refund.{Style.GRAY}                |")
    print("  |" + "_" * 55 + "|")
    print(Style.RESET)
    
    # 5. Final Bow (Quick Animation)
    time.sleep(1.0)
    for i in range(5):
        sys.stdout.write("\033[F") # Move up
        sys.stdout.write("\033[K") # Clear line
        
        if i % 2 == 0:
            print(f"{Style.GREEN}   \\o/   {Style.RESET}    {Style.YELLOW}APPLAUSE{Style.RESET}    {Style.GREEN}   \\o/   {Style.RESET}")
        else:
            print(f"{Style.GREEN}    |    {Style.RESET}    {Style.YELLOW}APPLAUSE{Style.RESET}    {Style.GREEN}    |    {Style.RESET}")
        time.sleep(0.3)
        
    time.sleep(1.0)
    print("\n" + Style.GRAY + "  (Curtains close...)" + Style.RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + Style.RESET + "Exiting prematurely... typical.")
        sys.exit(0)