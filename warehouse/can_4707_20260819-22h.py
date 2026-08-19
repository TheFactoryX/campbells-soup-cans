"""
Campbell's Soup Can #4707
Produced: 2026-08-19 22:41:35
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_colored(text, color):
    print(f"{color}{text}\033[0m")

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens, because I have too many unresolved emails."
    # Box dimensions
    inner_width = len(quote) + 2  # Spaces on each side
    width = inner_width + 2       # Total width including box corners
    top    = "╔" + "═" * (width - 2) + "╗"
    middle = "║ " + quote + " ║"
    bottom = "╚" + "═" * (width - 2) + "╝"

    yellow = "\033[93m"
    red    = "\033[91m"
    reset  = "\033[0m"

    # Print the box with a tiny pause for effect
    for line in (top, middle, bottom):
        print_colored(line, yellow)
        time.sleep(0.1)

    # Print the quote itself
    print_colored(quote, red)
    # Attribution
    print_colored("— Woody Allen (probably)", yellow)

if __name__ == "__main__":
    main()