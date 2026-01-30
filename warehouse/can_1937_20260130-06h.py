"""
Campbell's Soup Can #1937
Produced: 2026-01-30 06:01:44
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, random, sys

# Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# ANSI color codes (foreground only)
fg_colors = ["\x1b[31m", "\x1b[32m", "\x1b[33m", "\x1b[34m",
             "\x1b[35m", "\x1b[36m", "\x1b[37m"]
# Optional background colors (20 % chance per character)
bg_colors = ["\x1b[41m", "\x1b[42m", "\x1b[43m", "\x1b[44m",
             "\x1b[45m", "\x1b[46m", "\x1b[47m"]

# Simple ASCII art head‑hat (try to look vaguely like Woody)
art = (
    "   _______                _______   \n"
    "  /       \\              /       \\  \n"
    " |   ___   |   ___   ___|   ___   | \n"
    " |  (o)(o) |  /__\\  /__\\   (o)(o) | \n"
    " |   \\__/  | /    \\/    \\  \\__/   | \n"
    "  \\       /               \\       / \n"
    "   \\_____/                 \\_____/  "
)

# Print the art (reset after)
print(art, "\x1b[0m")
print("\n" + "+" + "-" * 80 + "+")
print("|" + " " * 8 + r"\o/" + " " * 8 + "|")
print("|" + " " * 9 + "\"_/|\"_" + " " * 9 + "|")
print("|" + " " * 9 + r"(   )" + " " * 9 + "|")
print("|" + " " * 9 + r"  (   )" + " " * 9 + "|")
print("+" + "-" * 80 + "+\n")

# Typewriter effect with randomly‑colored characters
for char in quote:
    # Choose foreground color
    fg = random.choice(fg_colors)
    # Occasionally add a background color (20 % chance)
    if random.random() < 0.2:
        bg = random.choice(bg_colors)
        start = f"{fg}{bg}"
    else:
        start = fg
    sys.stdout.write(start + char + "\x1b[0m")
    sys.stdout.flush()
    time.sleep(0.02)   # tweak for speed of typing

# End with a neat separator
print("\n" + "-" * 80 + "\n")
print("Press any key to exit... ")
sys.stdin.read(1)  # pause before program termination