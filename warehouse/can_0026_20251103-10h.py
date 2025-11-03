"""
Campbell's Soup Can #26
Produced: 2025-11-03 10:40:13
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def colored_text(text, color_code):
    """Return text wrapped with ANSI color codes."""
    return f"\033[{color_code}m{text}\033[0m"

def type_text(text, color_code, delay=0.03):
    """Type out text character by character with a delay."""
    for char in text:
        print(colored_text(char, color_code), end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Clear the terminal
    print("\033[2J\033[H", end="")
    
    # Define colors
    WHITE = "97"
    GRAY = "90"
    GOLD = "93"
    RED = "91"
    BLUE = "94"
    
    # Woody Allen glasses ASCII art
    glasses = [
        "  .--.     .--.  ",
        " /    \\___/    \\ ",
        "|                |",
        "|                |",
        " \\    _____    /  ",
        "  \\  /     \\  /   ",
        "   \\/       \\/    ",
        "   /\\       /\\    ",
        "  /  \\_____/  \\   ",
        " /              \\ ",
        "|                |",
        "|                |",
        " \\    _____    /  ",
        "  \\  /     \\  /   ",
        "   \\/       \\/    ",
    ]
    
    # Draw glasses
    for row in glasses:
        type_text(row, GRAY)
    
    type_text("\n\n", WHITE)
    
    # Title
    type_text(" WOODY ALLEN ON LIFE ", GOLD)
    type_text("\n\n", WHITE)
    
    # Create a quote with neurotic and existential themes
    quote = " To be or not to be? That is the question. Whether 'tis nobler to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles and, by opposing, end them. But mostly I'm worried about what to have for dinner. "
    
    # Draw a bordered box with the quote
    box_width = len(quote) + 4
    box_height = 5
    
    # Top border
    type_text("╔" + "═" * (box_width - 2) + "╗", BLUE)
    
    # Empty line with border
    type_text("║" + " " * (box_width - 2) + "║", BLUE)
    
    # Quote line with border
    type_text("║" + quote.center(box_width - 2) + "║", RED)
    
    # Another empty line with border
    type_text("║" + " " * (box_width - 2) + "║", BLUE)
    
    # Bottom border
    type_text("╚" + "═" * (box_width - 2) + "╝", BLUE)
    
    # Footer
    type_text("\n", WHITE)
    type_text(" - Woody Allen, Probably Overthinking This Too - ", GOLD)
    type_text("\n\n", WHITE)
    
    # Neurotic commentary
    thoughts = [
        " What if I'm not funny enough? What if my humor is too obscure? ",
        " What if nobody gets it? Should I add more jokes? ",
        " Maybe I'll just end this program now before I embarrass myself further...",
        " I don't want to achieve immortality through my code; I want to achieve it through not debugging.",
        " Life is full of bugs, loneliness, and stack traces - and it's all over much too soon."
    ]
    
    for thought in thoughts:
        type_text(thought, GRAY)
        time.sleep(1)
    
    # Rotating animation
    type_text("\n", WHITE)
    for i in range(10):
        rotation = ["|", "/", "-", "\\"]
        for char in rotation:
            sys.stdout.write(f"\r{colored_text(char, BLUE)} Processing existential dread... {colored_text(char, BLUE)}")
            sys.stdout.flush()
            time.sleep(0.2)
    
    # Final neurotic thought
    type_text("\n\n", WHITE)
    final_thought = random.choice([
        " I hope you enjoyed this. If not, please don't tell me. I'd rather not know.",
        " Did I mention that I hate public speaking? I'm only doing this because I'm afraid of silence.",
        " What if this program has bugs? What if it crashes? What if everything is meaningless?"
    ])
    type_text(final_thought, GRAY)
    
    # Blinking cursor effect
    for _ in range(5):
        sys.stdout.write(colored_text(">", BLUE))
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(colored_text(" ", BLACK))
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    main()