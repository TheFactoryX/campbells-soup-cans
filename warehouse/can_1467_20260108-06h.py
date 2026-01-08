"""
Campbell's Soup Can #1467
Produced: 2026-01-08 06:51:08
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def type_effect(text, delay=0.03, color_code="\033[97m"):
    """Prints text with a typewriter effect."""
    print(color_code, end="")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print("\033[0m")

def clear_screen():
    """Clears the screen."""
    # ANSI escape code to clear screen and move cursor to home
    print("\033[2J\033[H", end="")

def draw_curtains():
    """Animates opening curtains."""
    lines = []
    height = 10
    width = 40
    
    # Pre-calculate curtain frames
    for step in range(21):
        gap = int((step / 20) * width)
        left_space = " " * int((width - gap) / 2)
        right_space = left_space
        if gap % 2 != 0: right_space = right_space[:-1] + " "
        
        left_curtain = "\033[31m" + "[" + "\033[0m" + "\033[41m" + " " * (int((width - gap)/2) - 1) + "\033[0m"
        right_curtain = "\033[41m" + " " * (int((width - gap)/2) - 1) + "\033[0m" + "\033[31m" + "]\033[0m"
        
        lines.append(f"{left_curtain}{right_curtain}")
        
    # Print frames
    for frame in lines:
        print("\033[H") # Go to top
        print("\n" * 3)
        print(" " * 12 + frame)
        time.sleep(0.05)

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Setup stage
    clear_screen()
    
    # 1. The Setup (Intro text)
    print("\n" * 2)
    print("\033[33m" + " " * 15 + "..............................................")
    print(" " * 15 + ".                                            .")
    print(" " * 15 + ".           THE BROADWAY STAGE               .")
    print(" " * 15 + ".                                            .")
    print(" " * 15 + "..............................................\033[0m")
    time.sleep(1.5)
    
    # 2. The Drama (Curtains Open)
    draw_curtains()
    
    # 3. The Performance (The Quote with a wandering spotlight)
    print("\n\n")
    
    spotlight_pos = 0
    direction = 1
    
    # We will print the quote, character by character, but change the background color
    # to simulate a spotlight moving across the text.
    
    # Calculate split points for a visual effect
    segments = [quote[:25], quote[25:55], quote[55:]]
    
    print("\033[1;37m") # Bold White
    print(" " * 10, end="")
    
    for i, segment in enumerate(segments):
        # Alternating spotlight colors (dim yellow vs bright white)
        bg = "\033[43m" if i % 2 == 0 else "\033[107m"
        fg = "\033[30m" if i % 2 == 0 else "\033[34m"
        
        # Typewriter effect for each segment
        for char in segment:
            print(f"{bg}{fg}{char}\033[0m", end="", flush=True)
            time.sleep(0.05)
            
        # Pause slightly between segments
        time.sleep(0.2)
        
    print("\033[0m\n")
    
    # 4. The Punchline (The Neurotic Actor)
    time.sleep(1)
    print("\033[90m" + " " * 8 + "___")
    print(" " * 8 + "| o \\")
    print(" " * 8 + "|   /")
    print(" " * 8 + "|_|\\" + "\033[0m")
    
    type_effect(" " * 15 + "(nervously)", delay=0.05, color_code="\033[3m\033[36m")
    
    # 5. The Curtain Call
    time.sleep(1.5)
    print("\n" * 2)
    type_effect(" " * 12 + "* Bow *", delay=0.1, color_code="\033[33m")
    
    time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handle graceful exit if user hits Ctrl+C
        print("\033[0m\n[Exit by heckler]")
        sys.exit(0)