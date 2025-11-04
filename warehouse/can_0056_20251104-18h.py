"""
Campbell's Soup Can #56
Produced: 2025-11-04 18:44:25
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
import os

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
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BG_BLUE = '\033[44m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(text, color):
    return f"{color}{text}{Colors.END}"

def draw_woody():
    """ASCII art representation of Woody Allen"""
    return """
    .-""-.
   / o o \\
  |   \\/  |
   \\  --- /
    `-----'
      ||
     /||\\
"""

def woody_quote():
    """A Woody Allen-style philosophical quote"""
    quote = "I spend most of my time worrying about death. Not because it's frightening, but because I'm afraid it might be just like a cocktail party I wasn't invited to - awkward, filled with people I don't know, and no good canapés."
    attribution = "— Woody Allen"
    return quote, attribution

def type_text(text, color, speed=0.03):
    """Typewriter effect for text display"""
    for char in text:
        print(f"{color}{char}{Colors.END}", end="", flush=True)
        time.sleep(speed)
    print()

def display_art_frame(frame):
    """Display ASCII art with animation"""
    if frame == 0:
        return colored_text(draw_woody(), Colors.CYAN)
    elif frame == 1:
        return colored_text("    .-\"\"-.\n   / o o \\\n  |   \\/  |\n   \\  --- /\n    `-----'\n      ||\n     /||\\\n", Colors.MAGENTA)
    elif frame == 2:
        return colored_text("    .-\"\"-.\n   / o o \\\n  |   \\/  |\n   \\  --- /\n    `-----'\n      ||\n     /||\\\n", Colors.YELLOW)
    elif frame == 3:
        return colored_text("    .-\"\"-.\n   / o o \\\n  |   \\/  |\n   \\  --- /\n    `-----'\n      ||\n     /||\\\n", Colors.GREEN)
    elif frame == 4:
        return colored_text("    .-\"\"-.\n   / o o \\\n  |   \\/  |\n   \\  --- /\n    `-----'\n      ||\n     /||\\\n", Colors.RED)
    elif frame == 5:
        return colored_text("    .-\"\"-.\n   / o o \\\n  |   \\/  |\n   \\  --- /\n    `-----'\n      ||\n     /||\\\n", Colors.BLUE)

def display_quote():
    """Main function to display the quote with visual effects"""
    # Animated intro
    for i in range(6):
        clear_screen()
        print(display_art_frame(i))
        time.sleep(0.2)
    
    # Quote display
    clear_screen()
    
    # Decorative borders
    top_border = colored_text("╔═════════════════════════════════════════════════════════════════╗", Colors.YELLOW)
    bottom_border = colored_text("╚═════════════════════════════════════════════════════════════════╝", Colors.YELLOW)
    side_border = colored_text("║", Colors.YELLOW)
    
    print(top_border)
    print()
    
    quote, attribution = woody_quote()
    
    # Format the quote into lines
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        if len(' '.join(current_line)) > 65:
            lines.append(' '.join(current_line))
            current_line = []
    
    if current_line:
        lines.append(' '.join(current_line))
    
    # Display quote with typewriter effect
    print(side_border + " ", end="")
    type_text(lines[0], Colors.WHITE, 0.02)
    
    for line in lines[1:]:
        print(side_border + " ", end="")
        type_text(line, Colors.CYAN, 0.02)
    
    print()
    print(side_border + "  " + Colors.BOLD + Colors.ITALIC + Colors.MAGENTA + attribution + Colors.END, end="")
    time.sleep(0.5)
    print()
    print(side_border + " " + Colors.ITALIC + Colors.CYAN + "*sigh*" + Colors.END)
    
    print()
    print(bottom_border)
    
    # Animated outro
    time.sleep(2)
    clear_screen()
    
    # Final animated frames
    for i in range(5, -1, -1):
        clear_screen()
        print(display_art_frame(i))
        time.sleep(0.1)
    
    clear_screen()
    print(colored_text("The End.", Colors.BOLD + Colors.RED))
    time.sleep(1)
    clear_screen()

if __name__ == "__main__":
    display_quote()