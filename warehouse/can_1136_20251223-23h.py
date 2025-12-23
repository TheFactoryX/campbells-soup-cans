"""
Campbell's Soup Can #1136
Produced: 2025-12-23 23:31:04
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen style philosophical quote generator.
Neurotic, existential, and visually entertaining.
"""

import sys
import time

def print_colorful_text(text, color_code, bold=False):
    """Print text with ANSI color codes."""
    bold_code = "1;" if bold else ""
    print(f"\033[{bold_code}{color_code}m{text}\033[0m", end="")

def print_woody_allen_quote():
    """Display a Woody Allen style quote with creative formatting."""
    
    # Woody Allen quote
    quote = "Life is what happens when you're busy making other plans... terrible, anxiety-inducing plans that will definitely go wrong."
    
    # ASCII art of a worried face
    face = [
        "         ╱╲       ",
        "        ╱  ╲      ",
        "       ╱    ╲     ",
        "      │  ◕  ◕ │    ",
        "      │   ╥   │    ",
        "      ╲   ║   ╱   ",
        "       ╲  ║  ╱     ",
        "        ╲═╩═╱      ",
        "         ╰─╯       "
    ]
    
    print("\n" * 2)
    
    # Print the face in yellow
    for line in face:
        print_colorful_text("  " + line, "33")
        print()
    
    print("\n" * 2)
    
    # Create a decorative box around the quote
    quote_lines = quote.split("... ")
    
    print_colorful_text("  " + "╔" + "═" * 65 + "╗", "36", bold=True)
    print()
    
    for i, line in enumerate(quote_lines):
        if i == 0:
            print_colorful_text("  ", "36", bold=True)
            print_colorful_text("║", "36", bold=True)
            print_colorful_text(f"  {line}...", "33")
            print_colorful_text(" " * (65 - len("  " + line + "...") - 2), "36")
            print_colorful_text("║", "36", bold=True)
            print()
        else:
            print_colorful_text("  ", "36", bold=True)
            print_colorful_text("║", "36", bold=True)
            print_colorful_text(f"  {line}", "33")
            print_colorful_text(" " * (65 - len("  " + line) - 2), "36")
            print_colorful_text("║", "36", bold=True)
            print()
    
    print_colorful_text("  " + "╚" + "═" * 65 + "╝", "36", bold=True)
    print()
    
    # Print Woody's name blinking
    print("\n" * 2)
    print_colorful_text(" " * 25, "36")
    for _ in range(3):
        print_colorful_text("— Woody Allen", "35")
        time.sleep(0.5)
        print("\b" * 12, end="")
        print_colorful_text("            ", "35")
        time.sleep(0.5)
        print("\b" * 12, end="")
    print_colorful_text("— Woody Allen", "35")


if __name__ == "__main__":
    print_woody_allen_quote()
    print("\n\n")