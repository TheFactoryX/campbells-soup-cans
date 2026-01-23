"""
Campbell's Soup Can #1794
Produced: 2026-01-23 11:41:08
Worker: Qwen: Qwen3 235B A22B Instruct 2507 (qwen/qwen3-235b-a22b-2507)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'

# Fun typewriter effect
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Random color for each word
def rainbow_text(text):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    colored = ""
    for char in text:
        if char != ' ':
            colored += random.choice(colors) + char + ENDC
        else:
            colored += ' '
    return colored

# Animated coffee cup ASCII art
def print_coffee_art():
    art = """
        {0}  ( (
        ) )     {1}┌───────────────────────┐
    {0}  ........{1}│{2}   WOODY'S ANGST CAFE {1}│
    {0}  |      |{1}│{3}  Est. 1965 (probably {1}│
    {0}  |      |{1}│{4}   doomed to fail)     {1}│
    {0}_ |||||_{1} └───────────────────────┘
    {5}  \_________/  
    """.format(BLUE, MAGENTA, BOLD+YELLOW, WHITE, GREEN, RED)
    print(art)

# Clear screen (works in most terminals)
sys.stdout.write('\033[2J\033[H')  # Clear and move cursor to top

# Print header with animation
print(f"\n{BOLD}{YELLOW}─" * 60 + ENDC)
typewriter(f"{BOLD}{MAGENTA}     A MOMENT OF WOODY ALLEN WISDOM", 0.08)
print(f"{YELLOW}─" * 60 + ENDC)

# Show coffee art dramatically
time.sleep(0.5)
print_coffee_art()
time.sleep(1)

# The quote with typewriter effect
quote = "I'm not obsessed with mortality; I just think about it constantly, like every 8 seconds—mostly because I'm bad at crossword puzzles and need to occupy my brain with something equally unsolvable."

print(f"\n{BOLD}{CYAN}  🌀  EXISTENTIAL REALIZATION DETECTED  🌀{ENDC}\n")
time.sleep(0.5)

# Print quote word by word with random colors
words = quote.split()
colored_quote = " ".join([f"{random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])}{word}{ENDC}" for word in words])
typewriter(f"  {BOLD}{WHITE}“{ENDC}" + colored_quote + f"{BOLD}{WHITE}”{ENDC}", 0.07)

# Print attribution with blink effect (simulate blinking neon)
print()
for i in range(3):
    sys.stdout.write(f"  {BOLD}{RED}   — Woody Allen (probably while avoiding eye contact){ENDC}")
    sys.stdout.flush()
    time.sleep(0.4)
    sys.stdout.write('\r' + ' ' * 65 + '\r')
    sys.stdout.flush()
    time.sleep(0.2)
print(f"  {BOLD}{MAGENTA}   — Woody Allen (probably while avoiding eye contact){ENDC}")

# Footer with existential dread
time.sleep(1)
print(f"\n{YELLOW}─" * 60 + ENDC)
typewriter(f"{BOLD}{CYAN}  Remember: If nothing matters, does that mean my therapist overcharges?{ENDC}", 0.06)
print(f"{YELLOW}─" * 60 + ENDC + "\n")

# Final blinky dot
for _ in range(5):
    sys.stdout.write(f"{RED}    ✦{ENDC}")
    sys.stdout.flush()
    time.sleep(0.3)
    sys.stdout.write('\r    ' + ' ' + '\r')
    sys.stdout.flush()
    time.sleep(0.2)

print()