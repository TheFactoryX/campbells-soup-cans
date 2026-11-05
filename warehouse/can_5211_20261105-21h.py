"""
Campbell's Soup Can #5211
Produced: 2026-11-05 21:59:13
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def main():
    # ANSI color codes
    YELLOW = '\\033[33m'
    GREEN = '\\033[32m'
    CYAN = '\\033[36m'
    RESET = '\\033[0m'

    # Box dimensions
    interior_width = 40
    total_width = interior_width + 2  # including the two '|' chars and spaces

    # Top and bottom borders
    border = YELLOW + '+' + '─' * interior_width + '+' + RESET
    print(border)

    # Woody Allen quote (exactly 38 characters)
    quote = "I’m not afraid of death; I just don’t."

    # Build the line: | <quote> |
    line = f"{GREEN}| {CYAN}{quote}{RESET} |"
    print(line)

    # Bottom border
    print(border)

if __name__ == "__main__":
    main()