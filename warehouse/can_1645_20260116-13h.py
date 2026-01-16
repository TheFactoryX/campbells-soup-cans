"""
Campbell's Soup Can #1645
Produced: 2026-01-16 13:06:53
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    # Colors using ANSI escape codes
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"
    RESET = "\033[0m"
    
    # Woody Allen quote
    quote = """I tried to be a philosopher once, but I kept getting distracted by my own neurosis. 
Turns out, the meaning of life is that there is no meaning, but that's okay because at least 
I get to worry about it."""
    
    # Author
    author = "~ Woody Allen"
    
    # Display animation
    print("\n\n")
    
    # Animated title
    title = "WOODY ALLEN ON LIFE"
    for i in range(len(title)):
        sys.stdout.write(f"\033[92m{title[:i+1]}\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
    
    print("\n\n")
    
    # Top border with animated characters
    top_border = "╔═════════════════════════════════════════════════════════════════════════════════════════╗"
    for char in top_border:
        sys.stdout.write(f"{YELLOW}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")
    
    # Quote with typewriter effect
    lines = quote.split('\n')
    for i, line in enumerate(lines):
        if i == 0:
            color = BLUE
        elif i == 1:
            color = MAGENTA
        else:
            color = CYAN
        
        typewriter_effect(f"  {color}║{RESET} {line}", 0.02)
    
    print()
    
    # Author with animation
    author_line = f"  {GREEN}║{RESET}                              {BOLD}{ITALIC}{RED}{author}{RESET}"
    for char in author_line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()
    
    print()
    
    # Bottom border with animated characters
    bottom_border = "╚═════════════════════════════════════════════════════════════════════════════════════════╝"
    for char in bottom_border:
        sys.stdout.write(f"{YELLOW}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n\n")
    
    # Final animated message
    final_message = "Press any key to exit..."
    for char in final_message:
        sys.stdout.write(f"{MAGENTA}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    
    # Wait for key press
    input()

if __name__ == "__main__":
    main()