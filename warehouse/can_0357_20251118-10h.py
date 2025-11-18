"""
Campbell's Soup Can #357
Produced: 2025-11-18 10:39:44
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_quote():
    # ANSI color codes
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    # ASCII art Woody Allen with glasses
    woody_art = [
        "      ___",
        "     /   \\",
        "    |  O  O  |",
        "    |   ><   |",
        "    |  ___   |",
        "     \\_____/",
        "        |  |",
        "        |__|"
    ]
    
    # Frame decoration
    frame_top = "╔══════════════════════════════════════════════════════════════════════════════════════╗"
    frame_bottom = "╚══════════════════════════════════════════════════════════════════════════════════════╝"
    frame_side = "║"
    
    # Woody Allen style philosophical quote
    quote = f"""{frame_top}
{frame_side} {YELLOW}I'm not afraid of death; I'm afraid that there is no{END} {PURPLE}afterlife and this is all there is{END}. {YELLOW}Which would be fine, except then I'd have to{END} {RED}admit my therapist was right about everything{END}. {frame_side}
{frame_side} {YELLOW}Life is full of misery, loneliness, and suffering - and it's{END} {CYAN}all over much too soon, especially the good parts{END}. {YELLOW}I keep telling myself that at least I'm not{END} {GREEN}in New Jersey during the summer{END}. {frame_side}
{frame_side} {YELLOW}I don't want to achieve immortality through my work; I want{END} {BOLD}{ITALIC}to achieve it through not dying{END}. {YELLOW}But if I have to choose, I'd rather be{END} {BLUE}remembered for my neurotic insights than for my{END} {RED}complete and utter lack of talent{END}. {frame_side}
{frame_side} {BOLD}{PURPLE}-- Woody Allen --{END} {frame_side}
{frame_bottom}"""
    
    # Animation sequence
    clear_screen()
    print("\n" * 3)
    
    # Draw Woody ASCII art with colors and glasses
    for i, line in enumerate(woody_art):
        if i == 2:  # Eyes
            print(f"{BLUE}   {line}{END}")
        elif i == 3:  # Glasses
            print(f"{YELLOW}   {line}{END}")
        elif i == 4:  # Nose and mouth
            print(f"{RED}   {line}{END}")
        else:
            print(f"{YELLOW}   {line}{END}")
        time.sleep(0.1)
    
    # Animated title with typewriter effect
    title = f"{BOLD}{CYAN}WOODY ALLEN'S PHILOSOPHICAL MUSINGS{END}"
    type_text(title, 0.02)
    print("\n" * 2)
    
    # Print the quote with a typing effect
    lines = quote.split("\n")
    for line in lines:
        type_text(line, 0.01)
    
    # Add a flourish at the end with animated hearts
    print("\n" * 2)
    for _ in range(5):
        print(f"{RED}♥{END} " * 10)
        time.sleep(0.1)
        print(f"{BLUE}♥{END} " * 10)
        time.sleep(0.1)

if __name__ == "__main__":
    woody_quote()