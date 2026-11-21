"""
Campbell's Soup Can #5265
Produced: 2026-11-21 17:33:02
Worker: Nex AGI: Nex-N2.5-Mini (nex-agi/nex-n2.5-mini)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import sys
import time
from textwrap import fill

RESET = "\033[0m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
GRAY = "\033[90m"

quote = (
    "Existence is like being handed a cosmic lottery ticket that was already drawn, "
    "with your name misspelled on it. I've decided not to panic—though I have scheduled three separate panics, just in case one of them works."
)

width = 58

print(f"\n{GRAY}      .-~~~-.{RESET}")
print(f"{GRAY}   .-(       ).{RESET}")
print(f"{GRAY}  (__.__)__)__) {CYAN}☁{RESET}")

print(f"{CYAN}╔{'═' * width}╗{RESET}")
for line in fill(quote, width=width).splitlines():
    print(f"{CYAN}║{RESET} {YELLOW}{line:<{width}}{RESET} {CYAN}║{RESET}")
print(f"{CYAN}╚{'═' * width}╝{RESET}")

time.sleep(0.15)