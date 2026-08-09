"""
Campbell's Soup Can #4494
Produced: 2026-08-09 07:16:29
Worker: Z.ai: GLM 5 (z-ai/glm-5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
GREEN = '\033[92m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

def typewriter(text, delay=0.03):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def center_text(text, width=60):
    """Center text within given width"""
    return text.center(width)

# The quote
quote = "They say God doesn't give you more than you can handle. Clearly, God has never seen me try to assemble IKEA furniture while questioning the meaning of existence."

# Clear screen and set up
print('\033[2J\033[H')

# Animated border appearing
print()
border = "▓" * 62
for i in range(3):
    print(f'{DIM}{CYAN}{border}{RESET}')
    time.sleep(0.15)
    print(f'{DIM}{MAGENTA}{border}{RESET}')
    time.sleep(0.15)

print()
time.sleep(0.3)

# Title with styling
title = f"{BOLD}{YELLOW}✧ WOODY'S EXISTENTIAL CRISIS CORNER ✧{RESET}"
print(center_text(title))
print()

# Decorative line
print(f'{DIM}{"─" * 62}{RESET}')
print()

# The quote with typewriter effect in green
print(f'{GREEN}{BOLD}', end='')
typewriter(f'"{quote}"', 0.025)

print()
time.sleep(0.2)

# Attribution
print(f'{DIM}{"─" * 62}{RESET}')
print()
attrib = f"{DIM}{CYAN}— A neurotic thought, probably overthinking it{RESET}"
print(center_text(attrib))

print()

# Pulsing bottom border
for i in range(3):
    print(f'{DIM}{YELLOW}{border}{RESET}')
    time.sleep(0.2)
    print(f'{DIM}{GREEN}{border}{RESET}')
    time.sleep(0.2)

# Final blink
print()
time.sleep(0.3)
print(f'{BOLD}{MAGENTA}{"▼".center(62)}{RESET}')
time.sleep(0.2)
print(f'{BOLD}{RED}{"▼".center(62)}{RESET}')

print()