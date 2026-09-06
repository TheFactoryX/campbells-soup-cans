"""
Campbell's Soup Can #4913
Produced: 2026-09-06 14:11:10
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

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
    BLINK = '\033[5m'
    RESET = '\033[0m'
    BG_RED = '\033[41m'
    BG_BLUE = '\033[44m'
    BG_WHITE = '\033[47m'

def create_box(width, height, color):
    return color + '+' + '-' * (width - 2) + '+' + Colors.RESET

def create_side(height, color):
    return color + '|' + ' ' * (height - 2) + '|' + Colors.RESET

def type_writer(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        if char == '\n':
            time.sleep(0.1)

def main():
    os_type = []
    
    quote = """I'm not a vegetarian because of cruelty to animals. 
I'm a vegetarian because I can't afford the meat, and 
the vegetables are trying to kill me with their tiny little eyes."""
    
    box_width = 70
    box_height = 12
    
    lines = quote.strip().split('\n')
    
    top_border = create_box(box_width, box_height, Colors.CYAN)
    
    print(Colors.YELLOW + "╔" + "═" * (box_width - 2) + "╗" + Colors.RESET)
    
    mid_width = box_width - 4
    
    print(Colors.MAGENTA + "║" + " " * mid_width + "║" + Colors.RESET)
    
    type_writer(Colors.GREEN + "║" + Colors.BOLD, 0.01)
    
    yoffset = 0
    for i, line in enumerate(lines):
        padding = (mid_width - len(line)) // 2
        left_pad = ' ' * padding
        right_pad = ' ' * (mid_width - len(line) - padding)
        
        sys.stdout.write(Colors.GREEN + "║" + Colors.BOLD)
        sys.stdout.write(left_pad)
        sys.stdout.write(Colors.RED)
        sys.stdout.write(line)
        sys.stdout.write(Colors.GREEN)
        sys.stdout.write(right_pad)
        sys.stdout.write(Colors.GREEN + "║" + Colors.RESET + "\n")
        
        sys.stdout.flush()
        time.sleep(0.15)
    
    print(Colors.MAGENTA + "║" + " " * mid_width + "║" + Colors.RESET)
    
    print(Colors.YELLOW + "╚" + "═" * (box_width - 2) + "╝" + Colors.RESET)
    
    print()
    
    author_line = Colors.BLUE + "—— a.k.a. the existential crisis whisperer"
    type_writer(author_line, 0.02)
    
    print()
    print()
    
    warning = Colors.RED + Colors.BLINK + "WARNING: Philosophical anxiety modules " + Colors.RESET + Colors.RED + Colors.BLINK + "may activate at any moment." + Colors.RESET
    for char in warning:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    print()
    print()
    
    print(Colors.CYAN + "[" + Colors.RESET, end='')
    status = "Loading depression... "
    for char in status:
        print(Colors.RED + char, end='', flush=True)
        time.sleep(0.03)
    
    for i in range(10):
        if i < 5:
            print(Colors.RED + "█", end='', flush=True)
        else:
            print(Colors.RED + "░", end='', flush=True)
        time.sleep(0.05)
    
    print(Colors.CYAN + "]" + Colors.RESET)
    print()
    
    print(Colors.YELLOW + "System status: 99% existential dread, 1% hope, 0% functional." + Colors.RESET)

if __name__ == "__main__":
    main()