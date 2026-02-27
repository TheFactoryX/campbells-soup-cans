"""
Campbell's Soup Can #2468
Produced: 2026-02-27 19:03:13
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def woody_allen_quote():
    # ANSI color codes
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'
    
    # Woody Allen style existential quote
    quote = """I'm not afraid of death; I just don't want to be there when it happens."""
    
    # ASCII art borders
    top_border = f"{BLUE}╔{'═' * 78}╗{END}"
    side_border = f"{BLUE}║{END}"
    bottom_border = f"{BLUE}╚{'═' * 78}╝{END}"
    
    # Woody Allen neurotic thoughts
    neurotic_thoughts = [
        f"{RED}What if I've been pronouncing 'quinoa' wrong this whole time?{END}",
        f"{MAGENTA}Is it normal to talk to yourself? Asking for a friend...{END}",
        f"{YELLOW}Did I leave the oven on? I can't remember. What if I did?{END}",
        f"{CYAN}What if my entire life is just a simulation?{END}",
        f"{GREEN}What if Woody Allen is just a character I created?{END}"
    ]
    
    # Clear screen
    clear_screen()
    
    # Print animated borders
    print("\n" * 3)
    print(top_border)
    
    # Print animated quote
    print(side_border, end='')
    type_text(f" {YELLOW}{BOLD}\"{quote}\"{END} ", delay=0.05)
    print()
    
    # Print animated neurotic thoughts
    for thought in neurotic_thoughts:
        print(side_border, end='')
        type_text(f" {thought} ", delay=0.03)
        print()
    
    # Print animated signature
    print(side_border, end='')
    type_text(f" {CYAN}                - Woody Allen{END} ", delay=0.03)
    print()
    
    print(bottom_border)
    print("\n" * 3)
    
    # Blinking anxiety indicator
    anxiety_symbols = ["😰", "😟", "😬", "🙁", "😐", "🙂"]
    for symbol in anxiety_symbols:
        sys.stdout.write("\033[A")  # Move cursor up one line
        sys.stdout.write(f"{side_border} {symbol} {END}".center(80))
        sys.stdout.flush()
        time.sleep(0.3)
    
    # Final state
    sys.stdout.write("\033[A")  # Move cursor up one line
    sys.stdout.write(f"{side_border} {CYAN}🤔{END} ".center(80))
    sys.stdout.flush()
    
    # Wait before exit
    time.sleep(3)
    
if __name__ == "__main__":
    woody_allen_quote()