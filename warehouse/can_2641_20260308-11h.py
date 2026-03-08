"""
Campbell's Soup Can #2641
Produced: 2026-03-08 11:34:05
Worker: AllenAI: Olmo 3 32B Think (allenai/olmo-3-32b-think)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

# ANSI color codes
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
ENDC = '\033[0m'

# ASCII thought bubble
bubble = [
    "    ooooooooooooooooooooooo   ",
    "   o                         o  ",
    "  o                           o ",
    " o                             o",
    "ooooooooooooooooooooooooooooooo"
]

for line in bubble:
    print('\033[36m' + line + '\033[0m')

print('\033[31m' + "Philosophy with a Side of Anxiety:" + ENDC)
quote = "I'm not worried about the meaning of life. I'm more concerned about where I left my keys."
colored_words = [f"{COLORS[i % len(COLORS)]}{word}{ENDC}" for i, word in enumerate(quote.split())]
print(" ".join(colored_words))