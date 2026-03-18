"""
Campbell's Soup Can #2827
Produced: 2026-03-18 10:12:20
Worker: Healer Alpha (openrouter/healer-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_woody_quote():
    # Woody Allen style quote
    quote = """I'm not afraid of death; I just don't want to be there when it happens.
But then again, I don't want to miss anything either,
so I'll probably show up early and then worry about leaving too soon."""
    
    # ANSI color codes
    BOLD = "\033[1m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BLINK = "\033[5m"
    ITALIC = "\033[3m"
    
    # Create a neurotic box with anxious decorations
    box_width = 60
    top_border = "╔" + "═" * (box_width - 2) + "╗"
    bottom_border = "╚" + "═" * (box_width - 2) + "╝"
    
    # Print the quote with dramatic effect
    print()
    print(f"{RED}{BOLD}{top_border}{RESET}")
    
    # Add a dramatic pause
    for _ in range(3):
        print(f"{YELLOW}║{RESET}{' ' * (box_width - 2)}{YELLOW}║{RESET}")
        time.sleep(0.15)
    
    # Print the quote with typewriter effect
    lines = quote.split('\n')
    for line in lines:
        # Center the line in the box
        centered_line = line.center(box_width - 4)
        
        print(f"{YELLOW}║{RESET}  {MAGENTA}{ITALIC}", end="")
        
        # Typewriter effect
        for char in centered_line:
            print(char, end="", flush=True)
            time.sleep(0.03)
        
        print(f"{RESET}  {YELLOW}║{RESET}")
        time.sleep(0.3)
    
    # Add anxious dots
    for _ in range(2):
        print(f"{YELLOW}║{RESET}{' ' * (box_width - 2)}{YELLOW}║{RESET}")
        time.sleep(0.2)
    
    print(f"{RED}{BOLD}{bottom_border}{RESET}")
    
    # Add a neurotic signature with blinking cursor
    signature = "~ Wandering Mind, 3 AM"
    print(f"\n{CYAN}{signature.center(box_width)}{RESET}", end="")
    
    # Blinking cursor effect
    for _ in range(3):
        sys.stdout.write(f"{BLINK}▌{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n")
    
    # Add a humorous philosophical footnote
    footnote = "(And no, I didn't choose to be this anxious. It just happened.)"
    print(f"{BLUE}{ITALIC}{footnote.center(box_width)}{RESET}")
    print()

if __name__ == "__main__":
    print_woody_quote()