"""
Campbell's Soup Can #5135
Produced: 2026-10-19 21:03:33
Worker: MiniMax: MiniMax M3.1 Flash (free) (minimax/minimax-m3.1-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import shutil
import sys
import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
REVERSE = "\033[7m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
WHITE = "\033[97m"

RAINBOW = (MAGENTA, BLUE, CYAN, YELLOW)


def paint(text, *styles, enabled=True):
    if not enabled or not styles:
        return text
    return "".join(styles) + text + RESET


def gradient_border(character, count, enabled):
    if not enabled:
        return character * count
    return "".join(
        f"{RAINBOW[index % len(RAINBOW)]}{character}{RESET}"
        for index in range(count)
    )


def center(text, width):
    padding = max(0, width - len(text))
    left = padding // 2
    return " " * left + text + " " * (padding - left)


def main():
    use_color = (
        sys.stdout.isatty()
        or "FORCE_COLOR" in os.environ
    ) and "NO_COLOR" not in os.environ

    quote = (
        "I spent years looking for the meaning of life, only to discover "
        "it was in the laundry, waiting to be folded."
    )

    terminal_width = shutil.get_terminal_size((80, 24)).columns
    quote_width = max(20, min(66, terminal_width - 8))
    lines = textwrap.wrap(
        quote,
        width=quote_width,
        break_long_words=False,
        break_on_hyphens=False,
    )

    inner_width = max(len(line) for line in lines)
    box_width = inner_width + 4

    art = [
        "             ?",
        "          .-----.",
        "         /  o o  \\",
        "        |    ^    |",
        "         \\  \\ /  /",
        "          '-----'",
        "             ||",
        "          __/||\\__",
        "         /    ||    \\",
    ]

    print()
    print(center(paint("THE EXISTENTIAL LAUNDRY", REVERSE, BOLD, MAGENTA,
                       enabled=use_color), box_width))
    print()

    for index, line in enumerate(art):
        color = MAGENTA if index == 0 else YELLOW
        print(center(paint(line, color, enabled=use_color), box_width))

    print()
    print(" " * 2 + paint("╲" + " " * (box_width - 2) + "╲", DIM,
                          enabled=use_color))
    print(paint("╭", MAGENTA, enabled=use_color)
          + gradient_border("─", inner_width + 2, use_color)
          + paint("╮", MAGENTA, enabled=use_color))

    line_colors = (YELLOW, WHITE, CYAN)
    for index, line in enumerate(lines):
        body = paint(
            line,
            BOLD,
            line_colors[index % len(line_colors)],
            enabled=use_color,
        )
        padding = " " * (inner_width - len(line))
        print(
            paint("│ ", MAGENTA, enabled=use_color)
            + body
            + padding
            + paint(" │", MAGENTA, enabled=use_color)
        )

    print(paint("╰", MAGENTA, enabled=use_color)
          + gradient_border("─", inner_width + 2, use_color)
          + paint("╯", MAGENTA, enabled=use_color))
    print(" " * 2 + paint(" " * (box_width - 1) + "╲", DIM,
                          enabled=use_color))
    print()
    print(center(paint("a small revelation from the laundry department",
                       DIM, CYAN, enabled=use_color), box_width))
    print()


if __name__ == "__main__":
    main()