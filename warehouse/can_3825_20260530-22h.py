"""
Campbell's Soup Can #3825
Produced: 2026-05-30 22:14:54
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def print_line(text, color, delay):
    print(f"{color}{text}{RESET}", flush=True)
    time.sleep(delay)

# Welcome message with animation
print(cyan: for text, CYAN)
print(LINE 1: "🌟 Philosophical Insights Powered by Anxiety 🌟")
sys.stdout.flush()
time.sleep(1)

# Thinking animation
for i in range(4):
    dots = "." * i
    sys.stdout.write(f"\r{BLUE}Thinking{dots}{RESET}")
    sys.stdout.flush()
    time.sleep(0.3)
print()  # Move to next line after dots

# Box dimensions
box_width = 40

# Top border
top_border = "┌" + "─" * (box_width - 2) + "┐"
print_line(top_border, YELLOW, 0.2)

# Title
title = f"│  Woody Allen's Neurotic Nuggets  │"
print_line(title, YELLOW, 0.2)

# Separator
separator = "├" + "─" * (box_width - 2) + "┤"
print_line(separator, YELLOW, 0.2)

# Quote lines (each 36 chars to fit in box)
quote_lines = [
    f'{GREEN}I tried to contemplate existence but{RESET}',
    f'{GREEN}my cat\'s stare made me question{RESET}',
    f'{GREEN}everything. It\'s all very existen-{RESET}',
    f'{GREEN}ial, if you ignore the tuna.{RESET}'
]

for line in quote_lines:
    # Pad line to 36 chars and format
    padded_line = f"{line}{' ' * (36 - len(line) + len(GREEN) + len(RESET) - len(line))}"
    formatted_line = f"│ {padded_line} │"
    print_line(formatted_line, GREEN, 0.4)

# Bottom border
bottom_border = "└" + "─" * (box_width - 2) + "┘"
print_line(bottom_border, YELLOW, 0.2)

# Exit with a flourish
print("\n")
print_line("Press Ctrl+C to exit... or just close the window.", CYAN, 0.5)