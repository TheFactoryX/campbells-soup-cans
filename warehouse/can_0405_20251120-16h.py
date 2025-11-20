"""
Campbell's Soup Can #405
Produced: 2025-11-20 16:43:48
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import os
import sys

# ANSI escape codes for colors and styles
PINK = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
BOLD = '\033[1m'
END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    # ASCII art thought bubble
    print(f"{YELLOW}")
    print(r"          .--------.         ")
    print(r"        .'          '.       ")
    print(r"       /   O      O   \      ")
    print(r"      :                :     ")
    print(r"      |                |     ")
    print(r"      :    .------.    :     ")
    print(r"       \  '        '  /      ")
    print(r"        '.          .'       ")
    print(r"          '--------'         ")
    print(f"{END}")
    
    # Woody Allen style quote
    quote = (
        "I firmly believe life is absurd, but what really keeps me up at night\n"
        "is the suspicion that somewhere, someone might be having more fun\n"
        "being absurd than I am."
    )
    
    # Calculate box width
    max_line_length = max(len(line) for line in quote.split('\n'))
    box_width = max_line_length + 4
    
    # Print top border
    print(f"{PINK}╔{'═' * (box_width - 2)}╗{END}")
    
    # Print quote with animation
    for line in quote.split('\n'):
        padded_line = line.center(max_line_length)
        sys.stdout.write(f"{PINK}║{END} {GREEN}{BOLD}")
        typewriter(padded_line, delay=0.04)
        sys.stdout.write(f"{PINK}║{END}")
        print()
    
    # Print bottom border
    print(f"{PINK}╚{'═' * (box_width - 2)}╝{END}")
    
    # Add attribution
    time.sleep(0.5)
    print(f"\n{CYAN}— Woody Allen (probably){END}\n")
    
    # Add blinking cursor effect
    for _ in range(3):
        print(f"{BOLD}...{END}", end='', flush=True)
        time.sleep(0.5)
        print("\b\b\b   \b\b\b", end='', flush=True)
        time.sleep(0.5)

if __name__ == "__main__":
    main()