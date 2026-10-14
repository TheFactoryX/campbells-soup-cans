"""
Campbell's Soup Can #5106
Produced: 2026-10-14 17:11:05
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def colorize(line, color_code):
    return f"\033[1;{color_code}m{line}\033[0m"

def main():
    quote = [
        ("I'm not afraid of death,", 31),
        ("but I'm afraid of not dying,", 36),
        ("which implies I might actually die,", 32),
        ("and then, of course,", 33),
        ("why would I be afraid of something that's inevitable?", 34)
    ]

    max_length = max(len(line) for line, _ in quote)
    box_width = max_length + 4

    border = '+' + '-'*(box_width - 2) + '+'

    print("\033[35m          .-''-.")
    print("\033[34m       /  .-. \\")
    print("\033[34m      / /   \\ \\")
    print("\033[36m     / /     \\ \\")
    print("\033[36m    / /       \\ \\")
    print("\033[35m   |_ _ _ _ _ _|")
    print("\033[0m")
    time.sleep(2)

    print(colorize(border, 37))
    time.sleep(0.3)

    for text, color in quote:
        centered = text.center(box_width - 2)
        line = f"|{centered}|"
        print(colorize(line, color))
        time.sleep(0.5)

    time.sleep(0.5)
    print(colorize(border, 37))

if __name__ == "__main__":
    main()