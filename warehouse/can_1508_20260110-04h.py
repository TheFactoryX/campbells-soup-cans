"""
Campbell's Soup Can #1508
Produced: 2026-01-10 04:04:14
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
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
import os

def print_woody_allen_quote():
    # Clear screen and reset cursor
    print("\033[2J\033[H", end="")
    
    # ANSI color codes
    colors = [
        "\033[91m",  # red
        "\033[92m",  # green
        "\033[93m",  # yellow
        "\033[94m",  # blue
        "\033[95m",  # magenta
        "\033[96m",  # cyan
        "\033[97m",  # white
    ]
    
    # Woody Allen style neurotic quote
    quote = "I don't mind dying, I just don't want to be there when it happens. Also, I'm pretty sure my therapist is more depressed than I am."
    
    # ASCII art of a neurotic person (Woody Allen style glasses and hat)
    ascii_art = [
        "     _____      ",
        "    /     \\     ",
        "   | () () |    ",
        "    \\  ^  /     ",
        "     |||||      ",
        "      |||       ",
        "     /   \\      ",
        "    /     \\     ",
        "   |       |    ",
        "    \\_____/     ",
    ]
    
    # Print the ASCII art with blinking effect
    for _ in range(3):
        for i, line in enumerate(ascii_art):
            color = colors[i % len(colors)]
            print(f"{color}{line}\033[0m")
            time.sleep(0.1)
        print("\033[2J\033[H", end="")  # Clear screen
        time.sleep(0.2)
        
        for i, line in enumerate(ascii_art):
            # Make it blink by alternating colors
            if _ % 2 == 0:
                color = colors[i % len(colors)]
            else:
                color = "\033[2m"  # Dim mode
            print(f"{color}{line}\033[0m")
            time.sleep(0.1)
        print("\033[2J\033[H", end="")  # Clear screen
        time.sleep(0.2)
    
    # Print final art and quote
    print("\033[2J\033[H", end="")  # Clear screen
    
    # Print ASCII art in rainbow colors
    for i, line in enumerate(ascii_art):
        color = colors[i % len(colors)]
        print(f"{color}{line}\033[0m")
    
    print()
    
    # Print quote with typewriter effect and random color changes
    print("\033[1m\033[93m", end="")  # Bold yellow
    for char in quote:
        color = colors[random.randint(0, len(colors)-1)]
        print(f"{color}{char}\033[0m", end="", flush=True)
        time.sleep(0.05)
    
    print("\n")
    
    # Print neurotic signature
    signature = "~ Woody Allen (probably on the couch)"
    print(f"\033[90m{signature}\033[0m")
    
    # Add some neurotic thoughts as footer
    neurotic_thoughts = [
        "I should really call my mother...",
        "Is this quote too long? Am I rambling?",
        "I hope this isn't pretentious...",
        "Maybe I should've been a dentist..."
    ]
    
    print(f"\033[2m{random.choice(neurotic_thoughts)}\033[0m")

if __name__ == "__main__":
    print_woody_allen_quote()