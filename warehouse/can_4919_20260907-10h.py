"""
Campbell's Soup Can #4919
Produced: 2026-09-07 10:19:43
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'

# Colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Bright colors
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

# Backgrounds
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=WHITE, delay=0.03, newline=True):
    for char in text:
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def woody_face():
    """ASCII art of a neurotic Woody Allen face"""
    return [
        f"{BRIGHT_YELLOW}       .--.      {RESET}",
        f"{BRIGHT_YELLOW}      / .. \\     {RESET}",
        f"{BRIGHT_YELLOW}     |  __  |    {RESET}",
        f"{BRIGHT_YELLOW}     | |  | |    {RESET}",
        f"{BRIGHT_YELLOW}      \\ '__' /    {RESET}",
        f"{BRIGHT_YELLOW}       '.__.'     {RESET}",
    ]

def glasses():
    return [
        f"{BRIGHT_BLACK}    ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄ {RESET}",
        f"{BRIGHT_BLACK}   █       ██       █{RESET}",
        f"{BRIGHT_BLACK}   █  ▄▄▄  ██  ▄▄▄  █{RESET}",
        f"{BRIGHT_BLACK}   █  ███  ██  ███  █{RESET}",
        f"{BRIGHT_BLACK}   █       ██       █{RESET}",
        f"{BRIGHT_BLACK}   ▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀ {RESET}",
    ]

def draw_box(lines, padding=2, border_color=CYAN, title=None):
    max_len = max(len(line.replace('\033', '').replace('[0m', '').replace('[1m', '').replace('[2m', '').replace('[3m', '').replace('[4m', '').replace('[5m', '').replace('[30m', '').replace('[31m', '').replace('[32m', '').replace('[33m', '').replace('[34m', '').replace('[35m', '').replace('[36m', '').replace('[37m', '').replace('[90m', '').replace('[91m', '').replace('[92m', '').replace('[93m', '').replace('[94m', '').replace('[95m', '').replace('[96m', '').replace('[97m', '').replace('[40m', '').replace('[41m', '').replace('[42m', '').replace('[43m', '').replace('[44m', '').replace('[45m', '').replace('[46m', '').replace('[47m', '')) for line in lines)
    width = max_len + padding * 2
    
    # Top border
    if title:
        title_str = f" {title} "
        left = (width - len(title_str)) // 2
        right = width - len(title_str) - left
        print(f"{border_color}╭{'─' * left}{WHITE}{BOLD}{title_str}{RESET}{border_color}{'─' * right}╮{RESET}")
    else:
        print(f"{border_color}╭{'─' * width}╮{RESET}")
    
    # Content lines
    for line in lines:
        # Calculate visible length (strip ANSI)
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        spaces = width - len(clean)
        print(f"{border_color}│{RESET}{' ' * padding}{line}{' ' * spaces}{border_color}│{RESET}")
    
    # Bottom border
    print(f"{border_color}╰{'─' * width}╯{RESET}")

def animated_quote_reveal(quote, author="— Woody Allen (probably)"):
    clear_screen()
    hide_cursor()
    
    try:
        # Phase 1: Neurotic buildup
        print(f"\n{BRIGHT_BLACK}{'='*60}{RESET}")
        typewriter(f"{BRIGHT_BLACK}Initializing existential dread...{RESET}", BRIGHT_BLACK, 0.02)
        time.sleep(0.3)
        typewriter(f"{BRIGHT_BLACK}Calibrating neuroses...{RESET}", BRIGHT_BLACK, 0.02)
        time.sleep(0.3)
        typewriter(f"{BRIGHT_BLACK}Checking if the universe is indifferent...{RESET}", BRIGHT_BLACK, 0.02)
        time.sleep(0.5)
        typewriter(f"{BRIGHT_GREEN}Confirmed. Universe is indifferent.{RESET}", BRIGHT_GREEN, 0.02)
        print(f"{BRIGHT_BLACK}{'='*60}{RESET}\n")
        time.sleep(0.5)
        
        # Phase 2: Show Woody face with glasses
        face = woody_face()
        gl = glasses()
        print(f"{CYAN}{' '*15}WOODY ALLEN QUOTE GENERATOR v1.0{RESET}\n")
        
        for i in range(len(face)):
            print(f"{face[i]}  {gl[i] if i < len(gl) else ''}")
        print()
        
        # Phase 3: Typewriter the quote in a nice box
        quote_lines = []
        words = quote.split(' ')
        current_line = ""
        max_width = 50
        
        for word in words:
            if len(current_line + " " + word) <= max_width:
                current_line += (" " + word) if current_line else word
            else:
                quote_lines.append(current_line)
                current_line = word
        if current_line:
            quote_lines.append(current_line)
        
        # Add author
        quote_lines.append("")
        quote_lines.append(f"{ITALIC}{DIM}{author}{RESET}")
        
        print()
        draw_box(quote_lines, padding=3, border_color=MAGENTA, title=f"{BOLD}PHILOSOPHICAL GEM{RESET}")
        
        # Phase 4: Typewriter effect inside the box (simulated)
        print()
        typewriter(f"{YELLOW}>>> {RESET}{CYAN}", WHITE, 0.01, newline=False)
        for line in quote_lines[:-2]:  # Skip empty and author
            for char in line:
                print(f"{YELLOW}{char}{RESET}", end='', flush=True)
                time.sleep(0.02)
            print()
            time.sleep(0.15)
        
        # Author
        time.sleep(0.3)
        typewriter(f"{BRIGHT_BLACK}{quote_lines[-1]}{RESET}", BRIGHT_BLACK, 0.03)
        
        # Phase 5: Neurotic afterthoughts
        print()
        afterthoughts = [
            f"{DIM}...though I should probably fact-check that with my analyst.{RESET}",
            f"{DIM}Assuming I can afford one this week.{RESET}",
            f"{DIM}My analyst says I have a fear of commitment.{RESET}",
            f"{DIM}I'm committed to disagreeing with him.{RESET}",
        ]
        
        for thought in afterthoughts:
            time.sleep(0.4)
            print(f"  {thought}")
        
        print()
        print(f"{BRIGHT_BLACK}{'='*60}{RESET}")
        typewriter(f"{BRIGHT_BLACK}Existential dread successfully deployed. You're welcome.{RESET}", BRIGHT_BLACK, 0.02)
        print(f"{BRIGHT_BLACK}{'='*60}{RESET}\n")
        
    finally:
        show_cursor()

def main():
    # Original Woody Allen-style quote
    quote = (
        "I told my analyst I have an inferiority complex. "
        "He said, 'Don't worry, you're not that inferior.' "
        "So now I have a superiority complex about my inferiority complex. "
        "Which is progress, technically, but expensive."
    )
    
    animated_quote_reveal(quote)

if __name__ == "__main__":
    main()