"""
Campbell's Soup Can #5021
Produced: 2026-09-25 07:49:41
Worker: inclusionAI: Ling 3.0 Flash Fin (free) (inclusionai/ling-3.0-flash-fin:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os
import random

# ANSI color codes
class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, color=Color.WHITE, bold=False):
    """Print text with a typewriter effect."""
    prefix = Color.BOLD if bold else ''
    for char in text:
        if char == '\n':
            sys.stdout.write('\n')
        else:
            sys.stdout.write(prefix + color + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Color.RESET)

def print_border(char='━', length=60, color=Color.CYAN):
    print(color + char * length + Color.RESET)

def animated_banner():
    """Animate a fancy banner."""
    banner_lines = [
        "██████╗ ██╗     ███████╗███████╗██████╗ ",
        "██╔══██╗██║     ██╔════╝██╔════╝██╔══██╗",
        "██████╔╝██║     █████╗  ███████╗██████╔╝",
        "██╔══██╗██║     ██╔══╝  ╚════██║██╔═══╝ ",
        "██║  ██║███████╗██║     ███████║██║     ",
        "╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝     "
    ]
    colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.MAGENTA, Color.BLUE]
    
    for line in banner_lines:
        for i, color in enumerate(colors):
            pass
        # Just print in a cycling color
        for i, ch in enumerate(line):
            c = colors[i % len(colors)]
            sys.stdout.write(c + ch + Color.RESET)
        sys.stdout.flush()
        time.sleep(0.05)
        print()
    time.sleep(0.5)

def print_quote_box(quote, author):
    """Print the quote in a decorative box."""
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines) + 4
    
    top_border = "╔" + "═" * max_len + "╗"
    bottom_border = "╚" + "═" * max_len + "╝"
    
    print(Color.MAGENTA + top_border + Color.RESET)
    for line in lines:
        padding = max_len - len(line)
        print(Color.MAGENTA + "║" + Color.RESET + 
              Color.YELLOW + "  " + line + " " * (padding - 2) + 
              Color.MAGENTA + "║" + Color.RESET)
    print(Color.MAGENTA + bottom_border + Color.RESET)
    
    print()
    print(" " * (max_len // 2 - len(author) // 2) + 
          Color.CYAN + Color.BOLD + "— " + author + Color.RESET)

def main():
    clear_screen()
    print()
    print()
    
    # Animate the banner
    print(Color.RED + Color.BOLD + "         W O O D Y   A L L E N   Q U O T E   M A C H I N E" + Color.RESET)
    print()
    time.sleep(0.3)
    
    # Animated divider
    for i in range(3):
        print(Color.CYAN + "░" * random.randint(20, 60) + Color.RESET)
        time.sleep(0.2)
    print()
    
    # The quote (Woody Allen style!)
    quote = (
        "I'm not afraid of death;\n"
        "I just don't want to be there\n"
        "when it happens.\n"
        "\n"
        "And honestly, between you and me,\n"
        "the universe could not care less\n"
        "about my neuroses — and I am NOT\n"
        "fine with that."
    )
    
    # Print with typewriter effect
    print_border('═', 60, Color.YELLOW)
    print()
    
    # Print the philosophical framing
    typewriter("A philosophical thought, delivered with existential dread:", 0.04, Color.GREEN)
    print()
    time.sleep(0.3)
    
    # Print the quote box
    print_quote_box(quote, "Woody Allen (probably)")
    print()
    
    # Add some extra flair
    time.sleep(0.5)
    typewriter("\n" + Color.DIM + "...the universe said \"I don't think so.\"" + Color.RESET, 0.05, Color.DIM)
    time.sleep(0.3)
    typewriter(Color.BLUE + "\n                    * existential crisis achieved *" + Color.RESET, 0.05)
    time.sleep(0.3)
    print()
    print_border('═', 60, Color.YELLOW)
    print()
    print(Color.RED + Color.BOLD + "  Your time on Earth is limited. Stop overthinking it." + Color.RESET)
    print(Color.CYAN + "  (But you will overthink it anyway.)" + Color.RESET)
    print()
    print(Color.DIM + "  Press Ctrl+C to escape the existential void." + Color.RESET)
    print()

if __name__ == "__main__":
    main()