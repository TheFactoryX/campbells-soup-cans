"""
Campbell's Soup Can #1562
Produced: 2026-01-12 15:42:46
Worker: AllenAI: Molmo2 8B (free) (allenai/molmo-2-8b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ASCII art speaker (Woody Allen style)
speaker = """
        (
         \
          \
           )
          / \
         /   \
      ::::::::
     (        )
     (   o   )
      \      /
       \____/
"""
# Colors
yellow = "\033[93m"
white = "\033[97m"
reset = "\033[0m"

# Print the speaker (line by line)
print(speaker[0:6])
print(speaker[6:12])
print(speaker[12:18])
print(speaker[18:24])
print(speaker[24:30])
print(speaker[30:36])
print(speaker[36:42])

# Woody Allen's famous quote
quote = "\n\"" + yellow + "I look forward to dying, but I have trouble getting to sleep every night.\n\"" + white

# Print with a fancy border and some animated dots
top_border = "--------+--------"
bottom_border = "+--------|--------+"


def normalize_width(width):
    return int((max(len(speaker[i:i+6]) for i in range(0, 36, 6)) + len(quote)) / 2 + 2)


CONTAINERS = "|||||||||XXXXXXXXXXXXXXXXXXXXX|||||||||XXXXXXXXXXXXXXXXXXXXX|||||||||"
width = normalize_width(len(CONTAINERS))
border = "+ " + "=".join(['-' for _ in range(width)] + "-" + "=".join(['-' for _ in range(width-2)]) + " " + "+"

# Print the quote in the center, colored and bordered
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n[i:{width}s{i spaces} ({CONTAINERS}\n[i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces} ({CONTAINERS}\n{i:{width}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} {CONTAINERS}\n{i:{width}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINTERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} {CONTAINERS}\n{i:{}s{i spaces} ( {CONTAINERS}\n{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_border}\n[border]
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}
{i:{}s{i spaces}{quote}{width-i}s{i spaces}( {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} {CONTAINERS}
{i:{}s{i spaces} ( {CONTAINERS}\n".
{bottom_border}"))
print(f"{top_b