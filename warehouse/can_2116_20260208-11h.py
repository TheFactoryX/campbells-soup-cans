"""
Campbell's Soup Can #2116
Produced: 2026-02-08 11:36:17
Worker: Z.AI: GLM 4.7 (z-ai/glm-4.7)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import os

# --- ANSI Color Codes ---
C_RESET = '\033[0m'
C_BLACK = '\033[30m'
C_RED = '\033[31m'
C_GREEN = '\033[32m'
C_YELLOW = '\033[33m'
C_BLUE = '\033[34m'
C_MAGENTA = '\033[35m'
C_CYAN = '\033[36m'
C_WHITE = '\033[37m'
C_BOLD = '\033[1m'
C_DIM = '\033[2m'
C_UNDERLINE = '\033[4m'
C_BLINK = '\033[5m'
C_REVERSE = '\033[7m'

# --- Helper Functions ---

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def neurotic_print(text, base_color=C_WHITE):
    """
    Prints text with a typewriter effect, simulating neurotic hesitation,
    stuttering, and anxious color flickers.
    """
    for char in text:
        # Simulate human-like inconsistency
        rng = random.random()
        
        # 1. The Stutter: Type, then panic and backspace, then type again
        if rng < 0.08:
            sys.stdout.write(base_color + C_BOLD + char + C_RESET)
            sys.stdout.flush()
            time.sleep(0.04) # Brief pause
            sys.stdout.write('\b \b') # Erase it
            time.sleep(0.08) # Long anxious pause
            sys.stdout.flush()
        
        # 2. The Hesitation: Just stop and contemplate the void
        elif rng < 0.20:
            time.sleep(random.uniform(0.1, 0.25))
        
        # 3. The Panic Moment: Briefly turn red
        if rng > 0.92:
            sys.stdout.write(C_RED + C_BOLD + char + C_RESET)
        else:
            sys.stdout.write(base_color + C_BOLD + char + C_RESET)
            
        sys.stdout.flush()
        
        # Base typing speed (jittery)
        time.sleep(random.uniform(0.01, 0.05))

def draw_glasses():
    """Draws a simple ASCII art pair of thick-rimmed glasses."""
    art = r"""
        .-~-~-~-.
       /         \
      |  o     o   |
       \  \___/  /
        `-. .-.`
           \_/
    """
    print(C_MAGENTA + C_BOLD + art + C_RESET)

# --- Main Execution ---

def main():
    clear_screen()
    
    # Header
    print("\n" * 2)
    print(C_YELLOW + BANNER)
    
    # Visual Element: The Glasses
    print("\n")
    draw_glasses()
    print("\n")
    
    # Context
    print(C_DIM + C_BLUE + "    (adjusts tie, looks down at shoes)" + C_RESET)
    time.sleep(1.2)
    print("\n")
    
    # The Quote Box
    box_width = 70
    padding = 4
    
    # Top border
    print(C_YELLOW + "    " + "+" + "-" * (box_width - 2) + "+" + C_RESET)
    
    # Empty top line
    print(C_YELLOW + "    |" + C_RESET + " " * (box_width - 2) + C_YELLOW + "|" + C_RESET)
    
    # The Quote Line
    sys.stdout.write(C_YELLOW + "    |" + C_RESET)
    sys.stdout.write(" " * padding)
    
    # THE QUOTE (Neurotic, Existential, Funny)
    # A custom quote inspired by the style of Woody Allen
    quote_text = "I believe there is a force in the universe, but it's clearly disorganized, neurotic, and has a terrible sense of timing—basically, it’s me with a cape."
    
    # Print the quote with the neurotic effect
    neurotic_print(quote_text, base_color=C_CYAN)
    
    # Calculate spacing to close the box right
    # Note: len(quote_text) works because we printed the whole string before calculating spaces
    remaining_space = box_width - 2 - padding - len(quote_text)
    if remaining_space > 0:
        sys.stdout.write(" " * remaining_space)
    elif remaining_space < 0:
        # Fallback if quote is too long for the hardcoded box (unlikely here)
        pass
        
    sys.stdout.write(C_YELLOW + "|" + C_RESET)
    print() # End the line
    
    # Empty bottom line
    print(C_YELLOW + "    |" + C_RESET + " " * (box_width - 2) + C_YELLOW + "|" + C_RESET)
    
    # Bottom border
    print(C_YELLOW + "    " + "+" + "-" * (box_width - 2) + "+" + C_RESET)
    
    # Attribution
    print("\n")
    print(C_GREEN + "                          - Anxious Observer #42" + C_RESET)
    
    # Footer / Punchline
    print("\n" * 2)
    print(C_RED + C_BLINK + "    [ sighs audibly ]" + C_RESET)
    print("\n" * 3)

# Define banner string here to avoid cluttering logic
BANNER = r"""
    /////////////////////////////////////////////////////////////
    ///  EXISTENTIAL DREAD GENERATOR v1.0 (Neurotic Edition)  ///
    /////////////////////////////////////////////////////////////
"""

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Allow user to exit cleanly with Ctrl+C
        print("\n" + C_YELLOW + "Well, that's typical. You leave just when things get existential." + C_RESET)