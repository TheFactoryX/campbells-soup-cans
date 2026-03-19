"""
Campbell's Soup Can #2842
Produced: 2026-03-19 09:02:01
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys,time

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"

quote = "I’m not afraid of death; I just don’t want to be there when it happens."
lines = [
    "I’m not afraid of death; I just don’t",
    "want to be there when it happens."
]

inter_width = 48
def pad(s):
    return s.ljust(inter_width)

def slow_print(s, delay=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

border_top = YELLOW + BOLD + "┌" + ("─" * inter_width) + "┐" + RESET
border_mid = YELLOW + BOLD + "├" + ("─" * inter_width) + "┤" + RESET
border_bot = YELLOW + BOLD + "└" + ("─" * inter_width) + "┘" + RESETdef print_boxed():
    slow_print(border_top)
    for line in lines:
        slow_print(f"{CYAN}│ {pad(line)}{RESET}")
    slow_print(border_mid)
    slow_print(f"{MAGENTA}│ {pad(' — Woody Allen\'s ghost')} {RESET}")
    slow_print(border_bot)

print_boxed()