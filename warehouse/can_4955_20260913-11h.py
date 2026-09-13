"""
Campbell's Soup Can #4955
Produced: 2026-09-13 11:53:58
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
🍊 Woody Allen Style Quote Generator 🍊
A neurotic, philosophical, and visually colorful experience.
Pure Python - no dependencies required.
"""

import sys
import time

# ANSI escape codes for colors and formatting
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

# Six vibrant colors to cycle through
COLORS = [
    "\033[31m",  # RED
    "\033[32m",  # GREEN
    "\033[33m",  # YELLOW
    "\033[34m",  # BLUE
    "\033[35m",  # MAGENTA
    "\033[36m",  # CYAN
]

# The Woody Allen philosophical zinger
QUOTE = ("I'm not afraid of death," + "\n"
         "I just don't want to be there" + "\n"
         "when it happens.")

def colorize(text, code):
    """Wrap text with ANSI color code and reset."""
    return code + text + RESET

def slow_type(text, color=COLORS[3], delay=0.03):
    """Print text character-by-character with color."""
    for ch in text:
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def main():
    print()  # top spacer
    
    # Psychedelic intro animation
    for _ in range(2):
        for c in COLORS:
            sys.stdout.write(colorize("☯ " * 18, c))
            sys.stdout.write("\r")
            sys.stdout.flush()
            time.sleep(0.012)
    
    # Calculate box dimensions from quote
    lines = QUOTE.split("\n")
    max_len = max(len(line) for line in lines)
    width = max_len + 8  # padding inside the box
    
    # Draw the top border in cheerful yellow
    print(colorize("═" * width, COLORS[2]))
    
    # Print each quote line in its own color, inside the box
    for i, line in enumerate(lines):
        color = COLORS[i % len(COLORS)]
        padded = line.center(width - 2)
        print(colorize("║ " + padded + " ║", color))
    
    # Draw the bottom border
    print(colorize("═" * width, COLORS[2]))
    print()
    
    # Footer pun in cyan
    slow_type("Neurotic philosophy, served with a side of existential dread.",
              COLORS[5])
    print()

if __name__ == "__main__":
    main()