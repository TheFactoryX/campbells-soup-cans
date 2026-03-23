"""
Campbell's Soup Can #2924
Produced: 2026-03-23 11:55:20
Worker: Mistral Large (mistralai/mistral-large)
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
        "38;5;208",  # orange
        "38;5;226",  # yellow
        "38;5;46",   # green
        "38;5;45",   # sea green
        "38;5;39",   # blue
        "38;5;129",  # purple
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
    |   O O   |
    |    ∆    |
     \  ‿‿  /
      \_____/
    """

    frames = [frame1, frame2]

    for _ in range(3):
        for frame in frames:
            sys.stdout.write("\033[H\033[J")
            woody_print(frame, random.choice(colors))
            time.sleep(0.3)

    sys.stdout.write("\033[H\033[J")

    box_top = "╔" + "═" * 60 + "╗"
    box_bottom = "╚" + "═" * 60 + "╝"
    quote = "My one regret in life is that I am not someone else... preferably someone tall, successful, and with a full head of hair."
    wrapped_quote = [quote[i:i+58] for i in range(0, len(quote), 58)]

    woody_print(box_top, "38;5;208")
    woody_print("║" + " " * 60 + "║", "38;5;226")

    for line in wrapped_quote:
        woody_print("║  " + line.ljust(58) + "║", "38;5;46")

    woody_print("║" + " " * 60 + "║", "38;5;226")
    woody_print(box_bottom, "38;5;208")

    woody_print("\n\n\t- Woody Allen (probably)", "38;5;129", 0.1)

    time.sleep(2)
    for _ in range(3):
        sys.stdout.write("\033[5m")
        woody_print("\n\t...but then again, who isn't?", "38;5;208", 0.05)
        time.sleep(0.5)
        sys.stdout.write("\033[H\033[J")
        time.sleep(0.3)

if __name__ == "__main__":
    animate_quote()