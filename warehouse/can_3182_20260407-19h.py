"""
Campbell's Soup Can #3182
Produced: 2026-04-07 19:31:57
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

import sys
import time
import itertools

# ---------- ANSI color helpers ----------
ESC = "\033["
RESET = ESC + "0m"

def color(text: str, fg: int = 37, bg: int = 40, style: int = 0) -> str:
    """Return text wrapped in ANSI escape codes."""
    return f"{ESC}{style};{fg};{bg}m{text}{RESET}"

def rainbow_cycle(text: str, delay: float = 0.05):
    """Print the given text one character at a time, cycling through rainbow colors."""
    # 31‑36 are the basic foreground colors (red to cyan)
    colors = [31, 33, 32, 36, 34, 35]  # red, yellow, green, cyan, blue, magenta
    for i, ch in enumerate(text):
        col = colors[i % len(colors)]
        sys.stdout.write(color(ch, fg=col, style=1))
        sys.stdout.flush()
        time.sleep(delay)
    print()  # final newline


# ---------- ASCII art box ----------
def boxed(text: str, padding: int = 2) -> str:
    """Wrap a multi‑line string in a fancy box."""
    lines = text.splitlines()
    width = max(len(line) for line in lines) + padding * 2
    top = f"{color('╔' + '═' * width + '╗', fg=36)}"
    bottom = f"{color('╚' + '═' * width + '╝', fg=36)}"
    middle = []
    for line in lines:
        space = " " * (width - len(line) - padding * 2)
        middle.append(
            f"{color('║', fg=36)}"
            f"{' ' * padding}{line}{space}{' ' * padding}"
            f"{color('║', fg=36)}"
        )
    return "\n".join([top] + middle + [bottom])


# ---------- The quote ----------
quote = (
    "I told the universe I’d like to be left alone, "
    "but it kept calling me for a meeting that never started."
)

author = "- Woody Allen (probably)"

# Build the full message
msg = f"{quote}\n{author}"
boxed_msg = boxed(msg)

# ---------- Animated display ----------
def main():
    # Fade‑in the box line‑by‑line
    for line in boxed_msg.splitlines():
        rainbow_cycle(line, delay=0.01)
        time.sleep(0.05)

    # End with a blinking reminder
    blink = itertools.cycle([ESC + "5m", ESC + "25m"])  # blink on / off
    reminder = " (Press Ctrl‑C to exit) "
    for _ in range(6):
        sys.stdout.write(next(blink) + color(reminder, fg=33, style=1) + RESET + "\r")
        sys.stdout.flush()
        time.sleep(0.5)
    print()  # final clean line


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)