"""
Campbell's Soup Can #629
Produced: 2025-11-30 19:26:10
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

# ANSI color codes
colors = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bright_red': '\033[91;1m',
    'bright_green': '\033[92;1m',
    'bright_yellow': '\033[93;1m',
    'bright_blue': '\033[94;1m',
    'bright_magenta': '\033[95;1m',
    'bright_cyan': '\033[96;1m',
    'bright_white': '\033[97;1m'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, color='white', delay=0.03, end_with_newline=True):
    """Simulate typing effect with color"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if end_with_newline:
        sys.stdout.write(colors['reset'] + '\n')
    else:
        sys.stdout.write(colors['reset'])

def draw_box(text, width=70, color='yellow', animate=False):
    """Draw a simple ASCII box around text with optional animation"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    # Adjust width if needed
    box_width = max(width, max_len + 4)
    
    # Top border
    if animate:
        for i in range(box_width):
            sys.stdout.write(color + '+' if i == 0 or i == box_width-1 else color + '-')
            sys.stdout.flush()
            time.sleep(0.01)
        sys.stdout.write('\n')
    else:
        type_effect(color + '+' + '-' * (box_width - 2) + '+', delay=0.01)
    
    # Text lines with padding
    for line in lines:
        padding = (box_width - 4 - len(line)) * ' '
        if animate:
            sys.stdout.write(color + '|' + ' ')
            sys.stdout.flush()
            type_effect(line, delay=0.01)
            sys.stdout.write(padding + ' ' + color + '|')
            sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            type_effect(color + '|' + ' ' + line + padding + ' |', delay=0.01)
    
    # Bottom border
    if animate:
        for i in range(box_width):
            sys.stdout.write(color + '+' if i == 0 or i == box_width-1 else color + '-')
            sys.stdout.flush()
            time.sleep(0.01)
        sys.stdout.write('\n')
    else:
        type_effect(color + '+' + '-' * (box_width - 2) + '+', delay=0.01)

def blink_cursor(times=5, delay=0.3):
    """Create a blinking cursor effect"""
    for _ in range(times):
        sys.stdout.write(colors['bright_white'] + '_' + colors['reset'])
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(delay)

def main():
    clear_screen()
    
    # Title with blinking cursor
    type_effect(colors['bright_cyan'], delay=0.01)
    type_effect("WOODY ALLEN ON LIFE, DEATH, AND EVERYTHING IN BETWEEN", delay=0.02)
    type_effect(colors['reset'], delay=0.01)
    blink_cursor(times=3)
    
    # Add some space
    print("\n\n")
    
    # The quote with different colors for emphasis
    quote = "I've spent my entire life searching for the meaning of existence, "
    quote += "only to discover that the only certainty is that I'll never find it—"
    quote += "and that I'll probably be late for my own funeral."
    
    # Display the quote in typewriter style with color variations and animation
    type_effect(colors['bright_white'], delay=0.01)
    print()
    draw_box(quote, width=80, color=colors['bright_yellow'], animate=True)
    print()
    
    # Some additional commentary after a pause
    time.sleep(1)
    print("\n")
    type_effect(colors['blue'], delay=0.02)
    type_effect("— Woody Allen, probably worrying about something right now.", delay=0.03)
    type_effect(colors['reset'], delay=0.01)
    
    # Add a final thought with a dramatic pause
    time.sleep(1)
    print("\n")
    type_effect(colors['red'], delay=0.01)
    type_effect("P.S. If you're not worried, you're not paying attention.", delay=0.03)
    type_effect(colors['reset'], delay=0.01)
    blink_cursor()

if __name__ == "__main__":
    main()