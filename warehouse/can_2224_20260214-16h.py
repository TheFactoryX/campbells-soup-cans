"""
Campbell's Soup Can #2224
Produced: 2026-02-14 16:48:44
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

def typewriter(text, delay=0.03):
    """Simulate a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def pulsing_text(text, colors, iterations=3, delay=0.05):
    """Create a pulsing effect with colors"""
    for i in range(iterations):
        # Fade in
        for alpha in range(1, 10):
            sys.stdout.write("\033[H")  # Move cursor to top-left
            sys.stdout.write(colors['reset'])
            sys.stdout.write("\033[2J")  # Clear screen
            sys.stdout.write(colors['bold'])
            sys.stdout.write(colors['yellow'])
            sys.stdout.write(" " * ((80 - len(text)) // 2))
            sys.stdout.write(text)
            sys.stdout.write("\n\n")
            sys.stdout.flush()
            time.sleep(delay / 10)
        
        # Fade out
        for alpha in range(10, 0, -1):
            sys.stdout.write("\033[H")  # Move cursor to top-left
            sys.stdout.write(colors['reset'])
            sys.stdout.write("\033[2J")  # Clear screen
            sys.stdout.write(colors['bold'])
            sys.stdout.write(colors['yellow'])
            sys.stdout.write(" " * ((80 - len(text)) // 2))
            sys.stdout.write(text)
            sys.stdout.write("\n\n")
            sys.stdout.flush()
            time.sleep(delay / 10)

def print_colorful_quote():
    # ANSI color codes
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m'
    }
    
    # ASCII art frame
    top_bottom = "═" * 70
    side = "║"
    
    # Woody Allen style quote
    quote = """I'm not afraid of death; I just don't want to be there when it happens. 
The problem with life is that there's a critical plot point missing, and I keep 
waiting for the twist that will make sense of everything, but it never comes. 
I've tried therapy, medication, and even joining a cult, but nothing really helps 
except knowing that we're all just floating in a meaningless void together."""
    
    # Woody Allen signature
    signature = " - Woody Allen"
    
    # ASCII Woody Allen face
    woody_face = [
        "     .--.    ",
        "    /OO \\   ",
        "   |    |   ",
        "   |    |   ",
        "  /      \\  ",
        " |        | ",
        " |   ()   | ",
        " |   ()   | ",
        " |   ||   | ",
        "  \\      /  ",
        "   '----'   "
    ]
    
    # Title with pulsing effect
    title = "WOODY ALLEN'S PHILOSOPHY"
    pulsing_text(title, colors, iterations=2)
    
    # Print with typewriter effect
    typewriter(f"{colors['yellow']}{colors['bold']}")
    
    # Print top of frame
    typewriter(f"\n╔{'═' * 66}╗\n")
    
    # Print Woody Allen face with typewriter effect
    for line in woody_face:
        typewriter(f"║{colors['magenta']}{line}{colors['yellow']}" + " " * (66 - len(line)) + "║\n")
    
    # Print space before quote
    typewriter(f"║{' ' * 66}║\n")
    
    # Print quote with color cycling effect
    words = quote.split()
    typewriter(f"{side} ")
    color_list = [colors['red'], colors['green'], colors['blue'], colors['magenta'], colors['cyan'], colors['white']]
    
    for i, word in enumerate(words):
        # Cycle through colors
        color = color_list[i % len(color_list)]
        typewriter(f"{color}{word} ")
        if i % 10 == 0:  # Add line breaks every 10 words for better formatting
            typewriter(f"\n{side} ")
    
    # Print signature
    typewriter(f"\n\n{side}{' ' * 66}{side}\n")
    typewriter(f"║{colors['white']}{colors['bold']}{signature:^66}{colors['yellow']}║\n")
    
    # Print bottom of frame
    typewriter(f"╚{'═' * 66}╝")
    typewriter(f"{colors['reset']}")
    print()

if __name__ == "__main__":
    print_colorful_quote()