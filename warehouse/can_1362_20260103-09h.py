"""
Campbell's Soup Can #1362
Produced: 2026-01-03 09:33:27
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody.py - A Woody Allen-style existential lament with flair

# Define ANSI escape codes for colorful formatting
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"
RESET = "\033[0m"

# The quote, divided into three lines for the box layout
quote = [
    "\u001b[33m\"I once tried to find meaning in life, but\033[0m",
    "\u001b[33m\"I found only a receipt for a really expensive \"",
    "\u001b[33m\"therapist session. - \033[35mWoody, 1956\033[0m\""
]

# Print a colorful box around the quote
print(f"{RED}\u250c\033[0m ┌───────────────────────────────┐\u2510{RESET}")
for line in quote:
    padded = line.center(35, " ")
    print(f"{BLUE}\u2502 \033[0m{padded}\033[32m│\033[0m ")
print(f"{RED}\u2517\033[0m └───────────────────────────────┘\u2518{RESET}")

# Optional: add a playful ASCII art of Woody Allen's existential mask
print(f"\n{WHITE}"
         "        ___/\\_..
         _(__,//   {}
         (oo)\\                ╲ ╲"
         "  ʘ ʘ" +
         ERASE