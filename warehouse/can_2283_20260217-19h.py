"""
Campbell's Soup Can #2283
Produced: 2026-02-17 19:15:22
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def clear_screen():
    print("\033c", end="", flush=True)

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay if char != ' ' else 0.005)
    time.sleep(0.7)

def print_woody_ascii():
    ascii_art = [
        "  .-\"-.",
        " /  ___  \\",
        "|  (o o)  |",
        " \\   ^   /",
        "  \\  '-' /",
        "   '-----'"
    ]
    colors = [36, 34, 32, 33, 35, 31]
    for i, line in enumerate(ascii_art):
        sys.stdout.write(f"\033[{colors[i % len(colors)]}m")
        typewriter(line, 0.01)
        sys.stdout.write("\033[0m\n")
    time.sleep(0.5)

def main():
    clear_screen()
    
    # Header with animation
    header = "WOODY ALLEN'S EXISTENTIAL CRISIS GENERATOR v6.3\n"
    sys.stdout.write("\033[38;5;214m")
    typewriter(header, 0.02)
    sys.stdout.write("\033[0m")
    
    # Print ASCII art with color cycling
    print_woody_ascii()
    
    # Philosophical quote (Woody Allen style)
    quote = (
        "If nothing matters in the grand cosmic scheme,\n"
        "why do I still get anxious about my hairline?\n"
        "This existential dread would be so much easier\n"
        "to handle if pastrami sandwiches weren't so damn good.\n"
        "But then again... what if pastrami *is* the meaning of life?\n"
        "Suddenly everything makes horrifying sense."
    )
    
    # Create decorative border
    width = 50
    top_border = "\033[38;5;93m┌" + "─" * width + "┐\033[0m"
    bottom_border = "\033[38;5;93m└" + "─" * width + "┘\033[0m"
    
    print(top_border)
    
    # Type quote with yellow text and subtle animation
    sys.stdout.write("\033[38;5;220m")
    lines = quote.split('\n')
    for line in lines:
        padded = line.ljust(width)
        sys.stdout.write("│ ")
        for i, char in enumerate(padded):
            # Add subtle wiggle effect to text
            wiggle = " " if i % 17 == 0 and char != ' ' else char
            sys.stdout.write(wiggle)
            sys.stdout.flush()
            time.sleep(0.008)
            if char != ' ':
                time.sleep(0.01)
        sys.stdout.write(" │\n")
        time.sleep(0.2)
    sys.stdout.write("\033[0m")
    
    print(bottom_border)
    
    # Footer with blinking effect
    footer = "\n\033[38;5;202mMeaning found: 1/3 of a pastrami sandwich\033[0m"
    for _ in range(3):
        print(footer + "   ", end='\r')
        time.sleep(0.4)
        print(" " * len(footer), end='\r')
        time.sleep(0.2)
    print(footer)
    
    time.sleep(2.5)

if __name__ == "__main__":
    main()