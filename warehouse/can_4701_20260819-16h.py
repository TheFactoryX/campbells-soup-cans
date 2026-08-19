"""
Campbell's Soup Can #4701
Produced: 2026-08-19 16:46:40
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

# ANSI escape codes
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

# The quote
QUOTE = "I told my psychiatrist I've been hearing voices. He said, 'Good, that means you're finally listening to someone smarter than yourself.'"

WOODY_ART = r"""
        \   /
         \ /
      .--' '--.
     /   ^ ^   \
    |  (o) (o)  |    
    |     ^     |    
     \  \___/  /
      '.___.'
        | |
       /___\
"""

def clear_screen():
    print('\033[2J\033[H', end='')

def typewriter(text, color=WHITE, delay=0.03, newline=True):
    for char in text:
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def print_boxed_quote():
    lines = QUOTE.split('. ')
    max_len = max(len(line) for line in lines) + 4
    
    # Top border
    print(f'{BRIGHT_CYAN}╔{"═" * (max_len)}╗{RESET}')
    
    # Empty line
    print(f'{BRIGHT_CYAN}║{" " * (max_len)}║{RESET}')
    
    # Quote lines with colors
    colors = [BRIGHT_YELLOW, BRIGHT_GREEN, BRIGHT_MAGENTA, BRIGHT_CYAN]
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        padding = max_len - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f'{BRIGHT_CYAN}║{RESET}{" " * left_pad}{color}{ITALIC}{line}.{RESET}{" " * right_pad}{BRIGHT_CYAN}║{RESET}')
    
    # Attribution line
    attrib = "— Woody Allen (probably)"
    padding = max_len - len(attrib) - 2
    left_pad = padding // 2
    right_pad = padding - left_pad
    print(f'{BRIGHT_CYAN}║{" " * left_pad}{BRIGHT_BLACK}{DIM}{attrib}{RESET}{" " * right_pad}{BRIGHT_CYAN}║{RESET}')
    
    # Empty line
    print(f'{BRIGHT_CYAN}║{" " * (max_len)}║{RESET}')
    
    # Bottom border
    print(f'{BRIGHT_CYAN}╚{"═" * (max_len)}╝{RESET}')

def animate_woody():
    frames = [
        r"""
        \   /
         \ /
      .--' '--.
     /   ^ ^   \
    |  (o) (o)  |    
    |     ^     |    
     \  \___/  /
      '.___.'
        | |
       /___\
""",
        r"""
        \   /
         \ /
      .--' '--.
     /   ^ ^   \
    |  (-) (-)  |    
    |     ^     |    
     \  \___/  /
      '.___.'
        | |
       /___\
""",
        r"""
        \   /
         \ /
      .--' '--.
     /   ^ ^   \
    |  (o) (o)  |    
    |     ~     |    
     \  \___/  /
      '.___.'
        | |
       /___\
""",
    ]
    for _ in range(3):
        for frame in frames:
            print('\033[H', end='')
            print(f'{BRIGHT_YELLOW}{frame}{RESET}')
            time.sleep(0.3)

def main():
    clear_screen()
    
    # Print title
    print(f'\n{BRIGHT_MAGENTA}{BOLD}{"=" * 60}{RESET}')
    print(f'{BRIGHT_MAGENTA}{BOLD}    WOODY ALLEN PHILOSOPHY GENERATOR v1.0{RESET}')
    print(f'{BRIGHT_MAGENTA}{BOLD}    "Neuroses are just thoughts with better marketing" {RESET}')
    print(f'{BRIGHT_MAGENTA}{BOLD}{"=" * 60}{RESET}\n')
    
    # Animate Woody
    print(f'{BRIGHT_YELLOW}{WOODY_ART}{RESET}')
    time.sleep(0.5)
    
    # Typewriter intro
    typewriter(f'{BRIGHT_WHITE}{DIM}Generating existential crisis...{RESET}', BRIGHT_CYAN, 0.02)
    time.sleep(0.3)
    typewriter(f'{BRIGHT_WHITE}{DIM}Consulting my analyst...{RESET}', BRIGHT_GREEN, 0.02)
    time.sleep(0.3)
    typewriter(f'{BRIGHT_WHITE}{DIM}Checking for parking tickets...{RESET}', BRIGHT_YELLOW, 0.02)
    time.sleep(0.5)
    
    print()
    
    # Print the boxed quote with typewriter effect per line
    lines = QUOTE.split('. ')
    max_len = max(len(line) for line in lines) + 4
    
    print(f'{BRIGHT_CYAN}╔{"═" * (max_len)}╗{RESET}')
    print(f'{BRIGHT_CYAN}║{" " * (max_len)}║{RESET}')
    
    colors = [BRIGHT_YELLOW, BRIGHT_GREEN, BRIGHT_MAGENTA, BRIGHT_CYAN]
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        padding = max_len - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        sys.stdout.write(f'{BRIGHT_CYAN}║{RESET}{" " * left_pad}{color}{ITALIC}')
        sys.stdout.flush()
        for char in line + '.':
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        print(f'{RESET}{" " * right_pad}{BRIGHT_CYAN}║{RESET}')
        time.sleep(0.15)
    
    # Attribution
    attrib = "— Woody Allen (probably)"
    padding = max_len - len(attrib) - 2
    left_pad = padding // 2
    right_pad = padding - left_pad
    print(f'{BRIGHT_CYAN}║{" " * left_pad}{BRIGHT_BLACK}{DIM}{attrib}{RESET}{" " * right_pad}{BRIGHT_CYAN}║{RESET}')
    
    print(f'{BRIGHT_CYAN}║{" " * (max_len)}║{RESET}')
    print(f'{BRIGHT_CYAN}╚{"═" * (max_len)}╝{RESET}')
    
    print()
    
    # Final neurotic thought
    thoughts = [
        "Now if you'll excuse me, I need to go check if I left the stove on... in 1973.",
        "My therapist says I have a preoccupation with death. I told him, 'Doc, at my age, it's not a preoccupation—it's a scheduling conflict.'",
        "I'd make a joke about mortality, but I'm saving my best material for the afterlife. Assuming there's wifi.",
    ]
    
    typewriter(f'{BRIGHT_BLACK}{DIM}{random.choice(thoughts)}{RESET}', BRIGHT_BLACK, 0.02)
    print()
    print(f'{BRIGHT_MAGENTA}{"=" * 60}{RESET}\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{RED}Interrupted. Typical. Even my code has commitment issues.{RESET}')
        sys.exit(0)