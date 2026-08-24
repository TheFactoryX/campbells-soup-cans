"""
Campbell's Soup Can #4809
Produced: 2026-08-24 11:43:52
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
COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bold": "\033[1m",
    "reset": "\033[0m",
}

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def typewriter(text, color=COLORS["white"], delay=0.05):
    """Print text character by character with a slight delay."""
    for ch in text:
        sys.stdout.write(color + ch + COLORS["reset"])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def draw_box(content, width=None, pad=2, border_color=COLORS["cyan"], text_color=COLORS["yellow"]):
    """Draw a simple ASCII box around the content."""
    if width is None:
        width = max(len(line) for line in content.splitlines()) + 2 * pad
    top = border_color + "╔" + "═" * (width - 2) + "╗" + COLORS["reset"]
    bottom = border_color + "╚" + "═" * (width - 2) + "╝" + COLORS["reset"]
    sys.stdout.write(top + "\n")
    for line in content.splitlines():
        padded = line.ljust(width - 2 * pad)
        sys.stdout.write(border_color + "║" + COLORS["reset"])
        sys.stdout.write(" " * pad + text_color + padded + COLORS["reset"] + " " * pad)
        sys.stdout.write(border_color + "║" + COLORS["reset"] + "\n")
    sys.stdout.write(bottom + "\n")
    sys.stdout.flush()

def main():
    clear_screen()
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens."
    )
    # Optional: add a little whimsy above the quote
    intro = "Woody Allen once mused..."
    draw_box(intro, border_color=COLORS["magenta"], text_color=COLORS["white"])
    time.sleep(0.3)
    draw_box(quote, border_color=COLORS["green"], text_color=COLORS["yellow"])
    # A tiny footer for flair
    footer = "- (c) Existential Comedy Department"
    sys.stdout.write(COLORS["cyan"] + footer.center(50) + COLORS["reset"] + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()