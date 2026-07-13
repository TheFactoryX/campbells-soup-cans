"""
Campbell's Soup Can #4183
Produced: 2026-07-13 15:11:10
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
A tiny, colorful Woody‑Allen‑style philosophical quote printer.
Runs with no external dependencies – just the Python standard library.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour codes
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# A palette of warm, slightly neurotic colours
PALETTE = [
    "\033[38;5;202m",  # orange
    "\033[38;5;208m",  # bright orange
    "\033[38;5;166m",  # dark orange
    "\033[38;5;172m",  # peach
    "\033[38;5;180m",  # light peach
]

# ----------------------------------------------------------------------
# The quote (one‑liner, Woody‑Allen‑style)
# ----------------------------------------------------------------------
QUOTE = (
    "I fear the abyss, but mostly I'm terrified of the "
    "queue at the after‑life's DMV."
)

# ----------------------------------------------------------------------
# Helper: typewriter effect with colour cycling
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04) -> None:
    """
    Print `text` one character at a time, cycling through PALETTE colours.
    """
    color_cycle = itertools.cycle(PALETTE)
    for ch in text:
        # Use a new colour for each character
        sys.stdout.write(f"{next(color_cycle)}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")  # newline at the end


# ----------------------------------------------------------------------
# Helper: draw a decorative box around the quote
# ----------------------------------------------------------------------
def boxed(text: str, padding: int = 2) -> str:
    """
    Return `text` surrounded by a simple ASCII box.
    """
    lines = text.splitlines()
    width = max(len(line) for line in lines) + padding * 2
    top_bottom = f"+{'-' * width}+"
    box_lines = [top_bottom]
    for line in lines:
        padded = f"{' ' * padding}{line}{' ' * (width - len(line) - padding)}"
        box_lines.append(f"|{padded}|")
    box_lines.append(top_bottom)
    return "\n".join(box_lines)


# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main() -> None:
    # Compose the final visual output
    framed = boxed(QUOTE)
    # Print it with a gentle fade‑in using the typewriter effect
    typewriter(f"{BOLD}{framed}{RESET}", delay=0.02)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)