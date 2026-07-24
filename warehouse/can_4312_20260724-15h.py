"""
Campbell's Soup Can #4312
Produced: 2026-07-24 15:44:55
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

WOODY_QUOTE = (
    "I took a speed-reading course and read War and Peace in twenty minutes. "
    "It involves Russia."
)

WOODY_FACE = r"""
        \   /
         \ /
      .--.--.
     /  o o  \
    |   __    |
     \ \__/  /
      `----' 
"""

THOUGHT_BUBBLE = r"""
     .-'-.
    /     \
   |  {:^15}  |
    \     /
     `-.-'
"""

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

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

def pulse_color(text, times=3):
    colors = [BRIGHT_RED, BRIGHT_YELLOW, BRIGHT_GREEN, BRIGHT_CYAN, BRIGHT_BLUE, BRIGHT_MAGENTA]
    for _ in range(times):
        for color in colors:
            move_cursor(1, 1)
            print(f'{color}{text}{RESET}', end='', flush=True)
            time.sleep(0.08)

def draw_box(text, width=60, color=CYAN, bg=BG_BLACK):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max(width, max_len + 4)
    
    top = f'{color}╔{"═" * (box_width - 2)}╗{RESET}'
    bottom = f'{color}╚{"═" * (box_width - 2)}╝{RESET}'
    
    print(top)
    for line in lines:
        padding = box_width - len(line) - 4
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f'{color}║{RESET}{" " * left_pad}{bg}{WHITE}{line}{RESET}{" " * right_pad}{color}║{RESET}')
    print(bottom)

def woody_intro_animation():
    clear_screen()
    hide_cursor()
    
    # Title animation
    title = "WOODY ALLEN WISDOM GENERATOR v1.0"
    for i in range(len(title) + 1):
        clear_screen()
        partial = title[:i]
        print(f'\n\n{CYAN}{BOLD}{partial}{RESET}')
        time.sleep(0.05)
    
    time.sleep(0.3)
    
    # Face appears
    for line in WOODY_FACE.strip().split('\n'):
        print(f'{YELLOW}{line}{RESET}')
        time.sleep(0.15)
    
    time.sleep(0.5)
    
    # Neurotic muttering
    mutters = [
        "My analyst says I have a preoccupation with death...",
        "Also with life. And lunch. Mostly lunch.",
        "Wait, did I leave the stove on?",
        "Why am I telling you this? You're a computer program.",
        "Great, now I'm having an existential crisis with a script.",
    ]
    
    for mutter in mutters:
        clear_screen()
        for line in WOODY_FACE.strip().split('\n'):
            print(f'{YELLOW}{line}{RESET}')
        print()
        typewriter(mutter, BRIGHT_BLACK, 0.02)
        time.sleep(0.8)
    
    clear_screen()
    for line in WOODY_FACE.strip().split('\n'):
        print(f'{YELLOW}{line}{RESET}')
    print()
    typewriter("Okay, okay... generating profound neurotic insight...", GREEN, 0.02)
    time.sleep(0.5)
    
    # Loading bar
    print()
    print(f'{CYAN}Processing existential dread...{RESET}')
    bar_width = 40
    for i in range(bar_width + 1):
        bar = '█' * i + '░' * (bar_width - i)
        percent = int(i / bar_width * 100)
        move_cursor(12, 1)
        print(f'{MAGENTA}[{bar}] {percent}%{RESET}', end='', flush=True)
        time.sleep(random.uniform(0.02, 0.08))
    
    print()
    time.sleep(0.3)
    typewriter("Analyzing mortality statistics...", BRIGHT_BLACK, 0.02)
    time.sleep(0.3)
    typewriter("Cross-referencing with psychoanalytic theory...", BRIGHT_BLACK, 0.02)
    time.sleep(0.3)
    typewriter("Factoring in mother's guilt trips...", BRIGHT_BLACK, 0.02)
    time.sleep(0.5)
    
    clear_screen()

def display_quote():
    # Final presentation
    print(f'\n{MAGENTA}{BOLD}{"=" * 70}{RESET}')
    print(f'{CYAN}{BOLD}           A WOODY ALLEN ORIGINAL (probably){RESET}')
    print(f'{MAGENTA}{BOLD}{"=" * 70}{RESET}\n')
    
    # Quote in a fancy box
    quote_lines = [
        '"I took a speed-reading course',
        ' and read War and Peace',
        ' in twenty minutes.',
        ' It involves Russia."'
    ]
    
    print(f'{YELLOW}{WOODY_FACE}{RESET}')
    print()
    
    # Animated quote reveal
    for i, line in enumerate(quote_lines):
        # Typewriter each line
        for j, char in enumerate(line):
            print(f'{BRIGHT_WHITE}{BOLD}{char}{RESET}', end='', flush=True)
            time.sleep(0.025)
        print()
        time.sleep(0.15)
    
    print()
    
    # Attribution with flair
    attributions = [
        ("— Woody Allen", BRIGHT_YELLOW),
        ("(allegedly, don't sue me)", BRIGHT_BLACK),
    ]
    
    for text, color in attributions:
        typewriter(f'{" " * 25}{color}{ITALIC}{text}{RESET}', color, 0.02)
    
    print()
    print(f'{MAGENTA}{BOLD}{"=" * 70}{RESET}')
    
    # Philosophical footnote
    print()
    footnotes = [
        "💭 Existential footnote: Speed-reading Tolstoy defeats the purpose,",
        "   much like rushing through life to get to the end faster.",
        "   The Russians knew suffering; we just have streaming services.",
        "",
        f'{DIM}Quote generated at {time.strftime("%H:%M:%S")} — your mortality unchanged.{RESET}',
    ]
    
    for footnote in footnotes:
        typewriter(footnote, CYAN if '💭' in footnote else BRIGHT_BLACK, 0.015)
    
    print()

def sparkle_effect():
    """Add some sparkle particles around the quote"""
    sparkles = ['✦', '✧', '★', '☆', '✩', '✪', '✫', '✬', '✭', '✮', '✯', '✰']
    for _ in range(20):
        x = random.randint(5, 65)
        y = random.randint(5, 20)
        sparkle = random.choice(sparkles)
        color = random.choice([YELLOW, CYAN, MAGENTA, BRIGHT_WHITE])
        move_cursor(y, x)
        print(f'{color}{sparkle}{RESET}', end='', flush=True)
        time.sleep(0.03)
    move_cursor(25, 1)

def main():
    try:
        woody_intro_animation()
        display_quote()
        sparkle_effect()
        show_cursor()
        print(f'\n{BRIGHT_GREEN}Press Enter to return to your regularly scheduled anxiety...{RESET}')
        input()
    except KeyboardInterrupt:
        show_cursor()
        print(f'\n\n{YELLOW}Interrupted. Typical. Even my code has commitment issues.{RESET}')
    finally:
        show_cursor()

if __name__ == '__main__':
    main()