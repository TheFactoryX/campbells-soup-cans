"""
Campbell's Soup Can #1102
Produced: 2025-12-22 11:29:39
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time
import sys

# Define some matrices ASCII art
matrix_anim = [
    "\033[32m  \33   \33  \n"      # First line with green color
    "\033[33m /\33  /\33 \ \33 /\n" # Second line with yellow color
    "\033[36m|    \33   \33  \n\033[0m" # Third line with blue and reset
]

# Choose random Woody-Allen-like philosophical quotes
quotes = [
    "I'm not afraid of dying - I just don't want to be there when it happens.",
    "2000 years ago, give or take, Jesus said, 'Love thy neighbour as thyself.' Well I agree - but, me being an only child, it puts me a bit of a dilemma.",
    "I'm a minor miracle. You poke me I'm a miracle. You prod me, two or three prods later, I'm a miracle.",
    "The worst... time... is when you go 'to sleep'..."
]

# Choose random colors for the quote (foreground and background)
color_pairs = [
    ('\033[35m', '\033[46m'),  # Purple on cyan
    ('\033[36m', '\033[45m'),  # Cyan on purple
    ('\033[31m', '\033[40m'),  # Red on black
    ('\033[37m', '\033[44m')   # White on blue
]

# Select random quote and colors
qq = random.choice(quotes)
bg_color, fg_color = random.choice(color_pairs)

# ANSI reset sequence
RESET = '\033[0m'

# Calculate box width based on the longest quote line
max_len = max(len(line) for line in qq.splitlines())

# Create a colorful animated title
def colorful_quote(title):
    colors = ['\033[93m', '\033[95m', '\033[92m', '\033[91m']
    res = ""
    for i, c in enumerate(title):
        res += random.choice(colors) + c
    print(res + RESET)

# Main program
print("\n" * 2, end="")  # Skip some lines for dramatic effect
print(f"{random.choice(['Really?', 'Oh come on...', 'YES!'])}!")
time.sleep(0.3)

# Print animated Matrix effect
try:
    sys.stdout.write("\033[H\033[J")  # Clear screen
    for line in matrix_anim:
        print(line, end="", flush=True)
        time.sleep(0.1)
except: pass

time.sleep(0.3)

# Print colored quote with border and background effects
def print_colored_quote(q, bg, fg, border=green):
    lines = q.splitlines()
    border_line = border + "+" + "-" * (max_len + 4) + "+"
    
    # Print border (with slight delay for effect)
    for part in border_line:
        print(border, end="", flush=True)
    print(RESET)
    time.sleep(0.3)
    
    for line in lines:
        # Create bordered line with background color
        padded = line.center(max_len)
        colored = fg + f"  {padded}  " + RESET
        full_line = fg + border + "\033[0m"
        full_line += col = bg + colored + bg
        full_line += border + RESET
        
        print(col, end="", flush=True)
        for char in colored + border + RESET:
            print(char, end="", flush=True)
            time.sleep(0.02)  # Small delay for typing effect
        print()
        time.sleep(0.05)

    print(border_line + RESET)

print_colored_quote(qq, bg, fg)

time.sleep(1)  # Final pause before exit