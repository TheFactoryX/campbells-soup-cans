"""
Campbell's Soup Can #3436
Produced: 2026-04-24 23:55:43
Worker: Qwen: Qwen3 30B A3B Thinking 2507 (qwen/qwen3-30b-a3b-thinking-2507)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
inner_width = len(quote)
reset = "\033[0m"
blue = "\033[34m"
red = "\033[31m"
green = "\033[32m"

# Print top border
print(f"{blue}┌{'─' * inner_width}┐{reset}")

# Print quote with colored borders
print(f"{blue}│{reset}{red}{quote}{reset}{blue}│{reset}")

# Print bottom border
print(f"{blue}└{'─' * inner_width}┘{reset}")

# Add coffee cup ASCII art with sad face
coffee_art = [
    "  .-.",
    " / o o \\",
    " |  _  |",
    "  `---'",
    "   :("
]

for i, line in enumerate(coffee_art):
    time.sleep(0.1)
    print(f"{green}{line}{reset}", end = "\r" if i < len(coffee_art)-1 else "\n")