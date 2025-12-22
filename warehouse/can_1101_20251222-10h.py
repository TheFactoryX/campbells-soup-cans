"""
Campbell's Soup Can #1101
Produced: 2025-12-22 10:40:38
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

def woody_allen_quote():
    quotes = [
        "My brain is a labyrinth with no exit; I get lost in my own thoughts and the only map is a bodega receipt.",
        "I'm not afraid of death, I just don't want to be there when it happens. I prefer to make other plans.",
        "I asked the universe for meaning and it gave me a tax audit and a lower back pain.",
        "I took a speed reading course and finished War and Peace in 15 minutes. It involves Russia.",
        "My relationship with time is like a bad marriage: it passes, but I’m not sure we’re on speaking terms.",
        "I don't want to achieve immortality through my work; I want to achieve it by never dying, which seems unlikely."
    ]
    return random.choice(quotes)

def print_slow(text, delay=0.03, color_code="\033[37m"):
    for char in text:
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")

def draw_curtains():
    rows, cols = 20, 80
    top_curtain = ("\033[48;2;75;0;130m" + " " * cols + "\n") * 5
    bottom_curtain = ("\033[48;2;75;0;130m" + " " * cols + "\n") * 5
    sys.stdout.write("\033[2J\033[H") # Clear screen
    print(top_curtain)
    # Stage Floor
    print("\033[48;2;50;50;50m" + " " * cols)
    print("\033[48;2;30;30;30m" + " " * cols)

def main():
    # Clear screen and hide cursor
    sys.stdout.write("\033[?25l\033[2J\033[H")
    
    # 1. The Neurotic Curtain Rise
    draw_curtains()
    time.sleep(1.0)
    
    # 2. The Spotlight Effect (Center the text)
    sys.stdout.write("\033[2J\033[H") # Clear
    sys.stdout.write("\033[10;10H")   # Move cursor down/right for the "spotlight"
    
    # 3. The Dramatic Reveal
    quote = woody_allen_quote()
    
    # Animation of the person walking on stage (ASCII Art)
    sys.stdout.write("\033[38;5;250m") # Light gray for silhouette
    stick_figure = [
        "    O     ", # Head
        "   /|\\    ", # Body/Arms
        "   / \\    ", # Legs
        "  _/ \\_   "  # The Nervous Shuffle (Floor)
    ]
    
    for line in stick_figure:
        print("     " + line)
        time.sleep(0.2)
    
    time.sleep(0.5)
    
    # 4. The Quote Box
    box_width = len(quote) + 4
    top_border = "\033[33m╭" + "─" * box_width + "╮\033[0m"
    bottom_border = "\033[33m╰" + "─" * box_width + "╯\033[0m"
    
    print("\n" + top_border)
    print(f"\033[33m│ \033[0m\033[38;5;226m\033[1m{quote}\033[33m │\033[0m")
    print(bottom_border)
    
    # 5. The Existential Coda
    time.sleep(1.5)
    sys.stdout.write("\033[38;5;240m") # Dim gray
    print("\n(He exits stage left, tripping slightly over the microphone)")
    time.sleep(2.0)
    
    # Restore cursor
    sys.stdout.write("\033[?25h")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\n\033[?25h") # Restore cursor on exit
        sys.exit(0)