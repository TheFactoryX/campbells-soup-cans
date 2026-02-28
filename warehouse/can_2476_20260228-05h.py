"""
Campbell's Soup Can #2476
Produced: 2026-02-28 05:49:16
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
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03, color=None, variable_speed=True):
    for i, char in enumerate(text):
        if color:
            sys.stdout.write(color + char + '\033[0m')
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        
        # Variable typing speed for more natural effect
        if variable_speed:
            if char in '.,!?:;':
                time.sleep(0.15 + random.random() * 0.1)
            elif char == ' ':
                time.sleep(0.02 + random.random() * 0.02)
            else:
                time.sleep(delay + (i % 3) * 0.01 + random.random() * 0.02)
        else:
            time.sleep(delay)
    sys.stdout.write('\n')

def display_quote():
    clear_screen()
    
    # ASCII art frame
    top_border = "╔" + "═" * 70 + "╗"
    bottom_border = "╚" + "═" * 70 + "╝"
    side_border = "║"
    
    # Colors
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    
    print("\n")
    # Print colorful frame
    type_text(top_border, color=BLUE)
    for _ in range(3):
        type_text(side_border + " " * 68 + side_border, color=CYAN)
    
    # Print title
    title = " WOODY ALLEN'S PHILOSOPHICAL INSIGHTS "
    type_text(side_border + title.center(68) + side_border, color=MAGENTA)
    
    for _ in range(3):
        type_text(side_border + " " * 68 + side_border, color=CYAN)
    
    # Print the quote with gradient effect
    quote = "I tried to be happy once. It was the worst ten minutes of my life. Turns out happiness is just anxiety with a better marketing team."
    
    words = quote.split()
    type_text(side_border + " " * 2, color=GREEN, variable_speed=False)
    for i, word in enumerate(words):
        # Cycle through colors for each word
        color = [YELLOW, GREEN, RED, BLUE, CYAN][i % 5]
        type_text(word + " ", delay=0.05, color=color, variable_speed=False)
    print(" " * 68 + side_border, color=RESET)
    
    for _ in range(3):
        type_text(side_border + " " * 68 + side_border, color=CYAN)
    type_text(side_border + "   - Woody Allen (Probably)  " + side_border, color=YELLOW)
    for _ in range(3):
        type_text(side_border + " " * 68 + side_border, color=CYAN)
    type_text(bottom_border, color=BLUE)
    
    # Animated Woody at the end
    print("\n\n")
    woody_frames = [
        "       .-\"\"\"-.",
        "     .'          `.",
        "    /   O      O   \\",
        "   :                :",
        "   |                |",
        "   :                :",
        "    \\    --------    /",
        "     `.          .'",
        "       `-......-'",
        "",
        "     I'm not a",
        "     therapist,",
        "     but I play",
        "     one in my",
        "     own nightmares."
    ]
    
    for frame in woody_frames:
        sys.stdout.write("\r" + " " * 30 + "\r")  # Clear the line
        sys.stdout.write(frame.center(30))
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n\n" + RESET)
    time.sleep(2)  # Pause before exiting

if __name__ == "__main__":
    display_quote()