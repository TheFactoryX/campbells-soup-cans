"""
Campbell's Soup Can #3923
Produced: 2026-06-13 08:31:30
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

quote = """I don't believe in an afterlife, but I'm terrified of missing it 
because I might have misfiled my invitation."""

def type_print(text, color, delay=0.03):
    for char in text:
        print(color + char + "\033[0m", end='', flush=True)
        time.sleep(delay)
    print()

# Intro message with fade in effect (blue)
intro = "Calculating existential dread... Please wait."
for char in intro:
    print("\033[94m" + char + "\033[0m", end='', flush=True)
    time.sleep(0.05)
print()

# Progress bar with cyan blocks
print("\nLoading: ", end="", flush=True)
for _ in range(20):
    print("\033[96m#\033[0m", end="", flush=True)
    time.sleep(0.05)
print(" \033[92m100%\033[0m")

# Calculate box dimensions
quote_lines = quote.split('\n')
max_line_length = max(len(line) for line in quote_lines) + 2  # Add padding
box_width = max(max_line_length, 40)

# Top border
print("\n\033[96m┌" + "─" * (box_width - 2) + "┐\033[0m")

# Quote lines with typing effect
for line in quote_lines:
    padded_line = line.center(max_line_length - 2).rstrip()
    print("\033[96m│\033[0m", end="", flush=True)
    print("\033[93m" + " " * ((max_line_length - 2 - len(padded_line))//2), end="")
    for char in padded_line:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print("\033[96m" + " " * ((max_line_length - 2 - len(padded_line)) - (max_line_length - 2 - len(padded_line))//2) + "│\033[0m")

# Bottom border
print("\033[96m└" + "─" * (box_width - 2) + "┘\033[0m")

# Signature
time.sleep(0.2)
print("\n\033[95m― Woody Allen's existential crisis generator v1.0\033[0m")