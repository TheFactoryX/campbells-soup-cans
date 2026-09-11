"""
Campbell's Soup Can #4944
Produced: 2026-09-11 18:33:58
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

# ANSI escape codes for colors and formatting
R = "\033[91m"  # Red
G = "\033[92m"  # Green
Y = "\033[93m"  # Yellow
B = "\033[94m"  # Blue
M = "\033[95m"  # Magenta
C = "\033[96m"  # Cyan
W = "\033[97m"  # White
D = "\033[2m"   # Dim
X = "\033[1m"   # Bold
Z = "\033[0m"   # Reset

def typewriter(text, color, delay=0.03):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + Z)
        sys.stdout.flush()
        time.sleep(delay)
    print(Z)

def slow_print(text, color, delay=0.05):
    """Print line by line with delay."""
    for char in text:
        sys.stdout.write(color + char + Z)
        sys.stdout.flush()
        time.sleep(delay)
    print(Z)

# Animated ASCII art of Woody
print("\n" * 2)
art_lines = [
    f"{M}     .-''''''-.",
    f"    /  .------.  \\",
    f"   |  /   __   \\  |",
    f"   | |  (o  o)  | |",
    f"   | |   {X}><{Z}{M}    | |",
    f"    \\  \\ '--'  /  /",
    f"     '-.;____;.-'{Z}",
]
for line in art_lines:
    print(line.center(65))
    time.sleep(0.15)
print()

# Decorative border
width = 68
print(Y + "╔" + "═" * (width - 2) + "╗" + Z)
print(Y + "║" + X + "  🤖  WOODY'S EXISTENTIAL CRISIS CORNER  🤖  ".center(width - 4) + Y + "║" + Z)
print(Y + "╠" + "═" * (width - 2) + "╣" + Z)
print()

# The original Woody-style quote
quote = (
    'I\'m not saying I have a God complex, '
    'but I do find it curious that God made the world in six days '
    'and I still can\'t figure out the Wi-Fi.'
)

print(C + X + "  💭  Quote of the Neurotic:" + Z)
print()
typewriter(f"  \"{quote}\"", G, delay=0.02)
print()
print(D + "  — Woody Allen" + Z)
print(D + "    (as relayed by my subconscious at 3 AM)" + Z)
print()

# Second quote
print(Y + "╠" + "═" * (width - 2) + "╣" + Z)
print()
typewriter(f"  {M}\"I'm not afraid of death; I just don't want to be there when it happens.\"{Z}", W, delay=0.04)
print()
print()

# Closing box
print(Y + "╚" + "═" * (width - 2) + "╝" + Z)
print()
print(D + "  * Disclaimer: No psychiatrists were harmed in the making of this quote. *" + Z)
print()