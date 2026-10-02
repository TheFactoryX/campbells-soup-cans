"""
Campbell's Soup Can #5054
Produced: 2026-10-02 12:36:24
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

WOODY_QUOTE = (
    "I took a course in existentialism... "
    "the professor failed me because I didn't show up. "
    "I told him, 'I was there in spirit... "
    "but my body had a panic attack in the hallway.'"
)

WOODY_ART = r"""
       ╭─────────────────────────────────────╮
       │    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    │
       │   █  WOODY ALLEN SIMULATOR v1.0  █   │
       │   █  Neurotic Philosophy Engine  █   │
       │    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    │
       │                                     │
       │      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   │
       │     █  ┌─────────────────┐  █      │
       │     █  │  ☕  🧠  💊  │  █      │
       │     █  └─────────────────┘  █      │
       │      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   │
       ╰─────────────────────────────────────╯
"""

GLASSES_ART = r"""
        ▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄
       █  ░░  █    █  ░░  █
       █      █    █      █
       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀
          \    /  \    /
           \  /    \  /
            \/      \/
             \      /
              \    /
               \  /
                \/
"""

THOUGHT_BUBBLE = """
     .-'-.
    /     \\
   ;  @ @  ;
   |       |
   \  \_/  /
    '.___.'
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
    result = ''
    for i, char in enumerate(text):
        if char != ' ':
            result += f'{colors[i % len(colors)]}{char}{RESET}'
        else:
            result += ' '
    return result

def pulse_text(text, color=CYAN, cycles=3):
    for _ in range(cycles):
        for intensity in [DIM, '', BOLD]:
            print(f'\r{color}{intensity}{text}{RESET}', end='', flush=True)
            time.sleep(0.3)
    print()

def glitch_effect(text, color=GREEN, iterations=10):
    chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'
    for _ in range(iterations):
        glitched = ''.join(
            random.choice(chars) if random.random() < 0.1 and c != ' ' else c
            for c in text
        )
        print(f'\r{color}{glitched}{RESET}', end='', flush=True)
        time.sleep(0.05)
    print(f'\r{color}{text}{RESET}')

def draw_box(content_lines, border_color=CYAN, title=None, padding=1):
    width = max(len(line) for line in content_lines) + 2 * padding
    top = f'{border_color}╭{"─" * (width - 2)}╮{RESET}'
    bottom = f'{border_color}╰{"─" * (width - 2)}╯{RESET}'
    
    lines = [top]
    if title:
        title_line = f'{border_color}│{RESET} {BOLD}{YELLOW}{title.center(width - 4)}{RESET} {border_color}│{RESET}'
        lines.append(title_line)
        lines.append(f'{border_color}├{"─" * (width - 2)}┤{RESET}')
    
    for line in content_lines:
        padded = ' ' * padding + line + ' ' * (width - 2 - padding - len(line))
        lines.append(f'{border_color}│{RESET}{padded}{border_color}│{RESET}')
    
    lines.append(bottom)
    return '\n'.join(lines)

def animate_entrance():
    clear_screen()
    hide_cursor()
    
    # Scroll in the ASCII art
    art_lines = WOODY_ART.strip('\n').split('\n')
    for i, line in enumerate(art_lines):
        move_cursor(i + 2, 5)
        typewriter(line, CYAN, delay=0.005, newline=False)
        time.sleep(0.05)
    
    time.sleep(0.5)
    
    # Glasses appear
    glasses_lines = GLASSES_ART.strip('\n').split('\n')
    for i, line in enumerate(glasses_lines):
        move_cursor(i + 15, 20)
        typewriter(line, YELLOW, delay=0.01, newline=False)
        time.sleep(0.08)
    
    time.sleep(0.5)
    
    # Thought bubble
    bubble_lines = THOUGHT_BUBBLE.strip('\n').split('\n')
    for i, line in enumerate(bubble_lines):
        move_cursor(i + 25, 55)
        typewriter(line, MAGENTA, delay=0.02, newline=False)
        time.sleep(0.1)
    
    time.sleep(1)

def display_quote():
    # Split quote into parts for dramatic effect
    parts = [
        "I took a course in existentialism...",
        "the professor failed me because I didn't show up.",
        "I told him, 'I was there in spirit...",
        "but my body had a panic attack in the hallway.'"
    ]
    
    clear_screen()
    
    # Header
    print(f'\n{BRIGHT_CYAN}{"═" * 70}{RESET}')
    print(f'{BRIGHT_YELLOW}{BOLD}           WOODY ALLEN\'S DAILY PHILOSOPHICAL CRISIS{RESET}')
    print(f'{BRIGHT_CYAN}{"═" * 70}{RESET}\n')
    
    # Neurotic metrics
    metrics = [
        f'{RED}Anxiety Level:{RESET} ████████████████████ {BRIGHT_RED}100%{RESET}',
        f'{YELLOW}Existential Dread:{RESET} ██████████████████░░ {BRIGHT_YELLOW}90%{RESET}',
        f'{BLUE}Therapy Bills:{RESET} ████████████████████ {BRIGHT_BLUE}$47,000{RESET}',
        f'{GREEN}Will to Live:{RESET} ██░░░░░░░░░░░░░░░░░░░ {BRIGHT_GREEN}12%{RESET}',
    ]
    for m in metrics:
        print(f'  {m}')
    print()
    
    # The quote in a nice box
    quote_lines = []
    for part in parts:
        # Word wrap
        words = part.split(' ')
        line = ''
        for word in words:
            if len(line) + len(word) + 1 > 60:
                quote_lines.append(line)
                line = word
            else:
                line += (' ' if line else '') + word
        if line:
            quote_lines.append(line)
    
    box = draw_box(quote_lines, border_color=MAGENTA, title=' TODAY\'S NEUROTIC EPIPHANY ', padding=2)
    print(box)
    print()
    
    # Typewriter effect for the quote
    print(f'  {ITALIC}{DIM}Loading philosophical baggage...{RESET}')
    time.sleep(0.5)
    
    for i, part in enumerate(parts):
        prefix = f'  {BRIGHT_WHITE}▶{RESET} '
        if i == 0:
            typewriter(prefix + part, WHITE, delay=0.02)
        elif i == 1:
            typewriter(prefix + part, CYAN, delay=0.025)
        elif i == 2:
            typewriter(prefix + part, YELLOW, delay=0.03)
        else:
            typewriter(prefix + part, BRIGHT_RED, delay=0.035)
        time.sleep(0.4)
    
    print()
    
    # Punchline box
    punchline = "Moral: The universe is indifferent. Your mother, however, is not."
    punch_box = draw_box([punchline], border_color=YELLOW, title=' 💡 LESSON LEARNED ', padding=3)
    print(punch_box)
    print()
    
    # Footer with neurotic tips
    tips = [
        "Tip #1: Death is just nature's way of telling you to slow down.",
        "Tip #2: If you want to make God laugh, tell Him your 5-year plan.",
        "Tip #3: I don't believe in an afterlife, but I'm bringing a change of underwear.",
    ]
    print(f'  {BRIGHT_BLACK}{"─" * 66}{RESET}')
    for tip in tips:
        print(f'  {DIM}{ITALIC}{tip}{RESET}')
    print(f'  {BRIGHT_BLACK}{"─" * 66}{RESET}')
    print()

def animated_signature():
    sig_lines = [
        "          — Woody Allen (probably, maybe, I'm not sure, don't quote me)",
        "",
        f"  {DIM}This program has been psychoanalyzed and prescribed Zoloft.{RESET}",
        f"  {DIM}Side effects may include: existential laughter, sudden urge to see therapist.{RESET}",
    ]
    for line in sig_lines:
        print(line)
        time.sleep(0.2)

def neurotic_loading():
    phrases = [
        "Analyzing neuroses...",
        "Consulting inner child...",
        "Inner child on hold...",
        "Checking for repressed memories...",
        "Found 847 repressed memories...",
        "Computing existential dread...",
        "Calibrating anxiety levels...",
        "Optimizing self-sabotage...",
        "Ready to overthink.",
    ]
    for phrase in phrases:
        print(f'\r{CYAN}{BLINK}►{RESET} {YELLOW}{phrase}{RESET}   ', end='', flush=True)
        time.sleep(random.uniform(0.3, 0.6))
    print('\r' + ' ' * 50 + '\r', end='')

def main():
    try:
        # Initial neurotic loading
        clear_screen()
        print(f'\n\n  {BRIGHT_MAGENTA}{BOLD}INITIALIZING WOODY ALLEN PERSONALITY MODULE...{RESET}\n')
        neurotic_loading()
        time.sleep(0.5)
        
        # Animated entrance
        animate_entrance()
        time.sleep(1)
        
        # Main quote display
        display_quote()
        
        # Signature
        animated_signature()
        
        # Final glitter
        print(f'\n  {BRIGHT_CYAN}Press Ctrl+C to schedule a therapy appointment...{RESET}\n')
        show_cursor()
        
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f'\n\n  {YELLOW}"I\'m not afraid of death... I just don\'t want to be there when it happens."{RESET}')
        print(f'  {DIM}— Woody Allen, probably{RESET}\n\n')
        sys.exit(0)
    except Exception as e:
        show_cursor()
        print(f'\n{RED}Error: {e}{RESET}')
        print(f'{DIM}Even the code has anxiety.{RESET}\n')

if __name__ == '__main__':
    main()