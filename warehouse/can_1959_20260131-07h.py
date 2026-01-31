"""
Campbell's Soup Can #1959
Produced: 2026-01-31 07:42:38
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, color=Colors.WHITE):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.END + '\n')
    sys.stdout.flush()

def draw_border(width=70):
    border = Colors.CYAN + "╔" + "═" * (width - 2) + "╗" + Colors.END
    print(border)
    print(Colors.CYAN + "║" + " " * (width - 2) + "║" + Colors.END)

def draw_footer(width=70):
    border = Colors.CYAN + "╚" + "═" * (width - 2) + "╝" + Colors.END
    print(border)

def main():
    clear_screen()
    
    # Header
    print("\n" * 2)
    typewriter(" " * 20 + Colors.BOLD + Colors.YELLOW + "WOODY ALLEN ON LIFE" + Colors.END, delay=0.01)
    print("\n")
    
    # Border
    draw_border()
    
    # Quote with emphasis
    typewriter(" " * 5 + Colors.WHITE + "I've always thought that life is a", delay=0.03)
    typewriter(" " * 5 + Colors.RED + Colors.BOLD + "terminal illness", Colors.END + Colors.WHITE + " with a very", delay=0.03)
    typewriter(" " * 5 + Colors.GREEN + Colors.BOLD + "pleasant remission period", Colors.END + Colors.WHITE + ".", delay=0.03)
    typewriter(" " * 5 + Colors.WHITE + "The problem is, the treatment involves", delay=0.03)
    typewriter(" " * 5 + Colors.YELLOW + Colors.BOLD + "eating too much", Colors.END + Colors.WHITE + ", ", delay=0.03)
    typewriter(Colors.MAGENTA + Colors.BOLD + "drinking too much", Colors.END + Colors.WHITE + ", and", delay=0.03)
    typewriter(" " * 5 + Colors.CYAN + Colors.BOLD + "worrying", Colors.END + Colors.WHITE + " about whether", delay=0.03)
    typewriter(" " * 5 + Colors.WHITE + "the neighbor's cat likes you", delay=0.03)
    typewriter(" " * 5 + Colors.WHITE + "more than your own cat.", delay=0.03)
    
    # Footer
    draw_footer()
    
    # Signature
    print("\n")
    typewriter(" " * 30 + Colors.WHITE + "─" * 10, delay=0.02)
    typewriter(" " * 25 + Colors.YELLOW + Colors.BOLD + "─ WOODY ALLEN ─" + Colors.END, delay=0.03)
    typewriter(" " * 30 + Colors.WHITE + "─" * 10, delay=0.02)
    
    print("\n")
    typewriter(" " * 20 + Colors.BLUE + "Press Enter to exit...", color=Colors.BLUE, delay=0.01)
    input()

if __name__ == "__main__":
    main()