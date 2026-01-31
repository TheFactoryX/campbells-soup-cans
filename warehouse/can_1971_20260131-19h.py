"""
Campbell's Soup Can #1971
Produced: 2026-01-31 19:33:00
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
from itertools import cycle

def colored_text(text, color_code):
    """Print text with specified color using ANSI escape codes"""
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.05, color_code=37):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(colored_text(char, color_code))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_line(char, length, color_code=37):
    """Draw a line of characters with specified color"""
    line = char * length
    print(colored_text(line, color_code))

def draw_empty_line(length, color_code=37):
    """Draw an empty line with borders"""
    print(colored_text("║" + " " * (length - 2) + "║", color_code))

def draw_quote_box(quote, author, width=70):
    """Draw a decorative box around the quote"""
    # Top border with gradient colors
    colors = [34, 36, 35, 33, 31, 35, 36, 34]  # Blue to red to blue gradient
    color_cycle = cycle(colors)
    top_border = ""
    for i in range(width):
        top_border += colored_text("═", next(color_cycle))
    print(top_border)
    
    # Empty line
    draw_empty_line(width, 34)
    
    # Quote with color changes
    quote_colors = [33, 36, 37, 33, 36]  # Yellow, cyan, white, yellow, cyan
    quote_color_cycle = cycle(quote_colors)
    
    # Split quote into words for color cycling
    words = quote.split()
    colored_quote = "   "
    for word in words:
        colored_quote += colored_text(word + " ", next(quote_color_cycle))
    
    print(colored_text("║", 34) + colored_quote + colored_text("║", 34))
    
    # Empty line
    draw_empty_line(width, 34)
    
    # Author line
    author_line = "   " + author
    print(colored_text("║", 34) + colored_text(author_line.ljust(width - 2), 35) + colored_text("║", 34))
    
    # Bottom border
    print(top_border)

def main():
    # Woody Allen style quote
    quote = "I spent so much time worrying about whether I was happy that I missed out on actually being... well, mostly miserable."
    author = "─ Woody Allen"
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Animated title
    title = "Philosophical Musings"
    typewriter_effect("\n" * 5, 0.01)
    
    for char in title:
        sys.stdout.write(colored_text(char, 35) + " ")
        sys.stdout.flush()
        time.sleep(0.1)
    
    time.sleep(1)
    
    # Draw the quote box
    typewriter_effect("\n", 0.5)
    draw_quote_box(quote, author)
    
    typewriter_effect("\n", 0.5)
    
    # Final philosophical flourish
    flourish = " existential crisis: $12.99 + tax"
    typewriter_effect(flourish, 0.03, 31)
    
    typewriter_effect("\n" * 3, 0.2)
    typewriter_effect("The End", 0.1, 33)

if __name__ == "__main__":
    main()