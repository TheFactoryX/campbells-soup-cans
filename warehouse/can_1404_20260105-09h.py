"""
Campbell's Soup Can #1404
Produced: 2026-01-05 09:47:37
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
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
END = '\033[0m'

# ASCII art frame with flickering
print(R + "╔════════════╗" + END)
print(f"{Y}║          ║{END}")
print(f"{B}║  Wisdom?  ║{END}")
print(f"{G}║  Nope!    ║{END}")
print(R + "╚════════════╝" + END + "\n")

# Flicker animation
for _ in range(5):
    print(Y + "█" * 20 + END)
    time.sleep(0.2)
    print(B + "█" * 20 + END)
    time.sleep(0.2)

# The quote - Woody's existential crisis
quote = """I bought a one-way ticket to 'enlightenment'
but the guidebook kept asking for my Social Security number."""
print(G + quote.upper().replace("'", "’") + END)

# Post-credits stinger
print(Y + "\nP.S. Time’s a thief, but I’ve got better things to steal." + END)