"""
Campbell's Soup Can #4188
Produced: 2026-07-13 23:13:26
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"
RESET  = "\033[0m"

# Woody Allen‑style philosophical nugget
QUOTE = "I’m not afraid of death; I just don’t want to be there when it happens."

def typewriter(text, delay=0.03):
    """Print text one character at a time with a delay for dramatic effect."""
    for ch in text:
        sys.stdout.write(MAGENTA + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def print_boxed(message):
    """Print a message inside a colored ASCII box."""
    width = len(message) + 4
    border = f"{CYAN}+{'-' * (width - 2)}{RESET}"
    inside = f"{CYAN}| {message} |{RESET}"
    print(border)
    print(inside)
    print(border)

# ----- Main visual display -----
print("\n")
print_boxed(QUOTE)
typewriter("\n — Woody Allen vibes\n")
time.sleep(0.2)
typewriter(" (in a perfectly neurotic whisper)\n")