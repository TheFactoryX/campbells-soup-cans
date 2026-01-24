"""
Campbell's Soup Can #1824
Produced: 2026-01-24 19:28:14
Worker: Amazon: Nova 2 Lite (amazon/nova-2-lite-v1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody AllenStyleQuote.py

A playful, visually interesting Python program that prints ONE philosophical 
quote in the style of Woody Allen using ANSI escape codes for colors and 
creative formatting. The program features colorful ASCII art and a rotating 
text effect to mimic neurosis and existential musings.
"""

import time
import sys
import random

# ANSI escape codes for colors
COLORS = {
    "RESET": "\033[0m",
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
}

# List of funny philosophical quotes in Woody Allen's style
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "The lobsters are climbing over each other. You know they're eager to cook, but I think they just want to dance.",
    "I've made mistakes, but in my defense, I'm also right sometimes... probably.",
    "I would tell you a joke about loneliness, but I wouldn't have anyone to tell it to.",
    "I'm not really afraid of commitment... I'm just afraid of commitment devices that commit me to commitment.",
]

def rotate_text(text, steps=5):
    """Rotate the given text by the specified number of steps."""
    if not text:
        return ""
    rotated = text[steps:] + text[:steps]
    return rotated

def draw_frame(quote, color="CYAN"):
    """Draw a single frame with the quote inside ASCII art."""
    border = f"{COLORS[color]}┏" + "────────────────────────────┓" + COLORS["RESET"]
    inner_border = f"{COLORS[color]}┃" + "                          ┃" + COLORS["RESET"]
    quote_line = f"{COLORS[color]}┃" + f"{quote.center(34)}"[:34] + f"─┃" + COLORS["RESET"]
    
    return [
        border,
        inner_border,
        quote_line,
        inner_border,
        border
    ]

def main():
    """Main function to display the rotating quote."""
    # Choose a random quote
    quote = random.choice(QUOTES)
    
    # Introduce a delay for dramatic effect
    time.sleep(1)
    
    # Display each frame with color
    for i in range(20):  # Rotate through the quote gradually
        frames = draw_frame(rotate_text(quote, i % len(quote)), 
                           random.choice(["CYAN", "GREEN", "YELLOW", "MAGENTA"]))
        
        # Clear the screen for animation effect
        sys.stdout.write("\033[H\033[J")  # Move cursor to home and clear screen
        
        # Print each line with a small delay
        for line in frames:
            print(line)
        time.sleep(0.2)
    
    # Final display with a nice border and color
    time.sleep(0.5)
    sys.stdout.write("\033[H\033[J")
    final_frames = draw_frame(quote.center(34), "BLUE")
    for line in final_frames:
        print(line)

if __name__ == "__main__":
    main()