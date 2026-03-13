"""
Campbell's Soup Can #2747
Produced: 2026-03-13 19:01:41
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, random

QUOTE = (
    "I’m not sure if I’m an atheist or an agnostic, "
    "but I’m definitely convinced that the universe is just a bad joke "
    "and I forgot the punchline."
)

def delayed_print(text, delay=0.05):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # ANSI colours
    colours = [
        "\033[31m",  # red
        "\033[32m",  # green
        "\033[33m",  # yellow
        "\033[34m",  # blue
        "\033[35m",  # magenta        "\033[36m",  # cyan
        "\033[37m",  # white
    ]
    colour = random.choice(colours)
    reset = "\033[0m"

    width = len(QUOTE) + 4
    top = f"╔{'═'*width}╝"
    bottom = f"╚{'═'*width}╝"

    # Top border
    print(colour + top + reset)
    # Left side + opening space
    print(colour + "║  ", end='')
    # Quote typed out
    delayed_print(QUOTE, 0.04)
    # Closing spaces + right side
    print("  ║" + colour + reset)
    # Bottom border
    print(colour + bottom + reset)

if __name__ == "__main__":
    main()