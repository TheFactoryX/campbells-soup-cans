"""
Campbell's Soup Can #2016
Produced: 2026-02-03 11:01:13
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI color mapping
COLORS = {
    "reset": "\033[0m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "reverse": "\033[7m",
}

def color(text, fg="cyan", bg=None, attrs=()):
    """Wrap text with ANSI color codes."""
    codes = [COLORS["reset"]]
    if fg:
        codes.append(COLORS[fg])
    if bg:
        codes.append(COLORS[bg])
    for attr in attrs:
        codes.append(COLORS[attr])
    return "".join(codes) + text + COLORS["reset"]

def bouncing_bar(fg_color="magenta", length=20):
    """
    Horizontal bouncing bar animation.
    A segment (█) moves back and forth across a line of hyphens.
    """
    max_len = length
    for i in range(max_len + 1):
        segment = "█" if i <= max_len // 2 else " "
        left_part = "-" * (i % max_len)
        right_part = "-" * ((max_len - i) % max_len)
        bar = left_part + segment + right_part
        # Overwrite the current line
        sys.stdout.write("\r" + color(bar, fg=fg_color))
        sys.stdout.flush()
        time.sleep(0.07)
        # Erase characters before the new position to keep cursor aligned
        sys.stdout.write("\r" + " " * (i % max_len))
        sys.stdout.flush()

def main():
    # Woody Allen ASCII art banner
    banner_lines = [
        color("   __    __   ", fg="yellow", attrs=("bold",)),
        color("  /  \\  /  \\  ", fg="yellow", attrs=("bold",)),
        color(" |  -  |  -  | ", fg="yellow", attrs=("bold",)),
        color("  \\__/ \\__/   ", fg="yellow", attrs=("bold",)),
        color(" Woody Allen", fg="cyan", attrs=("bold",)),
    ]
    print("\n".join(banner_lines) + "\n", flush=True)

    # Small animation before the quote
    bouncing_bar(fg_color="cyan")

    # Woody Allen quote (single line)
    quote = color(
        "I'm not afraid of death; I just don't want to be there when it happens.",
        fg="cyan",
        attrs=("bold",)
    )
    print(quote, flush=True)

if __name__ == "__main__":
    main()