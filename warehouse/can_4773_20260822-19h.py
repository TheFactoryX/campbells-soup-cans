"""
Campbell's Soup Can #4773
Produced: 2026-08-22 19:34:51
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import textwrap
import os
import time

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BG_BLUE = "\033[44m"
BG_YELLOW = "\033[43m"

def print_slow(text, delay=0.03, end="\n"):
    """Print text with a typewriter effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print(end, flush=True)

def create_box(text, width=70, padding=2):
    """Create a stylish ASCII box around text."""
    lines = textwrap.wrap(text, width=width - 2 * padding - 4)
    
    # Calculate box dimensions
    box_width = width
    inner_width = box_width - 4
    
    # Top border
    top = "╔" + "═" * (box_width - 2) + "╗"
    bottom = "╚" + "═" * (box_width - 2) + "╝"
    
    # Build the box
    box_lines = [top]
    
    # Empty top padding
    box_lines.append("║" + " " * (box_width - 2) + "║")
    
    # Text lines
    for line in lines:
        padded_line = line.center(inner_width)
        box_lines.append("║ " + BG_BLUE + YELLOW + padded_line + RESET + " ║")
    
    # Empty bottom padding
    box_lines.append("║" + " " * (box_width - 2) + "║")
    box_lines.append(bottom)
    
    return "\n".join(box_lines)

def main():
    # Clear screen for better effect
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Woody Allen style quote
    quote = (
        "I don't want to achieve immortality through my work; "
        "I want to achieve it through not dying. But then again, "
        "if I stop working, who will write about my existential dread? "
        "The universe is indifferent, but at least my neurotic anxieties "
        "have good material for my next stand-up routine."
    )
    
    # Print intro
    print(BOLD + CYAN + "✨ WOODY ALLEN'S EXISTENTIAL CORNER ✨" + RESET)
    print()
    
    # Create and print the box
    box = create_box(quote)
    print(box)
    print()
    
    # Print some decorative elements
    print(BOLD + RED + "─" * 60 + RESET)
    print(YELLOW + "A philosophical thought brought to you by:" + RESET)
    print(BLUE + "An overthinking individual who's afraid of both death and life." + RESET)
    print(RED + "─" * 60 + RESET)
    
    # Print quote slowly
    print("\n" + BOLD + "Speak the wisdom slowly..." + RESET + "\n")
    print_slow(quote, delay=0.04)
    
    # Final touch
    print("\n" + CYAN + "Remember: Existence precedes essence, but anxiety comes first." + RESET)

if __name__ == "__main__":
    main()