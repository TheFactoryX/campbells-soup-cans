"""
Campbell's Soup Can #4310
Produced: 2026-07-24 11:55:43
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def animate_text(text, delay=0.05, color=""):
    """Prints text character by character for dramatic effect."""
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)

def draw_stage():
    """Renders an ASCII art stage setting."""
    colors = {
        'ed': "\033[91m",
        'yellow': "\033[93m",
        'cyan': "\033[96m",
        'white': "\033[97m",
        'eset': "\033[0m",
        'bold': "\033[1m"
    }
    
    stage = f"""
    {colors['yellow']}
          ________________________________________________
         /                                                \\
        |      {colors['white']}WELCOME TO THE EXISTENTIAL THEATER{colors['yellow']}      |
         \\________________________________________________/
                ||                              ||
         _______||______________________________||_______
        |                                                |
        |        {colors['cyan']}      [ Spotlight ON ]      {colors['white']}         |
        |________________________________________________|
    """
    print(stage)

def play_monologue():
    # ANSI Colors
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    ITALIC = "\033[3m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # The Quote (Woody Allen Style)
    quote = "“I have a profound fear of the infinite, which is difficult, because I'm also quite attached to my neuroses, and frankly, I don't have the energy to reinvent my anxiety for a new universe.”"
    
    draw_stage()
    
    time.sleep(1)
    print(f"\n{BOLD}{YELLOW}   [ A nervous man in a turtleneck steps into the light... ]{RESET}")
    time.sleep(2)

    print("\n" + " " * 10 + f"{RED}---")
    
    # The Dramatic Reveal
    animate_text(f"\n    {ITALIC}{quote}{RESET}", delay=0.03)
    
    print(f"\n{RED}---")

    time.sleep(1)
    print(f"\n{YELLOW}        (The audience stares awkwardly into the void...){RESET}")
    time.sleep(1)
    print(f"\n{CYAN}                [ Curtain Falls ]{RESET}\n")

if __name__ == "__main__":
    # Clear screen (works on most terminals)
    print("\033[H\033[J", end="")
    play_monologue()