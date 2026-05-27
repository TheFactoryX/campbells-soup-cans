"""
Campbell's Soup Can #3801
Produced: 2026-05-27 23:38:01
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophy Quote Generator
A neurotically delightful existential experience!
"""

import time
import sys
import random

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'

def typewriter_effect(text, delay=0.02, color=""):
    """Prints text with a typing effect"""
    if color:
        sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.005, 0.005))
    print(Colors.RESET)

def print_gradient(text, colors_list):
    """Prints text with gradient colors"""
    for i, char in enumerate(text):
        color_index = int((i / len(text)) * (len(colors_list) - 1))
        sys.stdout.write(colors_list[color_index] + char)
        sys.stdout.flush()
    print(Colors.RESET)

def main():
    # Woody Allen style quotes
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The universe is everything that exists - including you and me and pretty much everyone we know.",
        "I was having a wonderful dream, but I woke up before I could realize how wonderful it would have been."
    ]
    
    quote = random.choice(quotes)
    
    # Header with blinking effect
    print()
    for _ in range(3):
        print(f"{Colors.RED}{Colors.BOLD}   ╭─•──•─╮")
        print(f"   │  🤔  │ {Colors.RESET}WOODY ALLEN PHILOSOPHY{Colors.RED}{Colors.BOLD}")
        print(f"   ╰─•──•─╯{Colors.RESET}")
        time.sleep(0.3)
        print("\033[A" * 3 + "\033[2K" * 3)
        time.sleep(0.2)
    
    print(f"{Colors.MAGENTA}{Colors.BOLD}   ╭───────────────────────────────────────────╮")
    print(f"   │{Colors.BOLD}  💭 NEUROTIC PHILOSOPHICAL WISDOM 💭{Colors.RESET}")
    print(f"   ╰───────────────────────────────────────────╯{Colors.RESET}")
    print()
    
    # Animated quote box
    box_width = len(quote) + 4
    print(f"{Colors.CYAN}   {'═' * box_width}{Colors.RESET}")
    
    # Top border with animation
    for i in range(2):
        print(f"{Colors.CYAN}   ║{' ' * box_width}║{Colors.RESET}")
        time.sleep(0.1)
    
    # Quote with typing effect
    print(f"{Colors.CYAN}   ║{Colors.RESET}  ", end="")
    typewriter_effect(quote, 0.03, Colors.YELLOW)
    print(f"{Colors.CYAN}   ║{Colors.RESET}")
    
    # Bottom border
    print(f"{Colors.CYAN}   {'═' * box_width}{Colors.RESET}")
    print()
    
    # Existential footer
    print(f"{Colors.DIM}   ─────────────────────────────────────────────{Colors.RESET}")
    print(f"{Colors.RED}   |  {Colors.ITALIC}And that's why I'm still here, worrying about it...{Colors.RESET}")
    print(f"{Colors.DIM}   ─────────────────────────────────────────────{Colors.RESET}")
    print()
    
    # Signature with gradient
    signature = "            — Some Guy Who's Very Anxious"
    colors_gradient = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    print_gradient(signature, colors_gradient)
    print()

if __name__ == "__main__":
    main()