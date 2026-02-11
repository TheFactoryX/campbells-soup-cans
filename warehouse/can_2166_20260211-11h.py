"""
Campbell's Soup Can #2166
Produced: 2026-02-11 11:58:28
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Woody Allen meets Python: a colorful, animated philosophical quote.
Pure Python, no external dependencies.
"""

import sys
import time
import random

# ----- ANSI colour helpers -------------------------------------------------
FG_RESET = "0"
FG_BLACK = "30"
FG_RED   = "31"
FG_GREEN = "32"
FG_YELLOW= "33"
FG_BLUE  = "34"
FG_MAGENTA= "35"
FG_CYAN = "36"
FG_WHITE = "37"
FG_BOLD  = "1"   # optional bold prefix

def set_color(fg: str) -> str:
    """Return the ANSI escape code for the given foreground colour."""
    return f"\033[{fg}m"

def reset_color() -> str:
    """Return the ANSI escape code to reset all attributes."""
    return f"\033[{FG_RESET}m"

def colour(text: str, fg: str) -> str:
    """Wrap *text* with the colour *fg* and a reset."""
    return set_color(fg) + text + reset_color()


# ----- Visual helpers ------------------------------------------------------
def random_header() -> str:
    """Print a bold (ish) coloured headline."""
    colours = [
        FG_BLACK, FG_RED, FG_GREEN, FG_YELLOW,
        FG_BLUE, FG_MAGENTA, FG_CYAN, FG_WHITE,
    ]
    fg = random.choice(colours)
    # Occasionally make it bold for extra flair
    if random.random() < 0.3:
        prefix = set_color(FG_BOLD)
    else:
        prefix = ""
    return prefix + colour(
        "Woody Allen's Existential Thoughts",
        fg
    )


def typewriter(line: str, fg: str = FG_WHITE, speed: float = 0.03) -> None:
    """
    Type a line character‑by‑character using \r (carriage return).
    Each character appears in the supplied foreground colour.
    """
    for i, ch in enumerate(line):
        sys.stdout.write(f"\r{colour(line[:i+1], fg)}")
        sys.stdout.flush()
        time.sleep(random.uniform(speed*0.5, speed*1.2))
    # Final newline so the next text starts fresh
    sys.stdout.write("\n")
    time.sleep(random.uniform(0.05, 0.1))


# ----- Main routine --------------------------------------------------------
def main() -> None:
    # Title – colourful and a little unpredictable
    print(random_header())

    # A tiny ASCII “wine glass” that evokes Woody’s classic props
    wine_art = [
        "   ___   ___   ___   ___",
        "  /__\\ /__\\ /__\\ /__\\",
        "  |   | |   | |   | |   |",
        "  \\___/ \\___/ \\___/ \\___/",
        "   \\   /\\   /\\   /\\   /",
        "    \\ /  \\ /  \\ /  \\ / ",
        "    /\\   /\\   /\\   /\\ ",
        "   /  \\ /  \\ /  \\ /  \\",
    ]
    for line in wine_art:
        print(line)

    # Give the brain a second to catch up
    time.sleep(random.uniform(0.5, 1.0))

    # Woody Allen‑style philosophical quote – typed slowly
    quote = [
        "I'm not afraid of death;",
        "I just don't want to be there when it happens.",
        "",
        "Life is full of misery, loneliness, and suffering—",
        "and it's all over much too soon.",
        "",
        "I don't want to achieve immortality through my work;",
        "I want to achieve it through not dying."
    ]

    # Shuffle colours for each line (makes the animation lively)
    line_colours = [
        random.choice([FG_RED, FG_GREEN, FG_YELLOW,
                      FG_BLUE, FG_MAGENTA, FG_CYAN, FG_WHITE])
        for _ in quote
    ]

    for line, fg in zip(quote, line_colours):
        typewriter(line, fg)

    # Final one‑liner fades out like an existential‑dread marquee
    fade = "   (Ctrl+C to escape before the dread hits you.)"
    for ch in fade:
        sys.stdout.write(f"\r{colour(ch, FG_YELLOW)}")
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")

    # A tiny breather before the script exits
    time.sleep(0.5)


if __name__ == "__main__":
    main()