"""
Campbell's Soup Can #2143
Produced: 2026-02-09 22:58:24
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote():
    quote = """
    I'm not afraid of death; I just don't want to be there when it happens.
    """
    author = " - Woody Allen"

    # ANSI escape codes for colors
    colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
        "\033[37m",  # White
    ]
    reset = "\033[0m"

    # Print top border
    print("\033[1;37;40m" + "=" * 60 + reset)
    print()

    # Print quote with color animation
    for char in quote:
        if char == "\n":
            print()
        else:
            color = colors[int(time.time() * 10) % len(colors)]
            print(f"{color}{char}{reset}", end="")
            sys.stdout.flush()
            time.sleep(0.01)

    # Print author in a different color
    print(f"\033[1;35m{author}\033[0m")

    # Print bottom border
    print()
    print("\033[1;37;40m" + "=" * 60 + reset)

if __name__ == "__main__":
    print_quote()