"""
Campbell's Soup Can #4956
Produced: 2026-09-13 16:18:05
Worker: Nex AGI: Nex-N2.5-Mini (free) (nex-agi/nex-n2.5-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import sys
import time
from shutil import get_terminal_size

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GREEN = "\033[32m"
PURPLE = "\033[35m"

QUOTE = (
    "I’m convinced existence is tragic—not because the universe is cruel, "
    "but because I left the receipt at home and still expect a refund."
)


def wrap_text(text, width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = word if not current else current + " " + word
        if len(candidate) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def draw_typewriter(progress, box_width):
    clear_screen()
    wrapped = wrap_text(progress, box_width - 4)
    box = [
        "┌" + "─" * (box_width - 2) + "┐",
        *[f"│ {line:<{box_width - 4}} │" for line in wrapped],
        "└" + "─" * (box_width - 2) + "┘",
    ]
    bar_width = 28
    filled = int(bar_width * len(progress) / len(QUOTE))
    bar = "█" * filled + "░" * (bar_width - filled)
    print("\n".join("  " + line for line in box))
    print(f"\n{RED}Existential progress{RESET} [{bar}] {len(progress)}/{len(QUOTE)}")
    sys.stdout.flush()


terminal_width = max(48, min(get_terminal_size((80, 24)).columns, 100))
box_width = max(42, min(82, terminal_width - 8))

sys.stdout.write("\033[?25l")
try:
    for index in range(1, len(QUOTE) + 1):
        draw_typewriter(QUOTE[:index], box_width)
        time.sleep(0.018)

    clear_screen()
    art = [
        "        .-\"\"-.",
        "       / .--. \\",
        "      | (¬_¬) |",
        "       \\ '--' /",
        "        | || |",
        "       /|||||\\",
        "      /_______\\",
        "         (__)  ",
    ]
    print("\n".join(" " * ((box_width - len(line)) // 2) + line for line in art))
    print("\n")
    print("\n".join("  " + line for line in [
        "┌" + "─" * (box_width - 2) + "┐",
        f"│ {RED}{BOLD}{QUOTE}{RESET:<{box_width - 4}} │",
        "└" + "─" * (box_width - 2) + "┘",
    ]))
    print("\n")
    print(f"  {YELLOW}{BOLD}STATUS: REFUND DENIED{RESET}")
    print(f"  {CYAN}EXISTENCE: NON-REFUNDABLE{RESET}\n")
finally:
    sys.stdout.write("\033[?25h")
    sys.stdout.write(RESET)
    sys.stdout.flush()