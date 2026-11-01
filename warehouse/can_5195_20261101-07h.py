"""
Campbell's Soup Can #5195
Produced: 2026-11-01 07:33:06
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
    BLD = '\033[1m'
    DIM = '\033[2m'
    ITL = '\033[3m'
    UL = '\033[4m'
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
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

def typewriter(text, delay=0.03, color=''):
    for char in text:
        sys.stdout.write(f'{color}{char}{C.RST}')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitter_text(text, color, passes=3):
    for _ in range(passes):
        move_cursor(12, 20)
        glittered = ''.join(
            f'{C.BLD}{color}{c}{C.RST}' if random.random() < 0.3 else f'{color}{c}{C.RST}'
            for c in text
        )
        print(glittered, end='')
        sys.stdout.flush()
        time.sleep(0.15)

def draw_woody_face():
    face = [
        f"{C.YEL}        ╔════════════════╗{C.RST}",
        f"{C.YEL}        ║  {C.WHT}◉{C.YEL}  {C.CYN}┌─┐{C.YEL}  {C.WHT}◉{C.YEL}  ║{C.RST}",
        f"{C.YEL}        ║  {C.WHT}│{C.YEL}  {C.CYN}│ │{C.YEL}  {C.WHT}│{C.YEL}  ║{C.RST}",
        f"{C.YEL}        ║  {C.WHT}▼{C.YEL}  {C.CYN}└─┘{C.YEL}  {C.WHT}▼{C.YEL}  ║{C.RST}",
        f"{C.YEL}        ║      {C.MAG}┌─┐{C.YEL}       ║{C.RST}",
        f"{C.YEL}        ║      {C.MAG}│ │{C.YEL}       ║{C.RST}",
        f"{C.YEL}        ║      {C.MAG}└─┘{C.YEL}       ║{C.RST}",
        f"{C.YEL}        ╚════════════════╝{C.RST}",
    ]
    for i, line in enumerate(face):
        move_cursor(3 + i, 2)
        print(line)

def draw_glasses():
    frames = [
        f"{C.CYN}    ┌─────┐   ┌─────┐{C.RST}",
        f"{C.CYN}    │ ◉   │   │ ◉   │{C.RST}",
        f"{C.CYN}    └─────┘   └─────┘{C.RST}",
    ]
    for i, line in enumerate(frames):
        move_cursor(3 + i, 35)
        print(line)

def pulse_border(width=70, color=C.MAG):
    top = f"{color}╔{'═' * (width-2)}╗{C.RST}"
    bot = f"{color}╚{'═' * (width-2)}╝{C.RST}"
    return top, bot

def animate_quote_reveal(quote, author):
    width = 70
    lines = quote.split('\n')
    
    # Draw box
    top, bot = pulse_border(width)
    move_cursor(10, 15)
    print(top)
    for i in range(6):
        move_cursor(11 + i, 15)
        print(f"{C.MAG}║{C.RST}{' ' * (width-2)}{C.MAG}║{C.RST}")
    move_cursor(17, 15)
    print(bot)
    
    # Type quote line by line
    for i, line in enumerate(lines):
        move_cursor(12 + i, 18)
        typewriter(line, 0.02, C.WHT + C.ITL)
        time.sleep(0.15)
    
    # Author
    move_cursor(16, 18)
    typewriter(f"── {author}", 0.04, C.YEL + C.BLD)
    
    # Glitter effect on quote
    for _ in range(2):
        for i, line in enumerate(lines):
            move_cursor(12 + i, 18)
            glittered = ''.join(
                f'{C.BLD}{C.CYN}{c}{C.RST}' if c != ' ' and random.random() < 0.15 else f'{C.WHT}{C.ITL}{c}{C.RST}'
                for c in line
            )
            print(glittered, end='')
            sys.stdout.flush()
        time.sleep(0.3)
        for i, line in enumerate(lines):
            move_cursor(12 + i, 18)
            print(f'{C.WHT}{C.ITL}{line}{C.RST}', end='')
            sys.stdout.flush()
        time.sleep(0.3)

def floating_thoughts():
    thoughts = [
        "Wait, did I turn off the stove?",
        "My therapist says I have a preoccupation with death. \n       He's right. I'm preoccupied with it right now.",
        "I took a speed-reading course and read \n       'War and Peace' in twenty minutes. \n       It involves Russia.",
        "The universe is infinite. \n       Which means somewhere, \n       there's a version of me who flosses daily.",
        "I don't believe in an afterlife, \n       but I'm bringing a change of underwear \n       just in case.",
    ]
    
    for _ in range(2):
        thought = random.choice(thoughts)
        move_cursor(20, 15)
        print(f"{C.DIM}{C.CYN}💭 {thought}{C.RST}")
        sys.stdout.flush()
        time.sleep(2.5)
        move_cursor(20, 15)
        print(' ' * 80)

def main():
    hide_cursor()
    clear_screen()
    
    # Title animation
    title = "WOODY ALLEN WISDOM GENERATOR v3.14"
    move_cursor(1, 20)
    typewriter(title, 0.05, C.MAG + C.BLD)
    time.sleep(0.3)
    
    # Draw Woody face
    draw_woody_face()
    draw_glasses()
    
    # Subtitle
    move_cursor(11, 15)
    typewriter("Initializing neurosis protocols...", 0.03, C.DIM + C.CYN)
    time.sleep(0.5)
    move_cursor(11, 15)
    print(" " * 50)
    
    # The quote - ORIGINAL Woody Allen style
    quote = (
        "I spent three years in analysis \n"
        "trying to understand why I \n"
        "sabotage every relationship. \n"
        "Turns out, it's because I'm \n"
        "fundamentally unlovable. \n"
        "Breakthrough! Session over."
    )
    author = "Woody Allen (probably)"
    
    animate_quote_reveal(quote, author)
    
    # Floating thoughts
    move_cursor(19, 15)
    print(f"{C.DIM}{C.MAG}━━━ Random Neurotic Transmissions ━━━{C.RST}")
    
    try:
        for _ in range(4):
            floating_thoughts()
    except KeyboardInterrupt:
        pass
    
    # Final sign-off
    move_cursor(23, 15)
    typewriter("Remember: The universe doesn't care. \n       But your analyst charges either way.", 0.03, C.YEL + C.ITL)
    
    move_cursor(26, 15)
    print(f"{C.DIM}{C.BLU}Press Ctrl+C to exit existential dread...{C.RST}")
    
    show_cursor()
    
    # Keep alive for a bit
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        clear_screen()
        show_cursor()
        print(f"{C.GRN}Thanks for the neuroses! Come back soon. {C.MAG}◉‿◉{C.RST}")

if __name__ == "__main__":
    main()