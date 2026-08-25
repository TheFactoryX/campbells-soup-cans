"""
Campbell's Soup Can #4843
Produced: 2026-08-25 22:45:01
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen-style philosophical quote, served with Python ANSI colors."""
import time, sys

QUOTE = (
    "I do not want to achieve immortality through my work. "
    "I just want to exit gracefully before the universe forces "
    "me to debug the afterlife."
)

# ANSI color palette (bright xterm-256)
C = {
    "reset": "\033[0m",
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "red": "\033[91m",
    "bold": "\033[1m",
}


def typewriter(text, speed=0.03, color="green"):
    """Print text slowly, character by character, in the given color."""
    for ch in text:
        sys.stdout.write(C[color] + ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(C["reset"] + "\n")


if __name__ == "__main__":
    width = 60
    top = C["cyan"] + "╔" + "═" * width + "╗" + C["reset"]
    bottom = C["cyan"] + "╚" + "═" * width + "╝" + C["reset"]
    middle = C["cyan"] + "║" + " " * width + "║" + C["reset"]

    print(top)
    print(middle)
    print(C["yellow"] + "║" + " " * 20 + "WOODY'S PHILOSOPHY" + " " * 20 + C["cyan"] + "║" + C["reset"])
    print(middle)
    typewriter(QUOTE, speed=0.035, color="green")
    print(middle)
    print(bottom)
    typewriter(
        "⊂( ◕‿◕)ts Remember: even the afterlife needs a timeout setting.",
        speed=0.04,
        color="red",
    )