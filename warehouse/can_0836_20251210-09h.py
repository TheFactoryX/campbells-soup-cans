"""
Campbell's Soup Can #836
Produced: 2025-12-10 09:39:31
Worker: Amazon: Nova 2 Lite (amazon/nova-2-lite-v1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Style Philosophical Quote Generator
A visually interesting, colorful, and playful single-file Python program.
"""

import time
import sys
import random

# ANSI escape codes for colors and styles
COLORS = {
    "RESET": "\033[0m",
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "BRIGHT_RED": "\033[31;1m",
    "BRIGHT_GREEN": "\033[32;1m",
    "BRIGHT_YELLOW": "\033[33;1m",
    "BRIGHT_BLUE": "\033[34;1m",
    "BRIGHT_MAGENTA": "\033[35;1m",
    "BRIGHT_CYAN": "\033[36;1m",
    "BRIGHT_WHITE": "\033[37;1m",
    "BOLD": "\033[1m",
    "ITALIC": "\033[3m",
    "UNDERLINE": "\033[4m",
    "BLINK": "\033[5m",
    "INVERSE": "\033[7m",
    "HIDDEN": "\033[8m",
}

# Fancy box drawing characters
BOX = {
    "TOP_LEFT": "┌",
    "TOP_RIGHT": "┐",
    "BOTTOM_LEFT": "└",
    "BOTTOM_RIGHT": "┘",
    "HORIZONTAL": "─",
    "VERTICAL": "│",
    "TOP_T": "├",
    "BOTTOM_T": "└",
    "LEFT_T": "┬",
    "RIGHT_T": "┴",
    "CROSS": "┼",
}

# Woody Allen style philosophical quotes
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "The most confusing thing about people is that they always seem to be thinking about something else.",
    "If you want to make God laugh, tell him your plans.",
    "I'd rather have a small, happy life than a large, miserable one.",
    "I'm against picking on anyone softer or more attractive than myself.",
    "The problem with being neurotic is that it's so utterly boring.",
    "The future is completely unpredictable... and that's terrifying.",
    "I take care of my body. It's the only place I have to live... unfortunately.",
]

def clear_screen():
    """Clear the terminal screen."""
    # Cross-platform screen clearing
    if sys.platform == "win32":
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def centered_text(text, width, color=COLORS["WHITE"], style=""):
    """
    Center a text within a given width, applying color and style.
    
    Args:
        text (str): The text to center
        width (int): The total width to center within
        color (str): ANSI color code
        style (str): ANSI style code
        
    Returns:
        str: Centered formatted text
    """
    if len(text) > width:
        return f"{color}{style}{text}{COLORS['RESET']}"
    
    padding = (width - len(text)) // 2
    return f"{color}{style}{' '*padding}{text}{' '*padding}{COLORS['RESET']}"

def draw_boxed_quote(quote, width=80):
    """
    Draw a quote inside a fancy box with borders.
    
    Args:
        quote (str): The quote to display
        width (int): Width of the box
    """
    # Create the top border
    top_border = BOX["TOP_LEFT"] + BOX["HORIZONTAL"] * (width - 2) + BOX["TOP_RIGHT"]
    
    # Create the bottom border
    bottom_border = BOX["BOTTOM_LEFT"] + BOX["HORIZONTAL"] * (width - 2) + BOX["BOTTOM_RIGHT"]
    
    # Split the quote into lines
    lines = [line.strip() for line in quote.split('\n') if line.strip()]
    
    if not lines:
        lines = [quote]
    
    # Build the box
    result = [f"{COLORS['CYAN']}{top_border}{COLORS['RESET']}",
              f"{COLORS['CYAN']}{BOX['VERTICAL']}{COLORS['RESET']} {COLORS['BRIGHT_YELLOW']}{centered_text(lines[0], width - 4)}{COLORS['RESET']} {COLORS['CYAN']}{BOX['VERTICAL']}{COLORS['RESET']}"]
    
    # Add subsequent lines if any
    for line in lines[1:]:
        result.append(f"{COLORS['CYAN']}{BOX['VERTICAL']}{COLORS['RESET']} {COLORS['BRIGHT_YELLOW']}{centered_text(line, width - 4)}{COLORS['RESET']} {COLORS['CYAN']}{BOX['VERTICAL']}{COLORS['RESET']}")
    
    # Add the bottom border
    result.append(f"{COLORS['CYAN']}{bottom_border}{COLORS['RESET']}")
    
    # Add a Woody Allen signature
    signature = "– Woody Allen"
    result.append(f"{COLORS['MAGENTA']}{' ' * ((width - len(signature)) // 2)}{signature}{COLORS['RESET']}")
    
    return "\n".join(result)

def spinning_cursor(duration=2.0):
    """
    Display a spinning cursor animation.
    
    Args:
        duration (float): How long to spin in seconds
    """
    spinner = ["◧", "⧗", "⧙", "⧘"]
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for symbol in spinner:
            sys.stdout.write(f"\r{COLORS['BRIGHT_BLUE']}Spinning... {symbol}{COLORS['RESET']}")
            sys.stdout.flush()
            time.sleep(0.1)

def typewriter_effect(text, delay=0.03):
    """
    Print text with a typewriter effect.
    
    Args:
        text (str): Text to print
        delay (float): Delay between characters in seconds
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    """Main function to display the Woody Allen quote."""
    # Clear the screen
    clear_screen()
    
    # Display a fun animation
    print(f"\n{COLORS['BRIGHT_CYAN']}Woody Allen Quote Generator{COLORS['RESET']}\n")
    spinning_cursor(duration=1.5)
    
    # Select a random quote
    quote = random.choice(QUOTES)
    
    # Display with typewriter effect
    typewriter_effect(f"\n{COLORS['BRIGHT_MAGENTA']}A philosophical pearl of wisdom...{COLORS['RESET']}\n", delay=0.05)
    
    # Draw the boxed quote
    print("\n" + draw_boxed_quote(quote))
    
    # Add a philosophical disclaimer
    disclaimer = "Disclaimer: This quote may not actually be from Woody Allen. It's just pretend!"
    print(f"\n{COLORS['BRIGHT_GREEN']}{disclaimer}{COLORS['RESET']}")
    
    # Add a funny Footer
    footer = "Remember: It's not the years in your life that count. It's the life in your years... or something like that."
    print(f"\n{COLORS['BRIGHT_BLUE']}{footer}{COLORS['RESET']}")
    
    # Keep the program running for a bit so the user can see it
    input("\n\nPress Enter to exit...")

if __name__ == "__main__":
    import os  # Only import os if needed
    main()