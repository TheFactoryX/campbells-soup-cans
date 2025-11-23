"""
Campbell's Soup Can #464
Produced: 2025-11-23 08:37:01
Worker: xAI: Grok 4.1 Fast (x-ai/grok-4.1-fast)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
ESC = chr(27)
RESET = ESC + '[0m'
BOLD = ESC + '[1m'
RED = ESC + '[91m'
GREEN = ESC + '[92m'
YELLOW = ESC + '[93m'
BLUE = ESC + '[94m'
MAGENTA = ESC + '[95m'
CYAN = ESC + '[96m'
WHITE = ESC + '[97m'

# Rainbow colors cycle
rainbow = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

def clear_screen():
    sys.stdout.write(ESC + '[2J' + ESC + '[H')
    sys.stdout.flush()

def typewriter_rainbow(text, delay=0.04):
    for i, char in enumerate(text):
        color = rainbow[i % len(rainbow)]
        sys.stdout.write(color + BOLD + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Clear the screen
clear_screen()

# Animated intro title
title = "Woody Allen's Neurotic Nugget of Wisdom"
sys.stdout.write(CYAN + BOLD)
typewriter_rainbow(title, 0.08)
print()

# Funny ASCII art thinker (neurotic Woody vibe)
art = [
    "     .-\"-.     ",
    "    / _  _ \\    ",
    "   |  d  b  |   ",
    "    \\   ^   /   ",
    "     )  -  (    ",
    "    /       \\   ",
    "   |         |  ",
    "    \\ existential /",
    "     '-------'   "
]
for line in art:
    print(MAGENTA + line.center(50) + RESET)
    time.sleep(0.2)
print()

# The quote!
quote = "If the universe is expanding, why does my anxiety feel so claustrophobic?"
print(WHITE + " \"" + RESET, end="")
typewriter_rainbow(quote, 0.035)
print(WHITE + "\"" + RESET)

# Footer with a little existential sigh
time.sleep(0.5)
footer = " - A self-deprecating sigh from the cosmos"
print(GREEN + BOLD + footer.center(60) + RESET)

# End with a blinking existential question mark
time.sleep(0.5)
for _ in range(5):
    sys.stdout.write(RED + BOLD + " ...? " + RESET + "\r")
    sys.stdout.flush()
    time.sleep(0.3)
    sys.stdout.write("     " + "\r")
    sys.stdout.flush()
    time.sleep(0.3)
print()