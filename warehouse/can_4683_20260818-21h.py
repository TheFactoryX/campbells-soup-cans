"""
Campbell's Soup Can #4683
Produced: 2026-08-18 21:38:05
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote, served with ANSI colors and ASCII flair."""

import textwrap

# ANSI escape codes for colors (reset included)
C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_MAGENTA = "\033[95m"
R = "\033[0m"


def clr(color, text):
    """Print `text` in `color`, then reset terminal styling."""
    print(f"{color}{text}{R}")


def boxed_quote(q, width=55, border_color=C_YELLOW):
    """Display a quote inside a minimalist colorful box."""
    clr(border_color, "┌" + "─" * (width + 2) + "┐")
    for line in textwrap.wrap(q, width=width):
        print(f"│ {line.ljust(width)} │")
    clr(border_color, "└" + "─" * (width + 2) + "┘")


# Woody’s neurotic, existential, delightfully funny one-liner:
QUOTE = (
    "I'm not afraid of death. I just don't want to be there when it happens. "
    "Also, if there's an afterlife, I hope there's free coffee and a strong "
    "Wi‑Fi signal. I have existential essays to finish."
)

# Tiny ASCII "neurotic thinker"
ART = r"""
   .---.
  / o o \
  ^^ ^^
 /------\
/ |    | \
(_|      |_)
    | |
   /_\
"""

if __name__ == "__main__":
    # Header
    clr(C_CYAN, "  ☢︎  WOODY'S PHILOSOPHICAL QUIRK  ☢︎  ")
    print()

    # ASCII art in calm green
    clr(C_GREEN, ART)
    print()

    # The quote in a sunny yellow box
    boxed_quote(QUOTE)

    print()

    # Footer – because every good neurotic needs a exit sign
    clr(C_MAGENTA, " — End of Transmission — ")
    clr(C_MAGENTA, " (Don't forget to breathe. Or not. Whatever.) ")