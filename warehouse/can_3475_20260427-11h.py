"""
Campbell's Soup Can #3475
Produced: 2026-04-27 11:59:35
Worker: inclusionAI: Ling-2.6-1T (free) (inclusionai/ling-2.6-1t:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    print()

def sparkle():
    sparkles = ['✨', '🌟', '💫', '⭐', '🔮']
    return random.choice(sparkles)

def nervous_pulse():
    beats = ['❤️ ', '💔 ', '😰 ', '😅 ', '🥵 ', '🥶 ']
    return random.choice(beats)

print("\033[2J\033[H")  # Clear screen

# Animated border
border_color = 35  # Magenta
for i in range(40):
    print(color("░", border_color), end="", flush=True)
    time.sleep(0.02)
print()

# Title
title = " EXISTENTIAL CRISIS: THE WOODY ALLEN EDITION "
print(color(" " * ((40 - len(title)//2))), end="")
print(color(title, 33))  # Yellow

for i in range(40):
    print(color("▒", border_color), end="", flush=True)
    time.sleep(0.02)
print("\n")

# Draw a neurotic ASCII brain
brain = [
    "     " + color("＿＿", 36) + color("＿", 36) + color("＿", 36) + color("＿＿", 36),
    "   " + color("／", 36) + color("  ", 31) + color("＞", 36) + color("  ", 31) + color("＼", 36),
    "  " + color("／", 36) + color(" （", 31) + color("＿", 36) + color("） ", 31) + color("＼", 36),
    " " + color("／", 36) + color("／", 36) + color("／", 31) + color("  ", 36) + color("＼", 31) + color("＼", 36) + color("＼", 36),
    " " + color("／", 36) + color("／", 36) + color("／", 36) + color("|", 31) + color(" ＼", 36) + color("＼", 36) + color("＼", 36),
    " " + color("＼", 36) + color("＼", 36) + color("＼", 36) + color("--", 31) + color("＼", 36) + color("＼", 36) + color("＼", 36),
    " " + color("＼", 36) + color("＼", 36) + color("＿", 36) + color("＿＿", 31) + color("＿", 36) + color("＼", 36) + color("＼", 36),
    "   " + color("＼", 36) + color("＿", 36) + color("＿＿", 31) + color("＿", 36) + color("＼", 36),
    "     " + color("＼＿＿＿＿＿＿＿＿", 36),
]

for line in brain:
    print("    " + line)
    time.sleep(0.05)

print()

# The Quote Box
quote = (
    "I've been having the most terrible nightmares — I dream I'm a "
    "conscious being in an indifferent universe, and then I wake up "
    "and realize it's actually Tuesday and I haven't vacuumed since "
    "the Clinton administration, and my existential dread has now "
    "developed a separate dental plan."
)

words = quote.split()
current_line = ""
lines = []

for word in words:
    if len(current_line + word) < 50:
        current_line += word + " "
    else:
        lines.append(current_line)
        current_line = word + " "
if current_line:
    lines.append(current_line)

# Print quote in a box
box_width = 58
print(color("╔" + "═" * box_width + "╗", 36))
for i, line in enumerate(lines):
    padded = f" {line:<{box_width-2}} "
    if i == 0:
        print(color("║", 36) + color(padded, 33) + color("║", 36))
        print(color("╟" + "─" * box_width + "╢", 36))
    elif i == len(lines) - 1:
        print(color("║", 36) + color(padded, 33) + color("║", 36))
    else:
        print(color("║", 36) + color(padded, 33) + color("║", 36))
print(color("╚" + "═" * box_width + "╝", 36))

# Signature with animation
print()
time.sleep(0.5)
typewriter("      — Woody Allen (probably, while hyperventilating)", 0.05)

# Footer decorations
print()
for i in range(40):
    print(color(nervous_pulse(), random.choice([31, 33, 35, 32])), end="", flush=True)
    time.sleep(0.03)
print()

for i in range(40):
    print(color(sparkle(), 33), end="", flush=True)
    time.sleep(0.02)
print()

# Neurotic footer note
footnote = "Note: If you enjoyed this, my therapist hasn't returned my calls either."
print(color("  " + footnote, 90))
print()