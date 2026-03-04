"""
Campbell's Soup Can #2564
Produced: 2026-03-04 13:31:45
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def print_typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    sys.stdout.write('\n')

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def main():
    # ANSI color codes
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Clear screen for clean presentation
    clear_screen()
    
    # Draw Woody's iconic glasses (with a slight wobble)
    glasses = [
        f"{YELLOW}    o    o    {RESET}",
        f"{YELLOW}   ( O  O )   {RESET}",
        f"{YELLOW}    \\____/    {RESET}",
        f"{YELLOW}     \\  /     {RESET}",
        f"{YELLOW}      \\/      {RESET}"
    ]
    
    # Print the glasses with a wobble effect
    for i in range(3):
        for line in glasses:
            shift = ' ' * (2 if i % 2 == 0 else 3)
            print(shift + line)
            time.sleep(0.1)
        clear_screen()
    
    # Reprint glasses without animation
    for line in glasses:
        print(line)
    
    # The Woody Allen-style quote (original creation)
    quote = (
        "I don't believe in an afterlife, but I'm bringing a change of underwear\n"
        "just in case it turns out to be a long, awkward elevator ride to nowhere."
    )
    
    # Create a colorful quote box
    width = max(len(line) for line in quote.split('\n')) + 4
    top_border = f"{BLUE}╔{MAGENTA}{'═' * width}{BLUE}╗"
    bottom_border = f"{BLUE}╚{MAGENTA}{'═' * width}{BLUE}╝"
    
    # Print the quote with typewriter effect inside a colorful box
    print(top_border)
    for line in quote.split('\n'):
        padded_line = f"{MAGENTA}║ {GREEN}{BOLD}{line.ljust(width - 2)}{MAGENTA}║"
        print_typewriter(padded_line)
    print(bottom_border)
    
    # Add a final neurotic touch
    time.sleep(0.5)
    print(f"\n{RED}{BOLD}  (Note: This quote may cause spontaneous existential dread. "
          f"Side effects include: excessive coffee drinking, sudden interest in Kierkegaard, "
          f"and the urge to return your own mail.){RESET}")
    
    # Make the last word disappear like a thought
    final_line = "  ...and don't get me started on the meaning of life."
    for i in range(len(final_line), 0, -1):
        clear_screen()
        for glass_line in glasses:
            print(glass_line)
        print(top_border)
        for line in quote.split('\n'):
            print(f"{MAGENTA}║ {GREEN}{BOLD}{line.ljust(width - 2)}{MAGENTA}║")
        print(bottom_border)
        print(f"\n{RED}{BOLD}  ...and don't get me started on the meaning of life.{RESET}")
        print(f"{MAGENTA}{' ' * 2}{final_line[:i]}{RESET}", end='\r')
        time.sleep(0.08)

if __name__ == "__main__":
    main()