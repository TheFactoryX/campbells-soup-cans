"""
Campbell's Soup Can #1421
Produced: 2026-01-06 04:52:34
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
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
import random
import os

def get_terminal_size():
    try:
        cols, rows = os.get_terminal_size()
        return cols, rows
    except:
        return 80, 24

def type_writer(text, color_code, delay=0.03):
    """Prints text with a typewriter effect"""
    print(color_code, end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print('\033[0m')

def print_curtains(cols, rows):
    """Prints animated red curtains"""
    print("\033[2J\033[H", end='')  # Clear screen
    half_width = cols // 2
    
    # Draw top curtain
    for i in range(min(8, rows // 3)):
        left = "🟦" * (half_width - 2)
        right = "🟦" * (half_width - 2)
        print(f"\033[31m{left}\033[0m  \033[31m{right}\033[0m")
        time.sleep(0.1)
    
    # Draw stage floor
    floor = "➖" * (cols - 2)
    print(f"\033[33m{floor}\033[0m")
    time.sleep(0.2)

def print_idea_bulb():
    """Prints a glowing idea bulb with animation"""
    bulb = [
        "  🟡  ",
        " 🟡🟡 ",
        "🟡🟡🟡",
        "  🟡  ",
        "  🟡  ",
        "  🟡  ",
        " 🟡🟡 "
    ]
    
    colors = ["\033[93m", "\033[93m", "\033[93m", "\033[93m", "\033[93m", "\033[93m", "\033[93m"]
    
    print("\n")
    for line in bulb:
        print("   " + random.choice(colors) + line + "\033[0m")
        time.sleep(0.1)
    print("\n")

def print_neurotic_face():
    """Prints a neurotic ASCII face"""
    face = [
        "  😬  ",
        " 😟😟 ",
        "😟   😟",
        "  😳  ",
        "  😵  "
    ]
    
    for line in face:
        print("   " + "\033[36m" + line + "\033[0m")
        time.sleep(0.1)

def print_ending_thoughts(cols):
    """Prints fading existential thoughts"""
    thoughts = [
        "...but what does it all mean?",
        "...is this real?",
        "...am I just code?",
        "...should I call my mother?",
        "...is there a refund policy?"
    ]
    
    thought = random.choice(thoughts)
    print("\n" + " " * ((cols - len(thought)) // 2) + "\033[3m\033[90m" + thought + "\033[0m")
    time.sleep(1)

def main():
    # Get terminal dimensions
    cols, rows = get_terminal_size()
    
    # The Woody Allen style philosophical quote
    quote = "I'm not afraid of death... I just don't want to be there when it happens."
    
    # Create the visual experience
    print_curtains(cols, rows)
    
    # Print the neurotic face
    print_neurotic_face()
    time.sleep(0.5)
    
    # Print the idea bulb
    print_idea_bulb()
    
    # Print the quote with dramatic typing
    print("\033[1m" + " " * ((cols - 40) // 2) + "🎭 WOODY'S PHILOSOPHICAL MUSINGS 🎭\033[0m\n")
    time.sleep(0.3)
    
    # Box the quote
    box_width = len(quote) + 4
    box_top = "╔" + "═" * (box_width - 2) + "╗"
    box_bottom = "╚" + "═" * (box_width - 2) + "╝"
    box_middle = "║ " + quote + " ║"
    
    # Calculate center position
    left_pad = (cols - box_width) // 2
    
    # Print box with animation
    print(" " * left_pad + "\033[33m" + box_top + "\033[0m")
    time.sleep(0.1)
    print(" " * left_pad + "\033[33m" + box_middle + "\033[0m")
    time.sleep(0.1)
    print(" " * left_pad + "\033[33m" + box_bottom + "\033[0m")
    time.sleep(0.5)
    
    # Add some dramatic pauses and color flashes
    print("\n")
    for i in range(3):
        sys.stdout.write("\r" + " " * cols)
        sys.stdout.flush()
        time.sleep(0.2)
        print("\033[31m!\033[0m" + " " * (cols - 2) + "\033[31m!\033[0m")
        time.sleep(0.2)
    
    print("\n")
    type_writer("  (because honestly, who wants to stick around for the sequel?)", "\033[3m\033[36m", 0.02)
    
    # Final existential thoughts
    print_ending_thoughts(cols)
    
    # Final fade out
    print("\n")
    for i in range(3):
        print(" " * cols)
        time.sleep(0.3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31mFine, I'll stop pondering existence. Sheesh.\033[0m")
    except Exception as e:
        print(f"\033[31mWell, this is awkward: {e}\033[0m")