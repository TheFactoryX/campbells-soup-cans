"""
Campbell's Soup Can #2622
Produced: 2026-03-07 13:49:22
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, itertools

# ANSI color codes
ESC = "\x1b"
RESET = f"{ESC}[0m"
BOLD  = f"{ESC}[1m"
CYAN  = f"{ESC}[36m"
GREEN = f"{ESC}[32m"
YELLOW= f"{ESC}[33m"
RED   = f"{ESC}[31m"

quote = "Life is like an onion: You cry when you eat it, but it's the layers of regret that make it bittersweet."

def slow_print(s, delay=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    sys.stdout.flush()

box_top    = f"{CYAN}{BOLD}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}"
box_bottom = f"{CYAN}{BOLD}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}"
box_side   = f"{GREEN}{BOLD}┃{RESET}"

def print_centered(text, width=68):
    line = f"{box_side} {text:<{width-3}}{box_side}{RESET}"
    slow_print(line + "\n", 0)

slow_print(box_top + "\n", 0)

slow_print(f"{box_side}                                            {box_side}{RESET}\n", 0)
slow_print(f"{box_side}   \"{quote}\"                         {box_side}{RESET}\n", 0)
slow_print(f"{box_side}                                            {box_side}{RESET}\n", 0)
slow_print(f"{box_side} — Woody Allen — A neurotic musing on layers{RESET}\n", 0)
slow_print(f"{box_side}                                            {box_side}{RESET}\n", 0)
slow_print(f"{box_side}                                            {box_side}{RESET}\n", 0)

slow_print(box_bottom + "\n", 0)

# add a tiny sparkle effect at the bottom
sparkle = f"{YELLOW}{BOLD}✨{RESET}"
slow_print(f"{sparkle}  {RESET}", 0)