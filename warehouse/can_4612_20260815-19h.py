"""
Campbell's Soup Can #4612
Produced: 2026-08-15 19:33:53
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

# ANSI color codes
RESET = '\033[0m'
BORDER = '\033[36m'   # cyan
QUOTE = '\033[33m'    # yellow

# Woody Allen‑style philosophical quote (original)
QUOTE_TEXT = "I would love to be immortal, but only if I don't have to answer emails."

def main():
    # Calculate box width (quote + two side spaces + two border stars)
    width = len(QUOTE_TEXT) + 4
    top_bottom = BORDER + '*' * width + RESET

    # Draw top border
    print(top_bottom)

    # Left border
    sys.stdout.write(BORDER + '*' + RESET)
    sys.stdout.write(' ')  # inner left space

    # Type the quote character by character with a small delay
    for ch in QUOTE_TEXT:
        sys.stdout.write(QUOTE + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.05)

    # Inner right space and right border
    sys.stdout.write(' ')
    sys.stdout.write(BORDER + '*' + RESET + '\n')

    # Draw bottom border
    print(top_bottom)

if __name__ == '__main__':
    main()