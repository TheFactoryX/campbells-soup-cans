"""
Campbell's Soup Can #4770
Produced: 2026-08-22 16:40:47
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
BLINK = '\033[5m'

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
ORANGE = '\033[38;5;208m'
PINK = '\033[38;5;213m'
GRAY = '\033[38;5;245m'
DARK_GRAY = '\033[38;5;238m'

# Backgrounds
BG_BLACK = '\033[40m'
BG_DARK = '\033[48;5;234m'

WOODY_FACE = f"""
{GRAY}      ┌─────────────┐{RESET}
{GRAY}      │  {WHITE}●{GRAY}   {WHITE}●{GRAY}  │  {CYAN}*adjusts glasses nervously*{RESET}
{GRAY}      │  {DIM}┌─────┐{GRAY}  │{RESET}
{GRAY}      │  {DIM}│     │{GRAY}  │  {YELLOW}"The universe is{RESET}
{GRAY}      │  {DIM}└─────┘{GRAY}  │  {YELLOW}indifferent, so{RESET}
{GRAY}      └─────────────┘  {YELLOW}I'm indifferent{RESET}
{GRAY}       │  │  │  │     {YELLOW}right back."{RESET}
{DIM}     ~~~~~~~~~~~~~~~{RESET}
"""

QUOTE = "I asked the void for a sign. It sent me a tax audit. That's not a sign, that's a threat."

NEUROTIC_THOUGHTS = [
    "Wait, is that a lump?",
    "Did I leave the stove on?",
    "Am I breathing too loud?",
    "What if everyone hates me?",
    "Is this sweater itchy or is it existential dread?",
    "Should I have ordered the soup?",
    "My cholesterol...",
    "Does the void have WiFi?",
]

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=WHITE, delay=0.03, jitter=0.02):
    for char in text:
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(delay + random.uniform(-jitter, jitter))
    print()

def neurotic_typewriter(text, color=YELLOW, base_delay=0.025):
    for i, char in enumerate(text):
        # Random "hesitation" pauses
        if char in '.,!?' and random.random() < 0.3:
            time.sleep(random.uniform(0.3, 0.8))
            # Insert neurotic interjection occasionally
            if random.random() < 0.15:
                thought = random.choice(NEUROTIC_THOUGHTS)
                print(f'\n{DIM}  [{thought}]{RESET}', end='', flush=True)
                time.sleep(0.5)
                print('\r' + ' ' * (len(thought) + 4) + '\r', end='', flush=True)
        
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(base_delay + random.uniform(-0.015, 0.025))
    print()

def draw_box(width=70, height=12, y=5, x=5, title=" WOODY ALLEN'S DAILY AFFIRMATION "):
    # Top border
    move_cursor(y, x)
    print(f'{MAGENTA}╔{"═" * (width-2)}╗{RESET}')
    
    # Title line
    move_cursor(y+1, x)
    title_padded = f' {title} '.center(width-2)
    print(f'{MAGENTA}║{BOLD}{CYAN}{title_padded}{RESET}{MAGENTA}║{RESET}')
    
    # Separator
    move_cursor(y+2, x)
    print(f'{MAGENTA}╠{"═" * (width-2)}╣{RESET}')
    
    # Content area (empty, we'll fill it)
    for i in range(height - 4):
        move_cursor(y+3+i, x)
        print(f'{MAGENTA}║{" " * (width-2)}║{RESET}')
    
    # Bottom border
    move_cursor(y+height-1, x)
    print(f'{MAGENTA}╚{"═" * (width-2)}╝{RESET}')

def animate_quote_appearance():
    box_y, box_x = 3, 8
    box_w, box_h = 74, 14
    content_y, content_x = box_y + 3, box_x + 2
    content_w = box_w - 4
    
    draw_box(box_w, box_h, box_y, box_x)
    
    # Show Woody face on the right
    face_lines = WOODY_FACE.strip().split('\n')
    for i, line in enumerate(face_lines):
        move_cursor(box_y + i, box_x + box_w + 3)
        print(line)
    
    # Type the quote in the box
    move_cursor(content_y, content_x)
    neurotic_typewriter(QUOTE, YELLOW, 0.02)
    
    # Add some decorative elements after
    time.sleep(0.5)
    
    # Bottom decorations
    move_cursor(content_y + 2, content_x)
    print(f'{DIM}─' * 40 + f'{RESET}')
    
    move_cursor(content_y + 3, content_x)
    typewriter("— Woody Allen (probably, maybe, I didn't fact-check)", GRAY, 0.015)
    
    move_cursor(content_y + 4, content_x)
    typewriter("(He's too anxious to verify this quote exists)", DIM, 0.01)
    
    # Neurotic footer
    time.sleep(0.3)
    move_cursor(content_y + 6, content_x)
    print(f'{CYAN}┌{"─" * 38}┐{RESET}')
    move_cursor(content_y + 7, content_x)
    print(f'{CYAN}│{RESET} {ITALIC}Side effects may include:{RESET}           {CYAN}│{RESET}')
    move_cursor(content_y + 8, content_x)
    print(f'{CYAN}│{RESET}  • Sudden urge to see analyst       {CYAN}│{RESET}')
    move_cursor(content_y + 9, content_x)
    print(f'{CYAN}│{RESET}  • Questioning reality (again)      {CYAN}│{RESET}')
    move_cursor(content_y + 10, content_x)
    print(f'{CYAN}│{RESET}  • Craving pastrami on rye          {CYAN}│{RESET}')
    move_cursor(content_y + 11, content_x)
    print(f'{CYAN}└{"─" * 38}┘{RESET}')

def anxiety_particles():
    """Little floating anxiety particles around the screen"""
    particles = ['⚡', '💭', '❓', '😰', '💊', '🥄', '📞', '🧠']
    for _ in range(15):
        y = random.randint(1, 25)
        x = random.randint(80, 110)
        char = random.choice(particles)
        color = random.choice([RED, YELLOW, MAGENTA, CYAN])
        move_cursor(y, x)
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(0.02)

def main():
    clear_screen()
    hide_cursor()
    
    try:
        # Intro animation - scrolling neurotic thoughts
        print(f'{BOLD}{MAGENTA}')
        print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║    ██╗    ██╗███████╗██╗     ██╗     ██████╗ ██████╗ ███╗   ███╗ ║
    ║    ██║    ██║██╔════╝██║     ██║    ██╔════╝██╔═══██╗████╗ ████║ ║
    ║    ██║ █╗ ██║█████╗  ██║     ██║    ██║     ██║   ██║██╔████╔██║ ║
    ║    ██║███╗██║██╔══╝  ██║     ██║    ██║     ██║   ██║██║╚██╔╝██║ ║
    ║    ╚███╔███╔╝███████╗███████╗██║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║ ║
    ║     ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝ ║
    ║                                                                  ║
    ║           P R E S E N T S :   D A I L Y   D R E A D             ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
        """)
        print(f'{RESET}')
        
        time.sleep(1)
        
        # Neurotic loading
        loading_phrases = [
            "Initializing existential crisis...",
            "Calibrating neurosis levels...",
            "Checking if I left the iron on...",
            "Consulting analyst (voicemail)...",
            "Ordering pastrami on rye...",
            "Loading quote (with reservations)...",
        ]
        
        for phrase in loading_phrases:
            print(f'\r{GRAY}[{CYAN}...{GRAY}] {WHITE}{phrase}{RESET}', end='', flush=True)
            time.sleep(random.uniform(0.4, 0.8))
        
        print(f'\r{GRAY}[{GREEN}✓{GRAY}] {GREEN}Ready to overthink{RESET}' + ' ' * 20)
        time.sleep(0.5)
        clear_screen()
        
        # Main animation
        animate_quote_appearance()
        
        # Anxiety particles in background
        time.sleep(0.5)
        anxiety_particles()
        
        # Final pause
        move_cursor(22, 10)
        print(f'{DIM}Press Enter to repress this memory...{RESET}', end='', flush=True)
        input()
        
    finally:
        show_cursor()
        clear_screen()
        print(f'{GREEN}Thanks for the session. That\'ll be $300.{RESET}')
        print(f'{DIM}(Cash only. I don't trust the banking system.){RESET}\n')

if __name__ == '__main__':
    main()