"""
Campbell's Soup Can #1481
Produced: 2026-01-08 20:39:33
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

# ANSI escape codes for colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_frame(content, width=70, color=Colors.WHITE, style='normal'):
    """Print content within a decorative frame with different styles"""
    if style == 'double':
        border = color + '╔' + '═' * (width - 2) + '╗' + Colors.END
        left_border = color + '║' + Colors.END
        right_border = color + '║' + Colors.END
    else:
        border = color + '+' + '-' * (width - 2) + '+' + Colors.END
        left_border = color + '|' + Colors.END
        right_border = color + '|' + Colors.END
    
    print(border)
    lines = content.split('\n')
    max_line_length = max(len(line) for line in lines)
    
    for line in lines:
        padding = ' ' * ((width - max_line_length) // 2)
        print(left_border + padding + line + padding + ' ' * (width - len(line) - len(padding) - 2) + right_border)
    print(border)

def typewriter_effect(text, delay=0.05, color=Colors.WHITE, random_delay=False):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        if random_delay:
            time.sleep(delay * random.uniform(0.5, 1.5))
        else:
            time.sleep(delay)
    print()

def draw_woody():
    """Draw a simple ASCII art representation of Woody Allen"""
    woody = [
        "   ,---.         ",
        "  /  _  \\        ",
        " | / \\ | |       ",
        " | \\_/ | |       ",
        "  \\___/  |       ",
        "        _|       ",
        "       (_)       ",
        "      /   \\      ",
        "     |     |     ",
        "     '     '     ",
        "      \\___/      "
    ]
    return '\n'.join(woody)

def draw_thought_bubble():
    """Draw a thought bubble"""
    bubble = [
        "        .-.       ",
        "       (o o)      ",
        "        '-'       ",
        "         |        ",
        "        / \\       ",
        "       /   \\      ",
        "      /     \\     "
    ]
    return '\n'.join(bubble)

def bouncing_quote():
    """Create a bouncing quote effect"""
    quote = "I tried to be a philosopher once, but my thoughts kept getting distracted by my own neurosis. It's like trying to meditate in a room full of anxious squirrels."
    
    # Get terminal size
    try:
        columns, rows = os.get_terminal_size()
    except:
        columns, rows = 80, 24
    
    max_width = columns - 10
    if len(quote) > max_width:
        # We would need to wrap the quote, but for simplicity, let's just shorten it
        quote = quote[:max_width-3] + "..."
    
    # Bounce the quote around the screen
    x, y = 0, 0
    dx, dy = 1, 1
    
    for _ in range(50):  # Bounce for 50 iterations
        clear_screen()
        
        # Print Woody at the bottom
        print("\n" * (rows - 15))
        print(Colors.CYAN + draw_woody() + Colors.END)
        
        # Print the quote at current position
        print("\n" * y)
        print(" " * x + Colors.YELLOW + Colors.BOLD + quote + Colors.END)
        
        # Update position
        x += dx
        y += dy
        
        # Bounce off walls
        if x <= 0 or x >= columns - len(quote) - 5:
            dx = -dx
        if y <= 0 or y >= rows - 10:
            dy = -dy
            
        time.sleep(0.1)

def main():
    # The Woody Allen style quote
    quote = "I tried to be a philosopher once, but my thoughts kept getting distracted by my own neurosis. It's like trying to meditate in a room full of anxious squirrels."
    
    # Clear the screen
    clear_screen()
    
    # Title with typewriter effect
    typewriter_effect("\n" + Colors.BOLD + Colors.MAGENTA + "WOODY ALLEN ON PHILOSOPHY" + Colors.END + "\n\n", 0.03)
    
    # Draw Woody and thought bubble
    print(Colors.CYAN + draw_woody() + Colors.END)
    print(Colors.WHITE + draw_thought_bubble() + Colors.END)
    
    # Print the quote with random delay for a more natural feel
    print("\n")
    print_frame(quote, 75, Colors.GREEN, 'double')
    
    # Add some philosophical flourish
    typewriter_effect("\n" + Colors.ITALIC + Colors.BLUE + "   - Woody Allen" + Colors.END + "\n", 0.05)
    
    # Add a final thought
    time.sleep(1)
    typewriter_effect("\n" + Colors.RED + "P.S. I'd write more, but I think I left the stove on..." + Colors.END + "\n", 0.03)
    
    # Wait for a moment, then show the bouncing quote
    time.sleep(2)
    bouncing_quote()

if __name__ == "__main__":
    main()