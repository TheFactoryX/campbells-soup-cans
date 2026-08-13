"""
Campbell's Soup Can #4562
Produced: 2026-08-13 05:04:46
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote, rainbow‑styled."""
import time
import sys

QUOTE = ("I'm not afraid of death. I'm just afraid of "
         "dying before I figure out why I walked into this room, "
         "only to forget why I came.")

RESET = "\033[0m"
COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]

def typewriter(text, speed=0.02):
    """Print text character‑by‑character with cycling colors —
    like a neurotic thought stream short‑circuiting in real time."""
    for i, ch in enumerate(text):
        color = COLORS[i % len(COLORS)]
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print(RESET)

if __name__ == "__main__":
    print("...loading existential crisis...", flush=True)
    time.sleep(0.7)
    typewriter(QUOTE)