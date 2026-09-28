"""
Campbell's Soup Can #5039
Produced: 2026-09-28 22:02:15
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def main():
    quote = "I’m not sure if the universe is expanding or if it’s just avoiding my responsibilities."
    RESET = '\033[0m'
    CYAN = '\033[36m'
    YELLOW = '\033[93m'

    # Clear screen and move cursor to home
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

    inside_width = len(quote) + 2  # one space on each side of the quote
    # Top border
    sys.stdout.write(CYAN + '+' + '-' * inside_width + '+' + RESET + '\n')
    sys.stdout.flush()

    # Left border + space
    sys.stdout.write(CYAN + '| ' + RESET)
    # Typewriter effect for the quote in yellow
    for ch in quote:
        sys.stdout.write(YELLOW + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    # Right border + newline
    sys.stdout.write(CYAN + ' |' + RESET + '\n')
    sys.stdout.flush()

    # Bottom border
    sys.stdout.write(CYAN + '+' + '-' * inside_width + '+' + RESET + '\n')
    sys.stdout.flush()

    # Footer
    time.sleep(0.5)
    sys.stdout.write(YELLOW + "\n-- Woody Allen, probably\n" + RESET)
    sys.stdout.flush()

if __name__ == "__main__":
    main()