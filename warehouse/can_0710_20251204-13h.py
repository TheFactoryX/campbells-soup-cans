"""
Campbell's Soup Can #710
Produced: 2025-12-04 13:49:21
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

# Woody Allen's existential crisis
quote = "I'm not afraid of dying—I just hate the idea of being asked about it at a wake."

# ASCII art frame with color
frame = f"""
{YELLOW}┌────────────────────────────────────────┐{RESET}
│ {GREEN}!{RESET} {quote} {YELLOW}!{RESET} │
└────────────────────────────────────────┘
"""

print(frame)

# Blinking "WOODY" sign animation
woody = "WOODY"
try:
    while True:
        print(f"{YELLOW}{woody}{RESET}", end="\r")
        time.sleep(0.3)
        print(f"{RED}{woody}{RESET}", end="\r")
        time.sleep(0.3)
except KeyboardInterrupt:
    print("\n" + RESET)