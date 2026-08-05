"""
Campbell's Soup Can #4438
Produced: 2026-08-05 06:41:44
Worker: Ling-3.0-flash (free) (inclusionai/ling-3.0-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic, existential, Woody Allen–style philosophical experience.
Pure Python. No dependencies. Just colors, ASCII art, and anxiety.
"""

import time
import sys
import math

# ── ANSI escape codes ──────────────────────────────────────────────
RED     = '\033[91m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
GREEN   = '\033[92m'
MAGENTA = '\033[95m'
CYAN    = '\033[96m'
WHITE   = '\033[97m'
BOLD    = '\033[1m'
DIM     = '\033[2m'
RESET   = '\033[0m'
BG_BLUE = '\033[44m'
BG_RED  = '\033[41m'

def clear():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def print_slow(text, color='', delay=0.025):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_fast(text, color=''):
    print(color + text + RESET)

# ── ASCII Art: Woody Allen (sort of) ──────────────────────────────
def draw_woody():
    art = f"""
{RED}{BOLD}
          .---.
         / o o \\
        |  >-<  |
         \\ '-' /
          '---'
         ( ¯\\\\_（ツ）_/¯ )
{RESET}"""
    return art

# ── The Quote ──────────────────────────────────────────────────────
quote = (
    "I've been in therapy for years. "
    "My therapist says I have "
    f"{RED}{BOLD}existential dread{RESET}"
    f"{YELLOW} — I call it my hobby. "
    "The meaning of life? I don't know. "
    "But I do know that if I die today, "
    "I will be disappointed "
    f"{CYAN}— not because I didn't accomplish enough, "
    f"but because I didn't eat enough bagels.{RESET}"
)

# ── Decorative box ─────────────────────────────────────────────────
def draw_box(width):
    top    = '╔' + '═' * (width - 2) + '╗'
    middle = '║' + ' ' * (width - 2) + '║'
    bottom = '╚' + '═' * (width - 2) + '╝'
    return top, middle, bottom

# ── Main Show ──────────────────────────────────────────────────────
clear()
print()
print_slow(draw_woody(), MAGENTA, 0.01)
print()

# Animated title
title = "🎬  A Woody Allen Philosophy Moment  🎬"
print_slow(title, BOLD + CYAN, 0.04)
print()

# Draw the box
box_w = max(len(quote) + 4, 60)
top, middle, bottom = draw_box(box_w)

print(GREEN + top + RESET)
print(GREEN + middle + RESET)

# Print quote line by line with color accents
words = quote.split(' ')
line = ''
for word in words:
    test_line = line + ' ' + word if line else word
    if len(test_line) > box_w - 6:
        # Print current line centered in box
        padded = line.center(box_w - 2)
        print(GREEN + '║ ' + BOLD + padded + RESET + GREEN + ' ║' + RESET)
        line = word
    else:
        line = test_line
# Print last line
if line:
    padded = line.center(box_w - 2)
    print(GREEN + '║ ' + BOLD + padded + RESET + GREEN + ' ║' + RESET)

print(GREEN + middle + RESET)

# ── The punchline ──────────────────────────────────────────────────
punchline = f"{YELLOW}{BOLD}  \"I am not afraid of death. I just don't want to be there when it happens — \"{RESET}"
punchline2 = f"{YELLOW}{BOLD}   especially if there's no Wi-Fi.\"{RESET}"
print_slow(punchline, YELLOW + BOLD, 0.03)
time.sleep(0.3)
print_slow(punchline2, YELLOW + BOLD, 0.03)
print()

# ── Fading existential crisis ──────────────────────────────────────
crisis_lines = [
    f"{RED}  Is this all there is?{RESET}",
    f"{CYAN}  ...probably.{RESET}",
    f"{BLUE}  But at least we have WiFi.{RESET}",
    f"{GREEN}  And bagels.{RESET}",
    f"{MAGENTA}  {BOLD}  We are all just nervous apes{RESET}",
    f"{MAGENTA}  {BOLD}   trying to find meaning in a bagel.{RESET}",
]

for cline in crisis_lines:
    print_slow(cline, '', 0.15)

print()

# ── Animated sparkle ───────────────────────────────────────────────
sparkles = ['✨', '💫', '🌟', '✨', '💫', '🌟']
for _ in range(3):
    for s in sparkles:
        sys.stdout.write(BOLD + CYAN + f'  {s}  ' + RESET)
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b')
        sys.stdout.flush()
    time.sleep(0.1)

print()
print_slow(f"{BOLD}{WHITE}  — Woody Allen would be proud (or at least anxious).{RESET}", DIM, 0.02)
print()

# ── Footer ─────────────────────────────────────────────────────────
print(BLUE + '  ╭──────────────────────────────────────╮' + RESET)
print(BLUE + '  │  ' + DIM + 'Stay neurotic. Stay curious.' + RESET + '       │' + RESET)
print(BLUE + '  │  ' + DIM + 'Life is short. Eat the bagel.' + RESET + '       │' + RESET)
print(BLUE + '  ╰──────────────────────────────────────╯' + RESET)
print()

# Final cursor blink
sys.stdout.write(BOLD + RED + '  █' + RESET)
sys.stdout.flush()
time.sleep(0.3)
sys.stdout.write('\b \b')
sys.stdout.flush()
print()
print()