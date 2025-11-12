"""
Campbell's Soup Can #223
Produced: 2025-11-12 08:43:09
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import os
import time
import textwrap

# Colors and styles
 RESET = "\033[0m"
 BOLD = "\033[1m"
 FG_PURPLE = "\033[35m"
 FG_YELLOW = "\033[93m"
 FG_RED = "\033[31m"
 BG_DARKGRAY = "\033[40m"

def print_centered(text):
    """Print text centered on the current line."""
    width = os.get_terminal_size().columns
    print(text.center(width))

def print_woody_quote():
    """Print a Woody Allen-style quote in a visually styled box."""
    # Create a box structure
    box_width = 60
    horizontal = FG_PURPLE + "═" * (box_width + 4) + RESET
    border = FG_PURPLE + "║" + " " * (box_width + 2) + "║" + RESET
    face = [
        FG_PURPLE + "     .-.    " + RESET,
        FG_PURPLE + "    (o o)   " + RESET,
        FG_PURPLE + "     \_/    " + RESET
    ]

    # Woody Allen style quote
    quote = (
        "I'm not arguing, I'm just explaining why I'm right. " +
        "And I do it very enthusiastically because I'm "
        "terribly convinced by my own opinions, which are "
        "probably wrong and obtuse... but I present them "
        "with the seriousness of a dying philosopher."
    )
    
    # Wrap the quote to fit the box
    wrapped_quote = textwrap.fill(quote, width=box_width)
    quote_lines = wrapped_quote.split('\n')

    # Animation effect: typing style
    print_centered(BG_DARKGRAY + "              " + RESET)
    print_centered(BG_DARKGRAY + "    .-.   Wo...   " + RESET)
    print_centered(BG_DARKGRAY + "   (o o)  oops!    " + RESET)
    print_centered(BG_DARKGRAY + "    \\_/     ...tard. " + RESET)
    print_centered(BG_DARKGRAY + "              " + RESET)
    print_centered(BG_DARKGRAY + horizontal + RESET)
    
    for i, line in enumerate(quote_lines):
        # Introduce slight delay for effect
        time.sleep(0.05)
        print_centered(f"{BG_DARKGRAY}{FG_RED}{border}{RESET}")
        print_centered(f"{BG_DARKGRAY}{FG_YELLOW}║ {line} ║{RESET}")
    
    print_centered(f"{BG_DARKGRAY}{FG_RED}{horizontal}{RESET}")
    print_centered(BG_DARKGRAY + "              " + RESET)

# Run the program
if __name__ == "__main__":
    print_woody_quote()