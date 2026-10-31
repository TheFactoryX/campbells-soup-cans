"""
Campbell's Soup Can #5192
Produced: 2026-10-31 17:44:15
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

def colored(text, code):
    """Wrap text in ANSI color codes."""
    return f"\033[{code}m{text}\033[0m"

def main():
    # Woody Allen‑style philosophical quote
    quote = (
        "I’m terrified of death—just not as terrified\n"
        "as I am of being alive and realizing I never\n"
        "got to finish my thoughts."
    )

    # Box dimensions
    border = "+------------------------------------------+"
    inner = "|  " + quote.replace("\n", "\n  ") + "  |"

    # Print with colors: green border, yellow text
    sys.stdout.write(colored(border, "32") + "\n")
    sys.stdout.write(colored(inner, "33") + "\n")
    sys.stdout.write(colored(border, "32") + "\n")

if __name__ == "__main__":
    main()