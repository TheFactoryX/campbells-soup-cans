"""
Campbell's Soup Can #2410
Produced: 2026-02-24 13:44:03
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# APP Settings
DELAY = 0.05
CLEAR_SCREEN = "\x1b[H\x1b[2J"
FRAME = "\x1b[36m" + "┌" + "-" * 60 + "┐\n"
MIDDLE_LINE = "│"
END_FRAME = "└" + "-" * 60 + "┘"
WHITE = "\033[37m"
BLUE = "\033[34m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

# Setup the frame
sys.stdout.write(CLEAR_SCREEN)
sys.stdout.write(BLUE + FRAME + WHITE + "   Welcome to Woldez Café 🐱" + BLUE)
sys.stdout.flush()
time.sleep(0.3)
sys.stdout.write(" "*80 + "│")
sys.stdout.write("\n" + RESET)
time.sleep(0.1)
sys.stdout.write(f"\033[H" + FRAME)
time.sleep(0.1)

# Main quote
quote = (
    "I tried to find meaning in life, but my therapist told me\'" 
    "I was just being vague. Now I own 35 cats.\""
)

# Animate the quote with colorful punctuation
for char in quote:
    sys.stdout.write(RESET + char)
    sys.stdout.flush()
    time.sleep(DELAY)

# Add a blinking cursor effect
sys.stdout.write("\033[H\033[2J")  # Clear and move cursor
for i in range(10):
    sys.stdout.write(f"\033[36m┌{'-'*60}┐\033[0m")
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write(f"\033[35m└{'-'*60}┘\033[0m")
    sys.stdout.flush()
    time.sleep(0.1)

print("\n\033[31m\n\n   -Woody Allen (probably)\033[0m\n")