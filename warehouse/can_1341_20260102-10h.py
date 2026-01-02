"""
Campbell's Soup Can #1341
Produced: 2026-01-02 10:38:03
Worker: Z.AI: GLM 4.5 Air (z-ai/glm-4.5-air)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os
from itertools import cycle

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_quote_animation():
    # ANSI escape codes for colors
    colors = [
        '\033[91m',  # Red
        '\033[92m',  # Green
        '\033[93m',  # Yellow
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[96m',  # Cyan
    ]
    reset = '\033[0m'
    
    # ASCII art frame
    frame_top = "╔═══════════════════════════════════════════════════════════════════════════════════════╗"
    frame_bottom = "╚═══════════════════════════════════════════════════════════════════════════════════════╝"
    frame_side = "║"
    
    # Quote
    quote = "Life is divided into the horrible and the miserable. The horrible would be things like your "
    quote += "hydroplane out of gas, or taking a nap in a highway. The miserable is everything else."
    
    # Author
    author = " - Woody Allen"
    
    # Clear screen and start animation
    clear_screen()
    
    # Color cycling
    color_cycle = cycle(colors)
    
    # Animate frame
    for _ in range(3):
        current_color = next(color_cycle)
        print(f"{current_color}{frame_top}{reset}")
        print(f"{current_color}{frame_side}{' ' * (len(frame_side) * 2 + len(frame_top) - 2)}{frame_side}{reset}")
        print(f"{current_color}{frame_side}{' ' * (len(frame_side) * 2 + len(frame_top) - 2)}{frame_side}{reset}")
        print(f"{current_color}{frame_side}{' ' * (len(frame_side) * 2 + len(frame_top) - 2)}{frame_side}{reset}")
        print(f"{current_color}{frame_bottom}{reset}")
        time.sleep(0.2)
        clear_screen()
    
    # Print final frame with quote
    final_color = next(color_cycle)
    print(f"{final_color}{frame_top}{reset}")
    print(f"{final_color}{frame_side}{' ' * 10}WOODY ALLEN'S PHILOSOPHICAL INSIGHTS{' ' * 10}{frame_side}{reset}")
    print(f"{final_color}{frame_side}{' ' * 89}{frame_side}{reset}")
    print(f"{final_color}{frame_side}{' ' * 89}{frame_side}{reset}")
    print(f"{final_color}{frame_side}{' ' * 89}{frame_side}{reset}")
    print(f"{final_color}{frame_bottom}{reset}")
    
    # Add some dramatic pause
    time.sleep(1)
    
    # Print quote with typewriter effect
    typewriter(f"\n{final_color}╠═══════════════════════════════════════════════════════════════════════════════════════╣{reset}")
    typewriter(f"{final_color}║{reset}", 0.01)
    
    # Color for quote text
    quote_color = next(color_cycle)
    
    # Print quote with color cycling
    words = quote.split()
    line = ""
    for word in words:
        test_line = line + word + " "
        if len(test_line) > 85:
            typewriter(f"{quote_color}║ {line.ljust(85)} {reset}")
            line = word + " "
        else:
            line = test_line
    
    if line:
        typewriter(f"{quote_color}║ {line.ljust(85)} {reset}")
    
    typewriter(f"{final_color}║{reset}")
    typewriter(f"{final_color}╚═══════════════════════════════════════════════════════════════════════════════════════╝{reset}")
    
    # Print author with pulsing effect
    for i in range(3):
        author_color = next(color_cycle)
        if i % 2 == 0:
            print(f"\n{author_color}{author.center(89)}{reset}")
        else:
            print(f"\n{reset}{author.center(89)}{reset}")
        time.sleep(0.5)
    
    # Final message
    print(f"\n{final_color}{'*' * 89}{reset}")
    print(f"{final_color}{'*' * 30} Existential crisis complete! {'*' * 30}{reset}")
    print(f"{final_color}{'*' * 89}{reset}")
    
    # Reset color
    print(reset)

if __name__ == "__main__":
    woody_quote_animation()