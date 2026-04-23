"""
Campbell's Soup Can #3416
Produced: 2026-04-23 17:46:06
Worker: Google: Gemma 4 31B (free) (google/gemma-4-31b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def print_centered(text, width=80):
    print(text.center(width))

def typewriter_effect(text, delay=0.05, color="\033[37m"):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def generate_woody_experience():
    # Colors
    C_GOLD = "\033[93m"
    C_CYAN = "\033[96m"
    C_RED = "\033[91m"
    C_BOLD = "\033[1m"
    C_RESET = "\033[0m"

    # The "Philosophical" Quote
    quote = "I've decided that the only way to truly conquer my fear of the void is to fill it with an overwhelming amount of anxiety about my choice of appetizers."
    
    # ASCII Glasses (The iconic look)
    glasses = f"""
    {C_CYAN}   ooooooo       ooooooo
     (  X  )     |       (  X  )
      \___/------|------\___/
                 |
    {C_RESET}"""

    # Border elements
    top_border = f"{C_GOLD}╔" + "═" * 76 + "╗{C_RESET}"
    bottom_border = f"{C_GOLD}╚" + "═" * 76 + "╝{C_RESET}"
    side_l = f"{C_GOLD}║{C_RESET}"
    side_r = f"{C_GOLD}║{C_RESET}"

    # Sequence
    print("\n" * 2)
    print_centered(glasses)
    print_centered(f"{C_BOLD}A NEUROTIC REFLECTION{C_RESET}")
    print("\n")
    
    print(top_border)
    
    # Mimic "thinking" process
    thinking_dots = ["", ".", "..", "..."]
    for _ in range(3):
        for dot in thinking_dots:
            sys.stdout.write(f"\r{side_l} {C_RED}Existential crisis in progress{thinking_dots[0]}{dot}{C_RESET} {side_r}")
            sys.stdout.flush()
            time.sleep(0.3)
    
    # Clear the "thinking" line
    sys.stdout.write("\r" + " " * 80 + "\r")
    
    # Print the quote with typewriter effect inside the box
    # Splitting quote into lines to fit the box
    words = quote.split()
    line = ""
    for word in words:
        if len(line) + len(word) < 70:
            line += word + " "
        else:
            print(f"{side_l} {C_BOLD}{line.strip()}{C_RESET} {side_r}")
            line = word + " "
    print(f"{side_l} {C_BOLD}{line.strip()}{C_RESET} {side_r}")
    
    print(bottom_border)
    
    # Final neurotic punchline
    time.sleep(1)
    print_centered(f"\n{C_CYAN}*(Now, where did I leave my medication?)*{C_RESET}")
    print("\n" * 2)

if __name__ == "__main__":
    try:
        generate_woody_experience()
    except KeyboardInterrupt:
        print("\n\033[91mInterrupted! Just like my train of thought during a panic attack.\033[0m")