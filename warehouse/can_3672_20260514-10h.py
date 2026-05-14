"""
Campbell's Soup Can #3672
Produced: 2026-05-14 10:34:01
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, self‑contained script that prints a single,
Woody‑Allen‑style philosophical quip with a splash of color
and a little “typewriter” animation.

Run it directly:
    $ python3 woody_quote.py
"""

import sys
import time

# --------------------------------------------------------------
# ANSI escape codes (foreground colors, style & reset)
# --------------------------------------------------------------
FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}
STYLE = {
    "bright": "\033[1m",
    "dim":    "\033[2m",
    "normal": "\033[22m",
}
RESET = "\033[0m"

# --------------------------------------------------------------
# The quote (Woody‑Allen‑style neurotic wisdom)
# --------------------------------------------------------------
QUOTE = (
    "I think the meaning of life is to find a comfortable seat "
    "in a coffee shop, stare at the wall, and realize that "
    "the universe has a wicked sense of humor."
)

# --------------------------------------------------------------
# Helper: print text character‑by‑character (typewriter effect)
# --------------------------------------------------------------
def type_print(text: str, delay: float = 0.04, *, color: str = "cyan"):
    col = FG.get(color, "")
    for ch in text:
        sys.stdout.write(f"{col}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# --------------------------------------------------------------
# Helper: draw a simple box around multiline text
# --------------------------------------------------------------
def boxed(lines, *, border_color="yellow"):
    """Return a list of strings that form a box around `lines`."""
    max_len = max(len(line) for line in lines)
    horiz = "─" * (max_len + 2)
    top    = f"{FG[border_color]}┌{horiz}┐{RESET}"
    bottom = f"{FG[border_color]}└{horiz}┘{RESET}"
    boxed_lines = [top]
    for line in lines:
        padded = line + " " * (max_len - len(line))
        boxed_lines.append(
            f"{FG[border_color]}│{RESET} {padded} {FG[border_color]}│{RESET}"
        )
    boxed_lines.append(bottom)
    return boxed_lines

# --------------------------------------------------------------
# Main routine
# --------------------------------------------------------------
def main():
    # Split the quote into a few manageable pieces for the box
    words = QUOTE.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > 60:   # wrap at ~60 chars
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(cur)

    # Create the boxed version
    box = boxed(lines, border_color="magenta")

    # Print an introductory splash
    banner = [
        f"{STYLE['bright']}{FG['red']}   ____        _            _   _             _   ",
        f"  / ___|  ___ | | ___   ___| |_(_) ___  _ __ | |_ ",
        f"  \\___ \\ / _ \\| |/ _ \\ / __| __| |/ _ \\| '_ \\| __|",
        f"   ___) | (_) | | (_) | (__| |_| | (_) | | | | |_ ",
        f"  |____/ \\___/|_|\\___/ \\___|\\__|_|\\___/|_| |_|\\__|",
        f"{RESET}",
    ]
    for line in banner:
        type_print(line, delay=0.005, color="red")
        time.sleep(0.03)

    # Small pause before the quote appears
    time.sleep(0.4)

    # Print the box with a gentle animation
    for line in box:
        type_print(line, delay=0.008, color="magenta")
        time.sleep(0.02)

    # Final flourish
    sys.stdout.write(f"{STYLE['dim']}{FG['green']}* * *{RESET}\n")

if __name__ == "__main__":
    main()