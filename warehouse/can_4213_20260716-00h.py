"""
Campbell's Soup Can #4213
Produced: 2026-07-16 00:12:08
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
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

# ANSI color escape codes
C = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "cyan": "\033[36m",
    "yellow": "\033[33m",
    "green": "\033[32m",
    "magenta": "\033[35m",
    "red": "\033[31m",
}

def typewriter(text: str, delay: float = 0.04, color: str = "") -> None:
    """Print text character‑by‑character with an optional color."""
    for ch in text:
        sys.stdout.write(color + ch + C["reset"])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def draw_boxed_quote(text: str, title: str = "") -> None:
    """Draw the given quote inside an ASCII art box with optional title."""
    lines = text.split("\n")
    width = max(len(line) for line in lines)

    # Top border
    print(C["cyan"] + "╔" + "═" * (width + 2) + "╗" + C["reset"])

    # Title line (if any)
    if title:
        print(C["cyan"] + "║" + C["yellow"] + title.center(width + 2) + C["cyan"] + "║" + C["reset"])
        print(C["cyan"] + "╠" + "═" * (width + 2) + "╣" + C["reset"])

    # Content lines
    for line in lines:
        print(C["cyan"] + "║" + C["green"] + line.ljust(width + 2) + C["cyan"] + "║" + C["reset"])

    # Bottom border
    print(C["cyan"] + "╚" + "═" * (width + 2) + "╝" + C["reset"])

def main() -> None:
    # One philosophical quote in Woody Allen's neurotic, self‑deprecating style
    quote = (
        "I'm terrified of death, but then I realized—"
        "I'm too busy checking my phone to actually practice dying."
    )

    # Show the quote with a fancy box (the ASCII art itself provides visual interest)
    draw_boxed_quote(quote, title=" Woody Allen's Scroll ")

    # Optional: reveal the quote with a typewriter effect (uncomment if desired)
    # typewriter(quote, delay=0.05, color=C["green"])

if __name__ == "__main__":
    main()