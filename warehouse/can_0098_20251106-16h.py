"""
Campbell's Soup Can #98
Produced: 2025-11-06 16:44:42
Worker: DeepSeek: R1 Distill Llama 70B (free) (deepseek/deepseek-r1-distill-llama-70b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody_quote.py - Prints a Woody Allen-style philosophical quote with colorful box formatting

import sys
import time

# Woody Allen-style quote
QUOTE = "I'm not afraid of the dark, but I am afraid of the Milky Way exploding in my face."

# ASCII art decoration
STARẫnART = """
███████╗███████╗███████╗████████╗    ██╗     ██╗     ███╗   ███╗
██╔════╝██╔════╝██╔════╝╚══██╔══╝    ██║     ██║     ████╗ ████║
█████╗  █████╗  ███████╗   ██║       ██║     ██║     ██╔████╔██║
██╔══╝  ██╔══╝  ╚════██║   ██║       ██║     ██║     ██║╚██╔╝██║
███████╗███████╗███████║   ██║       ███████╗███████╗██║ ╚═╝ ██║
╚══════╝╚══════╝╚══════╝   ╚═╝       ╚══════╝╚══════╝╚═╝     ╚═╝
"""

def print_with_ansi_colors(text, color_code):
    """Print text with ANSI color formatting"""
    print(f"\033[{color_code}m{text}\033[0m")

def print_border(text, color_code=45):
    """Print text in a box with border character and specified color"""
    lines = text.split('\n')
    max_length = max(len(line) for line in lines) + 4
    border = '█' * max_length
    print_with_ansi_colors(f" {border} ", color_code)
    for line in lines:
        padded_line = f"   {line}   "
        print_with_ansi_colors(f"|{padded_line:^{max_length-2}}|", color_code)
    print_with_ansi_colors(f" {border} ", color_code)

def print_ascii_art_with_color(art, color_code):
    """Print ASCII art with color"""
    for line in art.split('\n'):
        if line.strip():  # Only color non-empty lines
            print_with_ansi_colors(line, color_code)
        else:
            print()

def main():
    # Print initial ASCII art with pink color
    print_with_ansi_colors("\n" * 5, 0)  # Clear screen with 5 newlines
    
    print_ascii_art_with_color(STARanylART, 45)  # 45 is pink color
    
    # Print quote in box with white text
    print("\n" * 2)
    print_border(QUOTE, 37)
    
    # Wait a moment for dramatic effect
    time.sleep(2)
    
    # Add some woody allen style SMALL ascii art
    print("\n\n")
    print_with_ansi_colors("""
    ░░░░░░░░░░░░▄▄░░░░░░░
    ░░░░░░░▄▄▄▄▀▀▀█▄▄█░
    ░░░░▀▀█▄▄█▀▀▀▀▀▀▀▀▀█
    ░░█▀▀▀▄▄▀█▀▀▀▄▄█▀▀▀█
    ▄██▄▄▄██▀▀▀▀█████▀▀▀
    ░▀█▄▀░░▀█▀▀▀▄▄▀█▀▀▀
    ░░░░▀▀▄▄█▀▀▀▄▄█▀▀▀▄
    ░░░░░░▀██▀▀▄▄██▀▀▀▄
    ░░░░░oogle.com Labrador
    """, 33)  # 33 is yellow
    
    time.sleep(2)
    
    # Finally, print a final quote about thinking
    print("\n" * 3)
    print_with_ansi_colors("Thought of the day:", 32)  # 32 is green
    print_with_ansi_colors("If you think too much, you might forget how to think at all.", 32)

if __name__ == "__main__":
    main()