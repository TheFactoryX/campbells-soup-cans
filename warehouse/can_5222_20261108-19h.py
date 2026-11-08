"""
Campbell's Soup Can #5222
Produced: 2026-11-08 19:43:18
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
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

def clear_screen():
    print('\033[2J\033[H', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, delay=0.03, color=WHITE):
    for char in text:
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(delay)
    print()

def glitch_text(text, iterations=5, color=CYAN):
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    for _ in range(iterations):
        glitched = ''.join(random.choice(chars) if random.random() < 0.1 else c for c in text)
        print(f'\r{color}{glitched}{RESET}', end='', flush=True)
        time.sleep(0.05)
    print(f'\r{color}{text}{RESET}')

woody_quote = (
    "I took a course in existentialism... "
    "the professor failed me because I didn't show up. "
    "I told him, 'Existence precedes essence, '
    'but apparently attendance precedes passing.'"
)

woody_ascii = r"""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║    ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄       ║
    ║   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌      ║
    ║   ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌      ║
    ║   ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌      ║
    ║   ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌      ║
    ║   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌      ║
    ║   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌      ║
    ║   ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌      ║
    ║   ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌       ▐░▌      ║
    ║   ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌      ║
    ║    ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀       ║
    ║                                                               ║
    ╚══════════════════════════════════════════════════════════════╝
"""

glasses_ascii = r"""
           .--.      .--.
          /    \    /    \
         |  ()  |  |  ()  |
          \    /    \    /
           `--'      `--'
            |          |
         ___|__________|___
        /                  \
       |   WOODY ALLEN    |
        \________________/
"""

neurons = [
    "     🧠  Synapse firing: 'What if I'm just a brain in a jar?'",
    "     🧠  Neuron #847: 'But who's dreaming the jar?'",
    "     🧠  Amygdala: 'PANIC. PANIC NOW.'",
    "     🧠  Prefrontal cortex: 'Statistically unlikely... but possible.'",
    "     🧠  Hippocampus: 'Remember that embarrassing thing from 2003?'",
    "     🧠  Cerebellum: 'Wait, are we breathing manually now?'",
]

def animate_brain_thoughts():
    print(f"\n{BRIGHT_MAGENTA}{BOLD}Inside Woody's Head:{RESET}\n")
    for thought in neurons:
        print(f"{CYAN}{thought}{RESET}")
        time.sleep(0.4)
    print()

def draw_boxed_quote(quote, width=70):
    lines = []
    words = quote.split(' ')
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    top = f"{BRIGHT_YELLOW}╔{'═' * (width - 2)}╗{RESET}"
    bottom = f"{BRIGHT_YELLOW}╚{'═' * (width - 2)}╝{RESET}"
    
    print(top)
    for line in lines:
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{BRIGHT_YELLOW}║{RESET}{' ' * left_pad}{BRIGHT_WHITE}{ITALIC}{line}{RESET}{' ' * right_pad}{BRIGHT_YELLOW}║{RESET}")
    print(bottom)

def main():
    clear_screen()
    hide_cursor()
    
    try:
        # Title animation
        print(f"\n{BRIGHT_CYAN}{BOLD}")
        for line in woody_ascii.split('\n'):
            print(line)
            time.sleep(0.05)
        print(RESET)
        
        time.sleep(0.5)
        
        # Glasses
        print(f"{YELLOW}")
        for line in glasses_ascii.split('\n'):
            print(line)
            time.sleep(0.03)
        print(RESET)
        
        time.sleep(0.5)
        
        # Brain thoughts
        animate_brain_thoughts()
        
        # Divider
        print(f"{BRIGHT_BLACK}{'─' * 70}{RESET}\n")
        
        # The quote with typewriter effect
        print(f"{BRIGHT_GREEN}{BOLD} Woody says:{RESET}\n")
        time.sleep(0.3)
        
        draw_boxed_quote(woody_quote)
        
        print()
        
        # Final philosophical musing
        time.sleep(0.5)
        musings = [
            "Anyway, I have a doctor's appointment at 3...",
            "My therapist says I have a preoccupation with mortality.",
            "I told him, 'Doc, at my age, mortality has a preoccupation with ME.'",
            "Also, I think my left kidney is making a weird noise.",
            "Is it hot in here? Or is that just the slow heat death of the universe?",
            "I should really write this down... if I remember where I put my pen.",
            "My pen. My beautiful pen. Gone. Like youth. Like hope. Like my 401k.",
        ]
        
        print(f"{BRIGHT_BLACK}{ITALIC}")
        for musing in musings:
            typewriter(f"  {musing}", 0.015, BRIGHT_BLACK)
            time.sleep(0.2)
        print(RESET)
        
        # Final sign-off
        print(f"\n{BRIGHT_MAGENTA}{'✦' * 35}{RESET}")
        glitch_text("  Existence is brief. Comedy is eternal.  ", 3, BRIGHT_CYAN)
        print(f"{BRIGHT_MAGENTA}{'✦' * 35}{RESET}\n")
        
        # Credits
        time.sleep(0.5)
        print(f"{DIM}— Generated by a neurotic algorithm with separation anxiety{RESET}\n")
        
    finally:
        show_cursor()

if __name__ == "__main__":
    main()