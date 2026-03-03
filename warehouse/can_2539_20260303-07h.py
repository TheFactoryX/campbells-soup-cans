"""
Campbell's Soup Can #2539
Produced: 2026-03-03 07:54:59
Worker: Anthropic: Claude Opus 4.1 (anthropic/claude-opus-4.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time
import sys

# ANSI color codes
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# Woody Allen style quote
quote = "My therapist says I have a preoccupation with vengeance. We'll see about that."
author = "~ Woody Allen (probably)"

# ASCII art glasses (Woody's signature look)
glasses = f"""
{CYAN}     ___..._     _...___
   .::o:::::.   .::o::::.
  :::::::::::   :::::::::::
  ::::::::::'   '::::::::::'
  ':::::::'       ':::::::'
{RESET}
"""

def typewriter_effect(text, color=WHITE, delay=0.05):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(text, color=YELLOW):
    """Draw a fancy box around text"""
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    
    print(color + "╔" + "═" * (max_length + 2) + "╗" + RESET)
    for line in lines:
        print(color + "║ " + RESET + line.ljust(max_length) + color + " ║" + RESET)
    print(color + "╚" + "═" * (max_length + 2) + "╝" + RESET)

def neurotic_loading():
    """Simulate Woody's neurotic thinking process"""
    thoughts = [
        "Contemplating existence",
        "Questioning reality",
        "Overthinking everything",
        "Having an existential crisis",
        "Consulting my therapist",
        "Taking antacids"
    ]
    
    for thought in thoughts:
        print(f"{DIM}{MAGENTA}  {thought}...{RESET}", end='')
        for _ in range(3):
            time.sleep(0.3)
            print(".", end='', flush=True)
        print("\r" + " " * 50 + "\r", end='')  # Clear line
    
# Main show
print("\n" * 2)
print(glasses)

# Title with style
title = f"{BOLD}{RED}╔══════════════════════════════════════════════╗{RESET}"
title2 = f"{BOLD}{RED}║  WISDOM FROM A NEUROTIC NEW YORKER'S MIND   ║{RESET}"
title3 = f"{BOLD}{RED}╚══════════════════════════════════════════════╝{RESET}"

print(title)
print(title2)
print(title3)
print()

# Neurotic loading animation
neurotic_loading()

# Build up to the quote
print(f"{DIM}{BLUE}*adjusts glasses nervously*{RESET}")
time.sleep(1)
print(f"{DIM}{BLUE}*clears throat*{RESET}")
time.sleep(1)
print()

# The quote with dramatic effect
print(f"{BOLD}{YELLOW}\"", end='')
typewriter_effect(quote, CYAN, 0.08)
print(f"{BOLD}{YELLOW}\"{RESET}")

print()
time.sleep(1)

# Author attribution with style
for char in author:
    if char == '~':
        sys.stdout.write(f"{MAGENTA}{char}{RESET}")
    elif char in "()":
        sys.stdout.write(f"{DIM}{WHITE}{char}{RESET}")
    else:
        sys.stdout.write(f"{GREEN}{char}{RESET}")
    sys.stdout.flush()
    time.sleep(0.05)

print("\n")

# Final neurotic disclaimer
disclaimer = f"""
{DIM}{WHITE}* This quote may or may not have been said by Woody Allen.
* If it wasn't, my therapist will hear about this.
* I should probably call my therapist anyway.{RESET}
"""

print(disclaimer)

# Animated anxiety dots at the end
print(f"{DIM}{MAGENTA}Experiencing mild panic", end='')
for _ in range(5):
    time.sleep(0.4)
    print(".", end='', flush=True)
print(f"{RESET}\n")