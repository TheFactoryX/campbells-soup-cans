"""
Campbell's Soup Can #3390
Produced: 2026-04-21 19:37:30
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]
RESET = "\033[0m"
BOLD = "\033[1m"

def type_writer(text, delay=0.05):
    """Print text character by character with cycling colors."""
    color_idx = 0
    for ch in text:
        sys.stdout.write(COLORS[color_idx % len(COLORS)] + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
        color_idx += 1
    print()  # newline after the quote

def main():
    # Woody Allen‑style quote
    quote = "I'm not afraid of the future; I'm just terrified that it will arrive before I finish my coffee."
    
    # Box dimensions
    width = len(quote) + 4  # padding inside box
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    sides = "║" + " " * (width - 2) + "║"
    
    # Print top border in cyan
    print(BOLD + "\033[96m" + top_bottom + RESET)
    
    # Print empty line with sides
    print(BOLD + "\033[96m" + sides + RESET)
    
    # Print the quote line with typewriter effect inside the box
    sys.stdout.write(BOLD + "\033[96m" + "║ " + RESET)
    type_writer(" " + quote + " ", delay=0.07)
    sys.stdout.write(BOLD + "\033[96m" + "║" + RESET)
    print()  # newline after the quote line (typewriter already added newline)
    
    # Print empty line with sides
    print(BOLD + "\033[96m" + sides + RESET)
    
    # Print bottom border in cyan
    print(BOLD + "\033[96m" + top_bottom + RESET)
    
    # Optional: a little blinking cursor for fun
    for _ in range(3):
        sys.stdout.write("\033[96m" + BOLD + " █" + RESET)
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\r  ")
        sys.stdout.flush()
        time.sleep(0.4)
    print()  # final newline

if __name__ == "__main__":
    main()