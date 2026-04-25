"""
Campbell's Soup Can #3444
Produced: 2026-04-25 13:39:25
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful Woody‑Allen‑style philosophical quote in a colorful, animated box.
"""

import sys
import time
import random
import shutil

# ANSI escape sequences
CSI = "\033["
RESET = CSI + "0m"
BOLD = CSI + "1m"
ITALIC = CSI + "3m"
UNDERLINE = CSI + "4m"
RED = CSI + "91m"
GREEN = CSI + "92m"
YELLOW = CSI + "93m"
BLUE = CSI + "94m"
MAGENTA = CSI + "95m"
CYAN = CSI + "96m"
WHITE = CSI + "97m"
BGBLACK = CSI + "40m"

# Quote
QUOTE = (
    f"{BOLD}{CYAN}I am afraid of being unnecessary.{RESET} "
    f"{ITALIC}{YELLOW}I am the only one who would ever be "
    f"{RED}actually{RESET}{ITALIC} useful in my own life!{RESET}"
)

# Animation helpers
def animate(text, delay=0.05, color=GREEN):
    """Type out text character by character with a color shimmer."""
    for i, ch in enumerate(text):
        # Randomly vary the color to give a shimmering effect
        chosen = random.choice([color, RED, YELLOW, BLUE, MAGENTA, CYAN])
        sys.stdout.write(f"{CSI}{30+257 if i%2==0 else 40+257}m{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def draw_borders(lines, width, color=WHITE):
    """Draw a colored box around the text."""
    horizontal = f"{color}+{'-' * width}+{RESET}"
    sys.stdout.write(horizontal + "\n")
    for line in lines:
        padded = line.ljust(width)
        sys.stdout.write(f"{color}|{RESET}{padded}{color}|{RESET}\n")
    sys.stdout.write(horizontal + "\n")

def main():
    # Split quote into lines fitting the terminal width
    term_width = shutil.get_terminal_size((80, 20)).columns - 4  # padding
    words = QUOTE.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= term_width:
            current = f"{current} {w}".strip() if current else w
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    # Clear screen, set background to black
    sys.stdout.write(CSI + "2J" + CSI + "H" + BGBLACK)
    sys.stdout.flush()

    # Draw the box
    draw_borders(lines, term_width, color=YELLOW)

    # Animate the quote inside the box
    sys.stdout.write("\n")
    for line in lines:
        animate(line, delay=0.04, color=CYAN)
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()