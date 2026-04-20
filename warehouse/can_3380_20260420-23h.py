"""
Campbell's Soup Can #3380
Produced: 2026-04-20 23:03:37
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
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

# ANSI Escape Codes for the Neurotic Aesthetic
CLR_CYAN = "\033[96m"
CLR_MAGENTA = "\033[95m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_WHITE = "\033[97m"
CLR_RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    print("\033[H\033[J", end="")

def typewriter(text, delay=0.06, color=CLR_WHITE):
    """Simulates a nervous, stuttering typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{CLR_RESET}")
        sys.stdout.flush()
        # Occasionally 'stutter' for comedic neurotic effect
        if random.random() > 0.95:
            time.sleep(delay * 5)
        else:
            time.sleep(delay)

def draw_frame(content, width=60):
    """Draws a neurotic-looking box around the quote."""
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    
    print(f"{CLR_MAGENTA}{top}{CLR_RESET}")
    
    # Center the content
    lines = content.split('\n')
    for line in lines:
        padding = (width - 2 - len(line)) // 2
        if padding < 0: # Handle long lines
            print(f"║ {line[:width-4]} ║")
        else:
            print(f"║{' ' * padding}{line}{' ' * (width - 2 - padding - len(line))}║")
            
    print(f"{CLR_MAGENTA}{bottom}{CLR_RESET}")

def glitch_effect(text):
    """Briefly flashes colors to simulate existential dread."""
    colors = [CLR_RED, CLR_YELLOW, CLR_CYAN, CLR_MAGENTA]
    for _ in range(3):
        sys.stdout.write(f"\r{random.choice(colors)}{text}{CLR_RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f"\r{' ' * len(text)}\r")
        time.sleep(0.05)

def main():
    quote = (
        "\"I asked my therapist if there is any meaning to life, \n"
        "and she said, 'Don't worry about meaning, worry about \n"
        "your cholesterol.' It's a terrifying time to be \n"
        "conscious.\""
    )

    clear_screen()

    # Intro animation: The "Panic" phase
    print(f"{CLR_RED}{BOLD}Initializing Existential Crisis...{CLR_RESET}\n")
    time.sleep(1)
    
    for i in range(3):
        sys.stdout.write(f"\r{CLR_YELLOW}Checking for cosmic significance... {'.' * (i+1)}{CLR_RESET}")
        sys.stdout.flush()
        time.sleep(0.7)
    print("\n")

    # The "Realization" phase
    glitch_effect("ERROR: PURPOSE NOT FOUND")
    time.sleep(1)
    
    clear_screen()

    # ASCII Art Header
    ascii_header = r"""
     _______  _______  _______  _______ 
    |       ||       ||       ||       |
    |    ___||    ___||    ___||    ___|
    |   |___ |   |___ |   |___ |   |___ 
    |    ___||    ___||    ___||    ___|
    |   |    |   |    |   |    |   |    
    |___|    |___|    |___|    |___|    
    ( Neurotic Thought Engine v0.1 )
    """
    print(f"{CLR_CYAN}{ascii_header}{CLR_RESET}")
    print(f"{CLR_WHITE}{'='*45}{CLR_RESET}\n")

    # The Main Event
    draw_frame(quote, width=55)

    print(f"\n{CLR_MAGENTA}{BOLD}--- End of Transmission (Before the inevitable heat death of the universe) ---{CLR_RESET}")
    print(f"{CLR_YELLOW}Press Ctrl+C to escape reality.{CLR_RESET}")

    try:
        while True:
            # Keep the screen "shimmering" with anxiety
            time.sleep(2)
            sys.stdout.write(f"\r{CLR_RED}Wait, did I leave the stove on?{CLR_RESET}      ")
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write(f"\r{' ' * 40}\r")
            sys.stdout.flush()
    except KeyboardInterrupt:
        print(f"\n\n{CLR_CYAN}Exiting... back to the mundane reality.{CLR_RESET}")

if __name__ == "__main__":
    main()