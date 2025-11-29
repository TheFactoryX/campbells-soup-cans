"""
Campbell's Soup Can #610
Produced: 2025-11-29 22:33:01
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
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
A whimsical, color‑rich, animated quote generator in the style of Woody Allen.
"""

import sys
import time
import textwrap

# ANSI colour codes
BOLD   = "\033[1m"
CYAN   = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET  = "\033[0m"

def clear_screen() -> None:
    """Clear terminal screen."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def typewriter(text: str, delay: float = 0.035) -> None:
    """Print text one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def boxed_quote(quote: str, max_width: int = 60, delay: float = 0.02) -> None:
    """Print a coloured, boxed, typewriter–style quote."""
    # Prepare wrapped lines
    lines = textwrap.wrap(quote, width=max_width)
    width  = max(len(line) for line in lines)

    # Top border
    sys.stdout.write(YELLOW + "+" + "-" * (width + 4) + "+" + RESET + "\n")

    # Each line: left border, content, right border
    for line in lines:
        padded = "  " + line.ljust(width) + "  "   # two spaces padding
        sys.stdout.write(YELLOW + "|" + RESET + CYAN)
        for ch in padded:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(RESET + YELLOW + "|" + RESET + "\n")

    # Bottom border
    sys.stdout.write(YELLOW + "+" + "-" * (width + 4) + "+" + RESET + "\n")

def main() -> None:
    clear_screen()

    # Introductory flourish
    intro = "Preparing your dose of existential dread..."
    typewriter(BOLD + CYAN + intro + RESET)
    sys.stdout.write("\n\n")
    time.sleep(0.3)

    # The Woody Allen‑style philosophical gem
    quote = (
        "I talk to my existential crisis like a therapist; "
        "it mostly takes me to therapy too."
    )
    boxed_quote(quote)

if __name__ == "__main__":
    main()