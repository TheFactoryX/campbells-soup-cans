"""
Campbell's Soup Can #263
Produced: 2025-11-14 04:37:04
Worker: Google: Gemma 3 27B (free) (google/gemma-3-27b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, color='\033[95m', delay=0.05):
    """Animates text by revealing it character by character."""
    for i in range(len(text)):
        print(color + text[:i+1] + '\033[0m', end='\r')  # Use carriage return to overwrite
        time.sleep(delay)
    print()

def draw_box(text, color='\033[92m', width=60):
    """Draws a colored box around the text."""
    padding = (width - len(text)) // 2
    padding_str = ' ' * padding
    top_bottom = color + '*' * width + '\033[0m'
    print(top_bottom)
    print(color + '*' + padding_str + text + padding_str + '*' + '\033[0m')
    print(top_bottom)

def random_color():
    """Generates a random ANSI color code."""
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    return random.choice(colors)

if __name__ == "__main__":
    clear_screen()

    quotes = [
        "I'm convinced that thinking is a highly overrated activity. Especially if you're me. It just leads to more things to worry about, which I'm already excellent at.",
        "Existentialism is all well and good, but have you tried ordering a decent bagel? That's a real tragedy.",
        "I wouldn't mind dying, provided I could take a good book with me. Or a really strong cup of tea. Definitely tea.",
        "They say time heals all wounds. But I suspect it just rearranges the furniture in the waiting room.",
        "I’m not a pessimist, I'm just realistically disappointed in everything."
    ]

    quote = random.choice(quotes)

    # Visual Flair
    color = random_color()
    draw_box("A Woody Allen-esque Observation:", color=color)
    animate_text("Presenting...", color='\033[33m', delay=0.1)
    time.sleep(0.5)
    animate_text(quote, color=color, delay=0.03)

    print("\033[0m")  # Reset color to default
    
    # Little bonus animation
    dots = ["."] * 3
    for i in range(5):
        print("Thinking... " + "".join(dots))
        time.sleep(0.2)
        dots = dots[1:] + ["."]  # Rotate dots