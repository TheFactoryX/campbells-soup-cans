"""
Campbell's Soup Can #2153
Produced: 2026-02-10 15:34:49
Worker: Writer: Palmyra X5 (writer/palmyra-x5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
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
def typewrite(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Random color from list
def random_color():
    return random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE])

# Build Woody Allen-style quote
quote = "I'm not exactly sure what I'm doing here, philosophically speaking—probably overanalyzing my anxiety about not mattering in a universe that doesn't care, which ironically gives me purpose."

# ASCII thought bubble with neurotic spiral
thought_bubble = [
    "     ╭───────────────────────────────────────────────╮",
    "     │                                               │",
    "     │         ∞  ∞∞  ∞   ∞∞∞   ∞  ∞∞  ∞   ∞∞∞       │",
    "     │       ∞   ∞  ∞  ∞ ∞      ∞   ∞  ∞ ∞ ∞          │",
    "     │       ∞   ∞  ∞  ∞ ∞∞∞    ∞   ∞  ∞ ∞ ∞∞∞        │",
    "     │        ∞  ∞  ∞  ∞ ∞      ∞   ∞  ∞ ∞ ∞          │",
    "     │         ∞ ∞  ∞   ∞∞∞      ∞ ∞  ∞   ∞∞∞         │",
    "     │                                               │",
    "     ╰───────────────────────────────────────────────╯"
]

# Print animated spiral header
print("\n" * 5)
for i, line in enumerate(thought_bubble):
    color = random_color()
    print(f"{' ' * (5 + i//2)}{color}{line}{ENDC}")
    time.sleep(0.2)

# Flashing existential crisis indicator
sys.stdout.write("  ")
for _ in range(6):
    sys.stdout.write(f"{RED}⚡{ENDC}")
    sys.stdout.write(f"{YELLOW}⚡{ENDC}")
    sys.stdout.flush()
    time.sleep(0.15)
    sys.stdout.write('\b\b\b\b\b\b      ')
    sys.stdout.flush()
    time.sleep(0.1)

print(f"\n{BOLD}{MAGENTA}WOODY ALLEN PRESENTS:{ENDC}\n")

# Type out the quote like a nervous monologue
typewrite(f"{BLUE}{BOLD}{quote}{ENDC}", 0.04)

# Add neurotic footnote
time.sleep(1)
footnote = f"{YELLOW}(I probably shouldn’t have said that. Now I’ll lie awake wondering if it made me sound pompous. Also, is 'overanalyzing' a real word?){ENDC}"
for i in range(len(footnote)):
    sys.stdout.write(footnote[i])
    sys.stdout.flush()
    time.sleep(0.03 if footnote[i] not in " .,?" else 0.1)

# Final dramatic pause
time.sleep(1.5)
print(f"\n{CYAN}— Probably Woody, if he were thinking too hard on a sleepless Tuesday{ENDC}\n")