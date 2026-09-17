"""
Campbell's Soup Can #4979
Produced: 2026-09-17 21:27:37
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
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

# ANSI escape codes for colors
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

def typewriter(text, delay=0.025, color=YELLOW):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border(char, width, color):
    """Print a colored border line."""
    print(color + char * width + RESET)

def main():
    width = 65
    
    # Clear screen (works on most terminals)
    print("\033[2J\033[H", end="")
    
    # Dramatic top border
    print_border("=", width, RED)
    print()
    
    # Title with animation
    title = "WOODY'S EXISTENTIAL DILEMMAS"
    print(BOLD + CYAN + " " * 12 + title + " " * 12 + RESET)
    print_border("-", width, BLUE)
    
    time.sleep(0.6)
    
    # The neurotic quote with color shifts
    quote = (
        "I asked my therapist if I had a death wish. "
        "He said, 'Only on Wednesdays.' "
        "So I stopped going on Wednesdays. "
        "But then I realized my couch also judges me on Wednesdays."
    )
    
    print()
    print(MAGENTA + "╔" + "═" * (width - 2) + "╗" + RESET)
    print(MAGENTA + "║" + RESET, end="")
    
    # Type quote with random neurotic color dips
    colors = [RED, YELLOW, BLUE, GREEN, CYAN, MAGENTA]
    for i, char in enumerate(quote):
        # Randomly shift color for "neurotic" effect
        if random.random() < 0.08:
            color = random.choice(colors)
        else:
            color = YELLOW
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.018)
    
    print(MAGENTA + " ║" + RESET)
    print(MAGENTA + "╚" + "═" * (width - 2) + "╝" + RESET)
    print()
    
    time.sleep(0.8)
    
    # Bottom border
    print_border("=", width, RED)
    
    # Attributed with style
    attribution = "- Woody Allen, probably (on a Wednesday)"
    print(BOLD + GREEN + " " * 16 + attribution + RESET)
    print_border("=", width, RED)
    
    # Blinking existential crisis footer
    print()
    print(DIM + " " * 15, end="")
    sys.stdout.flush()
    for dot in range(4):
        time.sleep(0.4)
        sys.stdout.write(BOLD + RED + "εxistενtιαl cριsιs " + "..."[:dot+1] + RESET)
        sys.stdout.flush()
        # Move cursor back
        sys.stdout.write("\033[K")
        print(DIM + " " * 15, end="")
        sys.stdout.flush()
    
    print(DIM + " " * 15 + "...and breathing." + RESET)
    print()

if __name__ == "__main__":
    main()