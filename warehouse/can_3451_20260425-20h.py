"""
Campbell's Soup Can #3451
Produced: 2026-04-25 20:57:16
Worker: Mistral: Mistral Large 3 2512 (mistralai/mistral-large-2512)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def woody_print(text, color_code, delay=0.05):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_quote():
    colors = [
        "33",  # yellow
        "36",  # cyan
        "35",  # magenta
        "32",  # green
        "31",  # red
    ]

    frame1 = r"""
       _____
     _|     |_
    |         |
    |   O O   |
    |    ∆    |
     \  ___  /
      \_____/
    """

    frame2 = r"""
       _____
     _|     |_
    |         |
    |   - -   |
    |    ∆    |
     \  ___  /
      \_____/
    """

    frames = [frame1, frame2]

    for _ in range(3):
        for frame in frames:
            sys.stdout.write("\033[H\033[J")
            woody_print(frame, random.choice(colors), 0.001)
            time.sleep(0.2)

    quote = (
        "My one regret in life is that I am not someone else... "
        "preferably someone who's not me."
    )

    box_top = "╔" + "═" * (len(quote) + 4) + "╗"
    box_mid = "║  " + " " * len(quote) + "  ║"
    box_bot = "╚" + "═" * (len(quote) + 4) + "╝"

    woody_print(box_top, "34")
    woody_print(box_mid, "34")
    woody_print(f"║  \033[33m{quote}\033[0m  ║", "34")
    woody_print(box_mid, "34")
    woody_print(box_bot, "34")

    final_thought = "   ...and that's why I need therapy."
    woody_print(final_thought, "31", 0.1)

if __name__ == "__main__":
    animate_quote()