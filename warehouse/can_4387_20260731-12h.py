"""
Campbell's Soup Can #4387
Produced: 2026-07-31 12:16:44
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen-style existential crisis in technicolor."""

import sys
import time
import random
import textwrap
from itertools import cycle

# ANSI color codes
class Color:
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
    BLINK = '\033[5m'
    RESET = '\033[0m'

# The quote - pure neurotic existentialism
QUOTE = (
    "I'm not afraid of death—I just don't want to be there "
    "when it happens... especially if it's going to be "
    "in the company of my in-laws."
)

# Color schemes to cycle through
COLORS = [Color.RED, Color.YELLOW, Color.CYAN, Color.MAGENTA]
DIM_COLORS = [Color.DIM + Color.RED, Color.DIM + Color.YELLOW, 
              Color.DIM + Color.CYAN, Color.DIM + Color.MAGENTA]

def print_slow(text, delay=0.03):
    """Print text character by character with a typewriter effect."""
    color = random.choice(COLORS)
    for char in text:
        print(f"{color}{char}", end='', flush=True)
        if char in '.?!':
            time.sleep(delay * 3)
        elif char == ',':
            time.sleep(delay * 2)
        elif char == '-':
            time.sleep(delay * 1.5)
        else:
            time.sleep(delay * random.uniform(0.5, 1.5))
    print(Color.RESET)

def draw_box():
    """Draw an animated ASCII art box frame."""
    box_chars_top = "╔═══════ Woody Allen's Brain ═══════╗"
    width = len(box_chars_top)
    
    # Top border with color cycling
    print("\n")
    colors_cycle = cycle([Color.MAGENTA, Color.CYAN, Color.YELLOW, Color.RED])
    
    top_line = f"╔{'═' * (width-2)}╗"
    for char in top_line:
        c = next(colors_cycle)
        print(f"{c}{char}", end='', flush=True)
        time.sleep(0.01)
    print()
    
    # Side borders for the title area
    title_line = "║" + f" {'█' * (width-10)} " + "╗"
    for char in title_line:
        c = next(colors_cycle)
        print(f"{c}{char}", end='', flush=True)
        time.sleep(0.005)
    print()
    
    return width

def draw_neurons():
    """Draw little ASCII neurons dancing around."""
    neurons = ['*', '·', '∘', '◦', '•', '‣', '⁂']
    width = 70
    for _ in range(3):
        line = ""
        for i in range(width):
            if random.random() < 0.1:
                char = random.choice(neurons)
                color = random.choice(DIM_COLORS)
                line += f"{color}{char}{Color.RESET}"
            else:
                line += " "
        print(line)
        time.sleep(0.3)

def print_quote_centered():
    """Print the quote with dramatic flair."""
    # Wrap the quote to fit nicely
    wrapped = textwrap.wrap(QUOTE, width=60)
    
    # Print each line with different styling
    line_styles = [
        (Color.BOLD + Color.YELLOW, Color.BOLD + Color.RED),
        (Color.ITALIC + Color.CYAN, Color.ITALIC + Color.MAGENTA),
        (Color.BOLD + Color.GREEN, Color.BOLD + Color.BLUE),
    ]
    
    for i, line in enumerate(wrapped):
        padding = " " * ((66 - len(line)) // 2)
        
        # Alternate between printing styles
        color1, color2 = line_styles[i % len(line_styles)]
        
        # Print the line slowly
        print(f"{padding}{color1}", end='', flush=True)
        for char in line:
            print(char, end='', flush=True)
            if char in '.,!?-':
                time.sleep(0.1)
            else:
                time.sleep(0.02)
        
        # Add some trailing punctuation animation
        if line.endswith('.'):
            time.sleep(0.2)
            print(f"{color2}•", end='', flush=True)
            time.sleep(0.2)
            print(f"{color1}•", end='', flush=True)
        
        print()
        time.sleep(0.1)

def draw_coffee_cup():
    """Draw an existential coffee cup."""
    cup = [
        "        (  )",
        "      (    )",
        "     (  ☕  )",
        "      (____)",
        "        ||||",
        "        ||||",
    ]
    colors_cycle = cycle([Color.YELLOW, Color.CYAN, Color.MAGENTA])
    for line in cup:
        c = next(colors_cycle)
        print(f"{c}{line.center(70)}{Color.RESET}")
        time.sleep(0.05)

def main():
    """Main function to orchestrate the neurotic display."""
    print("\033[2J\033[H")  # Clear screen
    time.sleep(0.5)
    
    # Title with flair
    title = "ANXIETY-FUELED PHILOSOPHY"
    subtitle = "A Brief Moment of Existential Dread"
    
    for i, char in enumerate(title):
        color = Color.MAGENTA if i % 2 == 0 else Color.CYAN
        print(f"{color}{char}{Color.RESET}", end='', flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.3)
    
    for i, char in enumerate(subtitle):
        color = Color.YELLOW if i % 3 == 0 else Color.DIM + Color.WHITE
        print(f"{color}{char}{Color.RESET}", end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.5)
    
    # Draw the box
    width = draw_box()
    time.sleep(0.3)
    
    # Draw dancing neurons
    draw_neurons()
    time.sleep(0.3)
    
    # Print the coffee cup of existential dread
    draw_coffee_cup()
    time.sleep(0.5)
    
    # Print the quote
    print_quote_centered()
    time.sleep(0.7)
    
    # Draw bottom border
    bottom_line = f"╚{'═' * 64}╝"
    colors_cycle = cycle([Color.RED, Color.YELLOW, Color.CYAN, Color.MAGENTA])
    for char in bottom_line:
        c = next(colors_cycle)
        print(f"{c}{char}", end='', flush=True)
        time.sleep(0.01)
    print()
    
    # Final flair
    time.sleep(0.5)
    final = "— Woody Allen (probably not really, but who's to know?)"
    print(f"\n{Color.DIM + Color.WHITE}{final.center(70)}{Color.RESET}")
    
    # Blinking dot for effect
    for _ in range(5):
        print(f"{Color.RED}.{Color.RESET}", end='', flush=True)
        time.sleep(0.3)
        print(f"{Color.YELLOW}.{Color.RESET}", end='', flush=True)
        time.sleep(0.3)
    print()

if __name__ == "__main__":
    main()