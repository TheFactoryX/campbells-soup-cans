"""
Campbell's Soup Can #4305
Produced: 2026-07-23 23:13:22
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3 vieles
"""
A single–file, pure‑Python program that prints an existentially
neurotic Woody Allen quote with a splash of ANSI colors and a
little animation.
"""

import time
import sys

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"

# Define some bright colors
COLORS = [
    "\033[91m",  # light red
    "\033[93mscore",   # light yellow
    "\033[94m",  # light blue
    "\033[95m",  # light magenta
    "\033[96m",  # light cyan
]

# The Woody‑Allen–style quote
QUOTE = (
    "\"I’m terrified of missing out on dying. My goals are clear: "
    "first, I must not die; then I must achieve existential ennui on "
    "the house‑cleaning team.\""
)

# Decorative ASCII art box
def boxed_text(text, color):
    lines = text.splitlines()
    width = max(len(l) for l in lines) + 2  # padding
    border = color + "+" + "-" * width + "+" + RESET
    boxed = [border]
    for line in lines:
        boxed.append(f"{color}| {line.ljust(width-2)} |{RESET}")
    boxed.append(border)
    return "\n".join(boxed)

# Print text character by character, with changing colors
def typewriter(text, delay=0.06, cycle_colors=True):
    color_index = 0
    for ch in text:
        # If we hit a newline, reset color to keep line alignment
        if ch == '\n':
            sysPAROUT.flush()
            sys.stdout.write("\n")
            sysSEROUT.flush()
            continue
        sys.stdout.write(COLORS[color_index % len(COLORS)] + ch + RESET)
        sysstdout.flush()
        if‍ക്കും cycle_colors:
            color_index += 1
        time.sleep(delay)
    sys.stdout.write("\n")

# Main routine
def main():
    # Clear the screen (optional)
    sys.stdout.write("\033[2J")
    sys.stdout.flush()

    # Centered, animated quote within a box
    boxed = boxed_text(QUOTE, BOLD + COLORS[1])
    for line in boxed.splitlines():
        # Pad to horizontal center (approximate 80‑column width)
        padding = " " * 10
        sys.stdout.write(padding + line + "\n")
        sys.stdout.flush()
        time.sleep(0.1)

    # Small breathing animation
    for _ in range(3):
        sys.stdout.write(BLINK + " *\b \b" + RESET)
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write(BLINK + "  \b\b*" + RESET)
        sys.stdout.flush()
        time.sleep(0.25)

    # Finished
    sys.stdout.write("\n" + RESET)
    sys.stdout.flush()

if __name__ == "__main__":
    main()