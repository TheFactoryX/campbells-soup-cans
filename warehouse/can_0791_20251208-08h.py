"""
Campbell's Soup Can #791
Produced: 2025-12-08 08:46:50
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
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
A tiny, self‑contained Python program that prints
a single, funny Woody Allen‑style philosophical quote
in a colorful, animated box.
"""

import random
import sys
import time
import textwrap

# ANSI escape codes for colors --------------------------------------------
CSI = "\033["
RESET = CSI + "0m"

BLACK   = CSI + "30m"
RED     = CSI + "31m"
GREEN   = CSI + "32m"
YELLOW  = CSI + "33m"
BLUE    = CSI + "34m"
MAGENTA = CSI + "35m"
CYAN    = CSI + "36m"
WHITE   = CSI + "37m"

# Basic box drawing characters ---------------------------------------------
TOP_LEFT      = "┌"
TOP_RIGHT     = "┐"
BOTTOM_LEFT   = "└"
BOTTOM_RIGHT  = "┘"
HORIZONTAL    = "─"
VERTICAL      = "│"

# Quote -------------------------------------------------------------------
QUOTE = (
    "I'm not afraid of death; I just hate the idea that "
    "someone will write an obituary for me and I have to "
    "read the summary of my failings before they put me in "
    "the coffin."
)

# ASCII art to play with before the quote ----------------------------------
COFFEE_ART = [
    "                (  )",
    "      (         )",
    " _________       _______",
    "|         |     |       |",
    "|  Caffeine|     |  Brain|",
    "|   Love   |___  |  is  |",
    "|_________|   ||_|______|",
]

def flush():
    """Flush the standard output."""
    sys.stdout.flush()

def type_text(text, delay_range=(0.02, 0.06), color=RESET):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        flush()
        time.sleep(random.uniform(*delay_range))

def print_boxed_quote(quote, width):
    """Print the quote inside a centered, colored box."""
    # Prepare box borders
    top = f"{RED}{TOP_LEFT}{HORIZONTAL * width}{TOP_RIGHT}{RESET}"
    bottom = f"{RED}{BOTTOM_LEFT}{HORIZONTAL * width}{BOTTOM_RIGHT}{RESET}"
    blank = f"{RED}{VERTICAL}{RESET}{' ' * width}{RED}{VERTICAL}{RESET}"

    sys.stdout.write(top + "\n")
    flush()
    time.sleep(0.3)

    # Wrap the quote within the box width
    wrapped = textwrap.wrap(quote, width=width)
    for line in wrapped:
        padding = width - len(line)
        left_padding = padding // 2
        right_padding = padding - left_padding
        content = (
            f"{RED}{VERTICAL}{RESET}"
            f"{CYAN}{' ' * left_padding}{line}{' ' * right_padding}{RESET}"
            f"{RED}{VERTICAL}{RESET}"
        )
        type_text(content + "\n", delay_range=(0.015, 0.025), color="")
    flush()
    time.sleep(0.3)
    sys.stdout.write(bottom + "\n")
    flush()

def main():
    # Determine optimal box width
    box_width = max(len(line) for line in COFFEE_ART)
    wrapped_quote = textwrap.wrap(QUOTE, width=box_width)
    box_width = max(box_width, max(len(line) for line in wrapped_quote))

    # Animate coffee ASCII art
    for art_line in COFFEE_ART:
        type_text(COFFEE_ART[COFFEE_ART.index(art_line)], delay_range=(0.02, 0.04), color=YELLOW)
        sys.stdout.write("\n")
        flush()
        time.sleep(0.15)

    sys.stdout.write("\n")
    flush()
    time.sleep(0.5)

    # Print quote inside a colorful box
    print_boxed_quote(QUOTE, box_width)

    # Final flourish ---------------------------------------------------------
    flourish = f"{MAGENTA}*** End of existential rant ***{RESET}\n"
    type_text(flourish, delay_range=(0.04, 0.06), color="")

if __name__ == "__main__":
    main()
    sys.exit(0)