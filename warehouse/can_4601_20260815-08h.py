"""
Campbell's Soup Can #4601
Produced: 2026-08-15 08:45:11
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def main():
    print('\n\x1b[31m' + '+' + '-' * 36 + '+')
    lines = [
        "I'm terrified of life.",
        "Death is scarier.",
        "50/50 chance: boredom or embarrassment.",
        "Why take the risk?"
    ]
    colors = [(32, 31), (33, 34), (36, 35), (93, 32)]
    max_len = 36

    for (line_color, border), line in zip(colors, lines):
        time.sleep(0.4)
        padded = '\x1b[' + str(border) + 'm' + line.ljust(max_len) + '\x1b[0m'
        sys.stdout.write(f"| {padded} |\n")
    print('\x1b[31m' + '+' + '-' * 36 + '+')

    # Post-quote flourish with ASCII art
    print('\n\x1b[36m☕\x1b[0m  Life is a tragedy for thinkers, \n    and a comedy for tripping philosophers.\n\n\x1b[33m    )_(    )_(    )_(\n    // \\\\/ \\\\\\\\  \x1b[0m\n\n\x1b[31mDeath: The only sequel that's actually worse than the original.\x1b[0m')

if __name__ == "__main__":
    main()