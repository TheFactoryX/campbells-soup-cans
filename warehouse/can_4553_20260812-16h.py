"""
Campbell's Soup Can #4553
Produced: 2026-08-12 16:11:03
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def typewriter(text, color, delay=0.05):
    """Print text character‑by‑character with a given ANSI color."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\033[0m')  # reset color

def main():
    # ANSI color codes
    CYAN    = '\033[36m'
    YELLOW  = '\033[33m'
    RESET   = '\033[0m'

    # Woody Allen‑style quote (original)
    quote = "I spend my life worrying about things that haven't happened yet, which is why I'm already tired."

    # Box dimensions
    inner_width = len(quote) + 2          # one space each side
    top_border    = '╔' + '═' * inner_width + '╗'
    bottom_border = '╚' + '═' * inner_width + '╝'
    side_border   = '║'

    # Clear screen and move cursor to home
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

    # Draw top border
    print(CYAN + top_border + RESET)

    # Left border, quoted text (typewriter effect), right border
    sys.stdout.write(CYAN + side_border + RESET)
    typewriter(quote, YELLOW, 0.07)
    sys.stdout.write(CYAN + side_border + RESET + '\n')

    # Draw bottom border
    print(CYAN + bottom_border + RESET)

if __name__ == "__main__":
    main()