"""
Campbell's Soup Can #879
Produced: 2025-12-12 08:46:40
Worker: MoonshotAI: Kimi K2 0905 (exacto) (moonshotai/kimi-k2-0905:exacto)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import random

def typewriter(text, delay=0.04, color_code="\033[38;5;214m"):
    """Print text like a nervous typewriter."""
    for ch in text:
        print(color_code + ch + "\033[0m", end="")
        sys.stdout.flush()
        time.sleep(delay if ch != " " else 0.02)

def fade_in_line(line, color=226, steps=8):
    """Fade a line from dim to bright yellow like an old bulb warming up."""
    for i in range(1, steps + 1):
        intensity = 5 + int((255 - 5) * i / steps)
        print(f"\r\033[38;5;{color};2;{intensity};{intensity};0m{line}\033[0m", end="")
        sys.stdout.flush()
        time.sleep(0.08)
    print()

def neurotic_cursor(duration=0.6):
    """Make the cursor jitter like Woody deciding whether to exist."""
    for _ in range(int(duration * 10)):
        print("\033[?25l" if _ % 2 else "\033[?25h", end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\033[?25h", end="")

# ---- theatrical intro ----
print("\n" * 2)
fade_in_line("╔══════════════════════════════════════════════════════════════════════════════╗")
fade_in_line("║                        A Nervous Metaphysical Brief                        ║")
fade_in_line("╚══════════════════════════════════════════════════════════════════════════════╝")
print()

# ---- the quote itself ----
quote = (
    "I’d never join a club that would have me as a member,\n"
    "but Death keeps sending complimentary vouchers.\n"
    "I’m tempted to RSVP maybe—commitment issues, you know?"
)

for line in quote.splitlines():
    typewriter("  " + line)
    neurotic_cursor()

# ---- existential signature ----
print()
print(" " * 54 + "\033[3m— Woody.exe\033[0m")

# ---- glitchy flickering outro ----
for _ in range(3):
    glitch = random.choice(["BUFFERING MORTALITY…", "404 SOUL NOT FOUND", "CTRL+Z LIFE?"])
    print(f"\r\033[38;5;{random.randint(196,226)}m{glitch}\033[0m", end="")
    sys.stdout.flush()
    time.sleep(0.3)
print("\r" + " " * len(glitch) + "\r", end="")

print("\n" * 2)