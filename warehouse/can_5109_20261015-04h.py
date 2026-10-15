"""
Campbell's Soup Can #5109
Produced: 2026-10-15 04:40:30
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

# ANSI Color Codes
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

# Background colors
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# The quote
QUOTE = "I took a speed-reading course and read War and Peace in twenty minutes. It involves Russia."
AUTHOR = "— Woody Allen (probably)"

# ASCII Art Woody face
WOODY_FACE = [
    "       ▄▄▄▄▄▄▄       ",
    "      █  ▄▄▄  █      ",
    "      █ █   █ █      ",
    "      █  ▀▀▀  █      ",
    "       ▀▀▀▀▀▀▀       ",
    "        ▄▄▄▄▄        ",
    "       █     █       ",
    "      █  ● ●  █      ",
    "      █  ▐▐▐  █      ",
    "      █  ▀▀▀  █      ",
    "       ▀▀▀▀▀▀▀       ",
]

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
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def fade_in(text, color=WHITE, steps=10):
    for i in range(steps + 1):
        intensity = i / steps
        # Simulate fade by printing with increasing brightness
        if intensity < 0.3:
            c = DIM + color
        elif intensity < 0.7:
            c = color
        else:
            c = BOLD + color
        print(f"\r{c}{text}{RESET}", end='', flush=True)
        time.sleep(0.05)
    print()

def draw_box(content_lines, border_color=CYAN, title="", title_color=YELLOW):
    max_len = max(len(line) for line in content_lines)
    if title:
        max_len = max(max_len, len(title) + 4)
    
    top = f"{border_color}╔{'═' * (max_len + 2)}╗{RESET}"
    bottom = f"{border_color}╚{'═' * (max_len + 2)}╝{RESET}"
    
    lines = [top]
    
    if title:
        title_line = f"{border_color}║ {title_color}{title}{border_color} {' ' * (max_len - len(title))} ║{RESET}"
        lines.append(title_line)
        lines.append(f"{border_color}╠{'═' * (max_len + 2)}╣{RESET}")
    
    for line in content_lines:
        padding = max_len - len(line)
        lines.append(f"{border_color}║ {line}{' ' * padding} ║{RESET}")
    
    lines.append(bottom)
    return '\n'.join(lines)

def neurotic_animation():
    """Show Woody's neurotic thoughts scrolling"""
    thoughts = [
        "Wait, did I leave the stove on?",
        "What if the universe is just a simulation?",
        "My therapist says I have a preoccupation with death.",
        "I told him, 'Doc, everyone's preoccupied with death.'",
        "He said, 'Not at 3 AM while checking WebMD.'",
        "Fair point.",
        "Anyway, where was I? Oh right. The quote.",
    ]
    
    print(f"{BRIGHT_BLACK}Neurotic background processes:{RESET}")
    for thought in thoughts:
        dots = random.randint(3, 8)
        print(f"  {DIM}{ITALIC}{thought}{'.' * dots}{RESET}")
        time.sleep(0.4)
    print()

def main():
    hide_cursor()
    try:
        clear_screen()
        
        # Title animation
        print(f"\n{BOLD}{MAGENTA}╔══════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{MAGENTA}║{RESET}  {BOLD}{YELLOW}WOODY ALLEN QUOTE GENERATOR v1.0{RESET}  {BOLD}{MAGENTA}║{RESET}")
        print(f"{BOLD}{MAGENTA}║{RESET}  {ITALIC}{CYAN}Neurotic, Existential, Mildly Hypochondriac{RESET}       {BOLD}{MAGENTA}║{RESET}")
        print(f"{BOLD}{MAGENTA}╚══════════════════════════════════════════════════════════════╝{RESET}\n")
        
        time.sleep(0.5)
        
        # Show Woody face with color cycling
        print(f"{BOLD}{CYAN}Summoning the spirit of neurotic wisdom...{RESET}\n")
        time.sleep(0.3)
        
        for i, line in enumerate(WOODY_FACE):
            colors = [CYAN, BLUE, MAGENTA, YELLOW, GREEN]
            color = colors[i % len(colors)]
            print(f"  {color}{line}{RESET}")
            time.sleep(0.08)
        
        print()
        time.sleep(0.4)
        
        # Neurotic thoughts
        neurotic_animation()
        
        # Build anticipation
        print(f"{YELLOW}{BOLD}Generating quote...{RESET}")
        for _ in range(3):
            for spinner in ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']:
                print(f"\r  {CYAN}{spinner} {DIM}Consulting existential dread database...{RESET}", end='', flush=True)
                time.sleep(0.03)
        print(f"\r  {GREEN}✓{RESET} {DIM}Consulting existential dread database...{RESET}    ")
        time.sleep(0.5)
        
        # The big reveal with typing effect
        print(f"\n{BOLD}{BLUE}┌{'─' * 68}┐{RESET}")
        print(f"{BOLD}{BLUE}│{RESET} {' ' * 68} {BOLD}{BLUE}│{RESET}")
        
        # Type the quote
        quote_words = QUOTE.split(' ')
        typed = ""
        for i, word in enumerate(quote_words):
            typed += word + " "
            # Center it
            padding = (68 - len(typed)) // 2
            line = " " * padding + typed
            print(f"\r{BOLD}{BLUE}│{RESET} {YELLOW}{ITALIC}{line}{' ' * (68 - len(line))} {BOLD}{BLUE}│{RESET}", end='', flush=True)
            time.sleep(0.15)
        
        print()  # Newline after typing
        print(f"{BOLD}{BLUE}│{RESET} {' ' * 68} {BOLD}{BLUE}│{RESET}")
        print(f"{BOLD}{BLUE}│{RESET} {' ' * 20}{MAGENTA}{AUTHOR}{' ' * (48 - len(AUTHOR))} {BOLD}{BLUE}│{RESET}")
        print(f"{BOLD}{BLUE}│{RESET} {' ' * 68} {BOLD}{BLUE}│{RESET}")
        print(f"{BOLD}{BLUE}└{'─' * 68}┘{RESET}")
        
        print()
        
        # Final neurotic commentary
        commentaries = [
            f"{DIM}{ITALIC}...I should really call my mother.{RESET}",
            f"{DIM}{ITALIC}...Wait, is that a symptom?{RESET}",
            f"{DIM}{ITALIC}...Note to self: schedule colonoscopy.{RESET}",
        ]
        
        time.sleep(0.8)
        for commentary in commentaries:
            print(f"  {commentary}")
            time.sleep(0.5)
        
        # Decorative footer
        print()
        print(f"  {BRIGHT_BLACK}{'─' * 60}{RESET}")
        print(f"  {DIM}Quote authenticity: {YELLOW}99.9%{DIM} | Anxiety level: {RED}MAXIMUM{DIM} | Therapy bills: {GREEN}∞{RESET}")
        print(f"  {BRIGHT_BLACK}{'─' * 60}{RESET}")
        print()
        
    finally:
        show_cursor()

if __name__ == "__main__":
    main()