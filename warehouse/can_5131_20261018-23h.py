"""
Campbell's Soup Can #5131
Produced: 2026-10-18 23:13:17
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# A Woody Allen style philosophical one-liner
QUOTE = (
    "I'm not afraid of death. "
    "I'm just afraid it'll happen while I'm still worrying "
    "whether I left the iron on."
)

# ANSI color codes (pure Python, no deps)
R = '\033[91m'  # bright red
Y = '\033[93m'  # bright yellow
C = '\033[96m'  # bright cyan
G = '\033[92m'  # bright green
RST = '\033[0m'  # reset

# Simple ASCII "neurotic brain"
BRAIN = r"""
     (\_/)
     (o o)
   /  ----  \
   |  O   O  |
   |    ^    |
   /`------`\
"""


def typewriter(text, speed=0.035):
    """Gently type the quote like a neurotic thought stream."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def main():
    # Dramatic intro
    print(Y + "♫ analyzing existential dread… ♫" + RST)
    time.sleep(0.4)

    # Print the neurotic brain in cyan
    print(C + BRAIN + RST)
    time.sleep(0.3)

    # Determine a comfortable box width
    width = max(len(QUOTE.split()[0]) * 2 + 4, 42)

    # Colored box with the quote
    print(R + "┌" + "─" * width + "┐" + RST)
    # Build each line wrapped nicely
    words = QUOTE.split()
    line = ""
    for w in words:
        if len(line) + len(w) + 1 <= width - 2:
            line += (" " if line else "") + w
        else:
            print(R + "│ " + line + " " * (width - 2 - len(line)) + " │" + RST)
            line = w
    if line:
        print(R + "│ " + line + " " * (width - 2 - len(line)) + " │" + RST)
    print(R + "└" + "─" * width + "┘" + RST)

    print()
    # Typewriter reveal for that classic Woody rhythm
    typewriter(C + QUOTE + RST)


if __name__ == "__main__":
    main()