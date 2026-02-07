"""
Campbell's Soup Can #2089
Produced: 2026-02-07 04:48:04
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
COLORS = {
    "YELLOW": "\033[93m",
    "RED": "\033[91m",
    "CYAN": "\033[96m",
    "PINK": "\033[95m",
    "RESET": "\033[0m"
}

def typewriter(text, delay=0.03, color=""):
    for char in text:
        sys.stdout.write(color + char + COLORS["RESET"])
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_thinker():
    thinker = r"""
    {YELLOW}
       ▄████████████▄
      ████        ████
     ███    \__/    ███
    ███   ◖(◣_◢)◗   ███
    ███▄    ███    ▄███
     █████▄▄▄▄▄▄▄████▀
       ▀███████████▀
    {RESET}
    """.format(**COLORS)
    print(thinker)

def print_quote():
    quote = [
        ("{PINK}┌─────────────────────────────────────────────────────┐{RESET}", 0),
        ("{PINK}│{RESET}                                                 {PINK}│{RESET}", 0.1),
        ("{PINK}│{RESET} {CYAN}I had an existential crisis once, but then I{RESET}     {PINK}│{RESET}", 0.03),
        ("{PINK}│{RESET} {CYAN}realized it wasn't scheduled in my calendar.{RESET}     {PINK}│{RESET}", 0.03),
        ("{PINK}│{RESET} {CYAN}Now I'm anxious about missing my next one.{RESET}       {PINK}│{RESET}", 0.03),
        ("{PINK}│{RESET}                                                 {PINK}│{RESET}", 0.05),
        ("{PINK}└─────────────────────────────────────────────────────┘{RESET}", 0.2)
    ]
    
    for line, delay in quote:
        formatted_line = line.format(**COLORS)
        if any(char in formatted_line for char in ["┌", "│", "└", "─"]):
            time.sleep(delay)
            print(formatted_line)
        else:
            typewriter(formatted_line.strip(), delay=0.03, color=COLORS["CYAN"])

def floating_dots():
    dot_anim = ["   ", ".  ", ".. ", "...", " ..", "  .", "   "]
    for _ in range(3):
        for frame in dot_anim:
            sys.stdout.write(f"\r{COLORS['YELLOW']}thinking{frame}{COLORS['RESET']}")
            sys.stdout.flush()
            time.sleep(0.2)

if __name__ == "__main__":
    print_thinker()
    floating_dots()
    print("\n")
    print_quote()
    time.sleep(1)
    print(f"\n{COLORS['RED']}  ― Woody Allen (probably){COLORS['RESET']}")