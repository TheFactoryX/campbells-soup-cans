"""
Campbell's Soup Can #3519
Produced: 2026-05-01 13:54:18
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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
import os

def typewriter(text, delay=0.05, color='\033[96m'):
    """Simulate a typewriter effect with colored text"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\033[0m\n')

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_allen_quote():
    # ASCII art border with Woody Allen's glasses
    border = [
        "╔══════════════════════════════════════════════════════════════╗",
        "║                                                              ║",
        "║    .-.   .-.   .-.   .-.   .-.   .-.   .-.   .-.   .-.   .-  ║",
        "║    '-'   '-'   '-'   '-'   '-'   '-'   '-'   '-'   '-'   '-  ║",
        "║                                                              ║",
        "║                                                              ║",
        "║                                                              ║",
        "╚══════════════════════════════════════════════════════════════╝"
    ]
    
    # Clear the screen and print the border
    clear_screen()
    for line in border:
        print(line)
    
    # The Woody Allen-style philosophical quote
    quote = "I've always been afraid of death, but I'm more terrified of dying with my to-do list unfinished."
    
    # Add typewriter effect to the quote
    typewriter(quote, delay=0.03, color='\033[93m')
    
    # Add Woody Allen's name with a creative flourish
    time.sleep(0.5)
    typewriter("                                                            ", delay=0.02)
    typewriter("                                                            ", delay=0.02)
    typewriter("                                                            ", delay=0.02)
    typewriter("                      - Woody Allen", delay=0.03, color='\033[91m')
    
    # Add a final thought with a different color
    time.sleep(1)
    typewriter("\nPS: My to-do list includes 'write will' and 'live forever'. Not sure which to prioritize.", delay=0.03, color='\033[92m')

if __name__ == "__main__":
    woody_allen_quote()