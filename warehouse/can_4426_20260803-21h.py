"""
Campbell's Soup Can #4426
Produced: 2026-08-03 21:29:54
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
    Cyan = "\033[36m"   # border color
    Yellow = "\033[33m" # quote color
    Reset = "\033[0m"   # reset all attributes

    # The Woody Allen‑style philosophical quote
    quote = (
        "I’m not scared of death; I just don’t want to be there when it happens, "
        "because the line at the afterlife is always too long."
    )

    # Build the framed output
    top_bottom = Cyan + "+---------------------------------------------------+" + Reset
    side = Cyan + "|" + Reset

    # Print the framed quote
    print(top_bottom)
    print(side + Yellow + quote + Reset + side)
    print(side + " " * 53 + side)  # empty line for visual breathing room
    print(top_bottom)

if __name__ == "__main__":
    main()