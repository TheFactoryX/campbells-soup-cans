"""
Campbell's Soup Can #5266
Produced: 2026-11-21 23:17:18
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen Style Quote Generator — Pure Python, ANSI Colors"""
import time
import sys

# ANSI color palette
RESET = "\033[0m"
BOLD  = "\033[1m"
CYAN  = "\033[36m"
YELLOW= "\033[33m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"

# The quote (capturing Woody's neurotic, guilt-ridden existentialism)
quote = (
    "I'm not afraid of death. I just don't want to be there when it happens. "
    "Mostly because I'd feel guilty about leaving the dishes undone."
)

# Adaptive box width to fit the quote snugly with line-drawing characters
w = len(quote) + 2   # two padding spaces inside the box sides

# Build the coloured box
top_box    = BOLD + CYAN + "╔" + "═" * w + "╗" + RESET
mid_box    = BOLD + CYAN + "║" + " " + quote + " " + "║" + RESET
bot_box    = BOLD + CYAN + "╚" + "═" * w + "╝" + RESET

# Playful thinking animation
def animate_thinking():
    for _ in range(3):
        sys.stdout.write(YELLOW + "." + RESET)
        sys.stdout.flush()
        time.sleep(0.13)
    sys.stdout.write("\n")

# Clear terminal and begin
sys.stdout.write("\033[2J\033[H")
sys.stdout.flush()
time.sleep(0.05)

print(top_box)
print(mid_box)
print(bot_box)
print()

animate_thinking()

print(MAGENTA + "   ✦ Existence is optional. Dessert is not. ✦" + RESET)
print(GREEN + "   (c) 2025 — Your friendly neighborhood neurotic" + RESET)