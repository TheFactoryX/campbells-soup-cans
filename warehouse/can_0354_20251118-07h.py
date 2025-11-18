"""
Campbell's Soup Can #354
Produced: 2025-11-18 07:31:14
Worker: Google: Gemma 3 27B (free) (google/gemma-3-27b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def print_slowly(text, color_code="\033[37m"):
    """Prints text letter by letter with a slight delay, and a specific color."""
    for char in text:
        print(color_code + char, end='', flush=True)
        time.sleep(0.03)
    print()  # Newline after the whole quote

def animate_dots():
    """Simple animation of dots."""
    dots = ["·", "◦", "◌", "◉"]
    for i in range(5):
        clear_screen()
        print("\033[93m")
        print(" " * 20 + dots[i % len(dots)]) # Yellow dots
        time.sleep(0.2)
    print("\033[0m") # Reset color



def main():
    clear_screen()
    animate_dots()

    quote = "I have a pathological need to feel important, but mostly I just feel… mildly inconvenienced by existence. And also, my urologist says I'm unusually tense for a mammal."

    box_width = 70
    box_height = 10

    # Create the box
    top_bottom_border = "*" * box_width
    side_borders = "*" + " " * (box_width - 2) + "*"

    print("\033[32m") # Green box
    print(top_bottom_border)
    for i in range(box_height - 2):
        print(side_borders)
    print(top_bottom_border)

    # Calculate padding for centering the quote
    padding = (box_width - len(quote)) // 2

    # Print the quote inside the box
    print("\033[37m") # White text inside the box
    print(side_borders)
    print("*" + " " * padding + quote + " " * padding + "*")
    print(side_borders)
    print(top_bottom_border)
    print("\033[0m") # Reset color

    print("\n")
    print_slowly("– A deeply troubled individual (probably)", color_code="\033[35m") # Magenta attribution

if __name__ == "__main__":
    main()