"""
Campbell's Soup Can #2523
Produced: 2026-03-02 11:46:31
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

BLUE = '\033[34m'
YELLOW = '\033[33m'
RESET = '\033[0m'
BOLD = '\033[1m'

art_width = 10
quote_width = 37
total_width = art_width + 1 + quote_width

art_lines = [
    "   _    _  ",
    "  (o)(o)   ",
    " /  ||  \\ ",
    "/   ||   \\",
    "*----||----",
    "    ||     ",
    "    ^^     "
]

quote_lines = [
    "I'm not saying I'm afraid of death, but I'd",
    "rather be in the audience than on the stage",
    "when it happens."
]

top_border = '+' + '-' * total_width + '+'

print(f"{BOLD}{BLUE}{top_border}{RESET}")
for i in range(7):
    art_str = art_lines[i] if i < len(art_lines) else ' ' * art_width
    art_str = art_str.ljust(art_width)
    
    quote_str = quote_lines[i] if i < len(quote_lines) else ''
    quote_str = quote_str.ljust(quote_width)
    
    base = '|' + BLUE + art_str + RESET + ' '
    
    if i < len(quote_lines):
        sys.stdout.write(base)
        sys.stdout.write(YELLOW)
        for c in quote_str:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.008)
        sys.stdout.write(RESET)
        sys.stdout.write('|\n')
    else:
        line = base + YELLOW + quote_str + RESET + '|'
        print(line)
print(f"{BOLD}{BLUE}{top_border}{RESET}")

print(f"\n{YELLOW}{BOLD}-- Woody Allen (if he were a neurotic ASCII art philosopher){RESET}")