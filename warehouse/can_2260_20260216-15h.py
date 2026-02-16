"""
Campbell's Soup Can #2260
Produced: 2026-02-16 15:01:49
Worker: Aurora Alpha (openrouter/aurora-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
FG_WHITE = "\033[97m"
BG_BLUE = "\033[44m"
FG_YELLOW = "\033[93m"
FG_CYAN = "\033[96m"

quote = "I think, therefore I panic; existence is a nervous breakdown with a side of coffee."
# Split into manageable width
max_width = 56
words = quote.split()
lines = []
cur = ""
for w in words:
    if len(cur) + len(w) + 1 <= max_width:
        cur += (" " + w) if cur else w
    else:
        lines.append(cur)
        cur = w
if cur:
    lines.append(cur)

# Build a box
box_width = max(len(line) for line in lines) + 4
top = f"{BG_BLUE}{FG_WHITE}{'┌' + '─' * (box_width - 2) + '┐'}{RESET}"
bottom = f"{BG_BLUE}{FG_WHITE}{'└' + '─' * (box_width - 2) + '┘'}{RESET}"
empty = f"{BG_BLUE}{FG_WHITE}{'│' + ' ' * (box_width - 2) + '│'}{RESET}"

def colored_line(text):
    padding = box_width - 2 - len(text)
    left = padding // 2
    right = padding - left
    return f"{BG_BLUE}{FG_WHITE}│{' ' * left}{text}{' ' * right}│{RESET}"

def type_print(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    type_print(top, 0.005)
    type_print(empty, 0.005)
    for line in lines:
        type_print(colored_line(f"{FG_CYAN}{BOLD}{line}{RESET}"), 0.01)
    type_print(empty, 0.005)
    type_print(bottom, 0.005)

if __name__ == "__main__":
    main()