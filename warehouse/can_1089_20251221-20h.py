"""
Campbell's Soup Can #1089
Produced: 2025-12-21 20:34:17
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
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

def print_slow(text, color=None, end='\n'):
    color_code = color or ''
    reset = "\033[0m"
    for char in text:
        sys.stdout.write(f"{color_code}{char}{reset}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.005, 0.03))
    sys.stdout.write(end)

def center_text_in_frame(text, frame_width=40):
    padding = (frame_width - len(text)) // 2
    return ' ' * padding + text

def print_frame(line, text, color=None):
    color_code = color or ''
    reset = "\033[0m"
    print(f"{line}| {text} |{color_code}{reset}")

# Woody Allen style quote
philosophical_quote = (
    "I have this terrible philosophy problem: Either I'm overreacting about everything, "
    "or I'm living the only way that makes sense in an insane universe. Paralysis is safer."
)

# Split into two lines to fit the box
lines = philosophical_quote.split(',')
line1 = lines[0] + ','
line2 = ' ' * len(line1.rstrip()) + lines[1]

# ANSI color codes
COOL = "\033[36m"  # Cyan
WARM = "\033[33m"  # Yellow
NEON_LIGHT = "\033[1;38;2;255;100;200m"  # Purple-ish neon
RESET = "\033[0m"

# Main loop for the animation
while True:
    # Clear screen (Linux/Mac) - alternative for Windows?
    print("\033c", end="")
    
    print(NEON_LIGHT + ' ' * 5 + "=" * 47 + RESET)
    print(NEON_LIGHT + ' ' * 4 + "|" + ' ' * 46 + "|" + RESET)
    print(NEON_LIGHT + ' ' * 4 + "|" + ' ' * 46 + "|" + RESET)
    
    print()
    print_frame(NEON_LIGHT, center_text_in_frame("THE KALTMANN PRINCIPLE", 40), COOL)
    print_frame(NEON_LIGHT, center_text_in_frame("from", 40), COOL)
    print_frame(NEON_LIGHT, center_text_in_frame("W. AllEiN'S VORPAL SOURCE", 40), COOL)
    
    print()
    print_frame(WARM, center_text_in_frame(line1, 40), RESET)
    print_frame(WARM, center_text_in_frame(line2, 40), RESET)
    print()
    
    print_line = NEON_LIGHT + ' ' * 4 + "|" + ' ' * 46 + "|" + RESET
    print(print_line)
    print(print_line)
    print(print_line)
    print(print_line)
    
    print(' ' * 4 + "|" + NEON_LIGHT + ' ' * 46 + "|" + RESET)
    print(' ' * 4 + "|" + NEON_LIGHT + ' ' * 46 + "|" + RESET)
    print(' ' * 4 + "|" + NEON_LIGHT + ' ' * 46 + "|" + RESET)
    print(' ' * 4 + "|" + ' ' * 46 + "|" + RESET)
    
    print(NEON_LIGHT + ' ' * 4 + "|                                   " + NEON_LIGHT + "H" + ' '*20 + "|" + RESET)
    print(NEON_LIGHT + ' ' * 4 + "|                                   " + COOL + "A" + ' '*20 + "|" + RESET)
    print(NEON_LIGHT + ' ' * 4 + "|                                   " + NEON_LIGHT + "L" + ' '*20 + "|" + RESET)
    print(NEON_LIGHT + ' ' * 4 + "|                                   " + WARM + "E" + ' '*20 + "|" + RESET)
    print(NEON_LIGHT + ' ' * 4 + "|                                   " + NEON_LIGHT + "N" + ' '*20 + "|" + RESET)
    
    print()
    time.sleep(1.5)