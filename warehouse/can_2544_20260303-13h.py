"""
Campbell's Soup Can #2544
Produced: 2026-03-03 13:32:56
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

def typewriter_effect(text, delay=0.03, color_code=''):
    for char in text:
        sys.stdout.write(color_code + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def colored_text(text, color_code):
    return f"{color_code}{text}\033[0m"

def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Title with animation
    title = "WOODY ALLEN'S PHILOSOPHY"
    for char in title:
        sys.stdout.write(colored_text(char, '\033[1;35m'))
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    
    # Animated border
    for i in range(3):
        print(colored_text("+" + "-" * 58 + "+", '\033[1;' + str(36 + i) + 'm'))
        time.sleep(0.1)
    
    # Woody Allen ASCII Art
    woody = [
        "    __/\\__",
        "   (  o o  )",
        "   \\  >  /",
        "    \\___/",
        "     ||||",
        "    |    |",
        "   |      |"
    ]
    
    print("\n")
    for line in woody:
        print(colored_text(line.center(60), '\033[1;33m'))
        time.sleep(0.1)
    
    # The quote
    quote = "Sex without love is an empty experience, but as empty experiences go, it's one of the best. I'm not afraid of death; I just don't want to be there when it happens. My one regret in life is that I'm not someone else."
    
    # Print the quote with typewriter effect and colors
    print("\n" + colored_text("WOODY ALLEN SAYS:", '\033[1;32m'))
    print()
    
    # Split the quote for better visual presentation
    lines = [
        quote[:70],
        quote[70:140],
        quote[140:]
    ]
    
    colors = ['\033[1;32m', '\033[1;34m', '\033[1;36m']
    
    for i, line in enumerate(lines):
        typewriter_effect(" " * 8 + line, 0.03, colors[i])
    
    # Add a footer
    print("\n" + colored_text("— Woody Allen".center(60), '\033[3;36m'))
    
    # Add a small animation at the end
    print("\n")
    for i in range(3):
        print(colored_text("NEUROSIS: MY NATURAL STATE".center(60), '\033[1;31m'))
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)
    
    print(colored_text("NEUROSIS: MY NATURAL STATE".center(60), '\033[1;31m'))
    print("\n")

if __name__ == "__main__":
    main()