"""
Campbell's Soup Can #4066
Produced: 2026-07-01 22:39:42
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
    """Prints text with a typewriter effect and specific color."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def draw_glasses():
    """ASCII art of neurotic glasses."""
    glasses = [
        "   _______       _______   ",
        "  /       \\     /       \\  ",
        " |   (O)   |---|   (O)   | ",
        "  \\_______/     \\_______/  "
    ]
    for line in glasses:
        print("\033[33m" + line + "\033[0m")

def main():
    # The Quote: Neurotic, existential, and slightly panicked.
    quote = (
        "My therapist told me the secret to happiness is to ignore "
        "the crushing weight of existence, but I'm too anxious to "
        "ignore the fact that I'm ignoring it."
    )

    # Colors
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Clear screen
    print("\033[2J\033[H")

    # Centering logic
    width = 80
    
    print("\n" * 5)
    
    # Top Border
    print(f"{MAGENTA}{'=' * width}{RESET}")
    print(f"{MAGENTA}{' ' * 20}{BOLD}THE NEUROTIC PHILOSOPHER{RESET}{MAGENTA}{' ' * 20}{'=' * (width-60)}{RESET}")
    print(f"{MAGENTA}{'=' * width}{RESET}\n")

    # Visuals
    print("\n".center(width))
    for line in [
        "      (  )  ", 
        "     /    \\ ", 
        "    /  ||  \\"
    ]:
        print(line.center(width))
    
    draw_glasses()
    print("\n".center(width))

    # Animation: "Thinking..."
    thinking_dots = ["Thinking...", "Thinking..", "Thinking.", "Panic setting in..."]
    for dot in thinking_dots:
        sys.stdout.write(f"\r{CYAN}{dot.center(width)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")

    # The reveal
    print(f"{YELLOW}{'~' * (width // 2)}".center(width))
    
    # Wrap text manually for the typewriter effect
    words = quote.split()
    line_length = 0
    current_line = ""
    
    for word in words:
        if line_length + len(word) > 60:
            typewriter_effect(current_line.center(width), color=BOLD + CYAN)
            current_line = word + " "
            line_length = len(word)
        else:
            current_line += word + " "
            line_length += len(word) + 1
    
    typewriter_effect(current_line.center(width), color=BOLD + CYAN)
    
    print(f"\n{YELLOW}{'~' * (width // 2)}".center(width))
    
    # Closing sign-off
    time.sleep(0.5)
    typewriter_effect("\n(Sighs deeply and adjusts glasses)".center(width), delay=0.08, color=MAGENTA)
    
    print("\n" * 3)
    print(f"{MAGENTA}{'=' * width}{RESET}".center(width))
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31mEven the program is having a panic attack!\033[0m")