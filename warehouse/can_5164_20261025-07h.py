"""
Campbell's Soup Can #5164
Produced: 2026-10-25 07:35:41
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"


def color(text, code):
    return f"{code}{text}{RESET}"


def clear_screen():
    print("\033[2J\033[H", end="")


def type_char(ch, code):
    sys.stdout.write(f"{code}{ch}{RESET}")
    sys.stdout.flush()


def main():
    clear_screen()

    WIDTH = 60
    QUOTE = (
        "I'm not afraid of death. I just don't want to be there when it happens, "
        "especially if there's a co-pay, bad lighting, and no one to hold my hand."
    )

    # ASCII art: neurotic glasses + existential tie
    art = [
        "   _______     _______   ",
        "  /       \   /       \  ",
        " |  (O)   | |   (O)   | ",
        "  \   > < /   \   > < /  ",
        "   \_______/   \_______/ ",
        "           | |           ",
        "          /   \          ",
    ]

    print(color("╔" + "═" * WIDTH + "╗", CYAN))
    for line in art:
        print(color("║", CYAN) + line.center(WIDTH) + color("║", CYAN))
    print(color("╠" + "═" * WIDTH + "╣", CYAN))

    title = "A NEUROTIC PHILOSOPHICAL MOMENT"
    print(color("║", CYAN) + color(title.center(WIDTH), MAGENTA) + color("║", CYAN))
    byline = "— Woody Allen (Probably)"
    print(color("║", CYAN) + color(byline.center(WIDTH), MAGENTA) + color("║", CYAN))
    print(color("╠" + "═" * WIDTH + "╣", CYAN))

    wrapped = textwrap.wrap(QUOTE, WIDTH - 4)
    for line in wrapped:
        sys.stdout.write(color("║ ", CYAN))
        for ch in line:
            type_char(ch, YELLOW)
            time.sleep(0.015)
        padding = WIDTH - 4 - len(line)
        sys.stdout.write(" " * padding)
        sys.stdout.write(color(" ║", CYAN) + "\n")

    print(color("╠" + "═" * WIDTH + "╣", CYAN))
    footer = " (It's probably fine. Mostly. Probably.)"
    print(color("║", CYAN) + color(footer.center(WIDTH), GREEN) + color("║", CYAN))
    print(color("╚" + "═" * WIDTH + "╝", CYAN))

    print()


if __name__ == "__main__":
    main()