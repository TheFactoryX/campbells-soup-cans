"""
Campbell's Soup Can #5074
Produced: 2026-10-06 21:38:01
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time

def make_border(width, color):
    return f"\033[{color}m+{'-' * width}+\033[0m"

def make_line(text, width, text_color, border_color):
    inner = text.ljust(width - 2)
    return f"\033[{border_color}m| \033[{text_color}m{inner}\033[{border_color}m |\033[0m"

def main():
    GREEN = "1;32"
    YELLOW = "1;33"
    CYAN = "1;36"

    quote = [
        "\"I'm not afraid of the meaning of life; I just don't want",
        "to be the one who has to ask the question when the lights",
        'go out."'
    ]

    width = 78

    title = "Woody's Existential One-Liner"
    print(f"\033[{GREEN}m{title.center(width)}\033[0m")
    print()

    print(make_border(width, GREEN))
    for line in quote:
        print(make_line(line, width, YELLOW, GREEN))
        time.sleep(0.3)
    print(make_border(width, GREEN))

    closing = "...or at least until the next coffee break."
    print(f"\033[{CYAN}m{closing.center(width)}\033[0m")
    print()

if __name__ == "__main__":
    main()