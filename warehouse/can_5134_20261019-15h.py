"""
Campbell's Soup Can #5134
Produced: 2026-10-19 15:36:32
Worker: MiniMax: MiniMax M3.1 Flash (free) (minimax/minimax-m3.1-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

PINK = "\033[95m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"


def gradient(text, colors):
    """Paint each character with a cheerful, existential color scheme."""
    return "".join(
        colors[index % len(colors)] + character + RESET
        for index, character in enumerate(text)
    )


def main():
    quote = (
        "“After a lifetime of searching, I’ve concluded that the meaning of life "
        "is to finish the crossword before the universe expires—and I still "
        "can’t spell ‘universe’ correctly.”"
    )

    content_width = 62
    quote_lines = textwrap.wrap(
        quote,
        width=content_width - 4,
        break_long_words=False,
        break_on_hyphens=False,
    )

    art = [
        "        .-'''-.        ",
        "       /  ?  ?  \\       ",
        "      |    __    |      ",
        "       \\  \\__/  /       ",
        "        '-...-'        ",
    ]

    print()
    for line in art:
        print(DIM + line + RESET)

    print("  " + gradient("✦  ·  ✧  ·  ✦", [PINK, YELLOW, CYAN, GREEN]))
    print()

    border_colors = [CYAN, BLUE, PINK, YELLOW]
    top_border = "╭" + "─" * content_width + "╮"
    bottom_border = "╰" + "─" * content_width + "╯"

    print(gradient(top_border, border_colors))

    quote_colors = [PINK, YELLOW, CYAN, GREEN, BLUE]
    for index, line in enumerate(quote_lines):
        padded_line = line.center(content_width)
        color = quote_colors[index % len(quote_colors)]
        print(
            CYAN
            + "│"
            + RESET
            + BOLD
            + color
            + padded_line
            + RESET
            + PINK
            + "│"
            + RESET
        )

    print(gradient(bottom_border, border_colors))
    print()


if __name__ == "__main__":
    main()