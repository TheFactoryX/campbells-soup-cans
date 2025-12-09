"""
Campbell's Soup Can #808
Produced: 2025-12-09 03:58:14
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'blink': '\033[5m'
}

def print_with_typewriter(text, delay=0.05):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_oscars_worries():
    """Draw a neurotic Oscar statue"""
    art = f"""
{COLORS['yellow']}        _____{COLORS['reset']}
{COLORS['yellow']}      .'     '.{COLORS['reset']}
{COLORS['yellow']}     /   . .   \\{COLORS['reset']}
{COLORS['yellow']}    |    ___    |{COLORS['reset']}
{COLORS['yellow']}    |   |___|   |{COLORS['reset']}
{COLORS['yellow']}     \\   ___   /{COLORS['reset']}
{COLORS['yellow']}      '. ___ .'  {COLORS['blink']}{COLORS['red']}← obsessing{COLORS['reset']}
{COLORS['yellow']}        '---'{COLORS['reset']}
"""
    print(art)

def main():
    # Clear screen and set background
    print('\033[2J\033[H', end='')
    
    # Header with anxiety
    print(f"{COLORS['blink']}{COLORS['red']}⚠{COLORS['reset']} ", end='')
    print_with_typewriter(f"{COLORS['bold']}{COLORS['magenta']}WOODY ALLEN'S DAILY EXISTENTIAL CRISIS{COLORS['reset']}", 0.08)
    print(f"{COLORS['blink']}{COLORS['red']}⚠{COLORS['reset']} ", end='')
    print_with_typewriter("Generated because therapy is expensive", 0.06)
    print()
    
    # Draw the anxious Oscar
    draw_oscars_worries()
    
    # The quote with maximum neurosis
    quote = "I don't believe in an afterlife, although I am bringing a change of underwear just in case."
    
    # Print quote with dramatic pauses
    print_with_typewriter(f"{COLORS['cyan']}— Woody Allen, probably during therapy{COLORS['reset']}", 0.07)
    print()
    
    # Box around the quote
    box_width = 60
    print(f"{COLORS['green']}╔{'═' * (box_width-2)}╗{COLORS['reset']}")
    
    # Split quote into lines for the box
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + word) + 1 <= box_width - 4:  # 4 for padding
            current_line += (" " + word) if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    for line in lines:
        padding = box_width - 4 - len(line)
        print(f"{COLORS['green']}║ {COLORS['yellow']}{line}{COLORS['green']}{' ' * padding} ║{COLORS['reset']}")
    
    print(f"{COLORS['green']}╚{'═' * (box_width-2)}╝{COLORS['reset']}")
    
    print()
    
    # Add some Woody-Allen-style footnotes
    footnotes = [
        "Footnote 1: The underwear is 100% cotton. Breathable, like my relationship with my mother.",
        "Footnote 2: I've been to 47 therapists. They all have the same look. The 'I've heard this before but I'll bill you anyway' look.",
        "Footnote 3: Existential dread: not covered by my HMO."
    ]
    
    for i, note in enumerate(footnotes):
        time.sleep(0.8)
        print(f"{COLORS['blue']}[Note {i+1}]{COLORS['reset']} ", end='')
        print_with_typewriter(note, 0.03)
    
    print()
    print_with_typewriter(f"{COLORS['bold']}{COLORS['cyan']}The universe is indifferent, but at least this code runs.{COLORS['reset']}", 0.05)

if __name__ == "__main__":
    main()