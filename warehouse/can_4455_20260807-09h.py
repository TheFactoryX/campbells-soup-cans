"""
Campbell's Soup Can #4455
Produced: 2026-08-07 09:15:05
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

def typewriter(text, delay=0.05, color="\033[37m"):
    """Prints text with a typewriter effect and color."""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")

def draw_border(width, char="*", color="\033[36m"):
    print(color + char * width + "\033[0m")

def animate_thought(quote):
    """Animate a neurotic existential crisis layout."""
    colors = {
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "white": "\033[37m",
        "dim": "\033[2m",
        "reset": "\033[0m"
    }

    clear_screen()
    
    # 1. The "Anxious Intro"
    print("\n")
    typewriter("... Analyzing existential dread...", 0.03, colors["dim"])
    time.sleep(0.5)
    typewriter("... Consulting the psychoanalyst...", 0.03, colors["dim"])
    time.sleep(0.8)
    
    # 2. The Reveal
    border_width = len(quote) + 10
    
    print("\n")
    draw_border(border_width, "═", colors["cyan"])
    
    # Centering the quote inside a box
    padding = " " * 4
    print(color_text(f"{padding}{quote}", colors["white"]))
    
    draw_border(border_width, "═", colors["cyan"])
    print("\n")

    # 3. The Self-Deprecating Outro
    time.sleep(1)
    typewriter("Anyway, I have a panic attack scheduled for 4 PM.", 0.06, colors["dim"])
    print("\n")

def main():
    # The Woody Allen Style Quote
    # Characteristics: Neurotic, fear of mortality, trivializing the cosmic.
    WOODY_QUOTE = "I find the concept of infinity quite comforting; it's the finite nature of my patience that truly haunts me."

    try:
        # A little "glitchy" animation effect to represent neuroticism
        for _ in range(3):
            clear_screen()
            print(color_text("\n" * 5 + "  [ SEARCHING FOR MEANING IN A CHAOTIC UNIVERSE ]  ", "\033[91m\n"))
            time.sleep(0.2)
            clear_screen()
            time.sleep(0.1)

        animate_thought(WOODY_QUOTE)

    except KeyboardInterrupt:
        print("\n\n\033[31mEven your exit is existential. Goodbye.\033[0m")

if __name__ == "__main__":
    # Check if running in a terminal that supports colors
    if sys.stdout.isatty():
        main()
    else:
        # Fallback for non-interactive shells
        print("I'm not afraid of running in a non-TTY environment; I'm just afraid of what it means for my social life.")