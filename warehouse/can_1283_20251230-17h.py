"""
Campbell's Soup Can #1283
Produced: 2025-12-30 17:35:42
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI escape codes for colors and styles
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
GREEN = "\033[1;92m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

def typewriter(text, color=YELLOW, delay=0.05):
    """Prints text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_quote():
    # Build the ASCII art box with colors
    box_top = CYAN + r'''
   ╔════════════════════════════════════════════════════╗
   ║''' + RESET
    box_bottom = CYAN + r'''   ╟────────────────────────────────────────────────────────────╢
   ║''' + GREEN + ITALIC + "       - Woody Allen's overthinking while brushing teeth      " + RESET + CYAN + '''║
   ╚════════════════════════════════════════════════════╝
    ''' + RESET

    # The neurotic quote
    quote = (
        "Life is absolutely terrifying and meaningless, which would be \n"
        "liberating if it didn't mean there's no good reason\n"
        "to eat dessert first—but now I'm paralyzed by the freedom!\n"
        "What if I choose poorly? What if the tiramisu judges me?"
    )

    parts = quote.split('\n')
    
    # Print the box top
    print('\n\n' + box_top)
    
    # Print each line with typewriter effect
    for i, part in enumerate(parts):
        sys.stdout.write(CYAN + "   ║ " + RESET)
        typewriter(part.rstrip(), ITALIC + YELLOW, delay=0.03)
        if i < len(parts)-1:
            sys.stdout.write(CYAN + "   ║ " + RESET + " " * len(part) + "\r" + CYAN + "   ║ " + RESET)
    
    # Print the box bottom
    print(box_bottom)

    # Add some dramatic pauses
    time.sleep(0.5)
    print(RED + "\n     [ Neurotic sweat droplets appear ]" + RESET)
    time.sleep(1)
    print(BOLD + "         (Why is existence so moist?)" + RESET)

if __name__ == "__main__":
    print_quote()