"""
Campbell's Soup Can #3002
Produced: 2026-03-28 03:16:22
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/envpython3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------
# Woody Allen meets ASCII art – a single, colorful, philosophical quote# ------------------------------------------------------------

# ANSI colour codes (no external libraries needed)
RED   = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW= "\x1b[33m"
BLUE  = "\x1b[34m"
MAGENTA= "\x1b[35m"
CYAN  = "\x1b[36m"
WHITE = "\x1b[37m"
RESET = "\x1b[0m"

# The quote we want to display – in true Woody Allen neurotic style
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

# A tiny ASCII "frame" that will hold the quote
FRAME = r"""
╔════════════════════════════════════════════════════════════════╗
║                                                                 ║║  """ + QUOTE + r"""                                                ║
║                                                                 ║
╚════════════════════════════════════════════════════════════════╝
"""

def colored_print(text, color_code):
    """Print `text` wrapped in the given ANSI colour, then reset."""
    print(f"{color_code}{text}{RESET}")

def main():
    # Choose a colour that feels "Woody Allen": a mix of melancholy and wit.
    # Here we cycle through a few shades for visual fun.
    colours = [CYAN, MAGENTA, YELLOW, BLUE, GREEN, WHITE]
    for col in colours:
        # Add a short pause-like effect with a tiny flicker (just extra newlines)
        print("\n")
        colored_print(FRAME, col)

        # Small pause to make it feel animated without external libs
        import time
        time.sleep(0.6)

    # Final clean line
    print("\n" + RESET + "Enjoy the existential chuckle!" + RESET)

if __name__ == "__main__":
    main()