"""
Campbell's Soup Can #1032
Produced: 2025-12-19 07:33:21
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
from time import sleep

# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Create ASCII art
front = [
    "    █████████████                     █████████████",
    "   ██                 ██         ██                ",
    "  ██      I am always      ██   ██          I am   ",
    " ██     afraid that some    ██ ██           afraid   ",
    "██       people like me    ██████            that    ",
    "███████████████████████████████████████████████",
    "   ██               ██             ██              ",
    "    ██             ██               ██             ",
    "     ██           ██                 ██           ",
    "      ██         ██                   ██         "
]

# Quote in Woody Allen's style
quote = "I'm not afraid of death; I just don't want to be around when the fun starts."
source = "– Woody Allen? Or maybe just my anxious thoughts?"

# Print animation effect
def print_with_effects(text, color, delay=0.05):
    print(color, end='', flush=True)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    print(RESET)

# Display the animation
print("\n" * 10)  # Clear screen
for line in front:
    print_with_effects(line, CYAN, 0.01)
    print()  # New line

print_with_effects("\n   ┌──────────────────────────────────────┐", GREEN, 0.05)
print_with_effects(f"   │{CYAN}            {quote.center(38)}{GREEN}             │", GREEN, 0.01)
print_with_effects(f"   │{CYAN}           {source.center(38)}{GREEN}           │", GREEN, 0.01)
print_with_effects("   └──────────────────────────────────────┘", GREEN, 0.05)