"""
Campbell's Soup Can #3209
Produced: 2026-04-09 19:36:52
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
from itertools import cycle

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_print(text, color_code, bg_color=None):
    if bg_color:
        print(f"\033[{color_code};{bg_color}m{text}\033[0m")
    else:
        print(f"\033[{color_code}m{text}\033[0m")

def print_fancy_box(text, width=70, title=""):
    # Top border with title
    top_border = '+' + '-' * (width - 2) + '+'
    colored_print(top_border, 36)
    
    if title:
        # Create centered title
        title_line = f"| {title:^{width-2}} |"
        colored_print(title_line, 35)
        # Add separator
        separator = '+' + '-' * (width - 2) + '+'
        colored_print(separator, 36)
    
    # Text lines
    lines = [text[i:i+width-2] for i in range(0, len(text), width-2)]
    for line in lines:
        colored_print(f"| {line:<{width-2}} |", 36)
    
    # Bottom border
    colored_print(top_border, 36)

def typewriter_effect(text, delay=0.03, color=0):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def woody_head():
    # ASCII art of Woody Allen with some flair
    return [
        "      .--.",
        "     |o_o |",
        "     |:_/ |",
        "    //   \\ \\",
        "   (|     | )",
        "  /'\\_   _/`\\",
        "  \\___)=(___/",
        "",
        "        (sigh)"
    ]

def main():
    clear_screen()
    
    # Title with dramatic effect
    title = "WOODY ALLEN ON LIFE"
    colored_print("\n" + "="*40, 35)
    colored_print(f" {title:^38} ", 35)
    colored_print("="*40 + "\n", 35)
    
    # Pause for effect
    time.sleep(1)
    
    # Display Woody Allen head
    for line in woody_head():
        colored_print(line, 36 if line != "(sigh)" else 33)
        time.sleep(0.2)
    
    time.sleep(1)
    colored_print("\n", 0)
    
    # The philosophical quote
    quote = "I spent a year in psychoanalysis and all I got was this lousy T-shirt... wait, that's not right. I spent a year in psychoanalysis and now I know I'm nothing but a collection of chemical reactions hurtling through space toward oblivion. But at least I'm fashionable about it."
    
    # Animate the quote with typewriter effect
    time.sleep(0.5)
    typewriter_effect("\n", 0.02, 0)
    typewriter_effect(quote, 0.03, 35)
    typewriter_effect("\n\n", 0.02, 0)
    
    # Print in a fancy box
    time.sleep(1)
    print_fancy_box(quote, width=70, title="A THOUGHT FOR YOU")
    
    # Final thoughts with dramatic effect
    time.sleep(1.5)
    
    # Blinking final thought
    final_thought = "Maybe I should have stuck to being neurotic... it paid better."
    for _ in range(3):
        colored_print("\n\n" + final_thought, 31)  # Red
        time.sleep(0.5)
        colored_print("\n\n" + final_thought, 0)  # Normal
        time.sleep(0.5)
    
    # Dramatic pause and signature
    time.sleep(1)
    colored_print("\n\n", 0)
    colored_print("~ Woody Allen (probably)", 33)
    time.sleep(0.5)
    
    # Final dramatic exit
    for i in range(5, 0, -1):
        colored_print(f"\nExiting in {i}...", 31)
        time.sleep(0.5)
    
    clear_screen()

if __name__ == "__main__":
    main()