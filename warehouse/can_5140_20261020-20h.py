"""
Campbell's Soup Can #5140
Produced: 2026-10-20 20:35:31
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
Woody Allen Quote Generator - Neurotic Wisdom Edition
A single-file philosophical anxiety simulator with ANSI pizzazz.
"""

import sys
import time
import random

# ═══════════════════════════════════════════════════════════════════════════
# ANSI COLOR PALETTE - because existential dread deserves good aesthetics
# ═══════════════════════════════════════════════════════════════════════════

class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    
    # Foreground
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_GRAY = '\033[100m'

# ═══════════════════════════════════════════════════════════════════════════
# THE QUOTE - Pure, uncut Woody Allen neuroses
# ═══════════════════════════════════════════════════════════════════════════

WOODY_QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\n"
    "It involves Russia. And peace. Mostly Russia.\n\n"
    "My therapist says I have a preoccupation with death.\n"
    "I told her, 'Doc, at my age, it's not a preoccupation — it's a scheduling conflict.'\n\n"
    "The universe is indifferent. My landlord is hostile.\n"
    "My cholesterol is winning. And somewhere, a philosopher is nodding sagely\n"
    "while I Google 'can you die from existential dread?' at 3 AM.\n\n"
    "I'd like to believe in an afterlife.\n"
    "But honestly? I can barely manage the *during* life.\n"
    "The paperwork alone would kill me."
)

# ═══════════════════════════════════════════════════════════════════════════
# ASCII ART ELEMENTS - Visual anxiety
# ═══════════════════════════════════════════════════════════════════════════

WOODY_FACE = r"""
       \   |   /
        \  |  /
     .--.\ | /.--.
    /     \|/     \
   |  @  @  |  @  @  |
   |        |        |
   |  \____/  \____/  |
    \                /
     '.__________.' 
        |      |
       _'      '_
"""

BRAIN_FART = r"""
    .--.
   /    \
  |  💭  |
   \    /
    '--'
     |
    \|/
   (o o)
    \_/
"""

ANXIETY_SPIRAL = [
    "    @    ",
    "   @ @   ",
    "  @   @  ",
    " @     @ ",
    "@       @",
    " @     @ ",
    "  @   @  ",
    "   @ @   ",
    "    @    ",
]

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS - For theatrical effect
# ═══════════════════════════════════════════════════════════════════════════

def clear_screen():
    """Clear terminal - like repression, but for text."""
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, delay=0.02, color=C.WHITE, end='\n'):
    """Type out text character by character - because thinking hurts."""
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def gradient_text(text, start_color, end_color, steps=None):
    """Apply a gradient across text. Because life is a gradient of disappointment."""
    if steps is None:
        steps = len(text)
    # Simple RGB interpolation for ANSI 256-color approximation
    result = ""
    for i, char in enumerate(text):
        ratio = i / max(1, len(text) - 1)
        # We'll use a simplified approach with 256-color codes
        color_code = 232 + int(ratio * 23)  # Grayscale gradient
        result += f'\033[38;5;{color_code}m{char}'
    return result + C.RST

def rainbow_text(text, offset=0):
    """Rainbow cycling text. Gay pride for your anxiety."""
    colors = [196, 202, 208, 226, 118, 46, 51, 45, 39, 33, 93, 163, 199]
    result = ""
    for i, char in enumerate(text):
        if char == '\n':
            result += '\n'
            continue
        color = colors[(i + offset) % len(colors)]
        result += f'\033[38;5;{color}m{char}'
    return result + C.RST

def boxed_text(lines, border_color=C.CYAN, title="", title_color=C.YELLOW):
    """Draw a pretty box around text. Like a coffin, but for wisdom."""
    max_len = max(len(line) for line in lines) if lines else 0
    width = max(max_len, len(title)) + 4
    
    top = f"{border_color}╭{'─' * (width - 2)}╮{C.RST}"
    bottom = f"{border_color}╰{'─' * (width - 2)}╯{C.RST}"
    
    result = [top]
    
    if title:
        padding = width - 2 - len(title)
        left_pad = padding // 2
        right_pad = padding - left_pad
        title_line = f"{border_color}│{C.RST}{' ' * left_pad}{title_color}{C.BOLD}{title}{C.RST}{' ' * right_pad}{border_color}│{C.RST}"
        result.append(title_line)
        result.append(f"{border_color}├{'─' * (width - 2)}┤{C.RST}")
    
    for line in lines:
        padding = width - 2 - len(line)
        result.append(f"{border_color}│{C.RST} {line}{' ' * padding} {border_color}│{C.RST}")
    
    result.append(bottom)
    return '\n'.join(result)

# ═══════════════════════════════════════════════════════════════════════════
# ANIMATION SEQUENCES - Visual theater
# ═══════════════════════════════════════════════════════════════════════════

def animate_spiral(duration=2.0):
    """Anxiety spiral animation. Mesmerizing like a therapist's watch."""
    start = time.time()
    frame = 0
    while time.time() - start < duration:
        clear_screen()
        spiral_frame = ANXIETY_SPIRAL[frame % len(ANXIETY_SPIRAL)]
        print(f'\n\n{C.MAGENTA}{C.BOLD}')
        for line in spiral_frame.split('\n'):
            print(f'                    {line}')
        print(f'{C.RST}\n')
        print(f'           {C.GRAY}{C.ITALIC}spiraling into the void...{C.RST}')
        time.sleep(0.15)
        frame += 1

def animate_brain_fart():
    """A thought bubble appears. Then pops. Like all my relationships."""
    clear_screen()
    print(f'\n\n{C.CYAN}')
    for line in BRAIN_FART.strip().split('\n'):
        print(f'                    {line}')
        time.sleep(0.1)
    print(C.RST)
    time.sleep(0.5)
    
    # Pop animation
    for i in range(3):
        clear_screen()
        print(f'\n\n{C.CYAN}')
        if i == 0:
            print('                    .--.')
            print('                   / POP \\')
            print('                  |  * *  |')
            print('                   \\     /')
            print('                    \'--\'')
        elif i == 1:
            print('                      * *')
            print('                     *   *')
            print('                      * *')
        else:
            print('                         ')
        print(C.RST)
        time.sleep(0.15)

def woody_entrance():
    """Woody slides in. Nervously."""
    clear_screen()
    print(f'\n\n{C.YELLOW}{C.BOLD}')
    
    # Slide in from left
    face_lines = WOODY_FACE.strip().split('\n')
    for step in range(40, -1, -2):
        clear_screen()
        print('\n\n')
        for line in face_lines:
            print(' ' * step + f'{C.YELLOW}{line}{C.RST}')
        time.sleep(0.03)
    
    # Blink animation
    for _ in range(3):
        clear_screen()
        print('\n\n')
        for line in face_lines:
            if '@  @' in line:
                line = line.replace('@  @', 'o  o').replace('@  @', 'o  o')
            print(f'                    {C.YELLOW}{line}{C.RST}')
        time.sleep(0.15)
        clear_screen()
        print('\n\n')
        for line in face_lines:
            print(f'                    {C.YELLOW}{line}{C.RST}')
        time.sleep(0.15)
    
    # Sigh
    clear_screen()
    print('\n\n')
    for line in face_lines:
        print(f'                    {C.YELLOW}{line}{C.RST}')
    print(f'\n                    {C.GRAY}{C.ITALIC}*adjusts glasses nervously*{C.RST}')
    time.sleep(1.5)

# ═══════════════════════════════════════════════════════════════════════════
# MAIN DISPLAY - The grand finale
# ═══════════════════════════════════════════════════════════════════════════

def display_quote():
    """Display the quote with maximum theatrical flair."""
    clear_screen()
    
    # Split quote into paragraphs
    paragraphs = WOODY_QUOTE.strip().split('\n\n')
    
    # Top decoration
    print(f'\n{C.MAGENTA}{C.BOLD}{"═" * 70}{C.RST}')
    print(f'{C.MAGENTA}{C.BOLD}│{C.RST} {C.YELLOW}{C.BOLD}WOODY ALLEN\'S DAILY AFFIRMATION (Prescribed by My Analyst){C.RST} {C.MAGENTA}{C.BOLD}│{C.RST}')
    print(f'{C.MAGENTA}{C.BOLD}{"═" * 70}{C.RST}\n')
    
    # Woody face small
    mini_face = r"""
      \  |  /
     .--.\|/.--.
    |  @ @  @ @ |
    |           |
     \   \_/   /
      '.___.' 
    """
    for line in mini_face.strip().split('\n'):
        print(f'                    {C.YELLOW}{line}{C.RST}')
    print()
    
    # Type each paragraph
    colors = [C.WHITE, C.BRIGHT_CYAN, C.BRIGHT_YELLOW, C.BRIGHT_GREEN, C.BRIGHT_MAGENTA, C.BRIGHT_WHITE]
    
    for i, para in enumerate(paragraphs):
        color = colors[i % len(colors)]
        lines = para.split('\n')
        
        for line in lines:
            if line.strip() == '':
                print()
                continue
            
            # Typewriter effect for first paragraph, faster for others
            delay = 0.015 if i == 0 else 0.008
            typewriter(f'  {line}', delay=delay, color=color)
        
        print()  # Paragraph break
        time.sleep(0.4)
    
    # Bottom decoration
    print(f'\n{C.MAGENTA}{C.BOLD}{"═" * 70}{C.RST}')
    
    # Random neurotic footer
    footers = [
        "*checks pulse* ...yep, still anxious.",
        "*refills Xanax prescription* ...third time this week.",
        "*stares at ceiling* ...the ceiling stares back. It wins.",
        "*whispers to plant* ...you're my only friend who doesn't judge.",
        "*googles 'early bird special near me'* ...it's 4 PM. I qualify.",
    ]
    footer = random.choice(footers)
    print(f'{C.GRAY}{C.ITALIC}{" " * 25}{footer}{C.RST}')
    print(f'{C.MAGENTA}{C.BOLD}{"═" * 70}{C.RST}\n')

def credits():
    """Rolling credits because every neuroses needs production value."""
    time.sleep(1)
    clear_screen()
    
    credits_text = [
        ("DIRECTED BY", "My Anxiety"),
        ("WRITTEN BY", "3 AM Insomnia"),
        ("STARRING", "Existential Dread as Itself"),
        ("CO-STARRING", "Cholesterol as The Villain"),
        ("THERAPIST", "Dr. 'How Does That Make You Feel?' Goldstein"),
        ("LANDLORD", "Mr. 'Rent Is Due' Schwartz"),
        ("", ""),
        ("SPECIAL THANKS", "WebMD for the hypochondria"),
        ("", "My mother for the guilt"),
        ("", "The universe for the indifference"),
        ("", ""),
        ("NO EGOS WERE HARMED", "(They Were Already Fragile)"),
        ("", ""),
        ("This quote has been approved by", "the American Neurosis Association"),
        ("", ""),
        ("Remember:", "You're not paranoid if"),
        ("", "they're actually out to get you."),
    ]
    
    # Scroll credits
    lines = []
    for title, name in credits_text:
        if title and name:
            lines.append(f'{C.YELLOW}{title:>20}{C.RST}  {C.WHITE}{name}{C.RST}')
        elif title:
            lines.append(f'{C.BRIGHT_CYAN}{C.BOLD}{title:^45}{C.RST}')
        else:
            lines.append('')
    
    # Print all at once with fade effect
    for i, line in enumerate(lines):
        print(line)
        time.sleep(0.15)
    
    print(f'\n{C.GRAY}{C.ITALIC}{" " * 15}Press Ctrl+C to return to your regularly scheduled anxiety...{C.RST}\n')
    
    # Wait with blinking prompt
    try:
        blink = True
        while True:
            move_cursor(len(lines) + 5, 15)
            if blink:
                print(f'{C.RED}{C.BLINK}► PRESS ANY KEY TO DISSOCIATE ◄{C.RST}', end='', flush=True)
            else:
                print(f'{" " * 35}', end='', flush=True)
            blink = not blink
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

# ═══════════════════════════════════════════════════════════════════════════
# MAIN - Where the magic (and panic attacks) happen
# ═══════════════════════════════════════════════════════════════════════════

def main():
    hide_cursor()
    
    try:
        # Act 1: The Spiral
        animate_spiral(1.5)
        
        # Act 2: Brain Fart
        animate_brain_fart()
        
        # Act 3: Woody Enters
        woody_entrance()
        
        # Act 4: The Quote
        display_quote()
        
        # Act 5: Credits
        credits()
        
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear_screen()
        print(f'\n{C.YELLOW}{C.BOLD}')
        print('    "I don\'t want to achieve immortality through my work.')
        print('    I want to achieve it through not dying."')
        print(f'                                    — Woody Allen (probably){C.RST}')
        print(f'\n{C.GRAY}Thanks for visiting my neurosis. Come back soon.{C.RST}\n')

if __name__ == '__main__':
    # Check if terminal supports ANSI
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        print(WOODY_QUOTE)
    else:
        main()