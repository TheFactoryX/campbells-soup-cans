"""
Campbell's Soup Can #314
Produced: 2025-11-16 11:25:46
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful portrait of Woody Allen’s existential humor – in ASCII and color!
"""

import sys, time, random

# ANSI colour codes – vibrant, neurotic, Woody‑like palette
COLOURS = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[36m",  # cyan
]
RESET = "\033[0m"

def colour_text(text: str, colour: str) -> str:
    """Return the text wrapped in a colour escape sequence."""
    return f"{colour}{text}{RESET}"

def typing_coloured(text: str, delay: float = 0.04) -> None:
    """Print a string one character at a time, each in a random colour."""
    for ch in text:
        sys.stdout.write(colour_text(ch, random.choice(COLOURS)))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def main() -> None:
    # The quoted line – a Woody‑style riff on toast and meaning
    quote = (
        "I keep pondering life's big questions while I try not to burn my toast; "
        "both are equally meaningless if the toast turns to charcoal."
    )

    # ASCII illustration of a slightly burnt toast
    toast_art = [
        "     _____     ",
        "    /     \\    ",
        "__ /       \\ __ ",
        "||  o   o   ||  ",
        "||   ___    ||  ",
        "|| ( ___ )  ||  ",
        "\\_____/\\___/   ",
    ]

    # Print the toast slowly, each line in a different colour
    for line in toast_art:
        sys.stdout.write(colour_text(line, random.choice(COLOURS)) + "\n")
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write("\n" + RESET)
    sys.stdout.flush()
    time.sleep(0.3)

    # Box around the quote
    width = len(quote) + 4  # padding of 2 spaces on each side
    top_border = "+" + "-" * width + "+"
    quote_line = "|  " + quote + "  |"
    bottom_border = top_border

    # Print the top border
    print(colour_text(top_border, random.choice(COLOURS)))

    # Print the quote line with a typing animation
    typing_coloured(quote_line)

    # Print the bottom border
    print(colour_text(bottom_border, random.choice(COLOURS)))

if __name__ == "__main__":
    main()