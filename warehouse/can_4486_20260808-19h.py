"""
Campbell's Soup Can #4486
Produced: 2026-08-08 19:44:47
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

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

# ANSI color codes
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"
RESET  = "\033[0m"

COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    padding = 2
    width = len(quote) + 2 * padding  # space inside the box

    # Animation: flashing colors
    for i in range(8):
        clear_screen()
        border_color = COLORS[i % len(COLORS)]
        text_color   = COLORS[(i + 2) % len(COLORS)]

        sys.stdout.write(border_color)
        print("+" + "-" * width + "+")
        sys.stdout.write(RESET)

        sys.stdout.write(text_color)
        print("|" + " " * padding + quote + " " * padding + "|")
        sys.stdout.write(RESET)

        sys.stdout.write(border_color)
        print("+" + "-" * width + "+")
        sys.stdout.write(RESET)

        time.sleep(0.15)

    # Final static display (white box, cyan text)
    clear_screen()
    sys.stdout.write(WHITE)
    print("+" + "-" * width + "+")
    sys.stdout.write(RESET)

    sys.stdout.write(CYAN)
    print("|" + " " * padding + quote + " " * padding + "|")
    sys.stdout.write(RESET)

    sys.stdout.write(WHITE)
    print("+" + "-" * width + "+")
    sys.stdout.write(RESET)

if __name__ == "__main__":
    main()