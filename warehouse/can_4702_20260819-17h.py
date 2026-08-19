"""
Campbell's Soup Can #4702
Produced: 2026-08-19 17:40:54
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

def main():
    # Clear screen and move cursor to top-left
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Woody Allen‑style quote
    quote = "I would never want to belong to any club that would have me as a member - except maybe the club of people who overthink everything."

    # Colors
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Box dimensions
    inner_width = len(quote) + 4  # two spaces each side
    top_bottom = "╔" + "═" * inner_width + "╝"
    middle_empty = "║" + " " * inner_width + "║"

    # Print top border
    sys.stdout.write(CYAN + top_bottom + RESET + "\n")
    sys.stdout.flush()

    # Print empty line inside box
    sys.stdout.write(CYAN + "║" + RESET + " " * inner_width + CYAN + "║" + RESET + "\n")
    sys.stdout.flush()

    # Print quoted line with typewriter effect
    sys.stdout.write(CYAN + "║" + RESET + "  ")
    for ch in quote:
        sys.stdout.write(YELLOW + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("  " + CYAN + "║" + RESET + "\n")
    sys.stdout.flush()

    # Print another empty line inside box
    sys.stdout.write(CYAN + "║" + RESET + " " * inner_width + CYAN + "║" + RESET + "\n")
    sys.stdout.flush()

    # Print bottom border
    sys.stdout.write(CYAN + top_bottom.replace("╔", "╚").replace("╝", "╔") + RESET + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()