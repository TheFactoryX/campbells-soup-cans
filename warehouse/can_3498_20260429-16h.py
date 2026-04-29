"""
Campbell's Soup Can #3498
Produced: 2026-04-29 16:53:49
Worker: Z.ai: GLM 4.5 (z-ai/glm-4.5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# Woody Allen style quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens. \
But let's be honest, I'm mostly just afraid of running out of things to worry about."

# ASCII art frame
FRAME_TOP = "╔" + "═" * 70 + "╗"
FRAME_BOTTOM = "╚" + "═" * 70 + "╝"
FRAME_SIDES = "║"

# Animated brain
BRAIN_ART = [
    "    .-""-.   ",
    "  .'      '.  ",
    " /  O    O  \\ ",
    "|     ∆     |",
    "|   \___/   |",
    '.          .',
    "  '-....-'  "
]

def typewriter_effect(text, color=WHITE, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_brain():
    """Print animated ASCII brain"""
    for line in BRAIN_ART:
        print(f"{CYAN}{line}{END}")
        time.sleep(0.1)

def main():
    # Clear screen (ANSI escape sequence)
    print("\033c", end="")
    
    # Print title
    print(f"\n{BOLD}{PURPLE}{' ' * 20}WOODY ALLEN'S EXISTENTIAL CRISIS{' ' * 20}{END}\n")
    
    # Print brain animation
    print_brain()
    
    # Print frame
    print(f"{RED}{FRAME_TOP}{END}")
    
    # Print quote with typewriter effect
    print(f"{RED}{FRAME_SIDES}{END}", end=" ")
    typewriter_effect(QUOTE, color=YELLOW)
    print(f"{RED}{FRAME_SIDES}{END}")
    
    # Print bottom frame
    print(f"{RED}{FRAME_BOTTOM}{END}\n")
    
    # Print signature
    print(f"{ITALIC}{BLUE}    - Neurotically yours, Woody Allen{END}\n")
    
    # Print final thought
    typewriter_effect("P.S. I'm also worried that this quote might be too long...", color=GREEN, delay=0.04)

if __name__ == "__main__":
    main()