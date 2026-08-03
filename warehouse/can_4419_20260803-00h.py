"""
Campbell's Soup Can #4419
Produced: 2026-08-03 00:12:57
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

def color_text(text, color_code):
    """Helper to wrap text in ANSI colors."""
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.05, color="37"):
    """Animates text appearing character by character."""
    for char in text:
        sys.stdout.write(color_text(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Clears the terminal screen."""
    print("\033[H\033[J", end="")

def generate_existential_dread():
    """The masterpiece of neurotic thought."""
    
    # Configuration
    THEME_COLOR = "36"  # Cyan
    ACCENT_COLOR = "35" # Magenta
    QUOTE = (
        "\"I'm not saying my life is a series of meaningless accidents "
        "leading toward an inevitable void, but if it were a play, "
        "the critics would call it 'excessively repetitive and "
        "disturbingly lacking in a coherent subplot.\""
    )

    # Visual Elements
    ASCII_ART = [
        "      ---.      ",
        "     /     \\     ",
        "    | () () |    ",
        "     \\  ^  /     ",
        "      '---'      ",
        "        |        ",
        "      --+--      ",
        "        |        "
    ]

    # 1. Intro Sequence
    clear_screen()
    print("\n" * 2)
    print(color_text("--- INITIALIZING NEUROSIS ---", "33"))
    time.sleep(1)
    print(color_text("--- ANALYZING EXISTENTIAL ANXIETY ---", "33"))
    time.sleep(1)
    print(color_text("--- SCANNING FOR MEANING... [NOT FOUND] ---", "33"))
    time.sleep(1.5)
    clear_screen()

    # 2. Decorative Border Animation
    border = color_text("~" * 60, "90")
    print("\n" + border)
    print(border)
    
    # 3. Center the ASCII Art
    for line in ASCII_ART:
        print(" " * 20 + color_text(line, THEME_COLOR))
    
    print("\n" + border)
    print(border)

    # 4. The Grand Reveal
    print("\n")
    typewriter_effect(QUOTE, delay=0.04, color=ACCENT_COLOR)
    print("\n")

    # 5. Final Flourish
    print(color_text("------------------------------------------------------------", "90"))
    time.sleep(1)
    print(color_text("Press Enter to accept your inevitable mortality...", "32"))
    input()

if __name__ == "__main__":
    try:
        generate_existential_dread()
    except KeyboardInterrupt:
        print("\n\nEven you can't escape the void that quickly.")