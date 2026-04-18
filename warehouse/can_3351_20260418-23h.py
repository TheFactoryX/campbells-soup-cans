"""
Campbell's Soup Can #3351
Produced: 2026-04-18 23:51:49
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

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_woody_allen_quote():
    # ANSI escape codes for colors
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'
    
    # ASCII art frame with decorative elements
    frame_top = f"{YELLOW}╔{'═' * 62}╗{END}"
    frame_bottom = f"{YELLOW}╚{'═' * 62}╝{END}"
    frame_side = f"{YELLOW}║{END}"
    
    # Woody Allen character with glasses
    woody = f"""
    {BLUE}       ___
     _.-'   '-.
    /  o    o  \\
   |     __     |
   |    |  |    |
    \\   \\__/   /
     '-.......-'{END} {YELLOW}(Woody Allen){END}
{ITALIC}"Life is full of anxiety, regret, and bad haircuts..."{END}
"""
    
    # The quote with different colors and formatting
    quote = f"""
    {GREEN}"I wanted to understand the universe, but then I realized I'd left my glasses at home.{END}
    {GREEN}Now I just squint at existence and hope it doesn't ask me too many difficult questions.{END}
    {RED}The only thing I've learned for sure is that mortality is much scarier than a dental appointment.{END}"{END}
    """
    
    # Attribution
    attribution = f"{BLUE}            - Woody Allen{END}"
    
    # Clear screen and display
    clear_screen()
    
    # Print Woody Allen character
    typewriter_effect(woody, 0.01)
    
    # Print frame with quote
    typewriter_effect(frame_top)
    typewriter_effect(f"{frame_side}                                                                          {frame_side}")
    typewriter_effect(f"{frame_side}                                                                          {frame_side}")
    typewriter_effect(f"{frame_side}    {BOLD}{PURPLE}A WOODY ALLEN PHILOSOPHICAL MEDITATION:{END}                                  {frame_side}")
    typewriter_effect(f"{frame_side}                                                                          {frame_side}")
    typewriter_effect(f"{frame_side}                                                                          {frame_side}")
    
    # Print quote with typewriter effect
    lines = quote.split('\n')
    for line in lines:
        if line.strip():
            typewriter_effect(f"{frame_side}    {line} {frame_side}")
    
    typewriter_effect(f"{frame_side}                                                                          {frame_side}")
    typewriter_effect(f"{frame_side}                                                                          {frame_side}")
    typewriter_effect(frame_bottom)
    
    # Print attribution with a blinking effect
    for i in range(3):
        if i % 2 == 0:
            sys.stdout.write(f"\n{attribution}")
        else:
            sys.stdout.write(f"\n{' ' * len(attribution)}")
        sys.stdout.flush()
        time.sleep(0.5)
    
    # Final attribution
    print(f"\n{attribution}")
    
    # Add a final thought
    time.sleep(1.5)
    final_thought = f"{YELLOW}\nI'd make a longer joke, but I'm afraid I'll run out of things to worry about.{END}"
    typewriter_effect(final_thought, 0.05)
    
    # Clean exit
    time.sleep(2)
    print(f"\n{END}")

if __name__ == "__main__":
    print_woody_allen_quote()