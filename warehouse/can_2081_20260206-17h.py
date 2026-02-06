"""
Campbell's Soup Can #2081
Produced: 2026-02-06 17:59:37
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

def typewriter(s, delay=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

quote = "I’m not afraid of death – I just keep forgetting to show up for it."

# ANSI color codes
c_reset = "\033[0m"
c_cyan    = "\033[96m"
c_magenta = "\033[95m"

# Build a colorful box around the quote
width = len(quote) + 4
border_top    = c_cyan + "┌" + "─" * width + "┐" + c_reset
border_mid    = c_cyan + "│ " + c_magenta + quote + c_cyan + " │" + c_reset
border_bottom = c_cyan + "└" + "─" * width + "┘" + c_reset

box = border_top + "\n" + border_mid + "\n" + border_bottom
typewriter(box, delay=0.02)