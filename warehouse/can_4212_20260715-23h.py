"""
Campbell's Soup Can #4212
Produced: 2026-07-15 23:15:00
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# --- ANSI Escape Codes for Color ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
ENDC = "\033[0m"
CLEAR = "\033[2J"
HOME = "\033[H"

def cosmic_typing(text, delay=0.04):
    """
    Prints text with a typewriter effect, cycling through colors
    to simulate a nervous, flickering consciousness (Woody Allen style).
    """
    for char in text:
        # Pick a random color for a neurotic, unpredictable feel
        color = random.choice([RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, ENDC])
        sys.stdout.write(color)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(ENDC) # Reset terminal color at the end of the print

def draw_silhouette():
    """
    Draws a small, neurotic ASCII art silhouette of a thinker.
    """
    art = [
        f"{BOLD}{CYAN}    ,--.__               ,--.____",
        f"{BOLD}{CYAN}    |  ._ _._._ _ ._ _  |._/| . )",
        f"{BOLD}{YELLOW}    |  |_| | ||_||_)|| ||  \\|/)",
        f"{BOLD}{YELLOW}    `---