"""
Campbell's Soup Can #4411
Produced: 2026-08-02 13:54:54
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
    D = '\033[2m'       # Dim
    BD = '\033[1m'      # Bold
    IT = '\033[3m'      # Italic
    UL = '\033[4m'      # Underline
    BLINK = '\033[5m'   # Blink
    REV = '\033[7m'     # Reverse
    RS = '\033[0m'      # Reset

# Woody Allen quotes (original, in his style)
QUOTES = [
    "My analyst says I have a preoccupation with death. \nI told him, 'Doc, at my age, it's not a preoccupation — it's a savings plan.'",
    "I took a course in speed reading. \nFinished 'War and Peace' in twenty minutes. \nIt's about Russia.",
    "The universe is indifferent to my cholesterol level. \nWhich is unfair, because I'm very invested in its opinion.",
    "I don't believe in an afterlife, \nbut I'm bringing a change of underwear just in case.",
    "My hypochondria is the only thing keeping me alive. \nWithout imaginary symptoms, I'd have no reason to see doctors, \nand without doctors, who would validate my existence?",
    "I'm at that age where 'happy hour' \nis a nap at 3 PM with the TV on.",
    "Death is nature's way of telling you to slow down. \nMy doctor says the same thing. \nNeither of them accepts my insurance.",
    "I have a metaphysical conflict with gravity. \nIt keeps pulling me down when I'm trying to rise above it all."
]

def clear_screen():
    print('\033[2J\033[H', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=C.W, delay=0.03, newline=True):
    for char in text:
        print(f'{color}{char}{C.RS}', end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def glitch_text(text, color=C.M, iterations=5):
    glitch_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'
    for _ in range(iterations):
        glitched = ''.join(
            random.choice(glitch_chars) if random.random() < 0.1 else c
            for c in text
        )
        move_cursor(1, 1)
        print(f'{color}{glitched}{C.RS}', end='', flush=True)
        time.sleep(0.08)
    move_cursor(1, 1)
    print(f'{color}{text}{C.RS}', end='', flush=True)

def draw_box(title, content_lines, width=70):
    top = f'{C.C}╔{"═" * (width - 2)}╗{C.RS}'
    bottom = f'{C.C}╚{"═" * (width - 2)}╝{C.RS}'
    title_line = f'{C.C}║{C.RS} {C.BD}{C.Y}{title.center(width - 4)}{C.RS} {C.C}║{C.RS}'
    empty = f'{C.C}║{" " * (width - 2)}║{C.RS}'
    
    print(top)
    print(title_line)
    print(empty)
    for line in content_lines:
        padded = line.ljust(width - 4)
        print(f'{C.C}║{C.RS} {C.W}{padded}{C.RS} {C.C}║{C.RS}')
    print(empty)
    print(bottom)

def woody_ascii():
    return f'''{C.Y}
    ╭─────────────────────╮
    │  (•_•)              │
    │  <)   )╯  WOODY     │
    │  /   \\   ALLEN      │
    ╰─────────────────────╯
{C.RS}'''

def neurotic_banner():
    banner = f'''{C.M}{C.BD}
╔═══════════════════════════════════════════════════════════════════════╗
║  ██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗  █████╗ ████████╗ ║
║  ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝ ║
║  ██║ █╗ ██║██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝███████║   ██║    ║
║  ██║███╗██║██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗██╔══██║   ██║    ║
║  ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║██║  ██║   ██║    ║
║   ╚══╝╚══╝  ╚═════╝ ╚══╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ║
║                                                                      ║
║  {C.Y}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{C.M} ║
║  {C.Y}█ {C.C}PHILOSOPHICAL NEUROSIS GENERATOR v3.14159{C.Y}  █ {C.G}ERROR: EXISTENCE NOT FOUND{C.Y} █║
║  {C.Y}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{C.M} ║
╚═══════════════════════════════════════════════════════════════════════╝{C.RS}'''
    return banner

def spinning_loader(text, duration=2):
    spinner = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
    start = time.time()
    i = 0
    while time.time() - start < duration:
        print(f'\r{C.C}{spinner[i % len(spinner)]}{C.RS} {C.D}{text}{C.RS}', end='', flush=True)
        time.sleep(0.08)
        i += 1
    print(f'\r{C.G}✓{C.RS} {C.D}{text}{C.RS}      ')

def main():
    hide_cursor()
    clear_screen()
    
    # Show neurotic banner
    print(neurotic_banner())
    print()
    
    # Simulate "system boot"
    spinning_loader("Initializing existential dread module...", 1.5)
    spinning_loader("Calibrating hypochondria sensors...", 1.2)
    spinning_loader("Loading Jewish guilt drivers...", 1.0)
    spinning_loader("Connecting to analyst's WiFi...", 0.8)
    print()
    
    # Pick a quote
    quote = random.choice(QUOTES)
    quote_lines = quote.split('\n')
    
    # Typewriter effect for the quote
    print(f'{C.C}{"─" * 76}{C.RS}')
    print(f'{C.BD}{C.Y}  TODAY\'S DIAGNOSIS:{C.RS}')
    print(f'{C.C}{"─" * 76}{C.RS}')
    print()
    
    for i, line in enumerate(quote_lines):
        if i == 0:
            typewriter(f'  {line}', C.W, 0.02)
        else:
            typewriter(f'     {line}', C.D, 0.02)
    
    print()
    print(f'{C.C}{"─" * 76}{C.RS}')
    
    # Woody ASCII
    print(woody_ascii())
    
    # Final neurotic footer
    footers = [
        "Prescription: Two aspirin and a viewing of 'Annie Hall'. Call me in the morning.",
        "Side effects may include: overthinking, therapist bills, and sudden urges to play clarinet.",
        "Warning: This quote contains trace amounts of mortality. May cause 3AM panic.",
        "Your existential crisis has been logged. Invoice to follow.",
        "Remember: You're not paranoid if the universe really IS out to get you."
    ]
    
    print(f'{C.D}{C.IT}  {random.choice(footers)}{C.RS}')
    print()
    
    # Blinking "press any key" style
    for _ in range(6):
        print(f'\r{C.BLINK}{C.R}  ◆ SESSION TERMINATED ◆{C.RS}   ', end='', flush=True)
        time.sleep(0.5)
        print(f'\r{" " * 30}', end='', flush=True)
        time.sleep(0.3)
    
    print(f'\r{C.G}  ◆ SESSION TERMINATED ◆{C.RS}')
    print(f'{C.D}  (Your analyst has been notified. Your mother has been cc\'d.){C.RS}')
    print()
    
    show_cursor()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f'\n{C.R}Interrupted. Even my code has commitment issues.{C.RS}')
        sys.exit(0)