"""
Campbell's Soup Can #4970
Produced: 2026-09-16 06:02:31
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote, served with ANSI colors and a typewriter animation."""
import sys, time

# A neurotic, existential, slightly self‑deprecating Woody Allen quote
QUOTE = (
    "I'm not afraid of death. I just don't want to be there when it happens. "
    "Also, if the afterlife is just a really long, really awkward dinner party "
    "where I don't know anyone, I'm out."
)

# ANSI color codes (built‑in, no external deps)
COLORS = [
    "\033[91m",  # bright red
    "\033[93m",  # bright yellow
    "\033[94m",  # bright blue
    "\033[92m",  # bright green
    "\033[95m",  # magenta
    "\033[96m",  # cyan
    "\033[0m",   # reset
]

def woody_print(text, speed=0.03, color_idx=2):
    """Print text character‑by‑character with a neurotic splash of color."""
    color = COLORS[color_idx]
    for ch in text:
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\033[0m\n")

# A simple colorful ASCII‑style border
BORDER = "\033[93m+{}+\033[0m".format("=" * 60)

if __name__ == "__main__":
    print(BORDER)
    woody_print(QUOTE)
    print(BORDER)