"""
Campbell's Soup Can #3928
Produced: 2026-06-13 20:40:36
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RESET = '\033[0m'
CYAN = '\033[96m'
YELLOW = '\033[93m'

# Woody Allen style philosophical quote
QUOTE = "I don't fear death; I fear the paperwork that comes with it. Also, the waiting room. And the terrible magazines."

def animate_text(text, color=YELLOW, delay=0.05):
    """Prints text character by character with a typing effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def create_woody_quote():
    """Creates a visually interesting quote box"""
    max_length = len(QUOTE)
    
    # Top border
    print(CYAN + "╔" + "═" * (max_length + 2) + "╗" + RESET)
    
    # Animated quote line
    print(CYAN + "║ " + RESET, end='')
    animate_text(QUOTE, YELLOW, 0.04)
    print(CYAN + " ║" + RESET)
    
    # Bottom border
    print(CYAN + "╚" + "═" * (max_length + 2) + "╝" + RESET)

if __name__ == "__main__":
    create_woody_quote()