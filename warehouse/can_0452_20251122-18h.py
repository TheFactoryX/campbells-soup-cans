"""
Campbell's Soup Can #452
Produced: 2025-11-22 18:40:33
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

# ---- ANSI colour definitions ---------------------------------------------
RESET      = '\033[0m'
BOLD       = '\033[1m'
IT        = '\033[3m'
UNDERLINE = '\033[4m'

# Foreground
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'

# Background
BG_BLACK   = '\033[40m'
BG_RED     = '\033[41m'
BG_GREEN   = '\033[42m'
BG_YELLOW  = '\033[43m'
BG_BLUE    = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN    = '\033[46m'
BG_WHITE   = '\033[47m'

# ---- The quote ------------------------------------------------------------
QUOTE = (
    "I am not afraid of death; I just want the universe to stop throwing "
    "existential jokes at my nervous system, which is far too dramatic."
)

# ---- Helper functions -----------------------------------------------------
def type_print(text, delay=0.04, color=WHITE):
    """Print a string to stdout, one character at a time, optionally coloured."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def display_box(text, bcolor=BG_BLACK, fcolor=CYAN):
    """Display the given text inside a colourful ASCII box with a fade‑in effect."""
    lines = text.split('\n')
    width  = max(len(line) for line in lines)
    border = "─" * (width + 2)

    top    = f"{bcolor}{FGCYAN}{BOLD}┌{border}┐{RESET}"
    bottom = f"{bcolor}{FGCYAN}{BOLD}└{border}┘{RESET}"
    # *since we have no GUI, we print line by line with a short pause*
    sys.stdout.write(top)
    sys.stdout.flush()
    time.sleep(0.1)

    for line in lines:
        padded = line.ljust(width)
        sys.stdout.write(f"{bcolor}{FGCYAN}{BOLD}│ {RESET}{fcolor}{padded}{RESET} ")
        sys.stdout.write(f"{bcolor}{FGCYAN}{BOLD}│{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(bottom + '\n')
    sys.stdout.flush()
    time.sleep(0.1)

# ---- Main program ----------------------------------------------------------
def main():
    # Header
    header = f"{YELLOW}{BOLD}✨  Philo‑Daily Woody‑Sigh  ✨{RESET}"
    type_print(header, delay=0.07)

    # ASCII art (a little, nefarious brain)
    brain = [
        "        .-'''-.",
        "       / .===. \\ ",
        "       \\/ 6 6 \\/",
        "       ( \\___/ )",
        "    ___ooo__ooo___",
        "   /    []         \\",
        "  /      []         \\",
        " |      []       ___|",
        " |_____[]______/    ",
    ]
    for line in brain:
        type_print(line, delay=0.02, color=BLUE)
        time.sleep(0.02)

    # The quote itself: typewriter effect
    type_print(QUOTE, delay=0.03, color=GREEN)

    # Decorative footer box
    display_box(
        f"{MAGENTA}||{RESET} {ITALIC}Sorry, I think I broke something mentally!{RESET} {MAGENTA}||{RESET}",
        bcolor=BG_BLUE, fcolor=CYAN
    )

if __name__ == "__main__":
    main()