"""
Campbell's Soup Can #4738
Produced: 2026-08-21 07:56:53
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
GRAY = '\033[90m'
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

# Woody Allen's original quote for this program
QUOTE = "My neuroses have neuroses. It's a whole ecosystem of anxiety in here — and the rent is outrageous."
ATTRIBUTION = "— Woody Allen (probably)"

# ASCII art frames
FRAMES = [
    # Frame 1: Simple
    ("┌", "┐", "└", "┘", "─", "│"),
    # Frame 2: Double
    ("╔", "╗", "╚", "╝", "═", "║"),
    # Frame 3: Rounded
    ("╭", "╮", "╰", "╯", "─", "│"),
    # Frame 4: Heavy
    ("┏", "┓", "┗", "┛", "━", "┃"),
]

WOODY_FACE = r"""
      __
     /  \
    | @ @ |    *sigh*
    |  >  |
     \ __ /
      |  |
     _|  |_
    (______)
"""

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

def rainbow_text(text):
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    result = ""
    for i, char in enumerate(text):
        if char != ' ':
            result += f"{colors[i % len(colors)]}{char}{RESET}"
        else:
            result += char
    return result

def pulse_color(text, colors, cycles=3):
    for _ in range(cycles):
        for color in colors:
            move_cursor(0, 0)
            print(f'{color}{text}{RESET}', end='', flush=True)
            time.sleep(0.15)

def draw_box(content_lines, frame_style=1, padding=2, color=CYAN):
    tl, tr, bl, br, h, v = FRAMES[frame_style]
    max_len = max(len(line) for line in content_lines)
    width = max_len + padding * 2
    
    top = f"{color}{tl}{h * width}{tr}{RESET}"
    bottom = f"{color}{bl}{h * width}{br}{RESET}"
    
    lines = [top]
    for line in content_lines:
        padded = line.center(max_len)
        lines.append(f"{color}{v}{RESET} {' ' * padding}{padded}{' ' * padding} {color}{v}{RESET}")
    lines.append(bottom)
    return '\n'.join(lines)

def animate_entrance():
    clear_screen()
    hide_cursor()
    
    # Phase 1: Face appears
    print(BRIGHT_YELLOW)
    for i, line in enumerate(WOODY_FACE.strip().split('\n')):
        move_cursor(i + 3, 5)
        print(line)
        time.sleep(0.15)
    
    time.sleep(0.8)
    
    # Phase 2: Thought bubble grows
    bubble_lines = [
        "  .....................  ",
        " .                   . ",
        ".                     .",
        "|                       |",
        "|                       |",
        "|                       |",
        "|                       |",
        "|                       |",
        "|                       |",
        ".                     .",
        " .                   . ",
        "  '''''''''''''''''''  "
    ]
    
    for frame in range(len(bubble_lines)):
        clear_screen()
        print(BRIGHT_YELLOW)
        for i, line in enumerate(WOODY_FACE.strip().split('\n')):
            move_cursor(i + 3, 5)
            print(line)
        
        print(BRIGHT_CYAN)
        for i in range(frame + 1):
            move_cursor(i + 2, 22)
            print(bubble_lines[i])
        time.sleep(0.08)
    
    time.sleep(0.5)
    
    # Phase 3: Text types into bubble
    words = QUOTE.split()
    line1 = " ".join(words[:8])
    line2 = " ".join(words[8:])
    
    for i, char in enumerate(line1):
        move_cursor(5, 26 + i)
        print(f"{WHITE}{char}{RESET}", end='', flush=True)
        time.sleep(0.02)
    
    for i, char in enumerate(line2):
        move_cursor(6, 26 + i)
        print(f"{WHITE}{char}{RESET}", end='', flush=True)
        time.sleep(0.02)
    
    # Attribution
    time.sleep(0.3)
    for i, char in enumerate(ATTRIBUTION):
        move_cursor(9, 30 + i)
        print(f"{GRAY}{ITALIC}{char}{RESET}", end='', flush=True)
        time.sleep(0.02)
    
    time.sleep(1.5)
    show_cursor()

def animated_finale():
    # Final stylized display with effects
    clear_screen()
    
    # Build the final quote with styling
    styled_lines = [
        f"{BRIGHT_YELLOW}{BOLD}WOODY ALLEN SIMULATOR v3.14{RESET}",
        f"{GRAY}{'─' * 50}{RESET}",
        "",
        f"{ITALIC}{CYAN}\"My neuroses have neuroses.{RESET}",
        f"{ITALIC}{CYAN}It's a whole ecosystem of anxiety{RESET}",
        f"{ITALIC}{CYAN}in here — and the rent is outrageous.\"{RESET}",
        "",
        f"{GRAY}{ITALIGN}— Woody Allen (probably){RESET}",
        "",
        f"{GRAY}{'─' * 50}{RESET}",
    ]
    
    # Print with fade-in effect
    for i, line in enumerate(styled_lines):
        move_cursor(i + 3, 10)
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.005)
        time.sleep(0.1)
    
    # Add Woody face at bottom
    move_cursor(14, 12)
    print(BRIGHT_YELLOW + WOODY_FACE + RESET)
    
    # Pulsing thought
    pulse_colors = [BRIGHT_RED, BRIGHT_YELLOW, BRIGHT_GREEN, BRIGHT_CYAN, BRIGHT_BLUE, BRIGHT_MAGENTA]
    thought = " *existential dread intensifies* "
    move_cursor(22, 15)
    
    for _ in range(6):
        for color in pulse_colors:
            move_cursor(22, 15)
            print(f"{color}{BLINK}{thought}{RESET}", end='', flush=True)
            time.sleep(0.2)
    
    move_cursor(22, 15)
    print(f"{GRAY}{thought}{RESET}")
    
    # Final message
    move_cursor(24, 10)
    typewriter("Press Ctrl+C to accept the absurdity of existence...", GREEN, 0.02)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clear_screen()
        show_cursor()
        print(f"\n{BRIGHT_GREEN}Thank you for your anxiety. It has been noted.{RESET}\n")
        sys.exit(0)

def main():
    try:
        animate_entrance()
        animated_finale()
    except KeyboardInterrupt:
        clear_screen()
        show_cursor()
        print(f"\n{GRAY}Aborted. The void thanks you for your time.{RESET}\n")
    except Exception as e:
        show_cursor()
        print(f"\n{RED}Error: {e}{RESET}\n")

if __name__ == "__main__":
    main()