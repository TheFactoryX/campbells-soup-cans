"""
Campbell's Soup Can #2601
Produced: 2026-03-06 13:20:29
Worker: OpenAI: o3 Deep Research (openai/o3-deep-research)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

quote = "My existential crisis can wait until after breakfast; I never face nothingness on an empty stomach."
text_color = "\033[96m"
border_color = "\033[95m"
reset_color = "\033[0m"

visible_length = len(quote) + 4

# Top border
print(border_color + "┌" + "─" * visible_length + "┐" + reset_color, flush=True)

# Quote line (with animation effect)
sys.stdout.write(border_color + "│ ")
sys.stdout.write(text_color + "\"")
for char in quote:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
sys.stdout.write("\"")
sys.stdout.write(border_color + " │" + reset_color + "\n")
sys.stdout.flush()

# Pause before bottom border
time.sleep(0.5)

# Bottom border
print(border_color + "└" + "─" * visible_length + "┘" + reset_color, flush=True)