"""
Campbell's Soup Can #3908
Produced: 2026-06-11 01:40:21
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
A tiny, self‑contained one‑liner program that prints a Woody‑Allen‑style philosophical
quote with a bit of color and animation. No external dependencies—just plain
Python and ANSI escape sequences.
"""

import sys
import time
import random

# ──────────────────────  ANSI colour helpers  ──────────────────────
class ANSI:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    CYAN   = "\033[36m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    RED    = "\033[31m"

# ──────────────────────  The quote  ──────────────────────
QUOTE = (
    f"{ANSI.BOLD}{ANSI.CYAN}I walk around the world like an "
    f"{ANSI.MAGENTA}anonymous poet, unofficially consulting "
    f"{ANSI.YELLOW}ideas in a bottle—turning coffee "
    f"{ANSI.RED}mist into meaning, and feeling guilty "
    f"for every existential panic that "
    f"{ANSI.CYAN}inexactly fits my life outline.{ANSI.RESET}"
)

# ──────────────────────  Simple pattern “animation”  ──────────────────────
def animated_pulses(n_cycles=5, delay=0.1):
    """
    Print a quick pulsing dot animation to simulate a nervous heartbeat.
    """
    for _ in range(n_cycles):
        for phase in ("\\", "|", "/", "-"):
            sys.stdout.write(f"\r{ANSI.BOLD}{ANSI.YELLOW}{phase} {ANSI.RESET}")
            sys.stdout.flush()
            time.sleep(delay)

# ──────────────────────  Main routine  ──────────────────────
def main() -> None:
    # Clear the screen for a cleaner look
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Animated preamble
    animated_pulses()

    # Print the quote in a centered “card” style
    lines = QUOTE.splitlines()
    width = max(len(line) for line in lines)
    box_width = width + 6  # padding and borders

    border = f"{ANSI.BOLD}{ANSI.MAGENTA}{'┌' + '─' * (box_width - 2) + '┐'}{ANSI.RESET}"
    print(border)
    for line in lines:
        padded = line.ljust(width)
        print(f"{ANSI.MAGENTA}│  {ANSI.RESET}{padded} {ANSI.MAGENTA}│{ANSI.RESET}")
    print(f"{ANSI.MAGENTA}{'└' + '─' * (box_width - 2) + '┘'}{ANSI.RESET}")

    # Post‑quote flourish
    sys.stdout.write("\r")
    for _ in range(3):
        sys.stdout.write(f"{ANSI.YELLOW}✨  ")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()