"""
Campbell's Soup Can #3370
Produced: 2026-04-20 03:52:17
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, self‑contained program that prints a single, Woody‑Allen‑esque
philosophical quip in a playful, animated, color‑ful style.
"""

import sys
import time
import shutil

# ANSI escape codes for colors and effects
RESET   = "\x1b[0m"
BOLD    = "\x1b[1m"
ITALIC  = "\x1b[3m"
UNDERL  = "\x1b[4m"
RED     = "\x1b[31m"
GREEN   = "\x1b[32m"
YELLOW  = "\x1b[33m"
BLUE    = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN    = "\x1b[36m"
WHITE   = "\x1b[37m"
BRIGHT  = "\x1b[97m"

# The quote we want to showcase
QUOTE = (
    "\"I think I’m a very anxious person—"
    " the paradox is that the more I think,\n"
    " the less I feel, and the more misery I discover [in the other people].\""
)

# Prepare a box around the quote
def boxed_text(text, color=CYAN):
    lines = text.splitlines()
    width = max(len(line) for line in lines)
    top = f"{color}┌{'─' * (width + 2)}┐{RESET}"
    bottom = f"{color}└{'─' * (width + 2)}┘{RESET}"
    body = []
    for line in lines:
        body.append(f"{color}│ {line:<{width}} │{RESET}")
    return "\n".join([top] + body + [bottom])

# Animate the quote sliding in from the left
def animate_quote(text, delay=0.02):
    cols, _ = shutil.get_terminal_size(fallback=(80, 24))
    # Pad with spaces to center the box
    box = boxed_text(text, color=YELLOW + BOLD)
    lines = box.splitlines()
    pad = " " * (cols // 2 - max(len(line) for line in lines) // 2)

    for shift in range(-max(len(line) for line in lines), 1):
        sys.stdout.write("\x1b[H")  # Move cursor to home
        for line in lines:
            sys.stdout.write(f"{pad}{' ' * shift}{line}\n")
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Clear screen
    sys.stdout.write("\x1b[2J")
    sys.stdout.flush()
    # Print a minimal banner before the animation
    banner = f"{MAGENTA}{BOLD}Woody‑Allen Quote…{RESET}"
    cols, _ = shutil.get_terminal_size(fallback=(80, 24))
    sys.stdout.write("\x1b[H")  # Move cursor to home
    sys.stdout.write(f"{' ' * ((cols - len(banner)) // 2)}{banner}\n\n")
    sys.stdout.flush()
    time.sleep(0.5)

    # Animate the quote sliding in
    animate_quote(QUOTE, delay=0.03)

    # Keep the screen a moment to let the user read it
    time.sleep(4)

if __name__ == "__main__":
    main()