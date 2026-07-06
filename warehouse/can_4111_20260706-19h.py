"""
Campbell's Soup Can #4111
Produced: 2026-07-06 19:04:51
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
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
C = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m",
}

def type_print(text, color="cyan", delay=0.05):
    """Print text character by character for a typewriter effect."""
    for ch in text:
        sys.stdout.write(C[color] + ch + C["reset"])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Fun ASCII brain/cogs
art = f"""{C["yellow"]}
          .-~~~~~-.
         /  _ _  \\
        |  ~ o ~  |
        |  .==.  |
       /   ===   \\
{C["reset"]}"""

print(art)

# Woody Allen style quote
quote = ("I don't fear death; I just fear that it will be an endless Zoom call where I'm muted and no one notices I've left.")

# Build a colorful box around the quote
width = max(60, len(quote) + 4)
top = C["magenta"] + "+" + "-" * (width - 2) + "+" + C["reset"]
title = C["magenta"] + "| " + "Woody's Preposterous Wisdom".center(width - 4) + " |" + C["reset"]
body = C["magenta"] + "| " + quote.ljust(width - 4) + " |" + C["reset"]
bottom = C["magenta"] + "+" + "-" * (width - 2) + "+" + C["reset"]

print(top)
print(title)
print(body)
print(bottom)

# A little wink to finish
wink = f"{C['cyan']}*(_ o _)*{C['reset']}"
print(wink)