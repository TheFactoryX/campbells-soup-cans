"""
Campbell's Soup Can #4427
Produced: 2026-08-03 23:18:59
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

print('\033[1;32m' + '+' + '-'*50 + '+' + '\033[0m')
quote = [
    "Life's a shipwreck and we're all passengers—most don't even know",
    "the water's freezing. But the real problem is that I missed the*",
    "lifeboat. Again. Just like every other life decision."
]
colors = [36, 33, 31]  # Cyan, Yellow, Red
for color, line in zip(colors, quote):
    centered = f"| {line.center(50)} |"
    print(f'\033[{color}m{centered}\033[0m')
print('\033[1;32m' + '+' + '-'*50 + '+' + '\033[0m')