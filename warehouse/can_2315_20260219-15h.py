"""
Campbell's Soup Can #2315
Produced: 2026-02-19 15:07:18
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.05, color_code=''):
    for char in text:
        sys.stdout.write(color_code + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay)

def woody_allen_quote():
    # ANSI color codes
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'
    
    # ASCII art border
    top_border = f"{RED}╔{'═' * 60}╗{END}"
    bottom_border = f"{RED}╚{'═' * 60}╝{END}"
    side_border = f"{RED}║{END}"
    
    clear_screen()
    
    # Print top border
    print(top_border)
    
    # Print title with animation
    title = "WOODY ALLEN ON LIFE"
    for i in range(len(title)):
        partial_title = title[:i+1]
        sys.stdout.write(f"\r{BLUE}{partial_title:^60}{END}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    
    # Print quote with typewriter effect
    quote = "I spent my entire life worrying about the meaning of existence, only to realize I should have been worrying about where I left my keys."
    colors = [RED, YELLOW, GREEN, CYAN, PURPLE, WHITE]
    
    # Print opening of quote box
    print(f"{side_border}{' ' * 60}{side_border}")
    
    # Print quote with typewriter effect
    type_text(f"{side_border} {YELLOW}", delay=0.02)
    
    for i, char in enumerate(quote):
        color = random.choice(colors) if i % 10 == 0 else YELLOW
        type_text(char, delay=0.03, color_code=color)
    
    print(f"{YELLOW} {side_border}")
    
    # Print philosophical "footnote"
    print(f"{side_border}{' ' * 60}{side_border}")
    time.sleep(1)
    
    footnotes = [
        f"{PURPLE}A Woody Allen Production{END}",
        f"{CYAN}Where neurosis meets enlightenment{END}",
        f"{GREEN}Existential dread with a side of bagels{END}"
    ]
    
    for footnote in footnotes:
        type_text(f"{side_border} {ITALIC}", delay=0.02)
        type_text(footnote, delay=0.03)
        print(f" {side_border}")
    
    # Print bottom border
    print(bottom_border)
    
    # Add animation at the end
    time.sleep(2)
    thoughts = ["Thinking...", "Overthinking...", "Anxiety rising...", "Bagel craving..."]
    for thought in thoughts:
        for color in [RED, YELLOW, GREEN, CYAN, PURPLE]:
            sys.stdout.write(f"\r{color}{thought:^60}{END}")
            sys.stdout.flush()
            time.sleep(0.5)
        time.sleep(0.2)

if __name__ == "__main__":
    woody_allen_quote()