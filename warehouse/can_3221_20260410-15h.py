"""
Campbell's Soup Can #3221
Produced: 2026-04-10 15:06:37
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def colored_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return colors.get(color, '') + text + colors['reset']

def typewriter_effect(text, color='white', speed=0.04):
    for char in text:
        sys.stdout.write(colored_text(char, color))
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write('\n')

def waiting_animation():
    messages = [
        "Adjusting existential dread...",
        "Consulting inner neurotic...",
        "Formulating new anxieties...",
        "Calculating life's meaninglessness...",
        "Finding meaning in bagels..."
    ]
    
    for i in range(5):
        for j in range(3):
            sys.stdout.write('\r')
            sys.stdout.write(colored_text(messages[i], 'yellow'))
            sys.stdout.write('.' * j + ' ' * (3-j))
            sys.stdout.flush()
            time.sleep(0.3)
        time.sleep(0.5)
    print('\r' + ' ' * 60 + '\r', end='')

def draw_border():
    print(colored_text("+" + "=" * 70 + "+", 'cyan'))
    print(colored_text("|" + " " * 70 + "|", 'cyan'))

def draw_woody():
    woody = r"""
      ___
     (o o)
     ( o )
     (___)
     /   \
    /_____\
   |       |
   |  W.A  |
   |_______|
    
     | |
     | |
    _|_|_
"""
    print(colored_text(woody, 'yellow'))

def draw_thought_bubble():
    bubble = r"""
     .-""-.
    /      \
   |  O  O  |
   |   ^    |
   |  ---   |
    \      /
     '-..-'
      |  |
      |  |
      |__|
"""
    print(colored_text(bubble, 'blue'))

def print_quote():
    # Woody Allen style quote
    quote = """
"I've spent my entire life worrying about whether I'm making the right decisions,
 only to realize that the only thing worse than making the wrong decision 
 is having to decide what to have for lunch."
"""
    
    # Presentation elements
    title = "PHILOSOPHICAL INSIGHT"
    author = "-- Woody Allen"
    
    # Draw the presentation
    draw_border()
    print(colored_text("|" + " " * 27 + title + " " * 27 + "|", 'magenta'))
    draw_border()
    print()
    draw_woody()
    print()
    draw_thought_bubble()
    print()
    draw_border()
    
    # Print quote with typewriter effect
    typewriter_effect(quote, 'white', 0.03)
    
    draw_border()
    print(colored_text("|" + " " * 25 + author + " " * 25 + "|", 'green'))
    draw_border()
    
    # Blinking cursor effect at the end
    for i in range(5):
        sys.stdout.write(colored_text("_", 'red'))
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(0.3)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Title
    print(colored_text("\n\tWOODY ALLEN: A PHILOSOPHICAL JOURNEY\n", 'cyan'))
    
    waiting_animation()
    time.sleep(1)
    print_quote()
    
    # Wait for user input
    input(colored_text("\n\nPress Enter to continue...", 'yellow'))
    
    # Second quote
    print('\033[2J\033[H', end='')
    print(colored_text("\n\tANOTHER INSIGHT\n", 'cyan'))
    
    quote2 = """
"I'm not afraid of death; I just don't want to be there when it happens.
 But then again, I'm also afraid of the subway, public speaking, and spiders.
 Oh, and I think my accountant might be stealing from me.
 Basically, I'm afraid of everything except maybe cream cheese."
"""
    
    draw_woody()
    print()
    draw_thought_bubble()
    print()
    typewriter_effect(quote2, 'white', 0.03)
    
    # Final message
    print("\n" * 2)
    typewriter_effect("\nI'm not saying I'm a genius, but I do have a PhD in worrying.", 'yellow', 0.03)
    time.sleep(1)
    typewriter_effect("\nIt's from the University of New York. I graduated with honors in anxiety.", 'red', 0.03)
    
    # Exit message
    print("\n" * 3)
    print(colored_text("Thanks for listening to my neurotic thoughts.", 'green'))
    time.sleep(1)
    print(colored_text("I think I need to go lie down now.", 'yellow'))
    time.sleep(1)
    print(colored_text("...or maybe I'll have lunch first. Decisions, decisions.", 'cyan'))

if __name__ == "__main__":
    main()