"""
Campbell's Soup Can #4772
Produced: 2026-08-22 18:48:50
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def main():
    # ANSI color codes
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    YELLOW  = "\033[1;33m"
    CYAN    = "\033[1;36m"

    # Quote text (Woody Allen style)
    part1 = f"{CYAN}{BOLD}I'm not afraid of dying; I'm just{BOLD}{RESET}"
    part2 = f"{CYAN}{BOLD}afraid I'll miss the punchline of my{BOLD}{RESET}"
    part3 = f"{CYAN}{BOLD}own life.{RESET}"

    # Box dimensions
    width = 48                     # number of '=' characters inside the box
    top_bottom = f"{YELLOW}{BOLD}+{'=' * width}+{RESET}"
    border   = f"{YELLOW}{BOLD}| {RESET}"

    # Assemble the box
    box = "\n".join([
        top_bottom,
        f"{border}{part1}{border}{RESET}",
        f"{border}{part2}{border}{RESET}",
        f"{border}{part3}{border}{RESET}",
        top_bottom
    ])

    print(box)

if __name__ == "__main__":
    main()