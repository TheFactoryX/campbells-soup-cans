"""
Campbell's Soup Can #5203
Produced: 2026-11-03 15:08:45
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A single-file Woody Allen style philosophical quote machine."""
import sys
import time

# ANSI escape codes
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_ITALIC = "\033[3m"
C_CYAN = "\033[96m"
C_MAGENTA = "\033[95m"
C_YELLOW = "\033[93m"
C_GREEN = "\033[92m"
C_RED = "\033[91m"

QUOTE = (
    "I don't want to achieve immortality through my work. "
    "I want to achieve it through not dying. "
    "Unfortunately, my body hasn't signed the contract yet, "
    "and my lawyer is on vacation."
)


def typewriter(text, color=C_YELLOW, delay=0.045):
    """Print text one character at a time like an old typewriter."""
    sys.stdout.write(color + C_ITALIC)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(C_RESET + "\n")


def thinking_animation():
    """A tiny neurotic thinking loop."""
    frames = ["(  ́︵`  ) pondering...", "(  ́︵`  ) pondering..", "(  ́︵`  ) pondering."]
    for _ in range(3):
        for frame in frames:
            sys.stdout.write(C_MAGENTA + frame + C_RESET + "\r")
            sys.stdout.flush()
            time.sleep(0.3)
    sys.stdout.write(" " * 30 + "\r")
    sys.stdout.flush()


def main():
    width = 58

    print()
    print(C_CYAN + "╔" + "═" * width + "╗" + C_RESET)
    print(
        C_MAGENTA + C_BOLD
        + "║"
        + " A WOODY ALLEN MOMENT ".center(width)
        + "║"
        + C_RESET
    )
    print(C_CYAN + "╚" + "═" * width + "╝" + C_RESET)
    print()

    thinking_animation()

    print(C_GREEN + "WOODY ALLEN (probably, at 3 a.m.):" + C_RESET)
    print()

    typewriter('"' + QUOTE + '"', delay=0.05)

    print()
    print(C_YELLOW + "Existential dread serviced daily. Anxiety included at no extra charge." + C_RESET)
    print()

    couch = r"""
          ___
         /   \___
        |  [_   _]   <-- you, lying down
         \___/ \___
    """
    print(C_CYAN + couch + C_RESET)


if __name__ == "__main__":
    main()