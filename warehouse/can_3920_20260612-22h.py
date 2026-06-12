"""
Campbell's Soup Can #3920
Produced: 2026-06-12 22:00:25
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
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
A tiny console‑art program that prints a single, neurotic,
Woody‑Allen‑style philosophical quote with a splash of colour.
"""

import sys
import time

# ----------------------------------------------------------------------
# ANSI colour utilities
# ----------------------------------------------------------------------
RESET = "\033[0m"

# style helpers
def rgb(r, g, b):
    """Return an ANSI escape for true‑color foreground."""
    return f"\033[38;2;{r};{g};{b}m"

def bold(text):
    return f"\033[1m{text}{RESET}"

def italic(text):
    return f"\033[3m{text}{RESET}"

def blink(text):
    return f"\033[5m{text}{RESET}"

# ----------------------------------------------------------------------
# The quote and its decorative layout
# ----------------------------------------------------------------------
QUOTE = (
    "I’m not afraid of death; I just don't want to be there when it "
    "happens."
)

# Choose a colour palette (soft, nervous pastels)
PALETTE = [
    rgb(255, 170, 0),   # warm orange
    rgb(255, 120, 120), # gentle red
    rgb(100, 180, 255), # calm blue
    rgb(180, 180, 255), # lilac
]

# ----------------------------------------------------------------------
# Helper to slowly “type” a line with a given colour
# ----------------------------------------------------------------------
def type_out(line: str, colour: str, delay: float = 0.025):
    for ch in line:
        sys.stdout.write(colour + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Build a simple ASCII box around the quote
# ----------------------------------------------------------------------
def build_box(text: str, padding: int = 2) -> list[str]:
    lines = text.split("\n")
    width = max(len(l) for l in lines) + padding * 2
    top = "╔" + "═" * width + "╗"
    bottom = "╚" + "═" * width + "╝"
    boxed = [top]
    for l in lines:
        padded = " " * padding + l.ljust(width - padding * 2) + " " * padding
        boxed.append("║" + padded + "║")
    boxed.append(bottom)
    return boxed

# ----------------------------------------------------------------------
# Main animation routine
# ----------------------------------------------------------------------
def main():
    # 1️⃣ Show a brief “thinking” animation
    thinking = [".  ", ".. ", "..."]
    sys.stdout.write(bold(rgb(150, 150, 150) + "Thinking" + RESET))
    for _ in range(6):
        for frame in thinking:
            sys.stdout.write("\r" + bold(rgb(150, 150, 150) + "Thinking" + RESET) + frame)
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write("\r" + " " * 20 + "\r")  # clear line

    # 2️⃣ Build and display the boxed quote with colour cycling
    box_lines = build_box(italic(QUOTE))
    for i, line in enumerate(box_lines):
        colour = PALETTE[i % len(PALETTE)]
        # make the top and bottom lines blink for extra drama
        if i == 0 or i == len(box_lines) - 1:
            line = blink(line)
        type_out(line, colour, delay=0.01)

    # 3️⃣ Final punch‑line in bold white
    time.sleep(0.5)
    print(bold(rgb(255, 255, 255) + "\n— Woody Allen (probably)" + RESET))

if __name__ == "__main__":
    main()