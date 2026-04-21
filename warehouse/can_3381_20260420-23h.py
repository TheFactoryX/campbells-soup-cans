"""
Campbell's Soup Can #3381
Produced: 2026-04-20 23:59:38
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
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

# ANSI Color Codes
class Color:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    print("\033[H\033[J", end="")

def typewriter_effect(text, delay=0.06, color=Color.CYAN):
    """Prints text one character at a time for dramatic effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Color.END}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_border(width, char="*", color=Color.MAGENTA):
    print(f"{color}{char * width}{Color.END}")

def neurosis_animation():
    """A little visual jitter to represent existential dread."""
    frames = [
        "  (O_O)  ",
        "  (>_<)  ",
        "  (o_o)  ",
        "  (;_;)  ",
        "  (O.O)  "
    ]
    for _ in range(3):
        for frame in frames:
            clear_screen()
            print("\n" * 5)
            print(f"{Color.YELLOW}{frame.center(40)}{Color.END}")
            print(f"{Color.BLUE}{'~' * 38}{Color.END}")
            time.sleep(0.1)

def run_performance():
    clear_screen()
    
    # The "Intro"
    draw_border(50, "=", Color.BLUE)
    print(f"{Color.BOLD}{'EXISTENTIAL CRISIS v1.0'.center(50)}{Color.END}")
    draw_border(50, "=", Color.BLUE)
    time.sleep(1)
    
    # Neurotic animation sequence
    neurosis_animation()
    
    clear_screen()
    print("\n" * 3)
    
    # The Quote Setup
    quote = (
        "\"I used to think that the meaning of life was to find "
        "happiness, but now I realize it's more about finding "
        "a way to distract myself from the fact that the universe "
        "is a vast, indifferent void that doesn't even have "
        "the courtesy to offer free snacks.\""
    )
    
    # Visual Container
    width = 60
    draw_border(width, "-", Color.MAGENTA)
    print(f"{Color.BOLD}{'A THOUGHT BY A VERY NERVOUS MAN':^{width}}{Color.END}")
    draw_border(width, "-", Color.MAGENTA)
    print("\n")

    # Typewriter the quote with line wrapping logic
    words = quote.split(' ')
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 < width - 4:
            current_line += word + " "
        else:
            typewriter_effect(current_line.strip(), 0.04, Color.WHITE)
            current_line = word + " "
    
    if current_line:
        typewriter_effect(current_line.strip(), 0.04, Color.WHITE)

    print("\n")
    draw_border(width, "-", Color.MAGENTA)
    
    # Final dramatic pause
    time.sleep(1.5)
    print(f"\n{Color.RED}{'[End of Transmission. Please seek therapy immediately.]'.center(width)}{Color.END}\n")
    print(f"{Color.BLUE}{'=' * width}{Color.END}")

if __name__ == "__main__":
    try:
        run_performance()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}Even your interruption is an expression of cosmic futility.{Color.END}")