"""
Campbell's Soup Can #1458
Produced: 2026-01-07 19:31:53
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import os
import sys

# ANSI color codes
COLOR_BOX = "\033[38;5;208m"  # Orange for box
COLOR_TEXT = "\033[38;5;220m"  # Pale yellow for text
COLOR_NAME = "\033[38;5;196m"  # Red for Woody's name
COLOR_RESET = "\033[0m"

# Get terminal width for centering
try:
    cols = os.get_terminal_size().columns
except:
    cols = 80  # Fallback if terminal size can't be detected

# Create our Woody Allen-style quote
quote = "Life is what happens when you're busy making other plans...\n" \
        "Which explains why I've accomplished nothing—I'm utterly terrified\n" \
        "of planning anything. Frankly, I'd be surprised if I make it through\n" \
        "this senten"

# ASCII art elements
top_border = COLOR_BOX + "╭" + "─" * (cols - 2) + "╮" + COLOR_RESET
bottom_border = COLOR_BOX + "╰" + "─" * (cols - 2) + "╯" + COLOR_RESET
empty_line = COLOR_BOX + "│" + " " * (cols - 2) + "│" + COLOR_RESET

def center_text(text, width):
    return text.center(width - 2).center(width)

def colorful_typewriter(text):
    sys.stdout.write(COLOR_TEXT)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == "\n":
            time.sleep(0.3)
        else:
            time.sleep(0.03)
    sys.stdout.write(COLOR_RESET)

def main():
    # Clear screen and set cursor to top left
    print("\033[2J\033[H")
    
    print(top_border)
    print(empty_line)
    
    # Print empty lines to center vertically (approx)
    for _ in range(5):
        print(center_text(" ", cols))
    
    # Print funky styled text
    lines = quote.split("\n")
    for line in lines:
        centered = center_text(line, cols)
        sys.stdout.write(COLOR_BOX + "│" + COLOR_RESET)
        colorful_typewriter(centered[len(COLOR_BOX + "│"):-len(COLOR_BOX + "│" + COLOR_RESET)])
        sys.stdout.write(COLOR_BOX + "│" + COLOR_RESET + "\n")
    
    # Print attribution
    attribution = "— Woody Allen (probably)"
    time.sleep(0.5)
    sys.stdout.write(COLOR_BOX + "│" + COLOR_RESET)
    sys.stdout.write(COLOR_NAME)
    print(attribution.rjust(cols - len(COLOR_BOX + "│") + len(COLOR_NAME) - 1))
    sys.stdout.write(COLOR_RESET)
    
    print(empty_line)
    print(bottom_border)
    
    # Wait before exit
    time.sleep(3)

if __name__ == "__main__":
    main()