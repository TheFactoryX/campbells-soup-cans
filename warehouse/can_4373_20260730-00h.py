"""
Campbell's Soup Can #4373
Produced: 2026-07-30 00:13:40
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
BLINK = '\033[5m'

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GRAY = '\033[90m'

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
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\n"
    "It involves Russia. And a lot of snow. And everyone's miserable.\n"
    "Which, come to think of it, describes my last three relationships\n"
    "and also Tuesday."
)

WOODY_ART = r"""
        ╔══════════════════════════════════════════════════════════════╗
        ║                                                               ║
        ║    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗    ║
        ║    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║    ║
        ║    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║    ║
        ║    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║    ║
        ║    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║    ║
        ║     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ║
        ║                                                               ║
        ║           ██████╗ ███████╗███████╗███████╗██████╗             ║
        ║           ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗            ║
        ║           ██████╔╝█████╗  ███████╗█████╗  ██████╔╝            ║
        ║           ██╔══██╗██╔══╝  ╚════██║██╔══╝  ██╔══██╗            ║
        ║           ██║  ██║███████╗███████║███████╗██║  ██║            ║
        ║           ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝            ║
        ║                                                               ║
        ╚══════════════════════════════════════════════════════════════╝
"""

GLASSES = r"""
         .--.      .--.
        /    \    /    \
       |  __  |  |  __  |
       | |  | |  | |  | |
       | |__| |  | |__| |
        \____/    \____/
"""

THOUGHT_BUBBLE = [
    r"""
       _
      (_)
     .-'-.
    /     \
   ;  @ @  ;
   |       |
   \  \_/  /
    '._.' 
""",
    r"""
        _
       (_)
      .-'-.
     /     \
    ;  - -  ;
    |       |
    \  \_/  /
     '._.' 
""",
    r"""
         _
        (_)
       .-'-.
      /     \
     ;  o o  ;
     |       |
     \  \_/  /
      '._.' 
""",
]

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=WHITE, delay=0.02, newline=True):
    for char in text:
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def blink_text(text, color=YELLOW, times=3, interval=0.4):
    for _ in range(times):
        print(f'\r{color}{BLINK}{text}{RESET}', end='', flush=True)
        time.sleep(interval)
        print(f'\r{color}{text}{RESET}', end='', flush=True)
        time.sleep(interval)
    print()

def animate_glasses():
    frames = [
        r"""
         .--.      .--.
        /    \    /    \
       |  __  |  |  __  |
       | |  | |  | |  | |
       | |__| |  | |__| |
        \____/    \____/
""",
        r"""
         .--.      .--.
        /    \    /    \
       |  __  |  |  __  |
       | |  | |  | |  | |
       | |__| |  | |__| |
        \____/    \____/
           \  /
            \/
""",
        r"""
         .--.      .--.
        /    \    /    \
       |  __  |  |  __  |
       | |  | |  | |  | |
       | |__| |  | |__| |
        \____/    \____/
            /\
           /  \
""",
    ]
    for frame in frames * 2:
        print('\033[H', end='')
        print(f'{CYAN}{frame}{RESET}')
        time.sleep(0.3)

def particle_burst(x, y, color=MAGENTA):
    particles = ['✦', '✧', '★', '☆', '✩', '✪', '✫', '✬', '✭', '✮']
    for _ in range(15):
        px = x + random.randint(-5, 5)
        py = y + random.randint(-3, 3)
        p = random.choice(particles)
        print(f'\033[{py};{px}H{color}{p}{RESET}', end='', flush=True)
    time.sleep(0.1)

def draw_quote_box(quote_lines):
    max_len = max(len(line) for line in quote_lines)
    width = max_len + 4
    
    top = f'{MAGENTA}╔{"═" * width}╗{RESET}'
    bottom = f'{MAGENTA}╚{"═" * width}╝{RESET}'
    
    print(top)
    for line in quote_lines:
        padding = width - 2 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f'{MAGENTA}║{RESET}{" " * left_pad}{CYAN}{ITALIC}{line}{RESET}{" " * right_pad}{MAGENTA}║{RESET}')
    print(bottom)

def main():
    hide_cursor()
    clear_screen()
    
    # Title animation
    print(f'{YELLOW}{BOLD}')
    for line in WOODY_ART.split('\n'):
        print(line)
        time.sleep(0.03)
    print(f'{RESET}')
    time.sleep(0.5)
    
    # Glasses appear
    print(f'{CYAN}{GLASSES}{RESET}')
    time.sleep(0.5)
    
    # Blinking thought bubble
    for _ in range(2):
        for bubble in THOUGHT_BUBBLE:
            print('\033[H\033[J', end='')
            print(f'{YELLOW}{BOLD}')
            for line in WOODY_ART.split('\n'):
                print(line)
            print(f'{RESET}')
            print(f'{CYAN}{GLASSES}{RESET}')
            print(f'{GREEN}{bubble}{RESET}')
            time.sleep(0.4)
    
    # Clear for quote
    clear_screen()
    
    # Typewriter the quote
    quote_lines = WOODY_QUOTE.split('\n')
    
    print(f'{MAGENTA}{BOLD}┌{"─" * 60}┐{RESET}')
    for i, line in enumerate(quote_lines):
        print(f'{MAGENTA}│{RESET} ', end='')
        typewriter(line, color=CYAN, delay=0.015, newline=False)
        print(f' {MAGENTA}│{RESET}')
        if i < len(quote_lines) - 1:
            time.sleep(0.3)
    print(f'{MAGENTA}└{"─" * 60}┘{RESET}')
    
    time.sleep(0.5)
    
    # Signature
    print()
    sig = "— Woody Allen (probably, or maybe just my therapist)"
    print(f'{GRAY}{DIM}{ITALIC}{sig.center(64)}{RESET}')
    
    # Final flourish
    time.sleep(0.5)
    blink_text(" * existential dread intensifies * ", MAGENTA, times=2)
    
    # Particle burst
    print()
    for _ in range(3):
        particle_burst(32, 1)
    
    print(f'\n{GRAY}Press Ctrl+C to accept the absurdity of existence...{RESET}')
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear_screen()
        print(f'{GREEN}{BOLD}Thanks for the neurosis! Come back soon. 🧠{RESET}\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f'\n{GREEN}Interrupted. Existence continues regardless.{RESET}\n')