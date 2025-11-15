"""
Campbell's Soup Can #296
Produced: 2025-11-15 15:29:38
Worker: Qwen: Qwen3 14B (free) (qwen/qwen3-14b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# Woody Allen-style philosophical quote
quote = "The universe is a cruel joke, and I'm the punchline who forgot to bring a punchline."
attribution = "– Woody Allen"

# Create ASCII border with randomized width
border_length = len(quote) + 6
border = "─" * (border_length - 2)
top_border = f"\033[94m┌{border}┐\033[0m"
bottom_border = f"\033[94m└{border}┘\033[0m"

# Function to simulate a flickering effect
def flicker_print(text, color):
    for _ in range(3):
        print(f"\033[38;2m{text}\033[0m")
        time.sleep(0.2)
        print(f"\033[38;5m{text}\033[0m")
        time.sleep(0.2)
    print(f"\033[93m{text}\033[0m")

# Clear screen and print the stylized header
print("\033c")
print("  \033[92m██╗   ██╗ █████╗  ██████╗\033[0m")
print("   \033[93m╚██╗ ██╔╝██╔══██╗██╔════╝\033[0m")
print("    \033[91m╚████╔╝ ██║  ██║██║     \033[0m")
print("     \033[95m╚██╔╝  ██║  ██║██║     \033[0m")
print("      \033[96m██║   ╚██████║╚██████╗\033[0m\n")

# Print top border
print(top_border)
time.sleep(0.8)

# Simulate typing effect with a blinking cursor
typed = '│  ' + ' ' * len(quote) + '  │'
print(f"\033[93m{typed}\033[0m")
time.sleep(0.5)

# Type the quote character by character
for i in range(len(quote)):
    time.sleep(0.03)
    typed = '│  ' + quote[:i+1] + ' ' * (len(quote) - i - 1) + '  │'
    print(f"\033[93m{typed}\033[0m", end='\r')

# Flicker the attribution with random colors
flicker_print(f"  {attribution}", "m")

# Print the bottom border with a slow fade
for i in range(10):
    color_code = f"\033[38;5m"
    print(f"{color_code}{' ' * (border_length + 2)}\033[0m")
    time.sleep(0.2)
    print(bottom_border)
    time.sleep(0.3)
    print("\033c")
    time.sleep(0.1)