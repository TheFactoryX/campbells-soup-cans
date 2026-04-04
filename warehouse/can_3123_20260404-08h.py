"""
Campbell's Soup Can #3123
Produced: 2026-04-04 08:59:10
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
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

# ---------- ANSI colour helpers ----------
def c(text, code):          # wrap text in ANSI colour codes
    return f"\033[{code}m{text}\033[0m"

def clear():
    # Works on most terminals (including Windows 10+)
    _ = sys.stdout.write("\033c")
    sys.stdout.flush()

# ---------- Quote ----------
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# ---------- Visual layout ----------
border = "═"
vertical = "│"
corner    = "┌┐└┘"

def make_border(width):
    return vertical + (" " + border * (width-2) + " ") + vertical

def make_line(text, width):
    padded = text.center(width-2)
    return vertical + padded + vertical

# Width of the box (including borders)
BOX_W = max(len(quote), 30) + 4   # +4 for inner padding

# Build the box line‑by‑line
box_lines = [
    f"{corner}{border * (BOX_W-2)}{corner}",                     # top border
    make_line(c("  " + quote + "  ", 31), BOX_W),                  # quoted text in bright magenta
    f"{vertical}{' ' * (BOX_W-2)}{vertical}",                    # empty line (optional spacing)
    f"{vertical}  (Woody Allen would nod approvingly)  {vertical}",# extra comedic comment
    f"{corner}{border * (BOX_W-2)}{corner}"                      # bottom border
]

# ---------- Optional slow‑type animation ----------
def typewriter(lines, delay=0.04):
    """Print each line character‑by‑character for a playful effect."""
    for line in lines:
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")
        sys.stdout.flush()

# ---------- Execute ----------
clear()
typewriter(box_lines, delay=0.02)   # small delay makes it feel lively

# Pause so the viewer can read before the terminal possibly clears
time.sleep(3)

# If you want the script to close automatically after the pause,
# you can uncomment the next line (works on most systems):
# os.system('pause' if sys.platform.startswith('win') else 'read -p "Press Enter..."')