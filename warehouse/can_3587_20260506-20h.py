"""
Campbell's Soup Can #3587
Produced: 2026-05-06 20:46:33
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

def typewriter_effect(text, delay=0.05, color="\033[0m"):
    """Prints text one character at a time with a specific color."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def main():
    # ANSI Colors
    BROWN = "\033[38;5;94m"
    GOLD = "\033[38;5;220m"
    GREY = "\033[38;5;244m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # The Quote
    quote = "I've decided to be an optimist. It's much more efficient for the anxiety; \n" \
            "now I can worry about the disaster while believing it's a miracle it hasn't happened yet."
    
    # ASCII Art of a neurotic pair of glasses
    glasses = f"""
    {GREY}     _______            _______
    {GREY}    /       \\          /       \\
    {GREY}   |   (O)   |----------|   (O)   |
    {GREY}    \\_______/          \\_______/
    {GREY}           \\            /
    {GREY}            \\__________/
    {RESET}"""

    # Border elements
    top_border = f"{GOLD}╔" + "═" * 80 + "╗"
    bottom_border = f"{GOLD}╚" + "═" * 80 + "╝"
    side_line = f"{GOLD}║"

    # Animation sequence
    print("\033[2J\033[H") # Clear screen
    
    # 1. Draw Glasses
    print("\n" * 2)
    print(glasses.center(80))
    time.sleep(1)

    # 2. Draw Box and Quote
    print("\n")
    print(top_border.center(80))
    
    # Center the quote manually for a better look
    lines = quote.split('\n')
    for line in lines:
        padding = (80 - len(line) - 2) // 2
        print(f"{side_line}{' ' * padding}{BOLD}{WHITE}{line}{RESET}{' ' * (80 - len(line) - 2 - padding)}{side_line}")
    
    print(bottom_border.center(80))

    # 3. The "Neurotic" Sign-off
    time.sleep(1)
    print("\n")
    typewriter_effect("...Wait, did I leave the stove on?", 0.08, BROWN)
    time.sleep(0.5)
    typewriter_effect("No, I don't even own a stove. I live in fear of the *idea* of a stove.", 0.06, GREY)
    
    print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\033[0m\nExiting... my anxiety couldn't handle this program anyway.")