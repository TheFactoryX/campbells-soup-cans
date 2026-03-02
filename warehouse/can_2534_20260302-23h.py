"""
Campbell's Soup Can #2534
Produced: 2026-03-02 23:43:39
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
RED  = "\033[91m"
YEL  = "\033[93m"
GRN  = "\033[92m"
CYAN = "\033[96m"
RESET= "\033[0m"

# Woody Allen‑style quote (ASCII only)
quote_lines = [
    "I'm not afraid of death;",
    "I just don't want to miss",
    "the punchline."
]

# Inner width of the box
WIDTH = 57

# Build the top/bottom border (cyan)
border = f"{CYAN}+{'-'*WIDTH}+{RESET}"

# Helper to wrap text in a color
def colored(txt, col):
    return f"{col}{txt}{RESET}"

# Assemble the frame
frame = [
    border,
    colored(f"|{quote_lines[0].center(WIDTH)}|", YEL),
    colored(f"|{quote_lines[1].center(WIDTH)}|", YEL),
    colored(f"|{quote_lines[2].center(WIDTH)}|", YEL),
    border
]

# Simple flicker animation for visual fun
for _ in range(2):
    for line in frame:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write("\033c")  # clear screen
    time.sleep(0.2)

# Final static display
sys.stdout.write("\n".join(frame))
sys.stdout.flush()