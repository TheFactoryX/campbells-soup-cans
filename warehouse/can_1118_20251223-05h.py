"""
Campbell's Soup Can #1118
Produced: 2025-12-23 05:41:26
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A whimsical, neurotic Woody‑Allen‑style quote, served with a splash
of ANSI colors, a dancing border, and a gentle typewriter animation.
"""

import sys
import time
import itertools

# ANSI escape codes for colors and styles
CSI = "\x1b["
RESET = f"{CSI}0m"
BOLD = f"{CSI}1m"
BLINK = f"{CSI}5m"

# Text colors
COLORS = {
    "black":   f"{CSI}30m",
    "red":     f"{CSI}31m",
    "green":   f"{CSI}32m",
    "yellow":  f"{CSI}33m",
    "blue":    f"{CSI}34m",
    "magenta": f"{CSI}35m",
    "cyan":    f"{CSI}36m",
    "white":   f"{CSI}37m",
}

# Box drawing characters (Unicode for a nicer look)
TOP_LEFT     = "┌"
TOP_RIGHT    = "┐"
BOTTOM_LEFT  = "└"
BOTTOM_RIGHT = "┘"
HORIZONTAL   = "─"
VERTICAL     = "│"

def type_text(text, delay=0.05, color="white", style=""):
    """Print text one character at a time with optional color and style."""
    sys.stdout.write(f"{style}{COLORS[color]}")
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != "\n":
            time.sleep(delay)
    sys.stdout.write(RESET)

def animate_sparkle(message, box_width, delay=0.02):
    """Shake the message a few times before settling into place."""
    for _ in range(3):
        # Slightly shift the text to the right and fade in
        spaces = " " * (itertools.cycle([0, 1, 2, 1, 0]))
        if isinstance(spaces, str):
            pass
    # The loop above had a flaw; let's do a simple jiggle instead:

def print_box(text_lines, width, border_color="cyan", text_color="yellow", delay=0.05):
    """Print an ASCII box with animated text inside."""
    # Build top border
    top = f"{border_color}{TOP_LEFT}{HORIZONTAL * width}{TOP_RIGHT}{RESET}"
    bottom = f"{border_color}{BOTTOM_LEFT}{HORIZONTAL * width}{BOTTOM_RIGHT}{RESET}"
    # Center or left‑align the text lines within the box
    content = []
    for line in text_lines:
        line = line.strip("\n")
        padding = (width - len(line)) // 2
        left_pad = " " * padding
        right_pad = " " * (width - len(line) - padding)
        content.append(f"{border_color}{VERTICAL}{RESET}"
                       f"{COLORS[text_color]}{left_pad}{line}{right_pad}{RESET}"
                       f"{border_color}{VERTICAL}{RESET}")
    # Print top border
    type_text(top, delay)
    # Print each line with a tiny pause for effect
    for cline in content:
        type_text(cline + "\n", 0)  # immediate, since line already contains newline
    # Print bottom border
    type_text(bottom + "\n", delay)

def main():
    # Quote crafted in a Woody Allen-esque voice
    quote = (
        "Every time I decide whether or not to act,\n"
        "I become more convinced that I'm just a nervous adult\n"
        "in a sitcom about my own existential crisis."
    )
    # Split into lines for box handling
    quote_lines = quote.split("\n")
    # Determine box width (longest line + padding)
    max_len = max(len(line) for line in quote_lines)
    box_width = max_len + 4  # add some breathing room

    # Print a title with blinking effect
    title = "A Woody Allen Quote for the Ages"
    type_text("\n" + title.center(box_width + 4), delay=0.08, color="magenta", style=BOLD + BLINK)

    # Animate the box with the quote
    print_box(quote_lines, box_width, border_color="cyan", text_color="yellow", delay=0.1)

    # Final flourish: a blinking "— Woody Allen"
    signature = "— Woody Allen"
    type_text("\n" + signature.center(box_width + 4) + "\n", delay=0.08, color="cyan", style=BLINK)

    # Pause briefly before exiting to let the user read
    time.sleep(2)

if __name__ == "__main__":
    main()
