"""
Campbell's Soup Can #4450
Produced: 2026-08-06 15:28:10
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
    for char in text:
        sys.stdout.write(color_text(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")

def draw_frame(width=60, height=10):
    """Draws a neurotic-looking frame."""
    top = "┌" + "─" * (width - 2) + "┐"
    bottom = "└" + "─" * (width - 2) + "┘"
    side_l = "│"
    side_r = "│"
    print(color_text(top, "\033[90m"))
    for _ in range(height - 2):
        print(color_text(f"{side_l}{' ' (width - 2)}{side_r}", "\033[90m"))
    print(color_text(bottom, "\033[90m"))

def main():
    # ANSI Colors
    GOLD = "\033[33m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    WHITE = "\033[37m"
    RED = "\033[31m"
    RESET = "\033[0m"
    
    # The neurotic philosopher's quote
    quote = (
        "\"I have a profound fear of the void, "
        "but an even greater fear that the void "
        "might actually find me interesting... "
        "which would be the ultimate cosmic tragedy.\""
    )

    # 1. Dramatic Entrance
    clear_screen()
    print("\n\n")
    print(color_text("   [ SYSTEM ERROR: EXISTENTIAL CRISIS DETECTED ]", RED))
    time.sleep(1)
    print(color_text("   [ REBOOTING NEUROSIS... ]", CYAN))
    time.sleep(1.5)
    clear_screen()
    print("\n")

    # 2. The ASCII Icon (A little neurotic glasses/face)
    icon = r"""
          -------
       /  _   _  \
      |  (o) (o)  |
      |     <     |
       \   ---   /
        -------
    """
    print(color_text(icon, GOLD))

    # 3. The Main Delivery
    print("\n")
    draw_frame(len(quote) + 8)
    
    # Moving the text into the frame via typewriter
    print(color_text("│", CYAN))
    # Print the quote line by line to fit the box
    lines = [quote[i:i+50] for i in range(0, len(quote), 50)]
    
    for line in lines:
        # Indent to simulate inside box
        sys.stdout.write(color_text("│  ", CYAN))
        typewriter_effect(line, 0.04, MAGENTA)
        sys.stdout.write(color_text("│  ", CYAN))
        sys.stdout.flush()

    # 4. Closing frame
    print(color_text("│  ", CYAN))
    draw_frame(len(quote) + 8) # Note: simplified for layout
    
    print("\n")
    print(color_text("--- End of existential monologue ---", WHITE))
    print(color_text("   (Please proceed to therapy immediately)   ", WHITE))
    print("\n")

if __name__ == "__main__":
    # Use a try-except to prevent messy terminal state if interrupted
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[0mInterrupted by reality. How predictable.")