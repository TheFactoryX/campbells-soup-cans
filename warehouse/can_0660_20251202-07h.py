"""
Campbell's Soup Can #660
Produced: 2025-12-02 07:33:55
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import random
import time
import sys

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end='', flush=True)

def print_wooden_style(text):
    colors = [38, 39]
    for char in text:
        print_colored(char, random.choice(colors))
        time.sleep(0.05)
    print()

def animate_background(chars, interval=0.02):
    for _ in range(15):  # Number of frames for animation
        remaining = chars[:]
        for _ in range(70):  # Width of animation area
            if not remaining:
                break
            pos = random.randint(0, 70)
            char = random.choice(remaining)
            print_colored(f"\r{pos*' '}{char}", random.choice([91, 93, 97]))
            remaining.remove(char)
            time.sleep(interval)

def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Miniaturized Woody Allen head
    wooden_head = [
        "        .(((((((((\\\\",
        "        \|    o-o  |]",
        "         |    /|\\   |",
        "         \  .` ` . \/",
        "          )      (    ",
        "         |_|_||_|_||",
        "         |__________]",
    ]
    
    for line in wooden_head:
        print_colored(line, 38)
    
    # ASCII quote block
    quote_block = [
        "┌───────────────────────────────────┐",
        "│                                   │",
        "│ Unable to work on life as it were │",
        "│ mirrored version of Shakespeare.  │",
        "│      Just couldn't get the hangs │",
        "│                on Hamlet...       │",
        "│                                   │",
        "│                ~ Woody Allen      │",
        "└───────────────────────────────────┘",
    ]
    
    # Animate ASCII block appearance
    for i in range(len(quote_block)):
        animate_background(list(quote_block[i]))
        quote_block[i] = colored_block_line(quote_block[i])
        print(quote_block[i])
        time.sleep(0.1)
    
    # Final presentation
    print_colored("\n\n   ✨ Press ENTER to view the Woody Allen insight!", 39)
    input()
    
    # Distorted quote delivery
    distortion_effect("               LIFE IS WOBBLY")
    distortion_effect("            ——>   --+        ")
    print_colored("           ————>   /           ", 38)
    distortion_effect("------------>               ", random.randint(30, 50))
    
    # Final quote
    print_colored("\n\n   \"Vanity is the best replacement for intelligence a person", 33)
    print_colored("     can ever have.\"      [Woody Allen Style]", 37)
    print_colored("(printed with intentional errors and fragmented format)", 38)

def colored_block_line(text):
    colors = [32, 33, 34, 35]
    return ''.join(random.choice(colors) and f"{char}" or char for char in text)

def distortion_effect(text, length=None):
    if length is None:
        length = random.randint(10, 25)
    for i in range(length):
        space = " " * i
        if i % 2 == 0:
            print_colored(f"\r{space}{text}", random.choice([91, 93, 97]))
        else:
            print_colored(f"\r{text}{space}", random.choice([91, 93, 97]))
        time.sleep(0.03)

if __name__ == "__main__":
    main()