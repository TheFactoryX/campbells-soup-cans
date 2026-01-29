"""
Campbell's Soup Can #1924
Produced: 2026-01-29 13:32:55
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI colour codes
RED  = "\033[91m"
GREEN= "\033[92m"
YELLOW=\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# The quote – classic Woody Allen neurotic existentialism
quote = ("I’m not afraid of death; I just don’t want to be there when it happens, "
         "but I am terrified that the afterlife will be a terrible stand‑up set.")

# A little typewriter animation for drama
def typewriter(s, delay=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Build a colourful, bordered frame
width = len(quote) + 4
border_top    = f"{GREEN}+{'-'*width}+{RESET}"
border_bottom = f"{GREEN}+{'-'*width}+{RESET}"
border_middle = f"{YELLOW}|{RESET} {' '*width} |{YELLOW}{RESET}"

# Print the animated, colourful box
print(border_top)
print(border_middle)
typewriter(f"{MAGENTA}{quote}{RESET}", delay=0.02)
print(border_middle)
print(border_bottom)

# Optional extra flourish: a blinking "Enter the void" sign
def blink(text, times=3, delay=0.5):
    for _ in range(times):
        sys.stdout.write(f"{RED}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\b\b\b\b\b\b\b\b")  # erase
        sys.stdout.flush()
        time.sleep(delay)

blink("Enter the void...", times=2, delay=0.4)