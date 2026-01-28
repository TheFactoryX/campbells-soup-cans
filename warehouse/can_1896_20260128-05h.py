"""
Campbell's Soup Can #1896
Produced: 2026-01-28 05:45:41
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import os

def typewriter(text, delay=0.03, color_code=''):
    """Print text with a typewriter effect and optional color"""
    for char in text:
        sys.stdout.write(color_code + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_quote():
    """Display a Woody Allen-style philosophical quote with visual effects"""
    clear_screen()
    
    # Title in a fancy box
    title = " WOODY ALLEN ON LIFE "
    typewriter("+" + "-" * (len(title) + 2) + "+", delay=0.01, color_code='\033[93m')
    typewriter("| " + title + " |", delay=0.01, color_code='\033[93m')
    typewriter("+" + "-" * (len(title) + 2) + "+", delay=0.01, color_code='\033[93m')
    print("\n")
    
    # Main quote in a thought bubble
    thought_bubble = [
        "    .-''''''-.",
        "  .'  O      `.",
        " :                :",
        " :   Life is a    :",
        " :   tragedy when :",
        " :   seen in      :",
        " :   close-up,    :",
        " :   but a comedy :",
        " :   in long-shot.",
        " :                :",
        "  `.    ,    ,    ,'",
        "    `-..______..-'"
    ]
    
    for line in thought_bubble:
        typewriter(line, delay=0.02, color_code='\033[96m')
    
    print("\n")
    
    # Woody Allen's commentary
    commentary = [
        ("It's true, you know. I've spent most of my life worrying about things that", '\033[95m'),
        ("probably won't happen, like what if my nose gets bigger or my next film", '\033[95m'),
        ("isn't funny enough to justify the therapy bills?", '\033[95m'),
        ("", '\033[0m'),
        ("I mean, statistically speaking, we're all just cosmic dust", '\033[91m'),
        ("with delusions of grandeur. But hey, at least we have", '\033[91m'),
        ("delusions! That's something, right?", '\033[91m'),
        ("", '\033[0m'),
        ("The trick is to enjoy the ride while you're still", '\033[92m'),
        ("on it. Or at least pretend to. I'm still working", '\033[92m'),
        ("on the pretending part myself.", '\033[92m')
    ]
    
    for line, color in commentary:
        if line:
            typewriter(line, delay=0.02, color=color)
        else:
            print()
    
    print("\n")
    
    # Footer
    footer = " - Woody Allen (probably) "
    typewriter("\033[3m" + footer + "\033[0m", delay=0.05, color_code='\033[90m')
    print("\n")
    
    # P.S. with typewriter effect
    typewriter("P.S. If you're not having panic attacks about your mortality,", delay=0.01, color_code='\033[93m')
    typewriter("you're probably not paying attention.", delay=0.01, color_code='\033[93m')
    time.sleep(2)

if __name__ == "__main__":
    woody_quote()