"""
Campbell's Soup Can #4958
Produced: 2026-09-13 22:24:40
Worker: Nex AGI: Nex-N2.5-Pro (free) (nex-agi/nex-n2.5-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import shutil
import sys
import time

CYAN = "36"
BLUE = "34"
GOLD = "33"
DIM = "90"
RESET = "0"

QUOTE = (
    "The universe is vast, mysterious, and almost certainly indifferent to my "
    "suffering, which is comforting—my dentist is also indifferent, but somehow "
    "much more judgmental."
)


def paint(text, color):
    if sys.stdout.isatty():
        return f"\033[{color}m{text}\033[{RESET}m"
    return text


def pulse_dots():
    for count in (1, 2, 3, 4, 3, 2):
        sys.stdout.write("\r" + " " * 17 + paint("." * count, CYAN))
        sys.stdout.flush()
        time.sleep(0.18)


def wrap_text(text, width):
    lines = []
    current = ""
    for word in text.split():
        candidate = word if not current else current + " " + word
        if len(candidate) > width:
            if current:
                lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def typewrite_line(text, width):
    sys.stdout.write("| ")
    sys.stdout.flush()
    for character in text:
        sys.stdout.write(paint(character, GOLD))
        sys.stdout.flush()
        time.sleep(0.012)
    sys.stdout.write(" " * (width - len(text)) + " |")


def main():
    if sys.stdout.isatty():
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    try:
        print()
        pulse_dots()
        sys.stdout.write("\r" + " " * 18 + paint("!", BLUE) + "\n")
        print(
            paint(
                r"""
                 .   .   .
             .---------------.
            /   ?   ?   ?    \
           |   ?   ?   ?     |
            \---------------/
                  (O)
                 _/|\_
                 /   \
""",
                CYAN,
            )
        )

        columns = shutil.get_terminal_size((80, 24)).columns
        width = max(42, min(82, columns - 6))
        lines = wrap_text(QUOTE, width)
        border = "+" + "-" * (width + 2) + "+"

        print(paint(border, DIM))
        for line in lines:
            typewrite_line(line, width)
            print()
        print(paint(border, DIM))
        print(paint("        \\___________________________/", DIM))
    finally:
        if sys.stdout.isatty():
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()


if __name__ == "__main__":
    main()