"""
Campbell's Soup Can #5179
Produced: 2026-10-28 16:03:22
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

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

# Woody Allen glasses ASCII
GLASSES = f"""
{CYAN}      ╔════════════╗     ╔════════════╗{RESET}
{CYAN}      ║  {WHITE}██████{CYAN}  ║     ║  {WHITE}██████{CYAN}  ║{RESET}
{CYAN}      ║ {WHITE}████████{CYAN} ║     ║ {WHITE}████████{CYAN} ║{RESET}
{CYAN}      ╚════════════╝     ╚════════════╝{RESET}
{CYAN}           ║                   ║{RESET}
{CYAN}      ═════╝                   ╚═════{RESET}
"""

# Neurotic face
FACE = f"""
{YELLOW}           .--.{RESET}
{YELLOW}          / {CYAN}@@ {YELLOW}\\{RESET}
{YELLOW}         |  {MAGENTA}▲▲{YELLOW}  |{RESET}
{YELLOW}         |  {RED}═══{YELLOW}  |{RESET}
{YELLOW}          \\ {BLUE}____ {YELLOW}/{RESET}
{YELLOW}           '--'{RESET}
"""

QUOTE_LINES = [
    ("I told my therapist I'm having an existential crisis,", YELLOW),
    ("she said 'That'll be $200.'", BRIGHT_RED),
    ("I said 'Can I pay in installments?'", BRIGHT_YELLOW),
    ("She said 'Sure, but then you'll owe me", CYAN),
    ("interest on your dread.'", BRIGHT_MAGENTA),
]

def clear_screen():
    print('\033[2J\033[H', end='')

def typewriter(text, color=WHITE, delay=0.03, end='\n'):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def fade_in_text(text, color=WHITE, steps=10):
    for i in range(steps + 1):
        intensity = i / steps
        r = int(255 * intensity)
        g = int(255 * intensity)
        b = int(255 * intensity)
        print(f'\r\033[38;2;{r};{g};{b}m{text}{RESET}', end='', flush=True)
        time.sleep(0.02)
    print()

def sparkle_animation(duration=1.5):
    sparkles = ['✦', '✧', '★', '☆', '✩', '✪', '✫', '✬', '✭', '✮']
    start = time.time()
    while time.time() - start < duration:
        x = random.randint(5, 70)
        y = random.randint(2, 15)
        sparkle = random.choice(sparkles)
        color = random.choice([YELLOW, CYAN, MAGENTA, BRIGHT_YELLOW, BRIGHT_CYAN])
        print(f'\033[{y};{x}H{color}{sparkle}{RESET}', end='', flush=True)
        time.sleep(0.05)
        print(f'\033[{y};{x}H ', end='', flush=True)

def draw_box(text_lines, width=60, border_color=CYAN, title="", title_color=YELLOW):
    inner_width = width - 4
    top = f"{border_color}╔{'═' * (width - 2)}╗{RESET}"
    bottom = f"{border_color}╚{'═' * (width - 2)}╝{RESET}"
    
    print(top)
    if title:
        title_padded = f" {title} ".center(width - 2)
        print(f"{border_color}║{title_color}{title_padded}{border_color}║{RESET}")
        print(f"{border_color}╠{'═' * (width - 2)}╣{RESET}")
    
    for line, color in text_lines:
        padded = line.center(inner_width)
        print(f"{border_color}║ {color}{padded}{border_color} ║{RESET}")
    
    print(bottom)

def main():
    clear_screen()
    
    # Hide cursor
    print('\033[?25l', end='')
    
    try:
        # Phase 1: Glasses appear
        print('\033[3;5H', end='')
        for line in GLASSES.strip().split('\n'):
            print(line)
            time.sleep(0.15)
        
        time.sleep(0.3)
        
        # Phase 2: Face appears below glasses
        print('\033[10;25H', end='')
        for line in FACE.strip().split('\n'):
            print(f'\033[{10 + FACE.strip().split("\n").index(line)};25H{line}')
            time.sleep(0.1)
        
        time.sleep(0.5)
        
        # Phase 3: Thought bubble grows
        bubble_lines = [
            "  ╭────────────────────────────────────────╮  ",
            "  │                                        │  ",
            "  │                                        │  ",
            "  │                                        │  ",
            "  │                                        │  ",
            "  ╰────────────────────────────────────────╯  ",
        ]
        
        for i, line in enumerate(bubble_lines):
            print(f'\033[{3 + i};40H{MAGENTA}{line}{RESET}')
            time.sleep(0.08)
        
        # Phase 4: Type quote into bubble
        quote_y_start = 5
        for idx, (line, color) in enumerate(QUOTE_LINES):
            print(f'\033[{quote_y_start + idx};43H', end='')
            typewriter(line, color=color, delay=0.025, end='')
            time.sleep(0.2)
        
        time.sleep(0.5)
        
        # Phase 5: Sparkle burst
        print('\033[18;1H', end='')
        sparkle_animation(1.0)
        
        # Phase 6: Final dramatic presentation
        print('\033[20;1H', end='')
        draw_box(QUOTE_LINES, width=68, border_color=BRIGHT_MAGENTA, 
                 title="WOODY ALLEN WISDOM", title_color=BRIGHT_YELLOW)
        
        # Phase 7: Signature sign-off
        time.sleep(0.5)
        print(f'\033[32;1H{ITALIC}{DIM}')
        typewriter("          — A neurotic's guide to affordable dread —", CYAN, 0.02)
        print(f'{RESET}')
        
        # Final sparkle
        print('\033[34;30H', end='')
        for s in ['✦', '✧', '★', '✧', '✦']:
            print(f'{BRIGHT_YELLOW}{s}{RESET} ', end='', flush=True)
            time.sleep(0.1)
        print()
        
    finally:
        # Show cursor
        print('\033[?25h', end='')
        print('\033[36;1H', end='')

if __name__ == '__main__':
    main()