"""
Campbell's Soup Can #3620
Produced: 2026-05-09 16:09:56
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
BOLD = '\033[1m'

def type_text(text, color, delay=0.05):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def print_box(lines, color):
    max_len = max(len(line) for line in lines)
    border = '*' * (max_len + 4)
    print(f"{CYAN}{border}{RESET}")
    for line in lines:
        padding = ' ' * (max_len - len(line))
        print(f"{CYAN}*{RESET} {color}{line}{padding}{RESET} {CYAN}*{RESET}")
    print(f"{CYAN}{border}{RESET}")

# The quote
quote_lines = [
    "I don't fear death — I just don't want",
    "to be there when it happens...",
    "Which is why I'm always 10 minutes",
    "late to my own existential crisis."
]

# Print with animation
print('\n')
type_text("Press Enter to contemplate mortality...", GREEN)
input()
print('\n')
print_box(quote_lines, YELLOW)

# ASCII art
print(f"\n{RED}", end='')
print("       .-''''''-.")

print(f"{GREEN}     .'          '.")
print(f"{YELLOW}    /   O      O   \\  ")
print(f"{RED}   :                :")
print(f"{GREEN}   |                |     ", end='')
type_text(" — Woody Allen (probably)", CYAN, 0.03)
print(f"{YELLOW}    \\    \\____/    /")
print(f"{RED}     '.          .'        ", end='')
type_text("(He's nervous about it)", CYAN, 0.03)
print("       '-......-'")

# Blinking ellipsis for dramatic effect
print("\n")
for _ in range(3):
    print(f"{BOLD}{YELLOW}...{RESET}", end='\r')
    time.sleep(0.5)
    print("   ", end='\r')
    time.sleep(0.5)
print(f"{BOLD}{YELLOW}...{RESET}")