"""
Campbell's Soup Can #4671
Produced: 2026-08-18 09:48:03
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

def woody_allen_experience():
    # The neurotic masterpiece
    quote = "I've decided that the only way to survive the crushing weight of existence is to pretend I'm an exceptionally well-dressed ghost in my own life."
    
    # ANSI Colors
    C_GOLD = "\033[38;5;220m"
    C_CYAN = "\033[36m"
    C_WHITE = "\033[97m"
    C_RESET = "\033[0m"
    C_BOLD = "\033[1m"

    # ASCII Art - A pair of neurotic glasses
    glasses = [
        "   _______       _______   ",
        "  /       \\     /       \\  ",
        " |   (O)   |---|   (O)   | ",
        "  \\_______/     \\_______/  "
    ]

    def slow_print(text, delay=0.05, color=C_RESET):
        for char in text:
            sys.stdout.write(color + char + C_RESET)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    # Clear screen
    print("\033[H\033[J")

    # Intro Animation
    for line in glasses:
        print(f"{C_GOLD}{line.center(60)}{C_RESET}")
        time.sleep(0.2)

    print("\n" + " " * 20 + f"{C_BOLD}{C_CYAN}A MOMENT OF NEUROTIC REFLECTION{C_RESET}\n")
    time.sleep(1)

    # The "Anxiety" Loading bar
    loading_text = "Calculating existential dread"
    print(f"{C_WHITE}{loading_text}{C_RESET}", end="")
    for _ in range(20):
        sys.stdout.write(f"{C_GOLD}■{C_RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

    # The Quote Box
    border_top = "╔" + "═" * 68 + "╗"
    border_bottom = "╚" + "═" * 68 + "╝"
    
    print(f"{C_CYAN}{border_top}{C_RESET}")
    
    # Split quote into lines to fit the box
    words = quote.split()
    line = ""
    for word in words:
        if len(line) + len(word) < 60:
            line += word + " "
        else:
            print(f"{C_CYAN}║{C_RESET} {C_WHITE}{line.ljust(66)}{C_RESET} {C_CYAN}║{C_RESET}")
            line = word + " "
    print(f"{C_CYAN}║{C_RESET} {C_WHITE}{line.ljust(66)}{C_RESET} {C_CYAN}║{C_RESET}")
    
    print(f"{C_CYAN}{border_bottom}{C_RESET}")

    time.sleep(1)
    print("\n" + " " * 25 + f"{C_GOLD}— Woody Allen (ish){C_RESET}\n")
    
    # Final punchline fade
    slow_print("...Now, where did I leave my medication?", 0.08, C_CYAN)
    print("\n")

if __name__ == "__main__":
    try:
        woody_allen_experience()
    except KeyboardInterrupt:
        print("\nInterrupted! Even the program has an anxiety attack.")