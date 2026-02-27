"""
Campbell's Soup Can #2473
Produced: 2026-02-27 23:38:29
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'

def clear_line():
    """Clear the current line."""
    sys.stdout.write('\r' + ' ' * 100 + '\r')
    sys.stdout.flush()

def typing_effect(text, color=Colors.YELLOW, delay=0.03):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    print()

def animate_box(quote, width=60):
    """Animate a box appearing around the quote."""
    border_chars = ['▀', '▄', '▌', '▐', '█', '▓', '▒', '░']
    
    # Top border animation
    for i in range(width):
        char = random.choice(border_chars)
        sys.stdout.write(Colors.BG_BLACK + Colors.CYAN + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    
    # Quote line
    padding = (width - len(quote) - 2) // 2
    print(Colors.BG_BLACK + Colors.CYAN + ' ' * padding + Colors.RESET, end='')
    typing_effect(quote, Colors.WHITE + Colors.BOLD, 0.02)
    print(Colors.BG_BLACK + Colors.CYAN + ' ' * padding + Colors.RESET)
    
    # Bottom border animation
    for i in range(width):
        char = random.choice(border_chars)
        sys.stdout.write(Colors.BG_BLACK + Colors.CYAN + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.01)
    print(Colors.RESET)

def main():
    # Clear screen and move cursor up
    sys.stdout.write('\033[2J\033[1;1H')
    
    # Woody Allen style quote (original)
    quote = "I'm not afraid of death; I just don't want to be there when it happens. " \
            "The difference between sex and death is, with death you can do it alone and nobody complains."
    
    # Opening animation - "neurotic" jittery text
    intro = "CONNECTING TO WOODY'S NEUROCES... "
    for char in intro:
        sys.stdout.write(Colors.RED + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.05 + random.uniform(-0.02, 0.05))
    
    # Simulate "connection" with random characters
    for _ in range(20):
        sys.stdout.write(Colors.GREEN + random.choice('01') + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")
    
    # Animate the quote in a fancy box
    animate_box(quote, width=70)
    
    # Add a playful "signature" at the bottom
    time.sleep(0.5)
    signature = "— Woody Allen (probably regretting this already)"
    
    # Staggered appearance of signature
    for i, char in enumerate(signature):
        sys.stdout.write('\033[' + str(24 + i%3) + ';' + str(10 + i) + 'H')  # Move cursor
        sys.stdout.write(Colors.MAGENTA + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Reset cursor and final message
    print("\n" * 2)
    time.sleep(0.5)
    typing_effect("(Puts existential crisis on hold to check if he left the oven on...)", 
                  Colors.BLUE, 0.04)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.RESET + "\n\nEven my interruption is neurotic. Fine, go ahead.\n")
        sys.exit(0)