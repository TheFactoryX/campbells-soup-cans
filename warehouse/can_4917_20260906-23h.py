"""
Campbell's Soup Can #4917
Produced: 2026-09-06 23:54:55
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time
import random

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03, color=""):
    """Print text with a typewriter effect"""
    for char in text:
        print(f"{color}{char}", end="", flush=True)
        time.sleep(delay)
    print("\033[0m")  # Reset color

def create_ascii_head():
    """Create a simple ASCII art head with glasses"""
    return """
    \033[1;33m    ┌─────┐
    │  ●  ●  │
    │   ───  │
    │   \\_/  │
    └─────┘\033[0m
    """

def create_animated_border(width=60):
    """Create an animated border with changing colors"""
    colors = ["\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m"]
    border = ""
    for i in range(width):
        color = colors[i % len(colors)]
        border += f"{color}━"
    return border + "\033[0m"

def woody_allen_quote():
    """Display a Woody Allen style quote with visual flair"""
    clear_screen()
    
    # Print ASCII head
    print(create_ascii_head())
    print()
    
    # Print animated top border
    print(create_animated_border())
    print()
    
    # The quote - original Woody Allen style
    quote = [
        "I don't mind being dead.",
        "It's just the being alive part",
        "that I find so exhausting."
    ]
    
    # Print quote with typewriter effect and colors
    print("\033[1;36m    ", end="")  # Cyan color for indentation
    for line in quote:
        print_slow(line + "\n    ", 0.05, "\033[1;36m")
    
    # Print animated bottom border
    print(create_animated_border())
    print()
    
    # Print attribution with a touch of existential dread
    attribution = [
        "\033[1;31m— Someone who probably shouldn't have",
        "but did anyway, and now regrets everything\033[0m"
    ]
    
    for line in attribution:
        print_slow(line + "\n", 0.04, "")
    
    # Add some existential footnotes
    print("\n" + "\033[3;37m" + 
          "P.S. I originally wrote this quote in my diary, but then I lost the diary. "
          "Now I'm not sure if I actually thought this or if I just wanted to sound profound. "
          "Either way, it's probably better this way.\033[0m")
    
    # Final existential touch - blinking cursor
    print("\033[5;31m█\033[0m", end="", flush=True)
    time.sleep(2)
    
    # Fade out effect
    for i in range(10):
        clear_screen()
        if i % 2 == 0:
            print(create_ascii_head())
            print()
            print(create_animated_border())
            print()
            print("\033[1;36m    I don't mind being dead.")
            print("    It's just the being alive part")
            print("    that I find so exhausting.\033[0m")
            print(create_animated_border())
        time.sleep(0.3)

if __name__ == "__main__":
    try:
        woody_allen_quote()
    except KeyboardInterrupt:
        print("\n\033[1;31mEven my existential dread got bored and left.\033[0m")