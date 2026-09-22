"""
Campbell's Soup Can #5004
Produced: 2026-09-22 04:57:37
Worker: Nex AGI: Nex-N2.5-Pro (free) (nex-agi/nex-n2.5-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import re
import shutil
import sys
import time

COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[31m",
    "yellow": "\033[33m",
    "green": "\033[32m",
    "cyan": "\033[36m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
}


def color(text, name):
    return f"{COLORS[name]}{text}{COLORS['reset']}"


def plain_len(text):
    return len(re.sub(r"\x1b\[[0-9;]*m", "", text))


def wrap(text, width):
    lines = []
    current = ""

    for word in text.split():
        candidate = word if not current else current + " " + word
        if plain_len(candidate) > width and current:
            lines.append(current)
            current = word
        else:
            current = candidate

    if current:
        lines.append(current)

    return lines


def paint(text):
    palette = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    out = []
    i = 0

    for ch in text:
        if ch.isspace() or ch in ".,;:!?—-":
            out.append(ch)
        else:
            out.append(color(ch, palette[i % len(palette)]))
            i += 1

    return "".join(out)


def type_line(text, speed=0.012):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    type_line("\n") if text != "\n" else None


def main():
    quote = "I don't fear the void; I fear the void has noticed me and is underwhelmed."

    term_width = shutil.get_terminal_size((80, 24)).columns
    inner_width = max(28, min(term_width - 8, 68))
    box_width = inner_width + 4
    lines = wrap(quote, inner_width)

    print()
    print(" " * ((term_width - 5) // 2) + color("?", "yellow"))
    print(" " * ((term_width - 7) // 2) + color("/\\", "yellow"))
    print(" " * ((term_width - 5) // 2) + color("O", "yellow"))
    print(" " * ((term_width - 7) // 2) + color("/|\\", "yellow"))
    print(" " * ((term_width - 7) // 2) + color("/ \\", "yellow"))
    print()

    type_line(color("╭" + "─" * (box_width - 2) + "╮", "cyan"))

    for line in lines:
        painted = paint(line)
        padding = inner_width - plain_len(line)
        type_line(color("│", "cyan") + " " + painted + " " * padding + " " + color("│", "cyan"))

    type_line(color("╰" + "─" * (box_width - 2) + "╯", "cyan"))
    print()
    print(" " * ((term_width - 30) // 2) + color("existential shrug detected", "dim"))


if __name__ == "__main__":
    main()