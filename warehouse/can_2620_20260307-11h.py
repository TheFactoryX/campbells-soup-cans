"""
Campbell's Soup Can #2620
Produced: 2026-03-07 11:33:07
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
from itertools import cycle

def woody_allen_quote():
    # ANSI color codes
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # ASCII art frames
    def print_frame(color, delay=0.05):
        frame = [
            f"{color}╔═════════════════════════════════════════════════════════════════╗{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}║                                                                 ║{RESET}",
            f"{color}╚═════════════════════════════════════════════════════════════════╝{RESET}"
        ]
        
        for line in frame:
            print(line)
            time.sleep(delay)
    
    # Animated typing effect
    def typewriter(text, color, delay=0.03):
        for char in text:
            sys.stdout.write(color + char + RESET)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Print animated frame
    colors = [CYAN, YELLOW, MAGENTA, GREEN, RED, BLUE]
    for _ in range(2):
        for color in colors:
            print_frame(color, 0.01)
    
    # Title
    typewriter("\n\tWOODY ALLEN ON LIFE:", YELLOW, 0.02)
    
    # Quote with different colors for different parts
    quote = "I spend most of my time worrying about things that probably won't happen, which is perfect preparation for the things that will."
    
    # Split quote into parts
    parts = [
        (quote[:30], BLUE),
        (quote[30:60], MAGENTA),
        (quote[60:90], GREEN),
        (quote[90:], YELLOW)
    ]
    
    # Print quote with typewriter effect
    typewriter("\n\t\t", RESET, 0.01)
    for text, color in parts:
        typewriter(text, color, 0.02)
    
    # Signature
    typewriter("\n\n\t\t\t\t\t\t\t- WOODY ALLEN", RED, 0.02)
    
    # Animated footer
    footer = "NEUROSIS: THE ULTIMATE PHILOSOPHY"
    for i in range(3):
        print("\n" + " " * 20 + RESET + CYAN + footer + RESET + " " * 20)
        time.sleep(0.5)
        print("\n" + " " * 20 + RESET + YELLOW + footer + RESET + " " * 20)
        time.sleep(0.5)

if __name__ == "__main__":
    woody_allen_quote()