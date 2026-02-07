"""
Campbell's Soup Can #2097
Produced: 2026-02-07 13:12:20
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os
import random

def colored_text(text, color_code, background=None):
    """Apply ANSI color codes to text."""
    if background:
        return f"\033[{color_code};{background}m{text}\033[0m"
    return f"\033[{color_code}m{text}\033[0m"

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typewriter_effect(text, delay=0.03, color_code=None):
    """Print text with a typewriter effect."""
    for char in text:
        if color_code:
            sys.stdout.write(colored_text(char, color_code))
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_centered(text, row, color_code=None):
    """Print text centered on a specific row."""
    cols = os.get_terminal_size().columns
    text_len = len(text)
    if text_len >= cols:
        text = text[:cols-1]
    padding = (cols - text_len) // 2
    if color_code:
        print(f"\033[{row};{padding}H{colored_text(text, color_code)}")
    else:
        print(f"\033[{row};{padding}H{text}")

def draw_neurotic_man(row, col, color):
    """Draw ASCII art of Woody Allen's neurotic character."""
    man = [
        "      .-\"\"\"-.",
        "     /        \\",
        "    /   O    O \\",
        "   |     .      |",
        "   |    \\____/  |",
        "    \\   \\____/  /",
        "     \\__________/",
        "       |    |",
        "       |    |",
        "    \\_/      \\_/"
    ]
    
    for i, line in enumerate(man):
        sys.stdout.write(f"\033[{row+i};{col}H{colored_text(line, color)}")
        sys.stdout.flush()

def main():
    """Main function to run the Woody Allen quote display."""
    clear_screen()
    
    # Color codes
    yellow = "33"
    cyan = "36"
    red = "31"
    green = "32"
    magenta = "35"
    white = "37"
    
    # Woody Allen's style quote
    quote = "I tried to find the meaning of life, but I got distracted by a sale at Macy's."
    quote2 = "Now I have a sweater with no purpose and existential dread - which is somehow appropriate."
    
    # Print animated title with neurotic elements
    title = "WOODY'S PHILOSOPHICAL INSIGHTS"
    title_chars = list(title)
    
    for i in range(1, len(title_chars)+1):
        partial_title = ''.join(title_chars[:i])
        print_centered(partial_title, 5, cyan)
        time.sleep(0.05)
        if i < len(title_chars):
            # Add random neurotic elements
            for _ in range(3):
                char = random.choice("!?#$%&*+=|")
                col = random.randint(10, os.get_terminal_size().columns-10)
                row = random.randint(7, 12)
                sys.stdout.write(f"\033[{row};{col}H{colored_text(char, yellow)}")
                sys.stdout.flush()
                time.sleep(0.02)
    
    # Clear the random characters
    print_centered(" " * len(title), 5, white)
    print_centered(partial_title, 5, cyan)
    
    # Draw Woody Allen's neurotic character
    draw_neurotic_man(8, 10, yellow)
    
    # Print decorative line
    print_centered("─" * 70, 20, magenta)
    
    # Print quote with typewriter effect
    print(f"\033[{22};10H")
    print_with_typewriter_effect(colored_text(quote, green), 0.05)
    print(f"\033[{23};10H")
    print_with_typewriter_effect(colored_text(quote2, green), 0.05)
    
    # Print signature
    signature = "─ WOODY ALLEN ─"
    print_centered(colored_text(signature, red), 25)
    
    # Print footer
    footer = "Press any key to exit..."
    print_centered(colored_text(footer, white), 27)
    
    input()

if __name__ == "__main__":
    main()