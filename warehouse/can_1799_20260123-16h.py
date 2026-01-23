"""
Campbell's Soup Can #1799
Produced: 2026-01-23 16:49:29
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

reset = "\033[0m"
bold = "\033[1m"
green = "\033[32m"
yellow = "\033[33m"
magenta = "\033[35m"

# 🎨 ASCII Art Frame
print(yellow + "█" + " " * 40 + "█" + reset)
print(yellow + "█" + " " * 40 + "█" + reset)
print(magenta + "█ " + "WOODY'S QUOTE GENERATOR " + "█" + reset)
print(yellow + "█" + " " * 40 + "█" + reset)
print(yellow + "█" + " " * 40 + "█" + reset)

# 🧠 The Quote (with style)
print("\n" + bold + green + "I’m not saying life’s meaningless—\n" + reset)
print(yellow + "but have you ever noticed how your fridge drawer\n" + "looks exactly like a tiny existential void? " + reset)
print(magenta + "—Woody" + reset)

# 🕺 Animation: Blinking Text
print("\033[33m" + "▄" * 50 + "\r", end="")
time.sleep(0.5)
print("\033[33m" + "▀" * 50 + "\r", end="")
time.sleep(0.5)
print("\033[33m" + "WOODY SAID: “YOU’RE ALL JUST A\n" + "DREAM INSIDE MY MENTAL REFRIGERATOR.”" + "\033[33m\r", end="")
time.sleep(1)
print(reset)