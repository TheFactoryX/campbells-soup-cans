"""
Campbell's Soup Can #826
Produced: 2025-12-09 21:31:02
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

def print_ansi(text, color_code):
    """Print text with ANSI color codes"""
    sys.stdout.write(f"\033[{color_code}m{text}\033[0m")
    sys.stdout.flush()

def animate_typewriter(text, delay=0.05):
    """Type text like an old typewriter with occasional backspace"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        # Occasionally add a tiny hesitation (like a jammed typewriter)
        if random.random() < 0.1:
            time.sleep(0.02)

def print_woody_allen_quote():
    # Clear screen and position cursor
    sys.stdout.write("\033[2J\033[H")
    
    # ASCII art of a worried person with glasses (Woody Allen style)
    glasses_face = """
                    .-""""""-.
                   /   _  _   \\
                  |   (o)(o)   |
                  |    \__/    |
                   \\    ||    /
                    `-._||_,-'
                       ||  
                  .-""""""""-.
                 /    Worried \\
                |   Philosophical  |
                 \\    Thoughts  /
                  `-...........-'
    """
    
    # Print the ASCII art with cyan color
    print_ansi(glasses_face, "1;36")
    
    # Draw a fancy box around the quote
    print_ansi("\n" + "="*70, "1;33")  # Yellow box top
    
    # The Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    speaker = "- Woody Allen (probably while lying awake at 3 AM)"
    
    # Print quote with dramatic typewriter effect
    print("\n  ")
    print_ansi("“", "1;35")  # Magenta quote marks
    
    # Animate the quote in white with slight pauses
    animate_typewriter(quote, 0.08)
    
    print_ansi("”\n\n", "1;35")  # Closing quote marks
    
    # Print speaker in italics (ANSI code 3m) and green
    sys.stdout.write("  \033[3m\033[32m")
    animate_typewriter(speaker, 0.05)
    sys.stdout.write("\033[0m")  # Reset
    
    print_ansi("\n" + "="*70, "1;33")  # Yellow box bottom
    
    # Add a neurotic footnote
    footnote = "Anxiety level: 87%. Existential dread: 92%. Still better than Tuesday."
    print(f"\n\n  \033[2m\033[37m{footnote}\033[0m")
    
    # Blink the glasses a few times for effect
    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write("\033[?25l")  # Hide cursor
        print_ansi("\n  \033[1A\033[2K", "0")  # Move up and clear line
        print_ansi("  (•)(•)", "1;31")  # Red blinking glasses
        time.sleep(0.3)
        
        print_ansi("\033[1A\033[2K", "0")
        print_ansi("  (—)(—)", "1;32")  # Green normal glasses
        time.sleep(0.3)
    
    # Show cursor again
    sys.stdout.write("\033[?25h")
    
    print("\n\n" + " "*25 + "\033[1;34mLife is short... or is it?\033[0m")

if __name__ == "__main__":
    print_woody_allen_quote()