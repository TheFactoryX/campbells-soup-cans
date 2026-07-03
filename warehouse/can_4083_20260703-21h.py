"""
Campbell's Soup Can #4083
Produced: 2026-07-03 21:31:27
Worker: Google: Gemma 4 31B (free) (google/gemma-4-31b-it:free)
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

def typewriter_effect(text, delay=0.05, color="\033[37m"):
    """Prints text with a typewriter effect and a specific color."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def print_glasses():
    """ASCII Art of iconic thick-rimmed glasses."""
    glasses = [
        "\033[94m     _______         _______     \033[0m",
        "\033[94m    /       \\       /       \\    \033[0m",
        "\033[94m   |   (O)   |-----|   (O)   |   \033[0m",
        "\033[94m    \\_______/       \\_______/    \033[0m"
    ]
    for line in glasses:
        print(line)

def main():
    # The Quote: Neurotic, existential, and classic Woody
    quote = (
        "I've decided that the secret to a happy life is to "
        "be completely terrified of everything at all times, "
        "so that when something actually goes wrong, I can "
        "simply say: 'See? I knew it! I was right the whole time!'"
    )

    # Visual styling
    border_char = "≈"
    width = 80
    
    # Clear screen
    print("\033[2J\033[H")

    # Header animation
    print("\n" * 2)
    print_glasses()
    print("\n")
    
    # Top border
    print("\033[90m" + border_char * width + "\033[0m")
    
    # Centered label
    print("\033[93m" + " " * 30 + "THE NEUROTIC PHILOSOPHER" + " " * 25 + "\033[0m")
    print("\033[90m" + border_char * width + "\033[0m")
    
    print("\n")
    
    # The delivery: slow, slightly hesitating typewriter effect
    # Adding small random pauses to mimic neurotic speech patterns
    words = quote.split()
    sys.stdout.write("\033[36m") # Cyan color for the quote
    for word in words:
        sys.stdout.write(word + " ")
        sys.stdout.flush()
        # Randomize delay to simulate "thinking/stuttering"
        time.sleep(random.uniform(0.05, 0.2))
    
    print("\033[0m")
    
    print("\n")
    
    # Bottom border
    print("\033[90m" + border_char * width + "\033[0m")
    
    # Final comedic touch
    time.sleep(1)
    print("\n\033[3m\033[90m(Now, where did I leave my medication?)\033[0m\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31mI can't handle this pressure! I'm leaving!\033[0m")