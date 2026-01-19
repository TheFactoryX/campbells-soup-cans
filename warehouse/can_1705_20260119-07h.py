"""
Campbell's Soup Can #1705
Produced: 2026-01-19 07:43:32
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colorful_quote():
    # ANSI color codes
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'
    
    # The quote
    quote = "I'm not afraid of death, I just want to make sure it happens when I'm not looking."
    
    # Clear screen
    clear_screen()
    
    # Title with dramatic entrance
    title = "WOODY ALLEN ON LIFE AND DEATH"
    for i, char in enumerate(title):
        sys.stdout.write(YELLOW + BOLD + char + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n" + YELLOW + BOLD + "═" * len(title) + RESET + "\n")
    
    # Woody Allen ASCII art
    woody = [
        YELLOW + "      .-.   .-.",
        "     (   \\ /   )",
        "      \\   '   /",
        "       \\     /",
        "        \\   /",
        "         \\ /",
        "          '",
        RESET
    ]
    
    # Print ASCII art with delay
    for line in woody:
        print(line.center(80))
        time.sleep(0.2)
    
    # Quote presentation with typewriter effect
    print("\n" + CYAN + BOLD + "─" * 80 + RESET)
    print()
    
    # Typewriter effect for the quote
    for char in quote:
        sys.stdout.write(MAGENTA + ITALIC + char + RESET)
        sys.stdout.flush()
        time.sleep(0.03 * (0.5 + random.random()))
    
    print("\n")
    print(CYAN + BOLD + "─" * 80 + RESET + "\n")
    
    # Author attribution with fade-in effect
    author = "                                - Woody Allen"
    for i, char in enumerate(author):
        sys.stdout.write(WHITE + BOLD + char + RESET)
        sys.stdout.flush()
        time.sleep(0.01)
    
    print("\n" * 2)
    
    # Animated stars at the end
    for _ in range(5):
        for i in range(3):
            time.sleep(0.3)
            star = random.choice(["✦", "✧", "✩", "✪", "✫", "✬", "✭", "✮", "✯"])
            sys.stdout.write(CYAN + star.center(80) + RESET + "\r")
            sys.stdout.flush()
    
    print("\n" * 3)

if __name__ == "__main__":
    print_colorful_quote()