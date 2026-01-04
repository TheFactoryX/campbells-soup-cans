"""
Campbell's Soup Can #1377
Produced: 2026-01-04 02:39:47
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI escape codes for colors
YELLOW = "\033[33m"
CYAN = "\033[36m"
RED = "\033[31m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, color=YELLOW, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    quote = (
        "I've wrestled with existential dread my whole life - \n"
        "which would be more impressive if it wasn't mostly \n"
        "about whether to get soup. What if the soup is bad?\n"
        "What if it's too hot? What if it outlives me?"
    )

    # ASCII art frame
    print(CYAN + "╔" + "═" * 58 + "╗" + RESET)
    print(CYAN + "║" + " " * 58 + "║" + RESET)
    typewriter_effect("║    " + quote.replace("\n", "\n║    "))
    print(CYAN + "║" + " " * 58 + "║" + RESET)
    print(CYAN + "╚" + "═" * 58 + "╝" + RESET)
    
    # Bouncing author credit
    time.sleep(1)
    spaces = 0
    direction = 1
    for _ in range(30):
        print("\033[F" + " " * 60, end="\r")  # Move cursor up and clear line
        print(" " * spaces + RED + "– Woody Allen" + RESET)
        spaces += direction
        if spaces >= 20 or spaces <= 0:
            direction *= -1
        time.sleep(0.08)
    
    print("\n")

if __name__ == "__main__":
    main()