"""
Campbell's Soup Can #3135
Produced: 2026-04-04 21:46:00
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

# ANSI color codes
class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ITALIC = '\033[3m'
    BLINK = '\033[5m'

def type_text(text, color=Colors.DARKCYAN, delay=0.05):
    """Simulate typing effect with optional color"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_line(char, width, color=Colors.YELLOW):
    """Draw a line of characters with color"""
    print(color + char * width + Colors.END)

def draw_box(text, width=70):
    """Draw a box around text with decorative elements"""
    # Top border
    draw_line("═", width, Colors.PURPLE)
    
    # Empty line with corners
    print(Colors.PURPLE + "║" + " " * (width-2) + "║" + Colors.END)
    
    # Text lines
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        if len(" ".join(current_line)) > width - 4:
            current_line.pop()
            lines.append(" ".join(current_line))
            current_line = [word]
    lines.append(" ".join(current_line))
    
    for line in lines:
        padding = (width - 4 - len(line)) // 2
        print(Colors.PURPLE + "║" + " " * padding + line + " " * (width - 4 - padding - len(line)) + "║" + Colors.END)
    
    # Empty line with corners
    print(Colors.PURPLE + "║" + " " * (width-2) + "║" + Colors.END)
    
    # Bottom border
    draw_line("═", width, Colors.PURPLE)
    
    # Signature
    time.sleep(0.5)
    print("\n")
    type_text("                                 - Woody Allen", Colors.RED, 0.03)

def animated_quote():
    """Display the quote with various visual effects"""
    # Clear screen
    print("\033[H\033[J", end="")
    
    # Animated title
    title = "WOODY ALLEN'S PHILOSOPHICAL INSIGHTS"
    for i, char in enumerate(title):
        sys.stdout.write(Colors.BOLD + Colors.BLUE + char + Colors.END)
        sys.stdout.flush()
        time.sleep(0.05)
    
    print("\n\n")
    
    # Main quote
    quote = ("I've spent twenty years in therapy analyzing my neuroses, only to discover "
             "that my greatest fear is not death or failure, but that someone might find "
             "out I'm not as smart as I pretend to be. Ironic, isn't it? Like trying to "
             "fix a leaky boat by drilling more holes.")
    
    # Draw box around quote
    draw_box(quote)
    
    # Add a blinking footer note
    time.sleep(1)
    print("\n")
    for _ in range(3):
        type_text("    ...and they say therapy doesn't work!", Colors.RED, 0.03)
        time.sleep(0.5)
        print("\033[A\033[K", end="")
        time.sleep(0.5)
    print()

if __name__ == "__main__":
    animated_quote()