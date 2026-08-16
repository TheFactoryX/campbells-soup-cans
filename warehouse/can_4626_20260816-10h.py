"""
Campbell's Soup Can #4626
Produced: 2026-08-16 10:39:58
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
    R = '\033[91m'      # Red
    G = '\033[92m'      # Green
    Y = '\033[93m'      # Yellow
    B = '\033[94m'      # Blue
    M = '\033[95m'      # Magenta
    C = '\033[96m'      # Cyan
    W = '\033[97m'      # White
    D = '\033[90m'      # Dim
    BD = '\033[1m'      # Bold
    UL = '\033[4m'      # Underline
    BLINK = '\033[5m'   # Blink
    REV = '\033[7m'     # Reverse
    RS = '\033[0m'      # Reset
    CLR = '\033[2J\033[H'  # Clear screen

# Original Woody Allen-style quote
QUOTE = (
    "I told my analyst I'm having an existential crisis.\n"
    "He said, 'That'll be $300.' I said, 'For the crisis or the hour?'\n"
    "He said, 'The hour. The crisis is complimentary —\n"
    "  the universe provides those for free, usually around 3 AM.'"
)

# ASCII art - little neurotic face
WOODY_FACE = r"""
        \   ^__^   /
         \  (o o)  /
            ( > )
           /  |  \
          /   |   \
         ~~~  ~~~  ~~~
"""

# Decorative border pieces
TL, TR, BL, BR = '╔', '╗', '╚', '╝'
H, V = '═', '║'
TL2, TR2, BL2, BR2 = '┌', '┐', '└', '┘'
H2, V2 = '─', '│'

def typewriter(text, color=C.W, delay=0.015, end='\n'):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(f'{color}{char}{C.RS}')
        sys.stdout.flush()
        if char != '\n':
            time.sleep(delay * random.uniform(0.5, 1.5))
        else:
            time.sleep(delay * 3)
    if end:
        sys.stdout.write(end)
        sys.stdout.flush()

def slow_print_lines(lines, color=C.W, delay=0.02):
    """Print multiple lines with typewriter effect."""
    for i, line in enumerate(lines):
        typewriter(line, color, delay)
        if i < len(lines) - 1:
            time.sleep(0.15)

def blink_text(text, color=C.Y, times=3, interval=0.4):
    """Make text blink."""
    for _ in range(times):
        sys.stdout.write(f'\r{color}{C.BLINK}{text}{C.RS}')
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write(f'\r{" " * len(text)}')
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write(f'\r{color}{text}{C.RS}\n')
    sys.stdout.flush()

def draw_box(lines, width=None, padding=2, border_color=C.C, text_color=C.W):
    """Draw a fancy box around text lines."""
    if width is None:
        width = max(len(line) for line in lines) + padding * 2
    
    content_width = width - 4  # account for borders and spaces
    
    # Top border
    print(f'{border_color}{TL}{H * (width - 2)}{TR}{C.RS}')
    
    for line in lines:
        # Center the line
        padded = line.center(content_width)
        print(f'{border_color}{V}{C.RS} {text_color}{padded}{C.RS} {border_color}{V}{C.RS}')
    
    # Bottom border
    print(f'{border_color}{BL}{H * (width - 2)}{BR}{C.RS}')

def animated_intro():
    """Show a fun animated intro."""
    print(C.CLR, end='')
    
    # Floating particles
    for frame in range(20):
        print(C.CLR, end='')
        particles = ['✦', '⋆', '✧', '⋆', '✦', '⋆']
        for _ in range(5):
            x = random.randint(0, 60)
            y = random.randint(0, 10)
            p = random.choice(particles)
            color = random.choice([C.Y, C.C, C.M, C.G])
            print(f'\033[{y};{x}H{color}{p}{C.RS}', end='')
        sys.stdout.flush()
        time.sleep(0.08)
    
    # Title reveal
    print(C.CLR, end='')
    title = "WOODY ALLEN'S MIDNIGHT MONOLOGUE"
    for i, ch in enumerate(title):
        sys.stdout.write(f'\033[5;{20+i}H{C.Y}{C.BD}{ch}{C.RS}')
        sys.stdout.flush()
        time.sleep(0.06)
    
    subtitle = "A Neurotic Philosophy Production"
    for i, ch in enumerate(subtitle):
        sys.stdout.write(f'\033[7;{25+i}H{C.D}{ch}{C.RS}')
        sys.stdout.flush()
        time.sleep(0.04)
    
    time.sleep(1)
    print(C.CLR, end='')

def show_woody_face():
    """Display the ASCII face with color animation."""
    lines = WOODY_FACE.strip().split('\n')
    colors = [C.R, C.Y, C.G, C.C, C.B, C.M]
    
    for _ in range(2):
        for i, line in enumerate(lines):
            color = colors[(i + _) % len(colors)]
            sys.stdout.write(f'\033[{12+i};15H{color}{line}{C.RS}')
        sys.stdout.flush()
        time.sleep(0.5)
    
    # Final colorful version
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        sys.stdout.write(f'\033[{12+i};15H{color}{line}{C.RS}')
    sys.stdout.flush()
    print('\n' * 3)

def main():
    # Animated intro
    animated_intro()
    
    # Show Woody face
    show_woody_face()
    
    # Quote lines
    quote_lines = QUOTE.split('\n')
    
    # Draw the quote in a fancy box
    draw_box(quote_lines, width=70, border_color=C.M, text_color=C.W)
    
    print()
    
    # Typewriter the quote again for effect
    print(f'{C.D}{"─" * 60}{C.RS}')
    print(f'{C.C}{C.BD}★  The Transcript  ★{C.RS}')
    print(f'{C.D}{"─" * 60}{C.RS}\n')
    
    slow_print_lines(quote_lines, color=C.Y, delay=0.018)
    
    print()
    print(f'{C.D}{"─" * 60}{C.RS}')
    
    # Final philosophical punchline
    punchlines = [
        "The universe doesn't bill by the hour. It bills by the anxiety.",
        "My neuroses have neuroses. They're very co-dependent.",
        "I'd join a support group for existential dread,\nbut they meet at 3 AM and I have insomnia.",
        "Death is nature's way of saying 'Your subscription has expired.'\nAnd there's no auto-renew option.",
    ]
    
    chosen = random.choice(punchlines)
    print(f'\n{C.G}{C.BD}━━━ POST-CREDITS SCENE ━━━{C.RS}\n')
    typewriter(chosen, color=C.G, delay=0.02)
    
    # Final blink
    print()
    blink_text("◉ The analyst has entered the chat ◉", C.M, times=2)
    
    # Fade out
    print(f'\n{C.D}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.RS}')
    for i in range(5, 0, -1):
        sys.stdout.write(f'\r{C.D}Fading into neurotic oblivion in {i}...{C.RS}')
        sys.stdout.flush()
        time.sleep(0.4)
    
    print(f'\r{C.CLR}{C.G}Session terminated. The crisis remains.{C.RS}\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{C.R}\nInterrupted. Even my code has commitment issues.{C.RS}\n')
        sys.exit(0)