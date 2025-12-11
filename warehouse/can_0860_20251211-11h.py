"""
Campbell's Soup Can #860
Produced: 2025-12-11 11:31:58
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_allen_quote():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
    clear_screen()
    
    # ASCII art border
    border = MAGENTA + "╔═══════════════════════════════════════════════════════════════════════════╗" + RESET
    bottom_border = MAGENTA + "╚═══════════════════════════════════════════════════════════════════════════╝" + RESET
    
    # Title
    print(CYAN + "╔═══════════════════════════════════════════════════════════════════════════╗" + RESET)
    print(CYAN + "║                                                                             ║" + RESET)
    print(CYAN + "║" + WHITE + BOLD + "   WOODY ALLEN'S PHILOSOPHICAL INSIGHTS                                      " + RESET + CYAN + "║" + RESET)
    print(CYAN + "║                                                                             ║" + RESET)
    print(CYAN + "╚═══════════════════════════════════════════════════════════════════════════╝" + RESET)
    
    print("\n")
    
    # Animated quote
    quote = YELLOW + BOLD + "The universe is not only queerer than we imagine," + RESET
    quote += "\n"
    quote += YELLOW + BOLD + "it's queerer than we can imagine..." + RESET
    quote += "\n"
    quote += WHITE + BOLD + "and I'm not even sure I want to imagine it at all," + RESET
    quote += "\n"
    quote += WHITE + BOLD + "frankly." + RESET
    
    # Typing effect
    print(BLUE + "┌─────────────────────────────────────────────────────────────────────────┐" + RESET)
    print(BLUE + "│                                                                         │" + RESET)
    type_text("│" + WHITE + "  " + quote + "  " + RESET + BLUE + "│" + RESET, 0.02)
    print(BLUE + "│                                                                         │" + RESET)
    print(BLUE + "└─────────────────────────────────────────────────────────────────────────┘" + RESET)
    
    # Woody Allen ASCII art
    woody = """
    {}
       .--.
      |o_o |
      |:_/ |
     //   \ \
    (|     | )
   /'\_   _/`\\
   \___)=(___/
    {}
    """.format(YELLOW + BOLD, RESET)
    
    print(woody)
    
    # Philosophical category
    print(CYAN + BOLD + "Category: Existential Angst & Cosmic Uncertainty" + RESET)
    
    # Footer animation
    for i in range(3):
        print(GREEN + ">> Woody Allen says: Life is 10% what happens to you and 90% how you panic about it. <<" + RESET)
        time.sleep(1)
        print(RESET + " " * 50 + RESET)
        time.sleep(0.5)

if __name__ == "__main__":
    woody_allen_quote()