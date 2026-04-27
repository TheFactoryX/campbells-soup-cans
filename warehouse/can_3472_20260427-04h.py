"""
Campbell's Soup Can #3472
Produced: 2026-04-27 04:00:17
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
from random import randint

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, color=93, delay=0.03):
    for char in text:
        if char == '\n':
            print()
        else:
            sys.stdout.write(colored_text(char, color))
            sys.stdout.flush()
            time.sleep(delay)
    print()

def woody_allen_quote():
    # ASCII art border
    top_border = "╔════════════════════════════════════════════════════════════════════════════════════════════╗"
    side_border = "║                                                                                              ║"
    bottom_border = "╚════════════════════════════════════════════════════════════════════════════════════════════╝"
    
    # Woody Allen's style quote
    quote = "I tried to be a philosopher, but I couldn't make a living at it. So I became a comedian - at least I get to make a living pointing out the absurdity of existence instead of just contemplating it in poverty. The only problem is, now I'm too busy making people laugh to actually solve any of life's existential dilemmas. It's a cruel twist of fate, really."
    
    # Title
    title = "WOODY ALLEN: ON THE PERILS OF PHILOSOPHY"
    
    # Animation
    clear_screen()
    for i in range(5):
        clear_screen()
        print(colored_text("Loading existential insight" + "." * (i + 1), "93"))
        time.sleep(0.2)
    
    clear_screen()
    
    # Print the title
    print(colored_text(top_border, "96"))
    print(colored_text(side_border, "96"))
    print(colored_text(f"║ {title:^80} ║", "95"))
    print(colored_text(side_border, "96"))
    
    # Woody Allen's glasses
    glasses = "║  o        o  ║"
    print(colored_text(glasses, "96"))
    print(colored_text(side_border, "96"))
    
    # Print the quote with typewriter effect
    typewriter_effect(f"║ {quote:^80} ║", 93)
    print(colored_text(side_border, "96"))
    print(colored_text(bottom_border, "96"))
    
    # Add a final interaction
    time.sleep(1)
    typewriter_effect("\nWoody's parting thought:", "95")
    time.sleep(0.5)
    typewriter_effect("'Life doesn't imitate art... it imitates bad television.'", "94")
    time.sleep(1)
    
    # Blinking cursor
    for _ in range(3):
        sys.stdout.write(colored_text("_", 95))
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(0.5)
    
    typewriter_effect("\n\nPress any key to exit...", "93")
    
    # Blinking cursor before exit
    for _ in range(3):
        sys.stdout.write(colored_text("_", 93))
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(0.5)
    
    input()

if __name__ == "__main__":
    woody_allen_quote()