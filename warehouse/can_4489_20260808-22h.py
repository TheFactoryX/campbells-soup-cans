"""
Campbell's Soup Can #4489
Produced: 2026-08-08 22:46:53
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI colors
RED    = "\033[31m"
GREEN  = "\033[32m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
RESET  = "\033[0m"

quote = "I'm not afraid of death; I just keep forgetting to bring my notebook to the afterlife."

def typewriter_print(s, delay=0.05):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def colored_box(text, colors):
    width = len(text) + 4
    top    = "╔" + "═"*(width-2) + "╗"
    middle = "║ " + text + " ║"
    bottom = "╚" + "═"*(width-2) + "╝"
    lines = [top, middle, bottom]
    colored = []
    for i, line in enumerate(lines):
        col = colors[i % len(colors)]
        colored.append(f"{col}{line}{RESET}")
    return "\n".join(colored)

colors = [RED, GREEN, CYAN, YELLOW]
box = colored_box(quote, colors)

for line in box.splitlines():
    for _ in range(2):
        typewriter_print(line, delay=0.03)
        time.sleep(0.2)