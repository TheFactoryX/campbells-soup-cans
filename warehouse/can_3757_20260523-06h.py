"""
Campbell's Soup Can #3757
Produced: 2026-05-23 06:45:35
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
A tiny, colorful, animated display of a Woody‑Allen‑style philosophical gem.
Run it directly – no external libraries required.
"""

import sys
import time

# ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"
FG_CYAN = "\033[36m"
FG_YELLOW = "\033[33m"
FG_MAGENTA = "\033[35m"
FG_GREEN = "\033[32m"
BG_BLACK = "\033[40m"

# The quote – neurotic, self‑deprecating, existential
quote = (
    "I think the meaning of life is to find a reason to stay up "
    "late, stare at the ceiling, and wonder if the universe "
    "is just an elaborate prank that even the gods find funny."
)

# Box drawing characters
TL, TR, BL, BR = "╔", "╗", "╚", "╝"
H, V = "═", "║"

def typewriter(text: str, delay: float = 0.03) -> None:
    """Print text character‑by‑character."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def framed_lines(lines, width):
    """Wrap lines inside a coloured box."""
    top    = f"{FG_CYAN}{TL}{H * (width+2)}{TR}{RESET}"
    bottom = f"{FG_CYAN}{BL}{H * (width+2)}{BR}{RESET}"
    print(top)
    for line in lines:
        padded = line.ljust(width)
        print(f"{FG_CYAN}{V}{RESET} {FG_YELLOW}{padded}{RESET} {FG_CYAN}{V}{RESET}")
    print(bottom)

def main():
    # Split the quote into reasonably sized chunks
    words = quote.split()
    max_len = 50
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > max_len:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(cur)

    # Choose a random colour for the text each run (deterministic here for simplicity)
    colours = [FG_MAGENTA, FG_GREEN, FG_YELLOW]
    text_colour = colours[int(time.time()) % len(colours)]

    # Decorative header
    header = f"{BG_BLACK}{BOLD}{text_colour}  WOODY‑ALLEN QUOTE  {RESET}"
    print("\n")
    typewriter(header, delay=0.06)
    time.sleep(0.3)

    # Animated reveal of the box
    width = max(len(l) for l in lines)
    for _ in range(2):
        framed_lines(lines, width)
        time.sleep(0.2)
        # Clear the box (move cursor up)
        sys.stdout.write(f"\033[{len(lines)+2}A")
    # Final display
    framed_lines(lines, width)

    # Footer smile
    smile = f"{FG_CYAN}¯\\_(ツ)_/¯{RESET}"
    print("\n" + smile)
    time.sleep(0.5)

if __name__ == "__main__":
    main()