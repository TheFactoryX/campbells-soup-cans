"""
Campbell's Soup Can #3217
Produced: 2026-04-10 09:38:33
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI color codes
RESET = "\033[0m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

# Woody Allen‑style philosophical quote
quote = "I spent hours pondering existence, then ordered pizza, and realized I was just hungry."

def typewriter_effect(s, delay=0.03):
    """Print text one character at a time for a simple animation."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.flush()

# Compute interior width to frame the quote nicely
width = len(quote) + 4  # accounts for surrounding spaces and pipes

# Top border
print(f"{YELLOW}+{'-'*width}+{RESET}")

# Middle line: left pipe, space, quote (typewritten in cyan), space, right pipe
sys.stdout.write(f"{YELLOW}|{RESET} ")
typewriter_effect(f"{CYAN}{quote}{RESET}")
sys.stdout.write(f" {RESET}|{RESET}\n")

# Bottom borderprint(f"{YELLOW}+{'-'*width}+{RESET}")