"""
Campbell's Soup Can #4474
Produced: 2026-08-08 08:02:10
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
class C:
    R = '\033[91m'      # Red
    G = '\033[92m'      # Green
    Y = '\033[93m'      # Yellow
    B = '\033[94m'      # Blue
    M = '\033[95m'      # Magenta
    C = '\033[96m'      # Cyan
    W = '\033[97m'      # White
    D = '\033[90m'      # Dark gray
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    X = '\033[0m'       # Reset

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.W, delay=0.03, newline=True):
    for char in text:
        print(f'{color}{char}{C.X}', end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def rainbow_text(text):
    colors = [C.R, C.Y, C.G, C.C, C.B, C.M]
    result = ''
    for i, char in enumerate(text):
        if char != ' ':
            result += colors[i % len(colors)] + char + C.X
        else:
            result += ' '
    return result

def draw_box(width, height, title="", color=C.C):
    top = f'{color}┌{"─" * (width - 2)}┐{C.X}'
    bottom = f'{color}└{"─" * (width - 2)}┘{C.X}'
    middle = f'{color}│{" " * (width - 2)}│{C.X}'
    
    print(top)
    if title:
        padding = (width - 2 - len(title)) // 2
        print(f'{color}│{C.X}{" " * padding}{C.BOLD}{title}{C.X}{" " * (width - 2 - padding - len(title))}{color}│{C.X}')
        print(middle)
    for _ in range(height - 3 - (1 if title else 0)):
        print(middle)
    print(bottom)

def woody_face():
    faces = [
        f"""{C.Y}
    ╭─────╮
    │ {C.W}◉ ◉{C.Y} │
    │ {C.M}▲{C.Y}   │
    │ {C.W}└─┘{C.Y} │
    ╰─────╯{C.X}""",
        f"""{C.Y}
    ╭─────╮
    │ {C.W}◉ ◉{C.Y} │
    │ {C.M}┌─┐{C.Y} │
    │ {C.W}└─┘{C.Y} │
    ╰─────╯{C.X}""",
        f"""{C.Y}
    ╭─────╮
    │ {C.W}◉ ◉{C.Y} │
    │ {C.M}╰─╯{C.Y} │
    │ {C.W}───{C.Y} │
    ╰─────╯{C.X}""",
    ]
    return random.choice(faces)

def glitch_text(text, intensity=0.1):
    glitch_chars = '░▒▓█▄▀▌▐▙▛▜▟▞▚▗▖▘▝▀▄'
    result = ''
    for char in text:
        if char != ' ' and char != '\n' and random.random() < intensity:
            result += f'{C.R}{random.choice(glitch_chars)}{C.X}'
        else:
            result += char
    return result

def main():
    hide_cursor()
    clear_screen()
    
    # The Woody Allen quote
    quote = "I took a speed-reading course and read War and Peace in twenty minutes.\nIt involves Russia."
    
    lines = quote.split('\n')
    
    # Animation: falling characters
    width = 70
    height = 20
    
    # Intro animation
    for frame in range(15):
        clear_screen()
        print(f'\n{C.D}{" " * 15}loading neuroses...{C.X}\n')
        
        # Draw progress bar
        bar_width = 40
        filled = int(bar_width * frame / 14)
        bar = f'{C.G}{"█" * filled}{C.D}{"░" * (bar_width - filled)}{C.X}'
        print(f'{" " * 15}[{bar}] {frame * 7}%')
        
        # Random Woody face
        if frame % 3 == 0:
            print(f'\n{C.D}{" " * 10}Current anxiety:{C.X}')
            print(woody_face())
        
        time.sleep(0.15)
    
    clear_screen()
    
    # Main display
    print(f'\n{C.M}{"=" * 60}{C.X}')
    print(f'{C.BOLD}{C.Y}{" " * 12}WOODY ALLEN PHILOSOPHY GENERATOR v2.3{C.X}')
    print(f'{C.M}{"=" * 60}{C.X}\n')
    
    # Draw the quote in a fancy box
    box_width = 58
    box_height = 10
    
    # Top border with sparkles
    sparkles = '✦✧⋆✦✧⋆✦✧⋆✦✧⋆✦✧⋆✦✧⋆✦✧⋆'
    print(f'  {C.D}{sparkles[:box_width]}{C.X}')
    print(f'  {C.C}╔{"═" * (box_width - 2)}╗{C.X}')
    
    # Empty line
    print(f'  {C.C}║{C.X}{" " * (box_width - 2)}{C.C}║{C.X}')
    
    # Quote lines with typewriter effect
    for i, line in enumerate(lines):
        print(f'  {C.C}║{C.X}  ', end='', flush=True)
        typewriter(line, color=C.W + C.ITALIC, delay=0.02, newline=False)
        # Calculate remaining spaces
        remaining = box_width - 4 - len(line)
        print(f'{" " * max(1, remaining)}{C.C}║{C.X}')
        time.sleep(0.3)
    
    # Empty line
    print(f'  {C.C}║{C.X}{" " * (box_width - 2)}{C.C}║{C.X}')
    
    # Attribution line
    attrib = "— Woody Allen (probably, he denies everything)"
    print(f'  {C.C}║{C.X}  {C.D}{attrib}{C.X}{" " * (box_width - 4 - len(attrib))}{C.C}║{C.X}')
    
    # Bottom border
    print(f'  {C.C}╚{"═" * (box_width - 2)}╝{C.X}')
    print(f'  {C.D}{sparkles[:box_width]}{C.X}\n')
    
    # Existential footer
    footers = [
        "The universe is indifferent. So is my therapist.",
        "Existence precedes essence. Anxiety precedes both.",
        "I think, therefore I am... worried.",
        "Nihilism: now with 50% less meaning!",
        "Death is nature's way of saying 'table for one, check please.'",
    ]
    
    footer = random.choice(footers)
    
    # Animate footer appearing
    time.sleep(0.5)
    print(f'  {C.Y}💭 {C.X}', end='', flush=True)
    typewriter(footer, color=C.D + C.ITALIC, delay=0.04)
    
    # Woody face at bottom
    print()
    print(woody_face())
    
    # Final message
    time.sleep(0.5)
    print(f'\n  {C.BOLD}{C.G}Press Ctrl+C to accept the absurdity of existence{C.X}')
    print(f'  {C.D}(or just close the window, the void doesn't judge){C.X}\n')
    
    # Subtle animation loop
    try:
        blink_state = True
        dot_count = 0
        while True:
            time.sleep(0.8)
            # Blink the cursor hint
            move_cursor(24, 2)
            if blink_state:
                print(f'{C.G}► Press Ctrl+C to embrace the void{C.X}   ')
            else:
                print(f'{C.D}► Press Ctrl+C to embrace the void{C.X}   ')
            blink_state = not blink_state
            
            # Rotate face occasionally
            if random.random() < 0.1:
                move_cursor(20, 2)
                print(woody_face())
    except KeyboardInterrupt:
        clear_screen()
        show_cursor()
        print(f'\n{C.Y}Thanks for the anxiety. Same time next week?{C.X}\n')
        print(f'{C.D}    ╭─────╮{C.X}')
        print(f'{C.D}    │ {C.W}◉ ◉{C.D} │{C.X}')
        print(f'{C.D}    │ {C.M}╰─╯{C.D} │{C.X}')
        print(f'{C.D}    ╰─────╯{C.X}\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f'\n{C.Y}Session terminated. The neurosis continues offline.{C.X}\n')
    except Exception as e:
        show_cursor()
        print(f'\n{C.R}Error: {e}{C.X}')
        print(f'{C.D}Even the code has existential dread.{C.X}\n')