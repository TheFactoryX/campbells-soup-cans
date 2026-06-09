"""
Campbell's Soup Can #3900
Produced: 2026-06-09 22:51:01
Worker: Nex AGI: Nex-N2-Pro (free) (nex-agi/nex-n2-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import shutil

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
GRAY = "\033[90m"

QUOTE = (
    "I asked the universe for meaning, and it sent me a parking ticket; "
    "so I guess existence is just bureaucracy with better lighting, "
    "and I’m the guy who forgot to renew the soul permit."
)


def typewriter(text, delay=0.025):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def centered_box(lines, width):
    width = max(width, max(len(line) for line in lines) + 4)
    top = "╭" + "─" * (width - 2) + "╯"
    bottom = "╰" + "─" * (width - 2) + "╯"
    print(CYAN + top + RESET)
    for line in lines:
        print(CYAN + "│" + RESET + line.center(width - 2) + CYAN + "│" + RESET)
    print(CYAN + bottom + RESET)


def main():
    terminal_width = shutil.get_terminal_size().columns
    width = min(max(terminal_width - 4, 44), 86)

    print()
    print("            " + MAGENTA + "✦" + RESET + "  " + CYAN + "tiny existential kiosk" + RESET + "  " + MAGENTA + "✦" + RESET)
    print(GRAY + "           opening drawer labeled: cosmic anxiety" + RESET)
    print()

    print("        " + MAGENTA + ".,,_,,." + RESET)
    print("       " + MAGENTA + "( o   o )" + RESET + "  " + CYAN + "staring into the void" + RESET)
    print("        " + MAGENTA + "\\  ^  /" + RESET + "  " + CYAN + "and finding it understocked" + RESET)
    print("         " + MAGENTA + "\\___/" + RESET)
    print()

    wrapped = []
    current = ""
    for word in QUOTE.split():
        test = (current + " " + word).strip()
        if len(test) <= width - 6:
            current = test
        else:
            wrapped.append(current)
            current = word
    if current:
        wrapped.append(current)

    colorful_lines = []
    for i, line in enumerate(wrapped):
        color = [CYAN, YELLOW, MAGENTA][i % 3]
        colorful_lines.append(color + line + RESET)

    print()
    centered_box(colorful_lines, width)
    print()
    print(GRAY + "           " + BOLD + "moral:" + RESET + " if life is a joke, at least I’m the punchline with receipts." + RESET)


if __name__ == "__main__":
    main()