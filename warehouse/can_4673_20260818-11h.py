"""
Campbell's Soup Can #4673
Produced: 2026-08-18 11:40:49
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Woody Allen‑style philosophical quote, dressed up with colors and a decorative box
quote = "I’m terrified of death because I don’t want to miss the chance to be late for my own funeral."

# ANSI escape codes: yellow text on a black background
YELLOW_ON_BLACK = "\033[93;40m"
RESET = "\033[0m"

top    = f"{YELLOW_ON_BLACK} ****************************** {RESET}"
middle = f"{YELLOW_ON_BLACK} * {quote} * {RESET}"
bottom = f"{YELLOW_ON_BLACK} ****************************** {RESET}"

print("\n" + top)
print(middle)
print(bottom + "\n")