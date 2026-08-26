"""
Campbell's Soup Can #4848
Produced: 2026-08-26 05:50:09
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A single Python script that prints a Woody Allen‑style philosophical quote
in a colorful, ASCII‑art box.
"""

import textwrap

# ANSI escape codes for colors
CYAN   = "\033[36m"
MAGENTA= "\033[35m"
YELLOW = "\033[33m"
RESET  = "\033[0m"

def main() -> None:
    # Box dimensions
    BOX_WIDTH = 60          # total width including the '+' and '|'
    inner_width = BOX_WIDTH - 2  # spaces between the side '|' characters

    # Build the top and bottom border
    top_bottom = f"{CYAN}+{'-' * inner_width}+{RESET}"

    # Side borders (empty lines)
    side_border = f"{CYAN}|{' ' * inner_width}|{RESET}"

    # The Woody Allen‑style quote
    quote = (
        "I’m terrified of death, but I’m more terrified of being forgotten, "
        "so I keep pretending I’m just a temporary glitch in the universe’s code."
    )
    # Wrap to fit nicely inside the box (max 48 characters per line)
    wrapped_lines = textwrap.wrap(quote, width=48)

    # Print the whole thing
    print(top_bottom)
    print(side_border)
    for line in wrapped_lines:
        print(f"|{MAGENTA}{line}{RESET}|")
    print(side_border)
    print(top_bottom)


if __name__ == "__main__":
    main()