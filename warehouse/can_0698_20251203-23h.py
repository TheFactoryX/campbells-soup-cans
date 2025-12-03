"""
Campbell's Soup Can #698
Produced: 2025-12-03 23:29:41
Worker: Qwen: Qwen3 Coder 480B A35B (free) (qwen/qwen3-coder:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def typewriter_effect(text, delay=0.03):
    """Simulate typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_fancy_box(lines, color='\033[93m'):
    """Print text in a fancy ASCII box with color"""
    max_len = max(len(line) for line in lines)
    border = "+" + "-" * (max_len + 2) + "+"
    
    print(color + border)
    for line in lines:
        padding = " " * (max_len - len(line))
        print(f"| {line}{padding} |")
    print(border + "\033[0m")

def print_woody_quote():
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")
    
    # Title with colors
    title_lines = [
        "    PHILADELPHIA    ",
        "     PHILOSOPHY     ",
        "       INSTITUTE    "
    ]
    
    # Print title with animation
    typewriter_effect("\033[96m" + "="*40 + "\033[0m", 0.01)
    typewriter_effect("\033[95m    WOODY ALLEN'S EXISTENTIAL CORNER\033[0m", 0.02)
    typewriter_effect("\033[96m" + "="*40 + "\033[0m", 0.01)
    print()
    
    # Wait a bit
    time.sleep(0.5)
    
    # The quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    attribution = "- Woody Allen (obviously)"
    
    # Print in a fancy box
    quote_lines = [
        "",
        quote,
        "",
        attribution,
        ""
    ]
    
    print_fancy_box(quote_lines, '\033[93m')
    
    # Add some "philosophical" decoration
    time.sleep(0.5)
    print()
    typewriter_effect("\033[90m* existential crisis sold separately *\033[0m", 0.05)
    
    # Add some random neurotic footnotes
    footnotes = [
        "\033[92mP.S. I would have said something more profound, but I was too busy\033[0m",
        "\033[92m      worrying about my dentist appointment.\033[0m",
        "",
        "\033[91mWARNING: This product may contain traces of nihilism.\033[0m"
    ]
    
    for footnote in footnotes:
        typewriter_effect(footnote, 0.03)

if __name__ == "__main__":
    print_woody_quote()