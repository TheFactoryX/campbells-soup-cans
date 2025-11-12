"""
Campbell's Soup Can #226
Produced: 2025-11-12 11:29:00
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

def animate_text(text, color, delay=0.1):
    """Animates text with a typing effect and specified color."""
    for i in range(len(text) + 1):
        print(f"\033[{color}m{text[:i]}\033[0m", end='\r')
        time.sleep(delay)
    print("\033[0m")  # Reset color after animation

def print_quote_in_box(quote, box_color=32, text_color=37):
    """Prints a quote inside a colorful box."""
    padding = 2
    line_length = len(quote) + 2 * padding
    
    # Top border
    print(f"\033[{box_color}m" + "═" * line_length + "\033[0m")
    
    # Quote with padding
    print(f"\033[{box_color}m" + "║" + " " * padding + "\033[0m" + "\033[{text_color}m" + quote + "\033[0m" + "\033[{box_color}m" + " " * padding + "║" + "\033[0m")
    
    # Bottom border
    print(f"\033[{box_color}m" + "═" * line_length + "\033[0m")

def main():
    """Main function to generate and print the quote."""
    
    quotes = [
        "I've discovered the meaning of life. It's remarkably disappointing.",
        "You know what existentialism is? It’s when you lose your car keys in a vast, uncaring universe.",
        "I'm not sure what's worse: being neurotic or having people point it out.",
        "Marriage is a wonderful institution...but who wants to live in an institution?",
        "I suffer from acute onset procrastination. I'll explain it to you later.",
        "Reality is a crutch for people who can't handle imagination. Also, I have allergies.",
        "I tried being optimistic, but it didn't suit my personality.  Too much smiling gives me gas."
    ]

    chosen_quote = random.choice(quotes)
    
    # Choose random colors for a playful effect
    box_color = random.choice([31, 33, 34, 35, 36])  # Red, Yellow, Blue, Magenta, Cyan
    text_color = 37 # White
    
    #Pick and animate a border character
    border_char = random.choice(["═", "║", "╬"])
    
    # Simple animation before revealing the box
    animate_text("Contemplating the Void...", 34, 0.05)
    time.sleep(0.5)
    
    print_quote_in_box(chosen_quote, box_color, text_color)

if __name__ == "__main__":
    main()