"""
Campbell's Soup Can #3418
Produced: 2026-04-23 21:07:21
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI color codes
BLUE = '\033[34m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RESET = '\033[0m'

quote = "I asked the universe for the meaning of life, but I think it's still on voicemail."
padding = 1

# Box drawing characters (Unicode)
top_left = '╔'
top_right = '╗'
bottom_left = '╚'
bottom_right = '╝'
horizontal = '═'
vertical = '║'

inner_width = len(quote) + 2 * padding

# Build box parts with colors
top_border = f"{BLUE}{top_left}{horizontal * inner_width}{top_right}{RESET}"
middle_blank = f"{BLUE}{vertical}{' ' * inner_width}{vertical}{RESET}"
bottom_border = f"{BLUE}{bottom_left}{horizontal * inner_width}{bottom_right}{RESET}"

# Title
print(f"{BOLD}{BLUE}Woody Allen says:{RESET}")
print()

# Print box without text
print(top_border)
print(middle_blank)

# Pause so user sees the empty box
time.sleep(0.5)

# Move cursor back to the middle line to type the quote
sys.stdout.write('\033[1A')  # up one line
sys.stdout.write(f'\033[{1+padding}C')  # move right to start of quote area
sys.stdout.write(YELLOW + BOLD)  # set quote color
sys.stdout.flush()

# Typewriter effect
for ch in quote:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.05)

sys.stdout.write(RESET)  # reset color
sys.stdout.flush()

# Move to next line for bottom border
sys.stdout.write('\n')
sys.stdout.flush()

# Print bottom border
print(bottom_border)

# Attribution
print()
print(f"    {BLUE}{BOLD}- Woody Allen (probably){RESET}")