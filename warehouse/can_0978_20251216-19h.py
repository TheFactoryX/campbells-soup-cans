"""
Campbell's Soup Can #978
Produced: 2025-12-16 19:30:32
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
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

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, color_code, speed=0.03):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def draw_woody_crisis():
    """Draw a simple ASCII art face representing a neurotic crisis."""
    art = r"""
           ,---.
          /     \
         |  (. .)  |   <-- (Existential Panic)
          \   ^   /
           |     |
           | '/' |    "My brain is trying to escape my skull."
           '-----'
    """
    print(f"\033[36m{art}\033[0m")

def main():
    clear_screen()
    
    # Setup variables
    quote = '"Life is full of misery, loneliness, and suffering... and it\'s all over much too soon."'
    attribution = "— Woody (Neurotic Mode)"
    
    # Phase 1: The Setup (Cyan text, slight hesitation)
    print("\n" * 2)
    typewriter("Initiating Neurosis Protocol...", "33", 0.05)
    time.sleep(0.5)
    print("\033[31m[ SYSTEM ALERT: MOOD SET TO 'ANXIOUS' ]\033[0m")
    time.sleep(1)
    
    clear_screen()
    
    # Phase 2: The ASCII Art appears
    print("\n")
    draw_woody_crisis()
    time.sleep(0.8)
    
    # Phase 3: The Quote (Typewriter effect, Red for drama)
    print("\033[3m") # Italic
    typewriter(quote, "31", 0.05) # Red text
    print("\033[0m") # Reset
    
    time.sleep(0.5)
    
    # Phase 4: The Punchline (Yellow text, distinct from the main quote)
    print("\n")
    typewriter(attribution, "33", 0.04)
    
    # Phase 5: Dramatic Exit
    time.sleep(1.5)
    sys.stdout.write("\r\033[K") # Clear line
    sys.stdout.write("\033[2A\r\033[K") # Go up and clear
    sys.stdout.write("\033[2A\r\033[K") # Go up and clear
    sys.stdout.flush()
    
    typewriter("Wait, did I leave the stove on? Or was that just my anxiety?", "35", 0.05)
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31mExiting crisis...\033[0m")