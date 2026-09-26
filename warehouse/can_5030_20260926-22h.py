"""
Campbell's Soup Can #5030
Produced: 2026-09-26 22:52:37
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A neurotic, colorful Woody Allen-style philosophical quote."""

# ANSI escape codes for colors
RESET = "\033[0m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
WHITE = "\033[37m"

# The raw quote text (no ANSI embedded, so formatting stays clean)
QUOTE = (
    "I'm not afraid of death\n"
    "just afraid it'll happen while I'm worrying\n"
    "about whether I locked the door\n"
    "and the afterlife has terrible lighting"
)

BOX_WIDTH = 60


def colorful_box(text, width=BOX_WIDTH, text_color=CYAN, border_color=BOLD + CYAN):
    """Print text inside a colorful ASCII ANSI-box."""
    border = border_color + "+" + "-" * width + RESET
    lines = text.split("\n")
    rows = [border]
    for line in lines:
        padded = line.ljust(width - 2)
        row = border_color + "|" + RESET + text_color + padded + RESET + border_color + "|" + RESET
        rows.append(row)
    rows.append(border)
    return "\n".join(rows)


if __name__ == "__main__":
    print(colorful_box(QUOTE))
    print(f"{YELLOW}            philosophy served with a neurotic smile{RESET}")