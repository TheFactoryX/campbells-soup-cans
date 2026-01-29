"""
Campbell's Soup Can #1925
Produced: 2026-01-29 14:59:01
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

def woody_quote():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Woody Allen ASCII art
    woody = MAGENTA + """
    __  __       _ _   _ _     _     _ 
    \ \/ / __ _ | | | | | | __| | __| |
     \  / / _` || | | | | |/ _` |/ _` |
     /  \| (_| || | | | | | (_| | (_| |
    /_/\_\\__,_||_|_|_|_|_|\__,_|\__,_|
    """ + RESET
    
    # Neurotic Woody character
    woody_character = CYAN + """
    (o o) 
    =.= 
    --- 
    """ + RESET
    
    # The quote (neurotic, philosophical, Woody Allen style)
    quote_lines = [
        "I wanted to achieve immortality through my work,",
        "but then I realized that most of my work is just",
        "worrying about whether I'll achieve immortality",
        "through my work. It's a recursive nightmare."
    ]
    
    # Box dimensions
    box_width = 70
    
    # Box border characters (simple ones that work everywhere)
    border_char = "-"
    corner_char = "+"
    side_char = "|"
    
    # Center each line in the box
    centered_lines = []
    for line in quote_lines:
        # Calculate padding to center the text
        total_padding = box_width - len(line)
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
        centered_line = side_char + " " * left_padding + RED + BOLD + line + RESET + " " * right_padding + side_char
        centered_lines.append(centered_line)
    
    # Empty lines for the box
    empty_line = side_char + " " * box_width + side_char
    
    # Top and bottom borders
    top_border = corner_char + border_char * box_width + corner_char
    bottom_border = corner_char + border_char * box_width + corner_char
    
    # Full box
    box = YELLOW + top_border + "\n" + empty_line + "\n" + "\n".join(centered_lines) + "\n" + empty_line + "\n" + bottom_border + RESET
    
    # Author attribution
    author = CYAN + "                               - Woody Allen" + RESET
    
    # Self-deprecating footnote
    footnote = GREEN + """
    P.S. I wrote this quote myself. If you think it's not authentic,
    that's just my neurotic imposter syndrome talking.
    """ + RESET
    
    # Blinking cursor
    cursor = BLUE + "█" + RESET
    
    # Print everything with delays for animation effect
    print(woody)
    time.sleep(0.5)
    print(woody_character)
    time.sleep(0.5)
    print("\n")
    
    # Print box with animation
    for line in box.split('\n'):
        print(line)
        time.sleep(0.2)
    
    time.sleep(0.5)
    print("\n" + author)
    time.sleep(0.5)
    print(footnote)
    time.sleep(1)
    
    # Blinking cursor effect
    for i in range(5):
        print(cursor, end="", flush=True)
        time.sleep(0.3)
        print(" ", end="", flush=True)
        time.sleep(0.3)
    print()

if __name__ == "__main__":
    woody_quote()