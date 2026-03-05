"""
Campbell's Soup Can #2577
Produced: 2026-03-05 06:03:25
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os
from random import randint

# ANSI color codes
C = lambda c: f"\033[{c}m"
RESET = C(0)
CYAN = C(96)
YELLOW = C(93)
MAGENTA = C(95)
RED = C(91)
GREEN = C(92)
WHITE = C(97)
BOLD = C(1)
ITALIC = C(3)

def typewriter(text, delay=0.03, color=WHITE):
    """Print text with typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        if randint(0, 100) < 5:
            time.sleep(delay * 5)
    sys.stdout.write(RESET + "\n")

def center(text, pad=0, color=WHITE):
    """Center text in terminal"""
    width = os.get_terminal_size().columns
    text_width = len(text) + 2 * pad if pad else len(text)
    padding = (width - text_width) // 2
    print(color + " " * padding + (" " * pad if pad else "") + text + (" " * pad if pad else "") + RESET)

def anxiety_meter():
    """Draw an anxiety meter"""
    center("ANXIETY LEVEL", RED + BOLD)
    for i in range(11):
        level = "█" * i + "░" * (10 - i)
        center(f"{level} {i*10}%", RED)
        time.sleep(0.1)
    center("Yep, that's about right.", ITALIC + YELLOW)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Title
    center("WOODY ALLEN'S PHILOSOPHICAL MUSINGS", BOLD + CYAN)
    print()
    
    # Anxiety meter
    anxiety_meter()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Quote
    quote = "I'm not afraid of dying, I'm just terrified of having to attend my own funeral and realizing I didn't RSVP."
    author = "─ Woody Allen"
    
    # Decorative frame
    width = max(len(quote), 50) + 6
    center("╔" + "═" * width + "╗", CYAN)
    center("║" + " " * width + "║", CYAN)
    center("║  ", WHITE, end="")
    typewriter(quote, 0.02, YELLOW)
    center("║", CYAN)
    center("║" + " " * width + "║", CYAN)
    center("║" + " " * (width//2 - len(author)//2) + 
            author + " " * (width//2 - len(author)//2) + "║", 
            CYAN)
    center("║" + " " * width + "║", CYAN)
    center("╚" + "═" * width + "╝", CYAN)
    
    # Commentary
    print()
    center("You know, I was thinking about this while trying to parallel park...", ITALIC + WHITE)
    time.sleep(1)
    center("And I realized death is just like parallel parking -", ITALIC + YELLOW)
    time.sleep(0.5)
    center("everyone's watching, and you'll probably bump into something.", ITALIC + YELLOW)
    
    # Thought bubble
    print("\n" * 2)
    bubble = [
        "      .-''''''-.",
        "     /           \\",
        "    |   O     O   |",
        "    |      ~      |",
        "     \\   \\___/   /",
        "      '-.......-'",
        "           |",
        "           |",
        "           |"
    ]
    for line in bubble:
        center(line, WHITE)
    
    # Exit message
    print("\n" * 2)
    center("Press any key to exit before I start worrying about the catering...", GREEN)
    input()

if __name__ == "__main__":
    main()