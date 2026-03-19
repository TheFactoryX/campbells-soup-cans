"""
Campbell's Soup Can #2852
Produced: 2026-03-19 19:54:46
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

pythonimport sys
import time
import random

# ANSI color codes
COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",
    "bold": "\033[1m",
}


def type_print(text: str, delay: float = 0.04, color: str = "") -> None:
    """Print text character‑by‑char with optional color."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(COLORS["reset"] + "\n")
    sys.stdout.flush()


def boxed_quote(quote: str, padding: int = 2) -> list[str]:
    """Return a list of lines forming a colored box around the quote."""
    width = len(quote) + 2 * padding
    top_bottom = "+" + "-" * width + "+"
    empty = "|" + " " * width + "|"
    quote_line = f"|{' ' * padding}{quote}{' ' * padding}|"
    return [top_bottom, empty, quote_line, empty, top_bottom]


def main() -> None:
    # Woody Allen‑style quote (original)
    quote = (
        "I’m not sure if the universe is expanding or if my motivation is just shrinking."
    )

    # Choose random colors for box and text
    box_color = random.choice(
        [COLORS["cyan"], COLORS["magenta"], COLORS["yellow"], COLORS["green"]]
    )
    text_color = random.choice(
        [COLORS["white"], COLORS["bold"] + COLORS["white"], COLORS["yellow"]]
    )

    # Clear screen (ANSI)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Build and display the box line‑by‑line with a slight typing effect
    lines = boxed_quote(quote)
    for line in lines:
        if line.startswith("|") and quote in line:
            # This is the actual quote line – type it out
            type_print(line, delay=0.05, color=box_color + text_color)
        else:
            # Borders – just print instantly
            print(box_color + line + COLORS["reset"])
            time.sleep(0.1)


if __name__ == "__main__":
    main()