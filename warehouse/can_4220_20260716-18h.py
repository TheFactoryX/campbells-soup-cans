"""
Campbell's Soup Can #4220
Produced: 2026-07-16 18:19:03
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
RESET = "\033[0m"

def typewriter_print(text, end="\n"):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.04)
    if end:
        print(end, end="")

# Title with sparkle
title = f"{CYAN}Woody's Cosmic One-Liner{RESET}"
typewriter_print("✨ " + title + " ✨\n", "")

# Top border
print(f"{YELLOW}╔════════════════════════════════════════════════════════════════╗{RESET}")

# Quote lines (colored)
quote_lines = [
    f"{GREEN}I'm terrified of the unknown, but I especially dread the known,{RESET}",
    f"{GREEN}because it's like a cosmic joke written in the language of random chance.{RESET}",
    f"{CYAN}(And yes, I'm pretty sure the punchline is \"you died again\").{RESET}",
]

# Print each line inside the box with a little star prefix
for line in quote_lines:
    print(f"{YELLOW}║{RESET} {CYAN}★{RESET} ", end="")
    typewriter_print(line, f"{YELLOW}║{RESET}\n")
    time.sleep(0.3)

# Bottom border
print(f"{YELLOW}╚════════════════════════════════════════════════════════════════╝{RESET}")

# Final quip
final = f"{YELLOW}...and that's just Tuesday morning.{RESET}"
typewriter_print(final + "\n", "")

# Keep output visible for a moment
time.sleep(2)