"""
Campbell's Soup Can #4289
Produced: 2026-07-22 12:03:06
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

def clear():
    """Clears the terminal screen."""
    print("\033[H\033[J", end="")

def color_text(text, color_code):
    """Wraps text in ANSI color codes."""
    return f"\033[{color_code}m{text}\033[0m"

def typewriter(text, delay=0.05, color="\033[37m"):
    """Simulates a neurotic, stuttering typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        # Random stuttering for neurotic effect
        time.sleep(delay)
        if char in [',', '.', ';', '?', '!'] and random.random() > 0.7:
            time.sleep(0.4)

def draw_frame(quote):
    """Draws a neurotic-looking frame around the quote."""
    width = len(quote) + 4
    top_border = "┌" + "─" * (width - 2) + "┐"
    bottom_border = "└" + "─" * (width - 2) + "┘"
    
    print(color_text(top_border, "\033[90m"))
    print(f"│ {quote} │")
    print(color_text(bottom_border, "\033[90m"))

def play_existential_loop():
    """Main execution loop for the philosophical performance."""
    colors = [
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
        "\033[93m",  # Yellow
    ]
    
    # The Quote
    quote = "I find my anxiety is the only thing that truly gives my life structure; without it, I'd just be a man wandering aimlessly through a deli."

    clear()
    
    # Part 1: The Intro (building tension)
    print("\n\n")
    typewriter("Initializing existential dread...", 0.1, "\033[90m")
    time.sleep(1)
    print("\n")
    time.sleep(1)

    # Part 2: The Philosophical Reveal
    # Let's do a dramatic fading effect
    for i in range(5, 0, -1):
        clear()
        print("\n" * i)
        print(color_text("...DEEP THOUGHTS COMMENCING...", "\033[33m"))
        time.sleep(0.5)

    clear()
    print("\n" * 2)
    
    # Draw the quote with a colorful typewriter effect
    target_color = random.choice(colors)
    typewriter(quote, 0.06, target_color)
    
    print("\n")
    draw_frame(quote)
    
    # Part 3: The Neurotic Outro
    print("\n")
    typewriter("Anyway, does anyone have a prescription for something stronger?", 0.04, "\033[91m")
    print("\n")
    time.sleep(2)

if __name__ == "__main__":
    try:
        play_existential_loop()
    except KeyboardInterrupt:
        print("\n\n[Life interrupted prematurely. Much like my enthusiasm.]")