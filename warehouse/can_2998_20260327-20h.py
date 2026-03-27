"""
Campbell's Soup Can #2998
Produced: 2026-03-27 20:55:46
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, sys# ANSI colour codes
RESET = "\033[0m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
MAGENTA= "\033[95m"

def coloured(text, colour):
    return f"{colour}{text}{RESET}"

quote = "I'm not afraid of death; I just don't want to be there when it happens."
border = "═"
box_width = len(coloured(quote, GREEN)) + 4  # 2 spaces padding on each sidetop    = f"┌{' '+border*box_width}┐"
bottom = f"└{' '+border*box_width}┘"
side   = f"│ {quote} │"

# Helper to print with a tiny delay for a simple animation
def printer(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline at the end

# Start the visual show
printer(coloured(top, CYAN))
printer(coloured("│", CYAN), 0)  # just a colour flicker
for i in range(box_width):
    sys.stdout.write(border)
    sys.stdout.flush()
    time.sleep(0.01)
printer(coloured("│", CYAN), 0)

printer(coloured("│", CYAN), 0)
printer(coloured(" ", 0), 0)  # spacer
printer(side, 0)
printer(coloured(" ", 0), 0)
printer(coloured("│", CYAN), 0)

printer(coloured(bottom, CYAN))
printer(f"{YELLOW}Press Ctrl-C to stop.{RESET}")