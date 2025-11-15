"""
Campbell's Soup Can #291
Produced: 2025-11-15 10:32:55
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

def animate_text(text, color_code):
    """Animates text with a color."""
    for char in text:
        print(f"\033[{color_code}m{char}\033[0m", end='', flush=True)
        time.sleep(0.03)  # Adjust speed as needed
    print()

def box_text(text, color_code):
    """Prints text inside a colored box."""
    width = len(text) + 4
    print(f"\033[{color_code}m" + "━" * width + "\033[0m")
    print(f"\033[{color_code}m┃ \033[0m" + text + f"\033[{color_code}m ┃\033[0m")
    print(f"\033[{color_code}m" + "━" * width + "\033[0m")

def choose_color():
    """Chooses a random ANSI color code."""
    colors = [91, 92, 93, 94, 95, 96]  # Red, Green, Yellow, Blue, Magenta, Cyan
    return random.choice(colors)

woody_allen_quote = "Existential dread is just my excuse for not folding laundry."

# Create Visuals
print(r"""
     _,-._
    / \_/ \
    >-(_)-<   Philosophizing...in Color!
    \_/ \_/
      `-'
""")

color = choose_color()
animate_text("Woody Allen, probably:", color)

for i in range(3):  # Add a little animation
    time.sleep(0.2)

color = choose_color()
box_text(woody_allen_quote, color)

time.sleep(0.5)

print("\n\033[38;5;208mThat's the story of my life... slightly neurotic, slightly orange.\033[0m") # Orange-ish color

print(r"""
                                   .---.
                                  /     \
                                  |()_()|
                                   \   /
                                    `-'
""")