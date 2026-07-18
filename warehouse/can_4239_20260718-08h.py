"""
Campbell's Soup Can #4239
Produced: 2026-07-18 08:58:36
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes (no external libs)
C_RED  = "\033[31m"
C_GREEN= "\033[32m"
C_YELLOW=\033[33m
C_BLUE =\033[34m
C_MAG  =\033[35m
C_CYAN = "\033[36m"
C_WHITE= "\033[37m"
R_RESET= "\033[0m"

# The Woody Allen‑style philosophical quote
QUOTE = "I’m not afraid of death; I just don’t want to be there when it happens, because then I’d miss the punchline of life."

# Simple decorative box edges
BORDER = "✦" * 55
TOP    = f"{C_MAG}{BORDER}{R_RESET}"
BOTTOM = f"{C_MAG}{BORDER}{R_RESET}"

def typewriter(text, color=C_CYAN, delay=0.03):
    """Prints text one character at a time with a delay for a typing effect."""
    for ch in text:
        sys.stdout.write(color + ch + R_RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Animate the border, then the quote, then finish the box
sys.stdout.write(f"{TOP}\n")
typewriter(QUOTE, color=C_YELLOW)
sys.stdout.write(f"{BOTTOM}\n")