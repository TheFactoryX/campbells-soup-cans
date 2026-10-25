"""
Campbell's Soup Can #5167
Produced: 2026-10-25 19:37:38
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
    # WOODY ALLEN-INSPIRED PHILOSOPHICAL QUOTE
    quote = "I’m not afraid of dying, but I’m terrified I’ll miss the part where God explains that being afraid of dying is the reason I’m alive at all."

    # COLOR SCHEME (Red, Green, Cyan, Yellow)
    colors = ['31', '32', '36', '33']  # ASCII codes for colors

    # ASCII ART (Anxious Question Mark with Glasses)
    def print_ascii():
        print("\n" + " " * 6 + ".,-:\"-.")
        print(" " * 6 + "|  o o  |")
        print(" " * 6 + "|   ^   |")
        print(" " * 5 + "/|  ___  |\\")
        print(" " * 4 + "//| '---' |\\\\")
        print(" " * 3 + "||/       |\\\\|")
        print(" " * 3 + "|/________\\__|")
        print(" " * 4 + "  |       |")
        print(" " * 4 + "  |       |")
        print(" " * 3 + "/         \\")
        print(" " * 3 + "---------------", end='')
        print("\033[F\" "\033[0m" * 12, end='')
        print()
        time.sleep(1)

    # COLOR FUNCTION
    def color_char(c, i):
        color_code = colors[i % len(colors)]
        return f"\033[{color_code}m{c}\033[0m"

    # BUILD COLORED BOX FRAME
    L = len(quote)
    box_top = '+' + '-' * (L + 4) + '+'
    box_bottom = '+' + '-' * (L + 4) + '+'

    # BUILD MIDDLE LINE WITH COLORED TEXT
    middle_line = '|  '
    for i, c in enumerate(quote):
        middle_line += color_char(c, i)
    middle_line += '  |'

    # EXECUTE VISUALS
    print_ascii()
    print("\033[K\033[2J", end='')  # Clear screen for drama
    print(box_top)
    print(middle_line)
    print(box_bottom)
    time.sleep(2)

    # DRAMATIC TWIST: CHAOS EFFECT
    def chaos():
        for char in "!?"*30:
            print(f"\033[35m{char}\033[0m", end='')
            time.sleep(0.1)
        print("\033[F\033[K")  # Erase last line

    chaos()
    print("\033[2J")  # Blackout again
    print("\033[35m\033[1mTHE MEANING OF LIFE:\033[0m")
    print(" " * 5 + "\033[35m" + quote + "\033[0m")

    time.sleep(3)
    print("\033[2J\033[H", end='')  # Final fade to black

if __name__ == "__main__":
    main()