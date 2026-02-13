"""
Campbell's Soup Can #2193
Produced: 2026-02-13 05:38:24
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

def random_color():
    return random.choice([31,32,33,34,35,36,37])  # red, green, yellow, blue, magenta, cyan, white

def colorize(text, fg):
    """Wrap text in ANSI escape codes for the given foreground color."""
    return f'\033[{fg}m{text}\033[0m'

# Woody Allen's minimalist head (ASCII art)
wood_art = r"""
   __
  /  \\
 ( • • )
  \\__/
    W
"""

# Flash the head with a bright cyan background for extra flair
sys.stdout.write(colorize(wood_art, random_color()))
sys.stdout.flush()
time.sleep(0.12)

# Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Build a random‑colored box around the quote
top = colorize('┌───────────────────────────────┐', random_color())
mid = f'│ {quote} │'
mid_colored = colorize(mid, random_color())
bottom = colorize('└───────────────────────────────┘', random_color())

# Show the box top, animate the middle line, then finish with the bottom
print('\n')
print(top)
for ch in mid_colored:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.02)
print('\n')
print(bottom)

# Reset terminal colors so the console stays tidy
print('\033[0m')