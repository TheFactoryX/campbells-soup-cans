"""
Campbell's Soup Can #1093
Produced: 2025-12-22 02:30:01
Worker: OpenAI: GPT-5.1 Chat (openai/gpt-5.1-chat)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI colors
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

quote = "I tried contemplating the meaning of existence, but I got distracted by my own anxiety—which, frankly, is the only thing in my life showing real commitment."

art = [
    "        .-''''-.        ",
    "       /        \\       ",
    "      |  O    O  |      ",
    "      |    --    |      ",
    "      |  .----.  |      ",
    "       \\ '----' /       ",
    "        '-.__.-'        ",
]

for frame in range(3):
    color = [RED, YELLOW, CYAN][frame % 3]
    print(color + "\n".join(art) + RESET)
    time.sleep(0.3)
    print("\033[2J\033[H", end="")  # clear screen

print(CYAN + "╔" + "═" * 70 + "╗" + RESET)
print(CYAN + "║" + RESET + " " * 70 + CYAN + "║" + RESET)
line = quote.center(70)
print(CYAN + "║" + RESET + line + CYAN + "║" + RESET)
print(CYAN + "║" + RESET + " " * 70 + CYAN + "║" + RESET)
print(CYAN + "╚" + "═" * 70 + "╝" + RESET)