"""
Campbell's Soup Can #4799
Produced: 2026-08-23 22:37:54
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def print_with_color(text, color_code):
    """Print text with ANSI color code"""
    print(f"\033[{color_code}m{text}\033[0m", end="", flush=True)

def typewriter_effect(text, delay=0.03, color_code="97"):
    """Print text with typewriter effect"""
    for char in text:
        print_with_color(char, color_code)
        time.sleep(delay)
    print()

def create_border(width, color="96"):
    """Create a decorative border"""
    border_chars = ["┌", "─", "┐", "│", "└", "┘"]
    top = border_chars[0] + border_chars[1] * (width - 2) + border_chars[2]
    bottom = border_chars[4] + border_chars[1] * (width - 2) + border_chars[5]
    
    print_with_color(top, color)
    print()
    print_with_color(bottom, color)

def center_text(text, width, color="97"):
    """Center text within given width"""
    padding = (width - len(text)) // 2
    centered = " " * padding + text + " " * (width - len(text) - padding)
    print_with_color(centered, color)

def woody_allen_quote():
    """Display a Woody Allen style quote with visual flair"""
    
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")
    
    # Title
    print_with_color("★ " * 5 + " WOODY ALLEN STYLE PHILOSOPHICAL MUSINGS " + "★" * 5, "93")
    print()
    
    # The quote
    quote = "I don't want to achieve immortality through my work. I want to achieve it through not dying. But since that's not working, I'll settle for a good nap. At least then I can pretend I'm dead and avoid existential dread for 20 minutes."
    
    # Break quote into lines
    max_width = 70
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(" ".join(current_line + [word])) <= max_width - 4:  # Account for padding
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(" ".join(current_line))
    
    # Create the box
    box_width = max_width + 4  # Add padding
    
    # Top border with shadow effect
    print_with_color("┌" + "─" * (box_width - 2) + "┐", "96")
    
    # Empty line
    print_with_color("│" + " " * (box_width - 2) + "│", "96")
    
    # Title line
    title = "EXISTENTIAL CRISIS"
    title_line = "│ " + title.center(box_width - 4) + " │"
    print_with_color(title_line, "93")
    
    # Empty line
    print_with_color("│" + " " * (box_width - 2) + "│", "96")
    
    # Separator
    print_with_color("├" + "─" * (box_width - 2) + "┤", "96")
    
    # Quote lines with typewriter effect
    for line in lines:
        centered_line = "│ " + line.center(box_width - 4) + " │"
        # Print with typewriter effect in white
        for char in centered_line:
            if char == "│":
                print_with_color(char, "96", end="")
            else:
                print_with_color(char, "97", end="")
            time.sleep(0.01)
        print()
    
    # Empty line
    print_with_color("│" + " " * (box_width - 2) + "│", "96")
    
    # Bottom border
    print_with_color("└" + "─" * (box_width - 2) + "┘", "96")
    
    # Footer with Woody Allen style humor
    print()
    print_with_color("★ " * 5 + " EXISTENCE IS PAINFUL BUT AT LEAST IT'S SHORT " + "★" * 5, "91")
    print()
    
    # Blinking cursor effect
    for _ in range(3):
        print_with_color("_", "97")
        time.sleep(0.3)
        print("\b \b", end="")
        time.sleep(0.3)
    
    print_with_color("\n\"The sad truth is that the truest thing in the world is that we are all alone.\"", "95")
    print_with_color("— Woody Allen (probably)", "90")

if __name__ == "__main__":
    woody_allen_quote()