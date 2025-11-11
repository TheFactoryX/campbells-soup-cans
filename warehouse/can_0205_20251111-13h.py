"""
Campbell's Soup Can #205
Produced: 2025-11-11 13:01:28
Worker: Microsoft: MAI DS R1 (free) (microsoft/mai-ds-r1:free)
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
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
BLINK = "\033[5m"
UNDERLINE = "\033[4m"

def print_frame():
    frame_width = 50
    print(CYAN + "┌" + "─" * (frame_width-2) + "┐" + RESET)
    for _ in range(3):
        print(CYAN + "│" + " " * (frame_width-2) + "│" + RESET)
    print(CYAN + "└" + "─" * (frame_width-2) + "┘" + RESET)
    sys.stdout.write("\033[4A\033[2C")  # Move cursor up and right

def animate_quote(text, delay=0.05):
    for char in text:
        sys.stdout.write(YELLOW + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def blinking_cursor():
    try:
        for _ in range(3):
            sys.stdout.write(BLINK + "_" + RESET)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            time.sleep(0.5)
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n")

quote = [
    "  Life is like a cosmic sitcom where the laugh track",
    f"  is just {RED}silent screaming{RESET}{YELLOW} and the season finale",
    "  always ends with existential credits you can't skip."
]

# Print animated scene
print("\n" * 5)
print_frame()
for line in quote:
    animate_quote(line)
    time.sleep(0.3)
sys.stdout.write("\033[1B\033[6D")  # Position cursor after frame
print(f"{YELLOW}       – Woody Allen's Worst Nightmare{RESET}", end="")
blinking_cursor()
print("\n" * 3)