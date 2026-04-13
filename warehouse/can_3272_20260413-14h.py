"""
Campbell's Soup Can #3272
Produced: 2026-04-13 14:07:36
Worker: Google: Gemini 3 Flash Preview (google/gemini-3-flash-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def woody_philosophy():
    # ANSI Color Codes
    CLEAR = "\033[2J\033[H"
    BOLD = "\033[1m"
    GOLD = "\033[38;5;220m"
    GRAY = "\033[38;5;244m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    quote = [
        "To be honest, I'm not so much plagued by the 'Why are we here?' question ",
        "as I am by the 'How much longer does this have to go on?' question. ",
        "I have a recurring dream where I finally find the meaning of life, ",
        "but it's written in Sanskrit and my glasses are always back at the hotel."
    ]

    glasses_art = [
        r"      _   _          ",
        r"     (O)_(O)         ",
        r"     _|   |_         ",
        r"    /       \        "
    ]

    def typewriter(text, delay=0.04):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

    # Initial screen clear
    print(CLEAR)

    # Draw the "Director's Chair" atmosphere
    print(f"{GRAY}")
    print("  _____________________________________________  ")
    print(" (                                             ) ")
    print(" (  " + f"{GOLD}{BOLD}AN EXISTENTIAL CRISIS IN PRODUCTION{GRAY}" + "    ) ")
    print(" (_____________________________________________) ")
    print(f"{RESET}")

    # The "Neurotic" Animation
    for i in range(3):
        sys.stdout.write(f"\r{GRAY}   [ Thinking intensely about mortality... ]{RESET}")
        time.sleep(0.5)
        sys.stdout.write(f"\r{GRAY}   [ Thinking intensely about a small mole... ]{RESET}")
        time.sleep(0.5)
    
    print("\n")

    # Display the Glasses
    for line in glasses_art:
        print(f"{WHITE}{line.center(50)}{RESET}")

    print("\n")

    # Print the quote with timing
    for line in quote:
        sys.stdout.write("    ")
        typewriter(f"{BOLD}{line}{RESET}")
        print()
        time.sleep(0.3)

    print(f"\n{GRAY}" + "--- Alvy Singer's Unused Monologue ---".center(55) + f"{RESET}\n")

    # Small jittery effect at the end
    time.sleep(1)
    for _ in range(5):
        sys.stdout.write("\r" + " " * random.randint(0, 5) + f"{GOLD}*sigh*{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")

if __name__ == "__main__":
    try:
        woody_philosophy()
    except KeyboardInterrupt:
        print("\n\nI was going to leave anyway; the catering was terrible.")