"""
Campbell's Soup Can #4421
Produced: 2026-08-03 07:46:24
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

quote = "I'm not afraid of the void; I just wish it had better Wi‑Fi."

def typewriter_quote(text):
    """Print the quote with a typewriter effect inside a colored box."""
    sys.stdout.write('\033[96m║\033[0m ')  # left border + space
    for ch in text:
        sys.stdout.write('\033[93m' + ch + '\033[0m')  # yellow text
        sys.stdout.flush()
        time.sleep(0.07)  # typing speed
    print(' \033[96m║\033[0m')  # space + right border

def main():
    # Dynamic box width based on quote length (+2 for the inner spaces)
    inner_width = len(quote) + 2
    horizontal = '═' * inner_width
    top_box    = f'\033[96m╔{horizontal}╗\033[0m'
    bottom_box = f'\033[96m╚{horizontal}╝\033[0m'

    print(top_box)
    typewriter_quote(quote)
    print(bottom_box)

if __name__ == "__main__":
    main()