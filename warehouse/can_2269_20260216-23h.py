"""
Campbell's Soup Can #2269
Produced: 2026-02-16 23:44:58
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, sys

# ANSI escape codes
RESET  = "\033[0m"
BOLD   = "\033[1m"
UNDERLINE = "\033[4m"
FG_RED    = "\033[31m"
FG_GREEN  = "\033[32m"
FG_YELLOW = "\033[33m"
FG_BLUE   = "\033[34m"
FG_MAGENTA = "\033[35m"

def slow_type(text, color=FG_YELLOW, delay=0.05, end=True):
    """Print each character of *text* with a small delay."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    if end:
        sys.stdout.write("\n")
        sys.stdout.flush()

# Opening frame
print(f"{BOLD}{FG_BLUE}{'╔' * 30}╗")
print(f"{FG_BLUE}{'║' + ' ' * 28 + '║'}")
print(f"{FG_BLUE}{'║' + BOLD + 'Woody Allen\'s Existential Blues' + RESET + FG_BLUE + ' ' * 28 + '║'}")
print(f"{FG_BLUE}{'║' + ' ' * 28 + '║'}")
print(f"{BOLD}{FG_BLUE}{'╚' * 30}╝\n")

# A nervous heartbeat before the quote appears
for _ in range(5):
    print(FG_BLUE + "…", end="", flush=True)
    time.sleep(0.3)
print(RESET)

# Woody‑style philosophical quote (type‑written)
quote = "I'm not afraid of death; I just don't want to be there when it happens."
slow_type(quote, color=FG_MAGENTA, delay=0.03, end=False)

# Closing frame
print("\n")
print(f"{BOLD}{FG_BLUE}{'╔' * 30}╗")
print(f"{FG_BLUE}{'║' + ' ' * 28 + '║'}")
print(f"{FG_BLUE}{'║' + BOLD + 'Thanks for reading!' + RESET + FG_BLUE + ' ' * 28 + '║'}")
print(f"{FG_BLUE}{'║' + ' ' * 28 + '║'}")
print(f"{BOLD}{FG_BLUE}{'╚' * 30}╝")