"""
Campbell's Soup Can #4905
Produced: 2026-09-05 12:43:35
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
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

def slow_print(text, color="", delay=0.07):
    """Print text character by character with optional color."""
    for ch in text:
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()

def draw_box(width, title="", border_color=YELLOW, fill_color=CYAN):
    """Draw a simple ASCII box with optional title."""
    top = f"{border_color}╔{'═' * (width - 2)}╗{RESET}"
    bottom = f"{border_color}╚{'═' * (width - 2)}╝{RESET}"
    sys.stdout.write(top + "\n")
    if title:
        padded = title.center(width - 2)
        sys.stdout.write(f"{border_color}║{RESET}{fill_color}{padded}{RESET}{border_color}║{RESET}\n")
        sys.stdout.write(f"{border_color}║{' ' * (width - 2)}║{RESET}\n")
    sys.stdout.write(bottom + "\n")

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    # Visual flair: a tiny Woody Allen‑ish face
    face = r"""
      (\_/)
     ( •‿• )
      / >🌰
    """
    width = max(len(quote) + 4, len(face.splitlines()[1]) + 4)
    draw_box(width, title=" Woody Allen Wisdom ", border_color=MAGENTA, fill_color=YELLOW)
    slow_print(quote.center(width - 2), color=CYAN, delay=0.05)
    # Print the face below the box
    for line in face.splitlines():
        sys.stdout.write(CYAN + line.center(width) + RESET + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()