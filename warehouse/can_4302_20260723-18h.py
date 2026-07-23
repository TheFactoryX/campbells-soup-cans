"""
Campbell's Soup Can #4302
Produced: 2026-07-23 18:37:06
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# Woody Allen style quote with existential dread and self-deprecation
QUOTE = [
    "I tried meditation today...",
    "It's terrifying. Just sitting there",
    "with nothing but your thoughts.",
    "",
    "My brain immediately starts replaying",
    "every awkward conversation I've ever had.",
    "",
    "I asked my therapist if this is normal.",
    "She said, 'Yes, you're having a normal anxiety attack.'",
    "",
    "So I left and had another one in the elevator.",
    "",
    "At least elevators are quick.",
    "Unlike eternity. Eternity takes forever.",
    "And that's if you're lucky."
]

COLORS = [
    "\033[95m",  # purple
    "\033[96m",  # cyan
    "\033[94m",  # blue
    "\033[93m",  # yellow
    "\033[92m",  # green
]

RESET = "\033[0m"

def print_woody_quote():
    max_len = max(len(line) for line in QUOTE) + 2
    border = "═" * (max_len + 2)
    
    sys.stdout.write("\n\033[1;37m╔" + border + "╗\n")
    for i, line in enumerate(QUOTE):
        color = COLORS[i % len(COLORS)]
        padding = max_len - len(line)
        sys.stdout.write(f"\033[1;37m║\033[0m")
        sys.stdout.write(f"{color}{line}{' ' * padding}{RESET}")
        sys.stdout.write(f"\033[1;37m║\n")
        time.sleep(0.15)
        sys.stdout.flush()
    sys.stdout.write("\033[1;37m╚" + border + "╝\n" + RESET)

if __name__ == "__main__":
    print("\n" * 2)
    time.sleep(0.3)
    print_woody_quote()
    time.sleep(0.5)
    print("\033[91m*nervous laughter echoes into the void*\n" + RESET)