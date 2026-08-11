"""
Campbell's Soup Can #4541
Produced: 2026-08-11 21:04:21
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen-Style Philosophical Quote Generator
A neurotic, colorful, animated existential crisis in pure Python.
"""

import sys
import time
import random
import shutil

# ANSI color codes
class Colors:
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    RESET = '\033[0m'

# The neurotic quote
QUOTE_LINES = [
    "I've been thinking about death a lot lately.",
    "Not the dramatic, cinematic kind—",
    "but the mundane, bureaucratic variety.",
    "",
    "You see, I figure if I'm going to exist",
    "in this absurd cosmic joke of a universe,",
    "I'd prefer a front-row seat.",
    "",
    "Unfortunately, I'm deathly allergic",
    "to both front rows and seats,",
    "so I end up watching life",
    "from the emergency exit aisle",
    "of a propeller-plane philosophy class",
    "taught by a man who thinks Sartre",
    "was a type of French cheese.",
    "",
    "And that's why I don't want to achieve",
    "immortality through my work...",
    "",
    "I want to achieve it through not dying,",
    "which seems like the same thing",
    "when you've seen my tax returns.",
]

def get_terminal_size():
    try:
        size = shutil.get_terminal_size()
        return size.columns, size.lines
    except:
        return 80, 24

def clear_screen():
    # Clear screen and move cursor to home
    print('\033[2J\033[H', end='', flush=True)

def draw_box(text, width=None, height=None):
    """Draw an ASCII art box around text with decorative borders."""
    if width is None:
        width = max(len(line) for line in text if line) + 8
    
    if height is None:
        height = len(text) + 4
    
    # Ensure width is even for nice corners
    if width % 2 != 0:
        width += 1
    
    top_border = "╔" + "═" * (width - 2) + "╗"
    bottom_border = "╚" + "═" * (width - 2) + "╝"
    
    inner_width = width - 4  # Account for padding
    
    print(Colors.MAGENTA + top_border + Colors.RESET)
    
    # Top padding
    print(Colors.MAGENTA + "║" + Colors.RESET + " " * (width - 2) + 
          Colors.MAGENTA + "║" + Colors.RESET)
    
    # Split text into lines and center them
    for line in text:
        if line:
            padded_line = line.center(inner_width)
        else:
            padded_line = " " * inner_width
        
        # Color cycling for visual interest
        color = random.choice([Colors.CYAN, Colors.YELLOW, Colors.GREEN, Colors.BLUE])
        print(Colors.MAGENTA + "║" + Colors.RESET + 
              color + Colors.ITALIC + padded_line + Colors.RESET +
              Colors.MAGENTA + "║" + Colors.RESET)
    
    # Bottom padding
    print(Colors.MAGENTA + "║" + Colors.RESET + " " * (width - 2) + 
          Colors.MAGENTA + "║" + Colors.RESET)
    
    print(Colors.MAGENTA + bottom_border + Colors.RESET)

def typewriter_effect(text, delay=0.05):
    """Print text with a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)
        if char == ' ':
            time.sleep(delay * 0.3)  # Faster for spaces
        elif char in '.,!?;:':
            time.sleep(delay * 3)  # Pause after punctuation
        elif char == '\n':
            time.sleep(delay * 5)  # Longer pause for new lines
        else:
            time.sleep(delay)
    print()  # New line after text

def animate_quote():
    """Animate the quote with typewriter effect and visual flair."""
    cols, rows = get_terminal_size()
    
    # Print header with flair
    header = " WOODY ALLEN-ISH PHILOSOPHICAL CRISIS™ "
    print(Colors.RED + Colors.BOLD + header.center(cols) + Colors.RESET)
    print(Colors.YELLOW + "━" * cols + Colors.RESET)
    print()
    
    # Draw a theater curtain effect
    curtain_width = min(cols - 4, 70)
    left_curtain = "╔" + "═" * (curtain_width // 2 - 1)
    right_curtain = "═" * (curtain_width // 2 - 1) + "╗"
    
    print(Colors.CYAN + left_curtain.rjust(cols // 2) + Colors.RESET)
    
    # Typewriter effect for the quote
    print(Colors.BOLD, end='')
    for line in QUOTE_LINES:
        if line:
            typewriter_effect(line, delay=random.uniform(0.02, 0.08))
        else:
            time.sleep(0.3)
            print()
    print(Colors.RESET)
    
    print(Colors.CYAN + "╚" + "═" * (curtain_width // 2 - 1) + 
          "╝".rjust(cols // 2 - curtain_width // 2 + 1) + Colors.RESET)
    
    # Add some blinking existential commentary
    print()
    time.sleep(0.5)
    
    # Pulsing "Existential Crisis Level" indicator
    levels = ["MINIMAL", "MODERATE", "SEVERE", "MAXIMUM"]
    for i, level in enumerate(levels):
        intensity = i / len(levels)
        r = int(255 * intensity)
        g = int(255 * (1 - intensity))
        color_code = f"\033[38;2;{r};{g};0m"
        print(f"\r{color_code}Existential Crisis Level: {level}{' ' * 10}{Colors.RESET}", 
              end='', flush=True)
        time.sleep(0.4)
    
    # Final blinking message
    print()
    time.sleep(0.3)
    
    for _ in range(5):
        print(Colors.BLINK + Colors.RED + 
              "☯  Nothing matters, but this quote looks nice on your desktop!  ☯"
              .center(cols) + Colors.RESET)
        time.sleep(0.8)
        clear_line()
        time.sleep(0.2)
    
    print(Colors.GREEN + Colors.BOLD + 
          "\n\n(Quote delivered with 100% more anxiety than your therapist recommends.)\n"
          .center(cols) + Colors.RESET)

def clear_line():
    """Clear the current line."""
    sys.stdout.write('\033[2K\r')
    sys.stdout.flush()

def print_ascii_art_frame():
    """Print a decorative ASCII art frame."""
    cols, rows = get_terminal_size()
    
    # Art deco style frame
    top = "┌" + "─" * (cols - 2) + "┐"
    bottom = "└" + "─" * (cols - 2) + "┘"
    
    print(Colors.YELLOW + top + Colors.RESET)
    
    # Add some decorative elements
    for i in range(2):
        line = "│"
        for j in range(cols - 4):
            if j % 10 == 0:
                line += random.choice("⚡⚡♆⚡⚡♆⚡⚡⚡")
            else:
                line += " "
        line += "│"
        print(Colors.YELLOW + line + Colors.RESET)
    
    return cols

def main():
    clear_screen()
    cols, rows = get_terminal_size()
    
    # Print title with dramatic flair
    title_lines = [
        " ╔══════════════════════════════════════╗ ",
        " ║    WOODY ALLEN EXISTENTIAL         ║ ",
        " ║         QUOTE GENERATOR           ║ ",
        " ╚══════════════════════════════════════╝ ",
    ]
    
    for line in title_lines:
        color = random.choice([Colors.RED, Colors.CYAN, Colors.MAGENTA])
        print(color + Colors.BOLD + line.center(cols) + Colors.RESET)
        time.sleep(0.3)
    
    print()
    time.sleep(0.5)
    
    animate_quote()
    
    # Print a small disclaimer
    print(Colors.DIM + Colors.ITALIC + 
          "\nDisclaimer: This program may cause temporary bouts of existential dread."
          .center(cols) + Colors.RESET)
    print(Colors.DIM + 
          "No philosophers were harmed in the making of this quote,".center(cols) + 
          Colors.RESET)
    print(Colors.DIM + 
          "but several neurotic comedians were inspired.".center(cols) + 
          Colors.RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Colors.YELLOW + 
              "Even your interruption is meaningless in the grand tapestry of existence." + 
              Colors.RESET)
    except Exception as e:
        print(f"\n{Colors.RED}Motherhood is unrated... also, an error occurred: {e}{Colors.RESET}")