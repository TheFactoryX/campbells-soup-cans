"""
Campbell's Soup Can #3717
Produced: 2026-05-18 00:10:26
Worker: Z.ai: GLM 4.5 Air (z-ai/glm-4.5-air)
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

def type_text(text, delay=0.05, color=None):
    """Simulate typing with optional color"""
    for char in text:
        if color:
            sys.stdout.write(color + char + "\033[0m")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def draw_separator(char='*', length=60):
    """Draw a separator line"""
    print("\033[94m" + char * length + "\033[0m")

def ascii_thought_bubble():
    """Create a thought bubble ASCII art"""
    bubble = [
        "      .--.",
        "     |o_o |",
        "     |:_/ |",
        "    //   \\ \\",
        "   (|     | )",
        "  /'\\_   _/`\\",
        " \\___)=(___/"
    ]
    return "\033[96m" + "\n".join(bubble) + "\033[0m"

def main():
    # ANSI color codes
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'reset': '\033[0m'
    }
    
    # Woody Allen style quotes
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "To love and be loved is to feel the the sun from both sides.",
        "Eighty percent of success is showing up.",
        "I'm not a lesbian. I'm just tired of men.",
        "My one regret in life is that I'm not someone else.",
        "The heart is the loneliest part of the body."
    ]
    
    # Get a random quote
    quote = random.choice(quotes)
    
    # Print the visual presentation
    draw_separator()
    print(colors['cyan'] + "      WOODY ALLEN ON LIFE" + colors['reset'])
    print(colors['yellow'] + "           (and other disasters)" + colors['reset'])
    draw_separator()
    
    # Print the thought bubble
    print(ascii_thought_bubble())
    
    # Print the quote with typing effect and color
    print("\n\033[95m" + "WOODY SAYS:" + colors['reset'])
    type_text(quote, delay=0.03, color=colors['green'])
    
    # Print a footer
    draw_separator()
    print(colors['purple'] + "      ...because existential dread is the best kind!" + colors['reset'])
    draw_separator()

if __name__ == "__main__":
    main()