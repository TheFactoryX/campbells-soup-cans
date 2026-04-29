"""
Campbell's Soup Can #3501
Produced: 2026-04-29 22:11:04
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def clear_screen():
    print("\033[H\033[J", end="")

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.05, color="\033[37m"):
    """Prints text with a neurotic, stuttering typewriter effect."""
    full_text = f"{color}{text}\033[0m"
    for char in text:
        # Simulate neurotic hesitation
        if random.random() < 0.1:
            time.sleep(0.2)
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(content, width=60):
    """Draws a decorative border around the quote."""
    border_color = "\033[36m"  # Cyan
    side_color = "\033[34m"    # Blue
    
    top = border_color + "╔" + "═" * (width - 2) + "╗" + "\033[0m"
    bottom = border_color + "╚" + "═" * (width - 2) + "╝" + "\033[0m"
    
    print(top)
    # Center the content
    lines = content.split('\n')
    for line in lines:
        padding = (width - len(line) - 2) // 2
        left_pad = " " * padding
        right_pad = " " * (width - len(line) - 2 - padding)
        print(f"{side_color}║\033[0m{left_pad}{line}{right_pad}{side_color}║\033[0m")
    print(bottom)

def main():
    # The Quote
    quote = (
        "\"I have a deep, abiding fear of the infinite... "
        "mainly because I suspect it has a very long line "
        "and no sense of humor.\""
    )

    # Colors
    PURPLE = "35"
    YELLOW = "33"
    CYAN = "36"
    MAGENTA = "35"
    WHITE = "37"

    clear_screen()

    # 1. Intro Animation: The Existential Dread Pulse
    for _ in range(3):
        print(color_text("  [ ANALYZING MEANING OF LIFE... ]  ", YELLOW))
        time.sleep(0.4)
        clear_screen()
        print(color_text("  [ SEARCHING FOR PURPOSE... ]      ", YELLOW))
        time.sleep(0.4)
        clear_screen()

    print("\n" * 2)
    
    # 2. ASCII Art Character (A nervous-looking tie/suit icon)
    ascii_art = color_text("""
       ____
      /    \\
     |  oo  |  <-- (Panic!)
      \\ -- /
      /|  |\\
     / |__| \\
       /  \\
    """, PURPLE)
    print(ascii_art, end="")

    print("\n" + color_text("--- A PHILOSOPHICAL MOMENT OF ANXIETY ---", CYAN) + "\n")
    time.sleep(1)

    # 3. The Big Reveal
    draw_frame(quote, width=65)
    
    print("\n")
    
    # 4. The Neurotic Afterthought (Typewriter style)
    afterthought = "Anyway, I'll probably just go have a bagel."
    typewriter_effect(afterthought, delay=0.07, color="\033[90m") # Grey color

    print("\n" * 2)
    print(color_text("Press Ctrl+C to return to your mundane reality.", "31"))
    print()

    try:
        while True:
            # Just a blinking cursor to keep the vibe alive
            sys.stdout.write("\033[37m.\033[0m")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\033[K") # Clear line
            sys.stdout.flush()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(color_text("\n\n[ DISCONNECTED FROM EXISTENCE ]", "31"))

if __name__ == "__main__":
    main()