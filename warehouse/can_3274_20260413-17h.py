"""
Campbell's Soup Can #3274
Produced: 2026-04-13 17:19:35
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, colorful, animated display of a Woody‑Allen‑style philosophical quote.
Run it in a terminal that understands ANSI escape codes.
"""

import sys
import time
import itertools

# ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"

FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}
BG = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
}


def center(text: str, width: int) -> str:
    """Return `text` centered in a field of `width`."""
    return text.center(width)


def typewriter(message: str, delay: float = 0.04) -> None:
    """Print `message` one character at a time."""
    for ch in message:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def rainbow_cycle():
    """Yield an infinite cycle of foreground colours."""
    colors = itertools.cycle([FG["red"], FG["yellow"], FG["green"],
                              FG["cyan"], FG["blue"], FG["magenta"]])
    while True:
        yield next(colors)


def main() -> None:
    quote = (
        "I think the meaning of life is to find something you're "
        "passionate about, then dread it the whole time you have to do it."
    )

    # Box dimensions
    width = max(len(line) for line in quote.split("\n")) + 6
    height = 5

    # Build the static parts of the box
    top = f"{FG['cyan']}╔{'═' * (width - 2)}╗{RESET}"
    bottom = f"{FG['cyan']}╚{'═' * (width - 2)}╝{RESET}"
    empty = f"{FG['cyan']}║{' ' * (width - 2)}║{RESET}"

    # Print the box with a simple fade‑in effect
    sys.stdout.write("\n")
    for line in [top, empty, empty, empty, bottom]:
        sys.stdout.write(line + "\n")
        time.sleep(0.1)

    # Overwrite the empty line with the quote, animated character‑by‑character
    # and colour‑cycling the text.
    quote_lines = [quote[i : i + width - 6] for i in range(0, len(quote), width - 6)]
    start_row = 3  # third row inside the box (1‑based)

    # Move cursor up to the line we want to replace
    sys.stdout.write(f"\033[{height - start_row + 1}A")  # up
    sys.stdout.flush()

    colour_gen = rainbow_cycle()
    for i, qline in enumerate(quote_lines):
        # Colour the whole line with the next rainbow colour
        colour = next(colour_gen)
        padded = center(qline, width - 6)
        content = f"{FG['cyan']}║ {colour}{padded}{RESET}{FG['cyan']} ║{RESET}"
        typewriter(content, delay=0.02)
        if i < len(quote_lines) - 1:
            # Move cursor down to the next inner line
            sys.stdout.write("\n")
    # Return cursor to the line after the box
    sys.stdout.write(f"\033[{height - start_row}B")  # down
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)