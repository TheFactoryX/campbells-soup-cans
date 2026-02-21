"""
Campbell's Soup Can #2345
Produced: 2026-02-21 02:48:21
Worker: Qwen: Qwen3 14B (qwen/qwen3-14b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI escape codes for colors
GREEN_BG = "\033[48;5;22m"       # Dark green background
WHITE_TEXT = "\033[38;5;255m"    # White text
YELLOW_TEXT = "\033[38;5;226m"   # Yellow text for the footer
RESET = "\033[0m"                # Reset to default

# Woody Allen-style philosophical quote
quote = "I'm not afraid of life's absurdity; I'm just terrified of having to think about it while waiting for the bus."

# Create a border of '=' characters
border = "=" * 60

# Create some random ASCII "stars" for flair
stars = " ".join(random.choice("★☆⭐💫✨") for _ in range(10))

# Print top border with green background and white text
print(GREEN_BG + WHITE_TEXT + border + RESET)
print(GREEN_BG + WHITE_TEXT + stars + RESET)

# Print the quote with a typing effect
print(GREEN_BG + WHITE_TEXT, end='')
for char in quote:
    print(char, end='', flush=True)
    time.sleep(0.05)
print(RESET)

# Print bottom border
print(GREEN_BG + WHITE_TEXT + border + RESET)

# Print the footer with yellow text
print(YELLOW_TEXT + "– Woody Allen (probably)" + RESET)