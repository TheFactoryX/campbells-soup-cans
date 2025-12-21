"""
Campbell's Soup Can #1071
Produced: 2025-12-21 02:30:29
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI escape codes for colors and styles
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

def typewriter(text, color=WHITE, delay=0.02, rnd_delay=False):
    for c in text:
        sys.stdout.write(color + c + RESET)
        sys.stdout.flush()
        if rnd_delay:
            time.sleep(delay * random.random() * 3)
        else:
            time.sleep(delay)
    print()

def main():
    os_name = sys.platform
    if os_name == "win32":
        print("This works best in Linux/Mac terminal!")

    # Text effects
    print("\n" * 2)
    typewriter(f"{BOLD}    *** Woody Allen's Cosmic Anxiety Hour ***{RESET}", MAGENTA, 0.03, True)
    print("\n" * 2)

    # ASCII art frame
    quote = [
        f"{BOLD}{CYAN}\"I've discovered the meaning of life,",
        "but the font was too small to read,",
        "and frankly, the conclusion seemed",
        "a bit rushed  - like God had",
        "a dinner reservation.{RESET}\""
    ]

    print(RED + "  " + "♥" * 58 + RESET)
    for i, line in enumerate(quote):
        time.sleep(0.3)
        colored_line = YELLOW + "  ♥ " + RESET + line.center(54) + YELLOW + " ♥ " + RESET
        typewriter(colored_line, delay=0.01 if i % 2 else 0.03)
    print(RED + "  " + "♥" * 58 + RESET)

    # Bottom text
    print("\n" * 2)
    typewriter(f"{UNDERLINE}Coming soon:{RESET} 'Existential Dread: The Musical'", WHITE, 0.05)
    typewriter("      (Lunchtime matinee performances only)", BLUE, 0.02)

    # Keep window open on Windows
    if os_name == "win32":
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()