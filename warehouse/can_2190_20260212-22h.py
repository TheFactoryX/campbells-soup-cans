"""
Campbell's Soup Can #2190
Produced: 2026-02-12 22:49:27
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
    ITALIC = '\033[3m'
    ENDC = '\033[0m'
    BG_CYAN = '\033[106m'
    BG_BLUE = '\033[104m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, color=Colors.WHITE):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.ENDC + '\n')
    sys.stdout.flush()

def print_border(char='-', width=70):
    print(Colors.CYAN + char * width + Colors.ENDC)

def print_quote():
    clear_screen()
    
    # City skyline ASCII art
    skyline = """
     {}
    /|\\
   / | \\
  /  |  \\
 /___|___\\
|   {}   |  {}
|   {}   |  {}
|   {}   |  {}
|   {}   |  {}
|___{}___|  {}
""".format(
        Colors.YELLOW + "  WOODY ALLEN'S PHILOSOPHER'S CORNER  " + Colors.ENDC,
        Colors.MAGENTA + "☕" + Colors.ENDC,
        Colors.BLUE + "I tried to find meaning in life," + Colors.ENDC,
        Colors.BLUE + "but it was all sold out." + Colors.ENDC,
        Colors.BLUE + "So I bought a hot dog" + Colors.ENDC,
        Colors.BLUE + "and pretended it was the answer." + Colors.ENDC,
        Colors.BLUE + "Turns out, mustard doesn't" + Colors.ENDC,
        Colors.BLUE + "solve existential dread." + Colors.ENDC,
        Colors.MAGENTA + "☕" + Colors.ENDC
    )
    
    print(skyline)
    
    print_border('=', 70)
    
    # Quote with typewriter effect
    typewriter(Colors.BOLD + "WOODY ALLEN SAYS:", 0.05, Colors.YELLOW)
    time.sleep(0.5)
    
    quote = Colors.ITALIC + "\"I tried to find meaning in life, but it was all sold out. " + \
            "So I bought a hot dog and pretended it was the answer. " + \
            "Turns out, mustard doesn't solve existential dread.\"" + Colors.ENDC
    
    typewriter(quote, 0.02, Colors.CYAN)
    
    print_border('=', 70)
    
    # Footer with decorative elements
    footer = Colors.UNDERLINE + Colors.MAGENTA + "A MOMENT OF DEEP REFLECTION BROUGHT TO YOU BY" + Colors.ENDC + \
             Colors.GREEN + " NEUROSIS & CO. " + Colors.ENDC + \
             Colors.MAGENTA + Colors.UNDERLINE + "EST. 1973" + Colors.ENDC
    
    typewriter(footer, 0.03, Colors.WHITE)
    
    print_border('-', 70)
    
    # Small animation at the end
    for i in range(3):
        sys.stdout.write(Colors.YELLOW + "☕" + Colors.ENDC)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(0.3)

if __name__ == "__main__":
    print_quote()
    
    # Ask if user wants to hear another quote (but we'll just show the same one)
    input(Colors.BLUE + "\nPress Enter to exit this moment of existential dread..." + Colors.ENDC)