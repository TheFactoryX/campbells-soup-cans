"""
Campbell's Soup Can #986
Produced: 2025-12-17 05:38:49
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os
import re
import shutil

def print_centered(text, term_width):
    try:
        # Remove ANSI codes for proper centering
        clean_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
        spaces = (term_width - len(clean_text)) // 2
        return ' ' * spaces + text
    except:
        return text.center(term_width)

# ANSI color codes
BLUE_BG = '\033[44m'
YELLOW = '\033[33m'
BLACK = '\033[30m'
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'

# Get terminal width
try:
    term_width = max(40, shutil.get_terminal_size().columns)
except:
    term_width = 80

# Berserk quote (Woody Allen style)
quote = (
    "I'm trying to decide if I should look for a lifelong partner--with the two of us arguing 20 hours a day, "
    "we'll never notice how completely pointless everything is."
)

# ASCII art of Woody Allen
woody_ascii = f"""
{YELLOW}         __________
{YELLOW}        /{RESET}          \\
{YELLOW}       /             \\
{YELLOW}      |           {BLACK}/{RESET}/{BLACK}\       |
{YELLOW}      |   {BLACK}o    o{RESET} {BLACK}_{RESET}       |
{YELLOW}      |     {BLACK}({RESET}..{BLACK}) {RESET}_     |
{YELLOW}      \\      {BLACK}__\\{RESET}   {BLACK}/|
{YELLOW}       \\________{BLACK}/_|{RESET}\\
        {YELLOW}  Cocky, Self-Destructive, And...Woody Allen
"""

# Setup frames for animation
frames = [
    "        /    |    \\", 
    "       /     |     \\", 
    "      /      |      \\", 
    "     /       |       \\", 
    "    /        |        \\"
]
loading = ["  Searching for my meaning...", "  Checking with psychiatry...", "  Analyzing existence..."]

# Animations
print(warning := print_centered(f"{BOLD}{YELLOW}** WARNING: DYING FOR SOME QI 🧠 \\|/**", term_width))
print(dwight := print_centered(f"{ITALIC}{RESET}An existence exploring venture...", term_width))
for i in range(3):
    print_centered(' ' * ((term_width - len(frames[i//3])) // 2) + frames[i//3] + ' ' * ((term_width - len(frames[i//3])) // 2))
    time.sleep(0.3)
print_centered(print_centered(f"{BOLD}{RESET}" + " " * ((term_width - len(loading[i])) // 2) + loading[i]) for i in range(3))
time.sleep(1)
print(len(warning) * '\r', end='', file=sys.stderr)
print(len(dwight) * '\r', end='', file=sys.stderr)
for _ in range(4):
    print('\r', end='', file=sys.stderr)
    time.sleep(0.4)

# Final display
print('\n' * 8)
print_centered(woody_ascii, term_width)
print()
print_centered(print_centered(f"{BLUE_BG}{BOLD}{RESET}" + " " * 2 + quote + " " * 2) for _ in range(term_width))
print()

# Sparkle effect
for i in range(10):
    dots = random.randint(1, 3)
    stars = random.randint(0, 2)
    print('\n' + ' ' * ((term_width - (dots + stars)) // 2) + '.' * dots + ' ' * random.randint(0, 3) + '*' * stars)
    time.sleep(0.4)

print()
print_centered(f"{BLUE_BG}{BOLD}{YELLOW}--- Philosophy by Woody Allen ---{RESET}", term_width)
print_centered(f"{BLUE_BG}{BOLD}{YELLOW}A nihilistic salad with extra suffering{RESET}", term_width)