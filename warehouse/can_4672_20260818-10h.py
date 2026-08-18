"""
Campbell's Soup Can #4672
Produced: 2026-08-18 10:46:46
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
    print("\033[2J\033[H", end="")

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, speed=0.05, color="\033[37m"):
    """Prints text with a slow, neurotic typewriter effect."""
    for char in text:
        sys.stdout.write(color_text(char, color))
        sys.stdout.flush()
        time.sleep(speed)
    print("\033[0m")

def draw_frame(content_width):
    """Draws a fancy neurotic-looking border around the quote."""
    border = "┌" + "─" * (content_width + 2) + "┐"
    bottom = "└" + "─" * (content_width + 2) + "┘"
    print(color_text(border, "\033[94m"))

def animate_existential_dread():
    """A visual experience of neurosis."""
    colors = ["\033[31m", "\033[33m", "\033[35m", "\033[36m", "\033[91m"]
    
    clear_screen()
    
    # Phase 1: The Sudden Realization
    for _ in range(3):
        sys.stdout.write(f"\r\033[K{color_text('...thinking about the void...', random.choice(colors))}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")

    # Phase 2: The Quote Box
    quote = "I find my anxiety to be quite helpful; it's the only thing that keeps me from"
    sub_quote = "realizing that the universe is just a giant, indifferent vacuum that"
    final_part = "doesn't even have a decent bagel shop in it."
    
    # Calculate width based on longest part
    max_w = max(len(quote), len(sub_quote), len(final_part))
    
    # Draw it
    draw_frame(max_w)
    
    # Animate the quote line by line
    typewriter_effect(f"│ {quote.ljust(max_w)} │", 0.04, "\033[97m")
    typewriter_effect(f"│ {sub_quote.ljust(max_w)} │", 0.04, "\033[97m")
    typewriter_effect(f"│ {final_part.ljust(max_w)} │", 0.04, "\033[93m")
    
    draw_frame(max_w)

    # Phase 3: The Existential Sigh
    print("\n")
    time.sleep(0.5)
    for _ in range(5):
        print(color_text("...sigh...", "\033[90m"))
        time.sleep(0.4)

    # Final punchline
    print("\n" + color_text("[End of existential crisis. Please try again tomorrow.]", "\033[32m"))

if __name__ == "__main__":
    try:
        animate_existential_dread()
    except KeyboardInterrupt:
        print("\n\n\033[91mEven your exit from this program is fraught with unnecessary drama.\033[0m")