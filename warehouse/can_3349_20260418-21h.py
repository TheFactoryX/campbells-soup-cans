"""
Campbell's Soup Can #3349
Produced: 2026-04-18 21:51:12
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

RED ='\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

quote = "I'm not afraid of death; I just don't want to be there when it happens."
total_width = 58padding = total_width - len(quote)
left_pad = padding // 2
right_pad = padding - left_pad
centered_text = ' ' * left_pad + quote + ' ' * right_pad

print(RED + '*' * 60 + RESET)
print(GREEN + centered_text + RESET)
print(RED + '*' * 60 + RESET)