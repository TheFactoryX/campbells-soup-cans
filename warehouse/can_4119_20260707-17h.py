"""
Campbell's Soup Can #4119
Produced: 2026-07-07 17:26:54
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
    cyan   = "\033[1;36m"
    magenta= "\033[1;35m"
    yellow = "\033[1;33m"
    reset  = "\033[0m"

    # The Woody Allen‑style philosophical quote
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."

    # Build the decorative box
    top    = f"{cyan}+{'-' * 50}+{reset}"
    middle = f"{yellow}| \"{quote}\" |{reset}"
    bottom = f"{cyan}+{'-' * 50}+{reset}"
    attribution = f"{magenta} — Woody Allen (probably){reset}"

    # Print with a little breathing room
    print("\n")
    print(top)
    print(middle)
    print(bottom)
    print(attribution)
    print("\n")

if __name__ == "__main__":
    main()