"""
Campbell's Soup Can #285
Produced: 2025-11-15 04:34:56
Worker: Google: Gemini 2.0 Flash Experimental (free) (google/gemini-2.0-flash-exp:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def animate_text(text, color):
    """Animates text with a colored typewriter effect."""
    for char in text:
        print(f"\033[{color}m{char}\033[0m", end='', flush=True)
        time.sleep(0.03)

def clear_line():
    """Clears the current line in the terminal."""
    print("\033[K", end='')

def box_text(text, color):
    """Draws a box around the text with a specified color."""
    lines = text.splitlines()
    max_len = max(len(line) for line in lines)
    padding = 2
    width = max_len + 2 * padding

    top_bottom = f"\033[{color}m" + "═" * width + "\033[0m"
    empty_line = f"\033[{color}m" + "║" + " " * width + "║" + "\033[0m"
    print(top_bottom)
    for line in lines:
        padded_line = " " * padding + line + " " * (width - len(line) - 2 * padding)
        print(f"\033[{color}m" + "║" + f"\033[0m{padded_line}" + f"\033[{color}m" + "║" + "\033[0m")

    print(top_bottom)

def main():
    """Main function to display a philosophical quote with animation and formatting."""

    woody_quote = (
        "I once asked my analyst, 'Am I crazy?' \n"
        "He said, 'Don't worry, you're perfectly neurotic.' \n"
        "And I said, 'Is that a good thing?' \n"
        "He paused...  and then raised his rates."
    )

    colors = ["31", "32", "33", "34", "35", "36"]  # ANSI color codes
    random_color = random.choice(colors)

    box_text(woody_quote,random_color)
    # animate_text(woody_quote, random_color)


if __name__ == "__main__":
    main()