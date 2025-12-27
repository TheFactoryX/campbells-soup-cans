"""
Campbell's Soup Can #1204
Produced: 2025-12-27 04:02:46
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors and effects
CYAN = "\033[36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"
CLEAR_SCREEN = "\033c"

# Our neurotic quote (original creation)
quote = [
    "I can't decide whether existence is terrifyingly absurd",
    "or absurdly terrifying. Then again, I couldn't decide",
    "what to order for lunch today either."
]

# Box dimensions
BOX_WIDTH = 66
BOX_TOP = CYAN + "╔" + "═" * BOX_WIDTH + "╗" + RESET
BOX_BOTTOM = CYAN + "╚" + "═" * BOX_WIDTH + "╝" + RESET
BOX_SIDE = CYAN + "║" + RESET

def type_effect(text, delay=0.03):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_centered(text, padded_length, color=YELLOW):
    """Center text within a padded area with color"""
    padded_text = text.center(padded_length)
    type_effect(color + padded_text + RESET)
    sys.stdout.flush()

def main():
    # Clear screen
    print(CLEAR_SCREEN, end="")

    # Print header with dramatic delay
    print(CYAN + "✨" + " WOODY ALLEN'S EXISTENTIAL PANIC SERVICE " + "✨\n" + RESET)
    time.sleep(1.2)

    # Start quote box
    print(BOX_TOP)
    
    # Print each centered line in the box
    padding = BOX_WIDTH - 2  # Account for side borders
    for i, line in enumerate(quote):
        sys.stdout.write(BOX_SIDE)
        print_centered(line, padding)
        print(BOX_SIDE)
        if i < len(quote)-1:
            time.sleep(0.4)  # Dramatic pause between lines
    
    print(BOX_BOTTOM)

    # Animated final flourish
    print("\n")
    for _ in range(3):
        for mood in ["😬", "😟", "🤔", "😖"]:
            sys.stdout.write(f"\r{mood}  Contemplating the void... ")
            sys.stdout.flush()
            time.sleep(0.3)
    
    print("\n\n" + CYAN + "(The meaning of life will arrive in 3-5 business days)" + RESET)

if __name__ == "__main__":
    main()