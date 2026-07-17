"""
Campbell's Soup Can #4232
Produced: 2026-07-17 19:32:39
Worker: Free Models Router (openrouter/free)
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

# Woody Allen style quotes
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering — and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "The talent for being happy is appreciating what you have, which I don't.",
    "I took a speed-reading course and read War and Peace in twenty minutes. It involves Russia.",
    "If you want to make God laugh, tell him about your plans. Or your cholesterol.",
    "I have a very bad feeling about this. Also, a very bad feeling about everything else.",
    "My one regret in life is that I am not someone else. Preferably someone with better health insurance.",
    "Eighty percent of success is showing up. The other twenty is pretending you belong there.",
    "I don't believe in the afterlife, although I am bringing a change of underwear.",
    "The food here is terrible... and such small portions!",
    "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
    "Death is not the end. There remains the litigation over the estate.",
    "I'm two with nature. Mostly because I can't afford a therapist.",
    "My analyst says I have a preoccupation with death. Which is ridiculous — I'll be dead soon enough.",
]

# ANSI color codes
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    
    # Foreground
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;213m'
    LIME = '\033[38;5;154m'
    TEAL = '\033[38;5;87m'
    GOLD = '\033[38;5;220m'
    
    # Background
    BG_BLACK = '\033[40m'
    BG_DARK = '\033[48;5;234m'
    BG_BLUE = '\033[48;5;17m'
    BG_RED = '\033[48;5;52m'

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.WHITE, delay=0.02, newline=True):
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def rainbow_text(text):
    colors = [C.RED, C.ORANGE, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    result = ''
    for i, char in enumerate(text):
        if char != ' ':
            result += f'{colors[i % len(colors)]}{char}{C.RST}'
        else:
            result += ' '
    return result

def draw_box(content_lines, width=70, border_color=C.CYAN, title="", title_color=C.GOLD):
    top = f'{border_color}╔{"═" * (width - 2)}╗{C.RST}'
    bottom = f'{border_color}╚{"═" * (width - 2)}╝{C.RST}'
    
    lines = [top]
    
    if title:
        title_str = f' {title} '
        pad = (width - 2 - len(title_str)) // 2
        line = f'{border_color}║{C.RST}{" " * pad}{title_color}{title_str}{C.RST}{" " * (width - 2 - pad - len(title_str))}{border_color}║{C.RST}'
        lines.append(line)
        sep = f'{border_color}╠{"═" * (width - 2)}╣{C.RST}'
        lines.append(sep)
    
    for line in content_lines:
        visible_len = len(line.replace('\033[', '').replace('m', ''))
        while '\033[' in line:
            idx = line.index('\033[')
            end = line.index('m', idx) + 1
            visible_len -= (end - idx)
            line = line[:idx] + line[end:]
        padding = width - 2 - visible_len
        lines.append(f'{border_color}║{C.RST} {line}{" " * padding}{border_color}║{C.RST}')
    
    lines.append(bottom)
    return '\n'.join(lines)

def woody_face():
    return f"""{C.YELLOW}
       ╭─────────╮
       │  @   @  │  {C.WHITE}•{C.YELLOW}  {C.WHITE}•{C.YELLOW}
       │    ^    │
       │  \\___/  │
       ╰─────────╯
{C.RST}"""

def animated_intro():
    frames = [
        f"{C.GRAY}Loading neuroses...{C.RST}",
        f"{C.GRAY}Calibrating existential dread...{C.RST}",
        f"{C.GRAY}Checking for hypochondria updates...{C.RST}",
        f"{C.GRAY}Optimizing self-deprecation algorithms...{C.RST}",
        f"{C.GREEN}Ready. Proceeding with inevitable disappointment.{C.RST}",
    ]
    for frame in frames:
        print(f'\r{frame}', end='', flush=True)
        time.sleep(0.5)
    print('\r' + ' ' * 50 + '\r', end='')

def main():
    hide_cursor()
    try:
        clear_screen()
        
        # Animated intro
        animated_intro()
        time.sleep(0.3)
        print()
        
        # Woody face
        print(woody_face())
        time.sleep(0.3)
        
        # Select quote
        quote = random.choice(QUOTES)
        
        # Typewriter effect for the quote inside a box
        print()
        box_width = 74
        quote_lines = []
        words = quote.split(' ')
        current_line = ''
        for word in words:
            test = current_line + (' ' if current_line else '') + word
            if len(test) > box_width - 6:
                quote_lines.append(current_line)
                current_line = word
            else:
                current_line = test
        if current_line:
            quote_lines.append(current_line)
        
        # Draw empty box first
        box_content = [''] * len(quote_lines)
        box = draw_box(box_content, width=box_width, title=" WOODY ALLEN WISDOM ", title_color=C.GOLD + C.BOLD)
        print(box)
        
        # Move cursor up to fill in lines
        lines_up = len(quote_lines) + 4  # top border + title + sep + content start
        move_cursor(lines_up - len(quote_lines), 4)
        
        # Type each line
        for i, line in enumerate(quote_lines):
            for char in line:
                print(f'{C.WHITE}{C.ITALIC}{char}{C.RST}', end='', flush=True)
                time.sleep(0.015)
            if i < len(quote_lines) - 1:
                move_cursor(lines_up - len(quote_lines) + i + 1, 4)
        
        # Signature
        time.sleep(0.5)
        move_cursor(lines_up + 1, 4)
        typewriter("— Woody Allen (probably)", C.GRAY + C.DIM, delay=0.03)
        
        # Decorative footer
        time.sleep(0.3)
        print()
        footer = f"{C.DIM}{C.CYAN}═══════════════════════════════════════════════════════════════════════════{C.RST}"
        print(footer)
        print(f"{C.DIM}  Existential crisis provided free of charge. No refunds. No exits.{C.RST}")
        print(f"{C.DIM}  Side effects may include: overthinking, insomnia, sudden urge to see analyst.{C.RST}")
        print(footer)
        
        # Final blink
        time.sleep(0.5)
        for _ in range(3):
            move_cursor(lines_up + 6, 0)
            print(f'{C.BLINK}{C.RED}  ◉  {C.RST}   ', end='', flush=True)
            time.sleep(0.4)
            print(f'       ', end='', flush=True)
            time.sleep(0.4)
        
        print()
        
    finally:
        show_cursor()

if __name__ == '__main__':
    main()