"""
Campbell's Soup Can #5017
Produced: 2026-09-24 15:07:07
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
import os

# ANSI escape codes
R = '\033[91m'; G = '\033[92m'; Y = '\033[93m'; B = '\033[94m'
M = '\033[95m'; C = '\033[96m'; W = '\033[97m'; D = '\033[2m'
X = '\033[0m'; H = '\033[1m'; S = '\033[7m'

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Print neurotic Woody Allen ASCII art
print(f"""
{H}{R}        .-''''''''-.{X}
{R}       /            \\{X}
{Y}      |   Woody      |{X}
{C}      |    Allen     |{X}
{G}      |  (neurotic)  |{X}
{B}       \\   ... ...  /{X}
{M}        '-........-'{X}
""")
time.sleep(0.5)

# The quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Rainbow typewriter effect
colors = [R, Y, G, C, B, M]
print("  ", end="", flush=True)
time.sleep(0.3)
for i, char in enumerate(quote):
    sys.stdout.write(colors[i % len(colors)] + char + X)
    sys.stdout.flush()
    time.sleep(0.025)
print()
time.sleep(0.5)

# Decorative box around author
author = "— Woody Allen"
box_w = len(author) + 4
print(f"\n  {D}{'═' * box_w}{X}")
print(f"  {D}║{X} {H}{C}{author}{X} {D}║{X}")
print(f"  {D}{'═' * box_w}{X}")
time.sleep(0.3)

# Neurotic footer
footer = "...and now I shall lie awake at 3am reconsidering everything."
print(f"\n  {D}{M}{footer}{X}\n")
time.sleep(0.5)

# Final existential pulse
print(f"  {H}{R}∩{X}{Y}＿_{X}{G}＼{X}{C}o{X}{B}ｏ{X}{M}ｕ{X}{R}l{X}{Y}＿{X}{G}／{X}")
print(f"  {D}existential dread in 48 colors{X}\n")