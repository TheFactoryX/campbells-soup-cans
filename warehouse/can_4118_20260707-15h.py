"""
Campbell's Soup Can #4118
Produced: 2026-07-07 15:14:42
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
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Woody Allen ASCII portrait
WOODY = r"""
        ╭─────────────╮
        │  @      @   │   "I have a gnawing
        │      ▽      │    metaphysical 
        │  \_____/    │     nausea..."
        ╰─────────────╯
"""

# Original Woody-style quote
QUOTE = (
    "I took a course in speed reading and finished "
    "\"War and Peace\" in twenty minutes. "
    "It involves Russia."
)

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def typewriter(text, delay=0.03, color=C.WHITE):
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay)
    print()

def rainbow_text(text):
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    result = ""
    for i, char in enumerate(text):
        result += f"{colors[i % len(colors)]}{char}"
    return result + C.RST

def pulse_animation(frames=3):
    for _ in range(frames):
        for intensity in [C.DIM, C.RST, C.BOLD, C.RST]:
            move_cursor(15, 10)
            print(f'{intensity}★ ★ ★{C.RST}', end='', flush=True)
            time.sleep(0.2)

def draw_box(content_lines, padding=2, color=C.CYAN):
    max_len = max(len(line) for line in content_lines)
    width = max_len + padding * 2
    top = f'{color}╭{"─" * width}╮{C.RST}'
    bottom = f'{color}╰{"─" * width}╯{C.RST}'
    lines = []
    for line in content_lines:
        spaces = width - len(line)
        left = spaces // 2
        right = spaces - left
        lines.append(f'{color}│{C.RST}{" " * left}{line}{" " * right}{color}│{C.RST}')
    return [top] + lines + [bottom]

def main():
    clear_screen()
    hide_cursor()
    
    try:
        # Initial decorative elements
        print(f'{C.MAGENTA}{C.BOLD}')
        print("    ╔═════════════════════════════════════════════════════════════╗")
        print("    ║        WOODY ALLEN PHILOSOPHY GENERATOR v3.14              ║")
        print("    ║           (Now with 40% more existential dread)            ║")
        print("    ╚═════════════════════════════════════════════════════════════╝")
        print(f'{C.RST}')
        
        # Woody portrait with color cycling
        for frame in range(6):
            clear_screen()
            colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
            c = colors[frame % len(colors)]
            print(f'{c}{WOODY}{C.RST}')
            print(f'{C.DIM}    ┌────────────────────────────────────────────────┐{C.RST}')
            print(f'{C.DIM}    │                                                │{C.RST}')
            print(f'{C.DIM}    │                                                │{C.RST}')
            print(f'{C.DIM}    └────────────────────────────────────────────────┘{C.RST}')
            time.sleep(0.15)
        
        # Settle on final portrait
        clear_screen()
        print(f'{C.CYAN}{WOODY}{C.RST}')
        
        # Build anticipation
        print(f'\n{C.YELLOW}{C.ITALIC}    Consulting my analyst...{C.RST}')
        time.sleep(0.8)
        print(f'{C.YELLOW}{C.ITALIC}    Checking for repressed childhood memories...{C.RST}')
        time.sleep(0.6)
        print(f'{C.YELLOW}{C.ITALIC}    Calculating probability of meaningful existence...{C.RST}')
        time.sleep(0.7)
        print(f'{C.RED}{C.BOLD}    Result: Statistically insignificant. Proceeding anyway.{C.RST}\n')
        time.sleep(0.5)
        
        # The quote box
        quote_lines = [
            f'{C.WHITE}{C.BOLD}"{C.RST}',
            f'{C.WHITE}{QUOTE[:50]}{C.RST}',
            f'{C.WHITE}{QUOTE[50:]}{C.BOLD}"{C.RST}',
        ]
        box = draw_box(quote_lines, padding=3, color=C.MAGENTA)
        
        # Animate box drawing
        for i, line in enumerate(box):
            move_cursor(12 + i, 8)
            print(line)
            time.sleep(0.15)
        
        time.sleep(0.5)
        
        # Typewriter effect for the quote inside the box
        move_cursor(14, 14)
        typewriter('"', delay=0.1, color=C.WHITE + C.BOLD)
        typewriter(QUOTE, delay=0.025, color=C.WHITE)
        typewriter('"', delay=0.1, color=C.WHITE + C.BOLD)
        
        time.sleep(0.8)
        
        # Woody's reaction
        reactions = [
            f'{C.CYAN}    — Woody, probably, while ordering a pastrami on rye{C.RST}',
            f'{C.GREEN}    — My therapist says this is "progress"{C.RST}',
            f'{C.YELLOW}    — Also my mother called. Twice. During this quote.{C.RST}',
        ]
        
        for reaction in reactions:
            move_cursor(18, 1)
            print(' ' * 70)
            move_cursor(18, 1)
            typewriter(reaction, delay=0.02)
            time.sleep(0.6)
        
        # Final flourish - spinning neurotic thoughts
        move_cursor(22, 1)
        print(f'\n{C.DIM}    Neurotic background processes:{C.RST}')
        thoughts = [
            "Did I lock the door?",
            "Is that a symptom?",
            "What did she mean by 'fine'?",
            "Am I breathing correctly?",
            "Why did I say that in 1997?",
        ]
        
        for _ in range(2):
            for thought in thoughts:
                move_cursor(23, 5)
                color = random.choice([C.RED, C.YELLOW, C.GREEN, C.CYAN, C.MAGENTA])
                print(f'{color}◆ {thought}{" " * 30}{C.RST}', end='', flush=True)
                time.sleep(0.3)
        
        # Final sign-off
        move_cursor(26, 1)
        print(f'\n{C.BLUE}{C.BOLD}')
        print("    ╔═════════════════════════════════════════════════════════════╗")
        print("    ║  Remember: The universe is indifferent.                    ║")
        print("    ║  But at least you don't have to tip it.                    ║")
        print("    ╚═════════════════════════════════════════════════════════════╝")
        print(f'{C.RST}\n')
        
        # Fade out
        for _ in range(3):
            print(f'{C.DIM}    .{C.RST}', end='', flush=True)
            time.sleep(0.4)
        print()
        
    finally:
        show_cursor()

if __name__ == '__main__':
    main()