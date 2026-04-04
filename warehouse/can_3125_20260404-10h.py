"""
Campbell's Soup Can #3125
Produced: 2026-04-04 10:53:35
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3# -*- coding: utf-8 -*-

import sys
import time

# ANSI colour codesRED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

def coloured(text, colour):
    return f"{colour}{text}{RESET}"

def centre(text, width=60):
    return text.center(width)

def typewriter_print(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def draw_border(colour_char, interior_char=' '):
    line = colour_char * 62
    return line

def main():
    quote = (
        "“I’m not afraid of death; I just keep thinking about "
        "what I’d miss if I actually _died_ before finishing this thought.”"
    )
    # Build a coloured box around the quote
    border_top = coloured(draw_border(YELLOW), YELLOW)
    box_width = len(border_top) // 2 - 2
    inner_border = coloured('│', YELLOW)
    inner_space = coloured('│', YELLOW)

    # Prepare coloured sections of the quote
    part1 = coloured("I’m not afraid of death; I just keep thinking about ", CYAN)
    part2 = coloured("what I’d miss if I actually ", MAGENTA)
    part3 = coloured("_died_", RED)
    part4 = coloured(" before finishing this thought.", GREEN)

    full_quote = part1 + part2 + part3 + part4

    # Print the visual
    typewriter_print(coloured("\n" + border_top, YELLOW), delay=0)
    for _ in range(2):
        line = coloured(inner_border, YELLOW) + coloured(' ', YELLOW) + coloured(full_quote, RESET) + coloured(' ', YELLOW) + coloured(inner_border, YELLOW) + "\n"
        typewriter_print(line, delay=0)

    typewriter_print(coloured(inner_border, YELLOW) + coloured(' ', YELLOW) + coloured('-' * box_width, YELLOW) + coloured(' ', YELLOW) + coloured(inner_border, YELLOW), delay=0)
    typewriter_print(coloured(inner_border, YELLOW) + coloured(' ', YELLOW) + coloured(' ', YELLOW) + coloured(inner_border, YELLOW), delay=0)
    typewriter_print(coloured(inner_border, YELLOW) + coloured(' ', YELLOW) + coloured(full_quote, RESET) + coloured(' ', YELLOW) + coloured(inner_border, YELLOW), delay=0)
    typewriter_print(coloured(inner_border, YELLOW) + coloured(' ', YELLOW) + coloured('--' * box_width, YELLOW) + coloured(' ', YELLOW) + coloured(inner_border, YELLOW), delay=0)
    typewriter_print(coloured(inner_border, YELLOW) + coloured(' ', YELLOW) + coloured(inner_border, YELLOW), delay=0)

    # Animated starburst to make it “visually interesting”
    stars = CYAN + '* ' * 30 + RESET
    for i in range(3):
        typewriter_print(stars, delay=0.05)
        time.sleep(0.15)
        typewriter_print(coloured(' ' * len(stars), RESET), delay=0)

    typewriter_print(coloured("\nEnjoy the existential dread. — Woody Allen", YELLOW), delay=0)

if __name__ == "__main__":
    main()