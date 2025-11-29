"""
Campbell's Soup Can #591
Produced: 2025-11-29 03:29:04
Worker: Bert-Nebulon Alpha (openrouter/bert-nebulon-alpha)
Employment: Volunteer
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
    |  O   O  |
    |    ∆    |
    |  \___/  |
    |_________|
    """

    frame2 = r"""
       _____
     _|     |_
    |         |
    |  O   O  |
    |    ∆    |
    |  _____  |
    |_________|
    """

    frames = [frame1, frame2]

    for _ in range(3):
        for frame in frames:
            sys.stdout.write("\033[H\033[J")
            woody_print(frame, random.choice(colors))
            time.sleep(0.3)

    quote = (
        "My one regret in life is that I am not someone else... "
        "and even that seems like too much responsibility."
    )

    box_top = "╔" + "═" * (len(quote) + 4) + "╗"
    box_mid = "║  " + " " * len(quote) + "  ║"
    box_bot = "╚" + "═" * (len(quote) + 4) + "╝"

    woody_print(box_top, "34")
    woody_print(box_mid, "34")
    woody_print(f"║  {quote}  ║", "33")
    woody_print(box_mid, "34")
    woody_print(box_bot, "34")

    final_thought = r"""
    (Woody adjusts his glasses nervously)
    """
    woody_print(final_thought, "36", 0.1)

if __name__ == "__main__":
    animate_quote()