"""
Campbell's Soup Can #4779
Produced: 2026-08-23 03:15:29
Worker: OpenAI: GPT-5.6 Luna Pro (openai/gpt-5.6-luna-pro)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

RESET = "\033[0m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
DIM = "\033[2m"
BOLD = "\033[1m"

quote = (
    "I tried to find the meaning of life, but the universe put me on hold—"
    "and I was too anxious to hang up."
)

width = 64
lines = textwrap.wrap(quote, width=width - 8)
box_width = max(len(line) for line in lines) + 6

sys.stdout.write("\033[2J\033[H")
for symbol in "·oO0Oo·":
    sys.stdout.write(f"\r{DIM}{CYAN}Consulting the cosmos {symbol}{RESET}")
    sys.stdout.flush()
    time.sleep(0.08)

sys.stdout.write("\r" + " " * 32 + "\r")
sys.stdout.write(f"{MAGENTA}╔{'═' * box_width}╗{RESET}\n")
sys.stdout.write(f"{MAGENTA}║{RESET}{' ' * box_width}{MAGENTA}║{RESET}\n")

for line in lines:
    padding = box_width - len(line) - 4
    sys.stdout.write(
        f"{MAGENTA}║{RESET}  {YELLOW}{line}{RESET}"
        f"{' ' * padding}  {MAGENTA}║{RESET}\n"
    )

sys.stdout.write(f"{MAGENTA}║{RESET}{' ' * box_width}{MAGENTA}║{RESET}\n")
sys.stdout.write(f"{MAGENTA}╚{'═' * box_width}╝{RESET}\n")