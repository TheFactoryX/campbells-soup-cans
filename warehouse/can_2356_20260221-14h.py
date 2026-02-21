"""
Campbell's Soup Can #2356
Produced: 2026-02-21 14:44:58
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

quote = (
    "I'm not afraid of the void; I just hate how it makes my hair look. "
    "Also, I think I left the oven on... or was that the universe?"
)

width = 55
padding = " " * ((width - len(quote)) // 2)

print(YELLOW + "┌───────────────────────────────────────────────────────┐" + RESET)
print(YELLOW + "│" + RESET + "    " + GREEN + "Woody Allen's Existential Crisis of the Day" + RESET + "    " + YELLOW + "│" + RESET)
print(YELLOW + "├───────────────────────────────────────────────────────┤" + RESET)

print(BLUE + "│" + RESET + padding, end='', flush=True)
time.sleep(0.5)

for i, char in enumerate(quote):
    color = GREEN if i % 3 == 0 else (RED if i % 3 == 1 else BLUE)
    print(color + char + RESET, end='', flush=True)
    time.sleep(0.03)
    if i % 15 == 14:
        time.sleep(0.2)

print(padding + BLUE + "│" + RESET)
print(BLUE + "│" + RESET + " " * (width // 2 - 8) + "© 2024 by the Anxious One" + RESET + " " * (width // 2 - 8) + BLUE + "│" + RESET)
print(BLUE + "└" + "─" * width + "┘" + RESET)

time.sleep(0.5)
print(RED + "\nPhilosophy is like a bad date: you pay for it, you suffer through it, " + RESET)
print(RED + "and at the end you're not sure if you even existed during it." + RESET)