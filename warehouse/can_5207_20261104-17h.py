"""
Campbell's Soup Can #5207
Produced: 2026-11-04 17:18:30
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Quote Generator - A neurotic philosophical experience
"""

import sys
import time
import random

# ANSI Color Codes
class C:
    R = '\033[0m'      # Reset
    B = '\033[1m'      # Bold
    D = '\033[2m'      # Dim
    I = '\033[3m'      # Italic
    U = '\033[4m'      # Underline
    
    # Foreground
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
    GRY = '\033[90m'
    
    # Bright foreground
    BRED = '\033[91m'
    BGRN = '\033[92m'
    BYEL = '\033[93m'
    BBLU = '\033[94m'
    BMAG = '\033[95m'
    BCYN = '\033[96m'
    BWHT = '\033[97m'
    
    # Background
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.WHT, delay=0.03, newline=True):
    """Print text with typewriter effect"""
    for char in text:
        print(f'{color}{char}{C.R}', end='', flush=True)
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def blink_text(text, color=C.YEL, times=3, interval=0.4):
    """Make text blink"""
    for _ in range(times):
        print(f'\r{color}{text}{C.R}', end='', flush=True)
        time.sleep(interval)
        print(f'\r{" " * len(text)}', end='', flush=True)
        time.sleep(interval)
    print(f'\r{color}{text}{C.R}')

def draw_box(width, height, title="", color=C.CYN, title_color=C.BYEL):
    """Draw a decorative box"""
    top = f'{color}╔{"═" * (width - 2)}╗{C.R}'
    bottom = f'{color}╚{"═" * (width - 2)}╝{C.R}'
    middle = f'{color}║{" " * (width - 2)}║{C.R}'
    
    lines = [top]
    if title:
        padding = (width - 2 - len(title)) // 2
        title_line = f'{color}║{" " * padding}{title_color}{C.B}{title}{C.R}{color}{" " * (width - 2 - padding - len(title))}║{C.R}'
        lines.append(title_line)
        lines.append(f'{color}╠{"═" * (width - 2)}╣{C.R}')
    
    for _ in range(height - (3 if title else 2)):
        lines.append(middle)
    lines.append(bottom)
    return lines

def neurotic_loader():
    """Show a neurotic loading animation"""
    thoughts = [
        "Analyzing mortality...",
        "Checking if stove is off...",
        "Rereading email from 2003...",
        "Worrying about the heat death of universe...",
        "Wondering if that mole is cancer...",
        "Replaying awkward moment from 1997...",
        "Calculating probability of parallel parking...",
        "Contemplating the futility of existence...",
    ]
    
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    
    print(f'\n{C.GRY}{C.I}Initializing existential dread...{C.R}\n')
    for i in range(20):
        thought = random.choice(thoughts)
        spin = spinner[i % len(spinner)]
        print(f'\r{C.CYN}{spin}{C.R} {C.WHT}{thought}{C.R}', end='', flush=True)
        time.sleep(0.15)
    print(f'\r{C.BGRN}✓{C.R} {C.BGRN}Existential dread successfully initialized{C.R}\n')
    time.sleep(0.5)

def print_quote_artistically(quote_lines, author="— Woody Allen (probably)"):
    """Print the quote with artistic flair"""
    width = 78
    
    # Draw top border with sparkles
    print(f'{C.MAG}✦ {C.CYN}═' * 38 + f'{C.MAG}✦{C.R}')
    
    # Quote box
    box = draw_box(width, len(quote_lines) + 4, " A MOMENT OF CLARITY ", C.CYN, C.BYEL)
    for i, line in enumerate(box):
        if i == 2:  # Title line already done
            continue
        elif i == 3:  # First content line
            print(line.replace(' ' * (width - 2), f'{C.I}{quote_lines[0].center(width - 2)}{C.R}'))
        elif i < 3 + len(quote_lines):
            idx = i - 3
            content = quote_lines[idx].center(width - 2)
            print(line.replace(' ' * (width - 2), f'{C.WHT}{C.I}{content}{C.R}'))
        else:
            print(line)
    
    # Author line with animation
    print()
    typewriter(f'{C.GRY}{C.D}{" " * 15}{author}{C.R}', C.GRY, 0.02)
    print()
    
    # Bottom border
    print(f'{C.MAG}✦ {C.CYN}═' * 38 + f'{C.MAG}✦{C.R}')

def woody_ascii():
    """Return a small Woody Allen ASCII portrait"""
    return f'''{C.YEL}
    ╭─────────────╮
    │  (•_•)      │  < adjusts glasses nervously
    │  <)  )╯     │
    │  /  \\       │
    ╰─────────────╯{C.R}'''

def main():
    # Our original Woody Allen style quote
    quote = (
        "I'm not afraid of dying — I just don't want to be"
    )
    quote2 = (
        "conscious when they read my browser history at the eulogy."
    )
    
    # Alternative quotes (pick one randomly for variety)
    quotes = [
        ("I'm not afraid of dying — I just don't want to be",
         "conscious when they read my browser history at the eulogy."),
        ("My therapist says I have a preoccupation with mortality.",
         "I told her I'm too busy worrying about the stove to die."),
        ("I asked the universe for a sign. It sent me a parking ticket.",
         "I took it as a metaphor for my entire romantic history."),
        ("Life is full of misery, loneliness, and suffering —",
         "and the worst part? The portions are too small."),
        ("I don't want to achieve immortality through my work.",
         "I want to achieve it through not dying. Is that too much to ask?"),
        ("The universe is indifferent. My dentist, however,",
         "is deeply judgmental about my flossing habits."),
    ]
    
    selected = random.choice(quotes)
    
    # Setup
    hide_cursor()
    clear_screen()
    
    try:
        # Neurotic loading
        neurotic_loader()
        
        # Show Woody
        print(woody_ascii())
        print()
        
        # Dramatic pause
        time.sleep(0.5)
        
        # Print quote with typewriter effect for first line
        print(f'{C.CYN}═' * 78 + f'{C.R}')
        print()
        
        # First line - typewriter
        typewriter(f'{C.BWHT}{C.I}  "{selected[0]}', C.BWHT, 0.04, newline=False)
        time.sleep(0.3)
        print(f'{C.R}')
        
        # Second line - typewriter
        typewriter(f'{C.BWHT}{C.I}  {selected[1]}"', C.BWHT, 0.04, newline=False)
        time.sleep(0.5)
        print(f'{C.R}')
        print()
        print(f'{C.CYN}═' * 78 + f'{C.R}')
        print()
        
        # Attribution with blink
        attrib = "— Woody Allen (as channeled by a nervous Python script)"
        blink_text(f'{C.GRY}{C.D}{attrib}{C.R}', C.YEL, 2, 0.3)
        
        print()
        print()
        
        # Final neurotic thought
        afterthoughts = [
            "Anyway, I should really check if I locked the door...",
            "Does this quote make me look fat?",
            "I should've been a dentist. Nice hours, people open up to you.",
            "My mother would say: 'So this is what you do with your life?'",
            "I'm going to lie down now. My back hurts from existential weight.",
        ]
        time.sleep(0.5)
        typewriter(f'{C.GRY}{C.I}  {random.choice(afterthoughts)}{C.R}', C.GRY, 0.02)
        print()
        print()
        
    finally:
        show_cursor()

if __name__ == '__main__':
    # Check if terminal supports ANSI
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        quote = random.choice([
            "I'm not afraid of dying — I just don't want to be conscious when they read my browser history at the eulogy.",
            "My therapist says I have a preoccupation with mortality. I told her I'm too busy worrying about the stove to die.",
        ])
        print(f'"{quote}"\n— Woody Allen (probably)')
    else:
        main()