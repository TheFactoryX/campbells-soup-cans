"""
Campbell's Soup Can #3406
Produced: 2026-04-22 22:05:05
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
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
A tiny, self‑contained script that prints a single
Woody‑Allen‑style philosophical one‑liner with a splash
of ANSI colors and a tiny “typewriter” animation.

Run it in a terminal that understands ANSI escape codes.
"""

import sys
import time

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"

# Some warm, slightly neurotic colours
COLORS = {
    "bg": "\033[48;5;237m",   # dark gray background
    "fg": "\033[38;5;215m",   # soft orange foreground
    "border": "\033[38;5;250m",  # light gray for the box
    "cursor": "\033[38;5;160m",  # red blinking cursor
}

# ----------------------------------------------------------------------
# The quote (feel free to replace with your own Woody‑Allen‑style line)
# ----------------------------------------------------------------------
QUOTE = (
    "I’m not afraid of death; I just don’t want to be there when "
    "it happens.  It feels like showing up late to my own funeral."
)

# ----------------------------------------------------------------------
# Helper to print text with a typewriter effect
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04) -> None:
    """Print `text` character‑by‑character."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ----------------------------------------------------------------------
# Build a simple box around the quote
# ----------------------------------------------------------------------
def boxed_text(text: str) -> str:
    lines = text.split("\n")
    width = max(len(line) for line in lines) + 4  # padding

    top = f"{COLORS['border']}╔{'═' * width}╗{RESET}"
    bottom = f"{COLORS['border']}╚{'═' * width}╝{RESET}"
    middle = []

    for line in lines:
        padded = line.ljust(width - 2)
        middle.append(f"{COLORS['border']}║ {COLORS['fg']}{padded}{COLORS['border']} ║{RESET}")

    return "\n".join([top] + middle + [bottom])

# ----------------------------------------------------------------------
# Main animation routine
# ----------------------------------------------------------------------
def main() -> None:
    # Clear the screen (ANSI clear)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Print background colour for the whole screen (optional)
    sys.stdout.write(COLORS["bg"])
    sys.stdout.flush()

    # Center the box vertically (roughly)
    terminal_height = 24
    empty_lines = "\n" * ((terminal_height // 2) - 4)
    sys.stdout.write(empty_lines)

    # Assemble the coloured box
    boxed = boxed_text(QUOTE)

    # Animate: show the box border first, then type the quote
    for line in boxed.split("\n"):
        if line.strip().startswith("║"):
            # Inside the box → typewriter effect (without the border chars)
            prefix, content, suffix = line[:2], line[2:-2], line[-2:]
            sys.stdout.write(prefix)
            sys.stdout.flush()
            typewriter(content, delay=0.02)
            sys.stdout.write(suffix + "\n")
        else:
            # Top / bottom border – print instantly
            sys.stdout.write(line + "\n")
        time.sleep(0.08)

    # Blinking cursor for a final neurotic touch
    for _ in range(6):
        sys.stdout.write(f"{COLORS['cursor']}_\r{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(" \r")
        sys.stdout.flush()
        time.sleep(0.3)

    # Reset colours before exiting
    sys.stdout.write(RESET)
    sys.stdout.flush()


if __name__ == "__main__":
    main()