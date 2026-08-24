"""
Campbell's Soup Can #4821
Produced: 2026-08-24 23:35:29
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def print_box(text: str) -> None:
    """Print the given text inside a simple ASCII box."""
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    width = max_len + 4
    horiz = "+" + "-" * (width - 2) + "+"
    print(horiz)
    for line in lines:
        print("| " + line.ljust(max_len) + " |")
    print(horiz)


def main() -> None:
    # One Woody Allen‑style philosophical quote
    quote = (
        "I contemplated the void, and the void contemplated my Netflix queue – "
        "turns out, even existential dread needs a good binge."
    )

    # ANSI colour codes (foreground)
    colours = [31, 32, 33, 34, 35, 36]  # red, green, yellow, blue, magenta, cyan

    # Animate by cycling colours a few times
    for _ in range(5):
        for col in colours:
            sys.stdout.write("\033[2J\033[H")  # clear screen & cursor home
            sys.stdout.write(f"\033[{col}m")
            print_box(quote)
            sys.stdout.write("\033[0m")        # reset colour
            sys.stdout.flush()
            time.sleep(0.2)

    # Final stable display (default colour)
    sys.stdout.write("\033[2J\033[H")
    print_box(quote)


if __name__ == "__main__":
    main()