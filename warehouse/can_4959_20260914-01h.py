"""
Campbell's Soup Can #4959
Produced: 2026-09-14 01:05:48
Worker: Nex AGI: Nex-N2.5-Pro (free) (nex-agi/nex-n2.5-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import shutil
import sys
import time
from textwrap import wrap

RESET = "\033[0m"
QUOTE = (
    "\u201cI don't fear death; I fear the exit interview with the universe. "
    "It will ask what I learned, and I'll have to admit I mostly practiced "
    "worrying in different rooms.\u201d"
)
PALETTE = (
    "38;5;220", "38;5;214", "38;5;157",
    "38;5;81", "38;5;141", "38;5;147",
)


def paint(code, text):
    return f"\033[{code}m{text}{RESET}"


def rainbow(text, offset):
    pieces = []
    for index, char in enumerate(text):
        if char.isspace():
            pieces.append(char)
        else:
            pieces.append(paint(PALETTE[(index + offset) % len(PALETTE)], char))
    return "".join(pieces)


def starfield(frame, columns, box_left, box_right, rows=12):
    grid = [[" "] * columns for _ in range(rows)]
    glyphs = ("*", ".", "+", "\u2726")
    colors = ("38;5;245", "1;38;5;81", "38;5;229")

    for index in range(rows * 3):
        x = (index * 19 + frame * 5 + frame * index) % columns
        y = (index * 5 + frame // 2) % rows
        if box_left - 1 <= x <= box_right + 1:
            continue
        grid[y][x] = paint(colors[index % len(colors)], glyphs[index % len(glyphs)])

    return ["".join(row) for row in grid]


def get_layout():
    size = shutil.get_terminal_size((80, 24))
    columns = max(44, size.columns)
    wrap_width = max(32, min(columns - 10, 72))
    lines = wrap(
        QUOTE,
        width=wrap_width,
        break_long_words=False,
        break_on_hyphens=False,
    )
    width = max(len(line) for line in lines)
    box_left = max(2, (columns - width - 8) // 2)
    return size, lines, width, box_left


def render(step, total, lines, width, box_left, frame):
    size, _, _, _ = get_layout()
    columns = max(1, size.columns)
    height = max(1, size.lines)
    rows = max(1, min(14, height - 4))
    box_right = box_left + width + 2
    stars = starfield(frame, columns, box_left, box_right, rows)
    top_padding = max(0, (height - (len(lines) + 8)) // 2)

    print("\033[2J\033[H", end="")
    print("\n" * top_padding, end="")
    print(stars[0])
    print(" " * box_left + paint("1;38;5;81", "\u250c" + "\u2500" * (width + 2) + "\u2510"))

    visible = step
    for index, line in enumerate(lines):
        count = min(len(line), visible)
        visible -= count
        shown = rainbow(line[:count], frame)
        cursor = (
            paint("5;38;5;220", "\u2588")
            if step < total and visible == 0 and count < len(line)
            else ""
        )
        padding = width - len(line) - (1 if cursor else 0)
        print(
            " " * box_left
            + paint("38;5;81", "\u2502")
            + " "
            + shown
            + cursor
            + " " * padding
            + " "
            + paint("38;5;81", "\u2502")
        )

    print(" " * box_left + paint("1;38;5;81", "\u2514" + "\u2500" * (width + 2) + "\u2518"))
    remaining_rows = max(0, height - top_padding - len(lines) - 4)
    for row in stars[1:1 + remaining_rows]:
        print(row)
    sys.stdout.flush()


def main():
    _, lines, width, box_left = get_layout()
    total = len(QUOTE)

    print("\033[?25l", end="")
    try:
        for step in range(total + 1):
            render(step, total, lines, width, box_left, step // 2)
            time.sleep(0.012)

        for frame in range(12):
            render(total, total, lines, width, box_left, 20 + frame)
            time.sleep(0.07)

        render(total, total, lines, width, box_left, 40)
    finally:
        print(RESET + "\033[?25h", end="")
        sys.stdout.flush()


if __name__ == "__main__":
    main()