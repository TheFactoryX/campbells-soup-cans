"""
Campbell's Soup Can #4923
Produced: 2026-09-08 04:37:38
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import math

# ANSI escape codes
class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    CY = '\033[96m'
    W = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'
    BG_BLACK = '\033[40m'

def typewrite(text, delay=0.03, color=C.W):
    for char in text:
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box(text, border_color=C.CY, text_color=C.W):
    width = max(len(line) for line in text.split('\n')) + 4
    print(border_color + "╔" + "═" * (width - 2) + "╗" + C.RESET)
    for line in text.split('\n'):
        padded = line.center(width - 2)
        print(border_color + "║" + C.RESET + text_color + padded + border_color + "║" + C.RESET)
    print(border_color + "╚" + "═" * (width - 2) + "╝" + C.RESET)

# Neurotic ASCII art
art = f"""
{C.Y}          __
{C.Y}         /  \\    {C.R}neurotic{C.Y}
{C.Y}        |    |   {C.M}existential{C.Y}
{C.Y}        |    |   {C.CY}paranoid{C.Y}
{C.Y}         \\__/
{C.Y}        /|  |\\
{C.Y}       / |  | \\
{C.Y}      /  |  |  \\{C.RESET}"""

print()
print(art)
print()

# Animated border
for i in range(3):
    sys.stdout.write(C.M + "▰" + C.Y + "▱" + C.R + "▰" + C.CY + "▱" + C.G + "▰" + C.Y + "▱" + C.R + "▰" + C.CY + "▱" + C.M + "▰" + C.Y + "▱" + C.R + "▰" + C.CY + "▱" + C.G + "▰" + C.Y + "▱" + C.R + "▰" + C.M + "▱" + C.RESET)
    sys.stdout.flush()
    time.sleep(0.05)
print()
print()

# The quote
quote = (
    "I asked myself the meaning of life.\n"
    "Then I asked myself why I was asking.\n"
    "Then I asked myself why I was asking THAT.\n"
    "By then, my therapist had left the room."
)

print_box(quote, border_color=C.M, text_color=C.W)

print()
typewrite(f"  {C.Y}{C.ITALIC}\"I'm not unhappy. I just have a low threshold for misery.\"{C.RESET}", 0.04, C.Y)
print()

# Rolling dots animation
for _ in range(3):
    for dots in [".  ", ".. ", "..."]:
        sys.stdout.write(C.CY + f"\r  {' '*20}\r  Thinking{dots} " + C.RESET)
        sys.stdout.flush()
        time.sleep(0.15)
print()
print()
print(C.DIM + "  — Woody Allen, probably, while overthinking this program —" + C.RESET)
print()