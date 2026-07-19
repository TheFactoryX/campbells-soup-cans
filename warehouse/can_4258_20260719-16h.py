"""
Campbell's Soup Can #4258
Produced: 2026-07-19 16:13:16
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

# ANSI Escape Codes for colors
class Colors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    print("\033[2J\033[H", end="")

def typewriter_effect(text, speed=0.05):
    """Prints text with a dramatic, neurotic typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def draw_frame(quote, color):
    """Draws a stylized, slightly shaky frame around the quote."""
    width = len(quote) + 4
    border = "┌" + "─" * (width - 2) + "┐"
    bottom = "└" + "─" * (width - 2) + "┘"
    
    print(color + border)
    print(f"│ {quote} │")
    print(bottom + Colors.END)

def neurosis_animation():
    """Simulates the visual manifestation of an existential crisis."""
    anxiety_levels = ["BREATHING...", "THINKING...", "OVERTHINKING...", "EXISTENTIAL DREAD...", "PANIC!"]
    glitch_chars = ["@", "#", "$", "%", "&", "*", "!", "?", "(", ")"]
    
    for _ in range(3):
        for level in anxiety_levels:
            clear_screen()
            print("\n" * 5)
            print(f"{Colors.RED}{Colors.BOLD}{level}{Colors.END}")
            # Add some 'jitter'
            jitter = "".join(random.choice(glitch_chars) for _ in range(10))
            print(f"{Colors.MAGENTA}{jitter}{Colors.END}")
            time.sleep(0.6)

def main():
    # The Woody Allen style quote
    QUOTE = "I'm not saying my life is a cosmic accident, but I've been looking for the punchline for thirty years and I'm starting to suspect the universe is just an extremely bad comedian."
    
    clear_screen()
    
    # Phase 1: The build-up
    print(f"\n\n{Colors.CYAN}Initializing Existential Crisis Protocol...{Colors.END}")
    time.sleep(1)
    
    # Phase 2: The Neurotic Animation
    neurosis_animation()
    
    # Phase 3: The Big Reveal
    clear_screen()
    print("\n" * 2)
    
    # Create a 'thought bubble' or frame effect
    # We'll split the quote for dramatic effect
    parts = [
        "I'm not saying my life is a cosmic accident,",
        "but I've been looking for the punchline",
        "for thirty years and I'm starting to suspect",
        "the universe is just an extremely bad comedian."
    ]
    
    print(f"{Colors.YELLOW}{Colors.BOLD}--- A MOMENT OF PROFOUND UNCERTAINTY ---{Colors.END}\n")
    time.sleep(1)
    
    for part in parts:
        print(f"{Colors.CYAN}{Colors.BOLD}")
        typewriter_effect(f"  > {part}", speed=0.06)
        time.sleep(0.5)
    
    print("\n" + Colors.MAGENTA + "♪ [Soft, neurotic jazz piano playing in the background] ♪" + Colors.END)
    print("\n" + Colors.YELLOW + "-------------------------------------------------------" + Colors.END)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEven your attempt to exit is a metaphor for the futility of human agency.")