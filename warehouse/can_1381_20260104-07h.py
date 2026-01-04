"""
Campbell's Soup Can #1381
Produced: 2026-01-04 07:32:51
Worker: Google: Gemini 2.0 Flash Experimental (free) (google/gemini-2.0-flash-exp:free)
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

def print_animated_quote(quote):
    """Prints a philosophical quote with a Woody Allen vibe in an animated, colorful way."""

    colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
        "\033[37m"   # White
    ]
    reset_color = "\033[0m"

    # ASCII Art - Silhouetted Woody Allen (sort of)
    woody_silhouette = """
     _,-._
    / \_/ \
    >-(_)-<    
    \_/ \_/   
      `-'
    """
    
    print(woody_silhouette)
    print("\n")
    
    # Box creation and animation
    box_width = len(quote) + 6  # Padding
    print_color = colors[0]
    
    def print_box_top(width, color_code):
        print(color_code + "┌" + "─" * (width - 2) + "┐" + reset_color)

    def print_box_bottom(width, color_code):
        print(color_code + "└" + "─" * (width - 2) + "┘" + reset_color)

    def print_box_line(text, width, color_code):
         padding = (width - len(text) - 2) // 2
         print(color_code + "│" + " " * padding + text + " " * (width - 2 - padding - len(text) + 1)  + "│" + reset_color)

    print_box_top(box_width, print_color)
    print_box_line("", box_width,print_color)
    print_box_line(quote, box_width, print_color)
    print_box_line("", box_width, print_color) #extra for spacing
    print_box_bottom(box_width, print_color)
    print("\n")

if __name__ == "__main__":
    woody_quote = "Eternity is a very long time, especially towards the end.  I'm thinking maybe a shorter lease?"
    print_animated_quote(woody_quote)