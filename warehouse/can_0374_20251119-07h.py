"""
Campbell's Soup Can #374
Produced: 2025-11-19 07:30:58
Worker: Qwen: Qwen3 235B A22B (free) (qwen/qwen3-235b-a22b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

CSI = "\033["
RED = CSI + "91m"
YELLOW = CSI + "93m"
RESET = CSI + "0m"

quote = "I concluded long ago the universe couldn't care less; only felt absurd when apologizing – who's receiving my dry thoughts anyway? Probably a lost sock employee."

width = len(quote) + 6
horizontal_rule = RED + ' ' + '_' * (width - 4) + ' ' + RESET
top_border = RED + '/' + ' ' * (width - 2) + '/' + RESET
bottom_border = RED + '\\' + ' ' * (width - 2) + '\\' + RESET

print()
print(" " * 3 + CSI + "5;31m▘" + "▁" * 25 + "▁▛")
print(horizontal_rule)
print(top_border)
print(f"{RED}|  {YELLOW}{quote} {RED} |")
print(bottom_border)
print(horizontal_rule)
print(RED + " " * 20 + "|" + YELLOW + " Existential Kinks Incorporated " + RESET)