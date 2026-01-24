"""
Campbell's Soup Can #1822
Produced: 2026-01-24 17:32:59
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

RESET = '\033[0m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'

quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying. But then I think, 'Wait, if I don't die, how will I stop working?'"
box_width = 80
inner_width = box_width - 4
padded_quote = quote.center(inner_width)
top_border = "┌" + "─" * inner_width + "┐"
middle = "| " + padded_quote + " |"
bottom_border = "└" + "─" * inner_width + "┘"

print(YELLOW + top_border + RESET)
print(CYAN + middle + RESET)
print(YELLOW + bottom_border + RESET)
print(MAGENTA + "  (And the universe replies: 'You're late for your own funeral.')" + RESET)