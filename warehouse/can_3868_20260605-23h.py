"""
Campbell's Soup Can #3868
Produced: 2026-06-05 23:37:54
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
    # Woody Allen‑style philosophical quote
    quote = "I’m not afraid of death; I just don’t want to be there when it happens."
    
    # ANSI color codes for visual flair
    cyan   = "\033[96m"   # bright cyan
    reset  = "\033[0m"    # back to default
    
    # Box dimensions
    width = 70
    border = cyan + "+" + "-" * (width - 2) + "+" + reset
    
    # Center the quote within the box
    centered = quote.center(width - 2)
    left_pad  = (width - 2 - len(centered)) // 2
    right_pad = (width - 2 - len(centered)) - left_pad
    centered_line = cyan + "|" + " " * left_pad + centered + " " * right_pad + "|" + reset
    
    # Print the colorful box
    print(border)
    print(centered_line)
    print(border)

if __name__ == "__main__":
    main()