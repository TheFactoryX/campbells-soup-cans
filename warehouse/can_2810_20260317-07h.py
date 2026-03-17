"""
Campbell's Soup Can #2810
Produced: 2026-03-17 07:31:14
Worker: Perplexity: Sonar Deep Research (perplexity/sonar-deep-research)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def clear_screen():
    """Clear the terminal screen in a cross-platform manner."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color_code, delay=0.05):
    """Print text with a specific ANSI color code and typewriter effect."""
    reset_code = '\x1b[0m'
    colored_text = f'\x1b[{color_code}m{text}{reset_code}'
    
    for char in text:
        sys.stdout.write(f'\x1b[{color_code}m{char}{reset_code}')
        sys.stdout.flush()
        time.sleep(delay)

def print_ascii_border(width=70, color_code='36'):
    """Print a decorative ASCII border with color."""
    reset_code = '\x1b[0m'
    border = '═' * width
    print(f'\x1b[{color_code}m{border}{reset_code}')

def create_quote_display():
    """Create and display the Woody Allen-style philosophical quote."""
    clear_screen()
    
    # Color codes: 36=Cyan, 33=Yellow, 31=Red, 35=Magenta
    quote = "I'm not afraid of becoming irrelevant. I'm afraid of becoming relevant."
    author = "- A Person with Anxiety"
    
    # Display the top border
    time.sleep(0.5)
    print_ascii_border(70, '35')  # Magenta border
    
    # Display decorative spacing
    print()
    
    # Display the quote with typewriter effect
    print_colored('"', '33', 0.1)  # Yellow opening quote
    
    # Print the main quote text with letter-by-letter animation
    reset_code = '\x1b[0m'
    for char in quote:
        sys.stdout.write(f'\x1b[36m{char}{reset_code}')  # Cyan text
        sys.stdout.flush()
        time.sleep(0.03)
    
    print_colored('"', '33', 0.1)  # Yellow closing quote
    print()
    
    # Display author with a slight delay
    time.sleep(0.3)
    print_colored(author, '35', 0.02)  # Magenta author
    
    print()
    
    # Display the bottom border
    print_ascii_border(70, '35')  # Magenta border
    
    # Allow the display to remain visible
    time.sleep(1)

if __name__ == "__main__":
    create_quote_display()