"""
Campbell's Soup Can #2597
Produced: 2026-03-06 08:56:03
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

quote = "I'm not a neurotic; I'm just a very well-organized person with a lot of problems."
colors = [31, 32, 33, 34, 35, 36, 37]  # Red, Green, Yellow, Blue, Magenta, Cyan, White

# Typing effect with color cycling
for i, char in enumerate(quote):
    color = colors[i % len(colors)]
    print(f"\033[{color}m{char}\033[0m", end='', flush=True)
    time.sleep(0.05)

print("\n\n\033[36m" + "     ┌───────────────────────────────────────┐" + "\033[0m")
print("\033[32m" + "     │  " + " " * 38 + "  │" + "\033[0m")
print("\033[34m" + "     │  " + "I'M NOT A NEUROTIC... I'M A" + " " * 10 + "  │" + "\033[0m")
print("\033[33m" + "     │  " + "NEUROTIC GENIUS! (PROBABLY)  " + " " * 5 + "  │" + "\033[0m")
print("\033[35m" + "     │  " + "   (BUT I'M STILL AFRAID OF" + " " * 8 + "  │" + "\033[0m")
print("\033[31m" + "     │  " + "        THE FUTURE...          " + " " * 10 + "  │" + "\033[0m")
print("\033[32m" + "     │  " + " " * 38 + "  │" + "\033[0m")
print("\033[36m" + "     └───────────────────────────────────────┘" + "\033[0m")

# Brain animation (wobbly!)
print("\n\033[33m", end='')
for _ in range(5):
    print("  _____  " * 2)
    print(" /     \\ " * 2)
    print("| (o o) |" * 2)
    print("|   |   |" * 2)
    print(" \\  ---  /" * 2)
    print("  \\_____/" * 2)
    time.sleep(0.3)
    print("\033[F" * 10, end='')  # Move up 10 lines to overwrite

print("\n\033[35m" + "          -- Woody Allen's Neurotic Wisdom --" + "\033[0m")