"""
Campbell's Soup Can #4638
Produced: 2026-08-16 22:36:18
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def wrap(text, width):
    """Wrap text to fit within the given width (characters)."""
    words = text.split()
    lines = []
    current = ""
    for w in words:
        # +1 for the space between words
        if len(current) + len(w) + (1 if current else 0) <= width:
            current = (current + " " + w) if current else w
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines

def main():
    # ANSI color codes
    Cyan   = "\033[96m"   # cyan for the box
    Yellow = "\033[93m"   # yellow for the quote
    Reset  = "\033[0m"    # reset colors

    # Box dimensions (including the side characters)
    box_width = 70
    # Top and bottom borders
    print(Cyan + "╔" + "═" * (box_width - 2) + "╗" + Reset)

    # The Woody Allen‑style philosophical quote
    quote = (
        "I’m not afraid of death; I just don’t want to be there when it happens—"
        "because then I’d miss the chance to be late to my own funeral."
    )

    # Wrap the quote so it fits inside the box (leaving room for the side borders)
    wrapped_lines = wrap(quote, box_width - 4)  # -4 for "║ " and " ║"

    # Print each line of the quote inside the box
    for line in wrapped_lines:
        print(
            Cyan + "║ " + Yellow + line + Reset + " ║"
        )

    # Bottom border
    print(Cyan + "╚" + "═" * (box_width - 2) + "╝" + Reset)

if __name__ == "__main__":
    main()