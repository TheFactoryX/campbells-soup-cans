"""
Campbell's Soup Can #5005
Produced: 2026-09-22 09:58:20
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import shutil
import textwrap

RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
DIM = "\033[2m"

quote = "Life has no inherent meaning, but I still panic when the waiter asks what I want."
terminal_width = shutil.get_terminal_size((80, 24)).columns
box_width = max(44, min(terminal_width - 6, 72))
inner_width = box_width - 4
lines = textwrap.wrap(quote, width=inner_width)

print(f"\n        {DIM}.   o        .{RESET}")
print(f"   {CYAN}╭{'─' * box_width}╮{RESET}")
for line in lines:
    print(f"   {CYAN}│{YELLOW} {line:<{inner_width}} {CYAN}│{RESET}")
print(f"   {CYAN}╰{'─' * (box_width - 6)}╯{MAGENTA}╲{RESET}")
print(f"                  {MAGENTA}╲  o{RESET}\n")