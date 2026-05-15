"""
Campbell's Soup Can #3687
Produced: 2026-05-15 22:11:10
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
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

# ANSI color codes
COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_gray": "\033[100m",
}

def type_writer(text: str, color: str = COLORS["white"], delay: float = 0.05):
    """Print text character by character with a slight delay."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(COLORS["reset"] + "\n")

def print_boxed(title: str, content: str, border_color=COLORS["cyan"], title_color=COLORS["yellow"]):
    """Print a simple ASCII box with title and content."""
    width = max(len(title), len(content)) + 4
    top_bottom = border_color + "╔" + "═" * (width - 2) + "╝" + COLORS["reset"]
    middle = border_color + "║" + COLORS["reset"] + " " + title_color + title.center(width - 2) + COLORS["reset"] + " " + border_color + "║" + COLORS["reset"]
    content_line = border_color + "║" + COLORS["reset"] + " " + content.ljust(width - 2) + " " + border_color + "║" + COLORS["reset"]
    bottom = border_color + "╚" + "═" * (width - 2) + "╝" + COLORS["reset"]
    sys.stdout.write(top_bottom + "\n")
    sys.stdout.write(middle + "\n")
    sys.stdout.write(content_line + "\n")
    sys.stdout.write(bottom + "\n")

def main():
    # A little neurotic ASCII art (just for fun)
    neurotic_art = r"""
      (\_/)
      ( •_•)
      / >🥜
    """
    # Print the art in a funny color
    sys.stdout.write(COLORS["magenta"] + neurotic_art + COLORS["reset"])

    # Woody Allen‑style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens — preferably with a good Wi‑Fi signal."

    # Display inside a colorful box
    print_boxed("Woody Allen Wisdom", quote, border_color=COLORS["blue"], title_color=COLORS["bold"])

    # Optional: type‑writer effect for extra flair (uncomment if desired)
    # type_writer(quote, color=COLORS["cyan"], delay=0.07)

if __name__ == "__main__":
    main()