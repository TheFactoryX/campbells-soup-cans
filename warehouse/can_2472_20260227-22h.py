"""
Campbell's Soup Can #2472
Produced: 2026-02-27 22:43:44
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# ANSI color codes
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Create a Woody Allen-style quote
quote = "I don't want to die. I just want to be able to die without leaving a mess for the funeral director."

# Set up the box dimensions
width = 40
height = 7

# Center the quote in the box
inner_width = width - 4
if len(quote) > inner_width:
    quote = quote[:inner_width]
padding = (inner_width - len(quote)) // 2
centered_quote = " " * padding + quote + " " * (inner_width - len(quote) - padding)

# Build the box
top = "┌" + "─" * (width - 2) + "┐"
bottom = "└" + "─" * (width - 2) + "┘"
mid = "│ " + centered_quote + " │"

# Clear terminal and position cursor
os.system('cls' if os.name == 'nt' else 'clear')
print("\033[{};{}H".format(1, 1))

# Print the box with animation
for i in range(15):
    # Change color based on iteration
    color = RED if i % 2 == 0 else BLUE
    
    # Print the animated box
    print(color + top + RESET)
    print(color + mid + RESET)
    print(color + bottom + RESET)
    
    # Add moving stars (simulating a starfield)
    for star in range(12):
        x = 2 + (star * 3) % (width - 2)
        y = 2 if i % 3 == 0 else 3 if i % 3 == 1 else 4
        if y == 2: 
            print(f"\033[{y};{x}H{GREEN}★{RESET}")
        else:
            print(f"\033[{y};{x}H{RED}★{RESET}")
    
    # Add a blinking cursor effect
    if i % 5 == 0:
        print(f"\033[3;{width//2}H{RED}▌{RESET}")
    
    # Small pause for animation
    time.sleep(0.1)
    
    # Clear previous animation (move up and erase)
    print("\033[3A\033[2K" + "\033[2K" * 3)

# Final reveal with green highlight
print(GREEN + top + RESET)
print(GREEN + mid + RESET)
print(GREEN + bottom + RESET)
print(f"\n\033[1;32m{quote}\033[0m")