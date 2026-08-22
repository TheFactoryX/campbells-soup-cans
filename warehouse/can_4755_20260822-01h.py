"""
Campbell's Soup Can #4755
Produced: 2026-08-22 01:49:51
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
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

# Bright colors
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

# Backgrounds
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

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(x, y):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, delay=0.03, color=WHITE):
    for char in text:
        sys.stdout.write(f'{color}{char}{RESET}')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch_text(text, x, y, color=WHITE, glitch_chars='!@#$%^&*()_+-=[]{}|;:,.<>?'):
    for i, char in enumerate(text):
        move_cursor(x + i, y)
        if random.random() < 0.1:
            sys.stdout.write(f'{RED}{random.choice(glitch_chars)}{RESET}')
        else:
            sys.stdout.write(f'{color}{char}{RESET}')
        sys.stdout.flush()
        time.sleep(0.02)

def draw_box(width, height, x, y, color=CYAN, title=""):
    # Top border
    move_cursor(x, y)
    print(f'{color}┌{"─" * (width - 2)}┐{RESET}', end='')
    
    # Title
    if title:
        move_cursor(x + (width - len(title)) // 2, y)
        print(f'{color}┤ {BOLD}{title}{RESET}{color} ├{RESET}', end='')
    
    # Side borders
    for i in range(1, height - 1):
        move_cursor(x, y + i)
        print(f'{color}│{" " * (width - 2)}│{RESET}', end='')
    
    # Bottom border
    move_cursor(x, y + height - 1)
    print(f'{color}└{"─" * (width - 2)}┘{RESET}', end='')

def sparkle_animation(width, height, x, y, duration=2):
    chars = ['✦', '✧', '⋆', '✵', '✸', '✹', '✺', '✷', '✶', '✴', '✳', '❋', '❊', '❉', '✱', '✲', '✳', '✴']
    colors = [BRIGHT_YELLOW, BRIGHT_CYAN, BRIGHT_MAGENTA, BRIGHT_WHITE, BRIGHT_GREEN]
    start = time.time()
    while time.time() - start < duration:
        for _ in range(3):
            sx = random.randint(x + 1, x + width - 2)
            sy = random.randint(y + 1, y + height - 2)
            move_cursor(sx, sy)
            c = random.choice(chars)
            col = random.choice(colors)
            print(f'{col}{c}{RESET}', end='')
            sys.stdout.flush()
        time.sleep(0.1)
        # Clear sparkles
        for _ in range(3):
            sx = random.randint(x + 1, x + width - 2)
            sy = random.randint(y + 1, y + height - 2)
            move_cursor(sx, sy)
            print(' ', end='')
            sys.stdout.flush()

def woody_face():
    return f"""{YELLOW}
    ╭─────────────╮
    │  @      @   │  ← My therapist says I have
    │             │     a preoccupation with
    │   \\_____/   │     mortality. I told him,
    │             │     "Doc, I'm not preoccupied
    ╰─────────────╯     with it. I'm just...
                        very well-acquainted."
{RESET}"""

def main():
    clear_screen()
    hide_cursor()
    
    # The Woody Allen quote
    quote = "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia."
    
    # Alternative quotes (pick one)
    quotes = [
        "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
        "My one regret in life is that I'm not someone else. Preferably someone with better posture and a 401(k).",
        "The universe is indifferent, my back hurts, and I'm pretty sure my toaster is judging me.",
        "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
        "Life is divided into the horrible and the miserable. I'm currently hovering at 'horrible' with a chance of 'miserable' by Tuesday.",
        "I'm not a hypochondriac, I'm just... symptomatically curious. WebMD says I have 47 fatal diseases. It's Thursday.",
        "God is silent. Now if only my mother would be.",
        "I have a existential crisis scheduled for 3 PM. Can we reschedule? My anxiety has a prior engagement.",
        "Death is nature's way of telling you to slow down. My cholesterol is nature's way of telling you to stop eating pastrami.",
        "I can't listen to Wagner. I start getting the urge to conquer Poland. I can't even conquer my inbox."
    ]
    
    selected_quote = random.choice(quotes)
    
    # Screen dimensions
    term_width = 80
    term_height = 25
    
    # Draw main box
    box_w = 70
    box_h = 16
    box_x = (term_width - box_w) // 2
    box_y = 3
    
    draw_box(box_w, box_h, box_x, box_y, CYAN, " WOODY ALLEN WISDOM ")
    
    # Draw Woody face on the left
    face_lines = woody_face().split('\n')
    face_x = box_x - 20
    face_y = box_y + 2
    for i, line in enumerate(face_lines):
        move_cursor(face_x, face_y + i)
        print(line, end='')
    
    # Animate sparkles around the box
    import threading
    sparkle_thread = threading.Thread(target=sparkle_animation, args=(box_w, box_h, box_x, box_y, 3))
    sparkle_thread.start()
    
    # Type the quote in the box
    quote_x = box_x + 4
    quote_y = box_y + 3
    
    # Word wrap the quote
    words = selected_quote.split()
    lines = []
    current_line = ""
    max_width = box_w - 8
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_width:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Type each line
    for i, line in enumerate(lines):
        move_cursor(quote_x, quote_y + i * 2)
        typewriter(line, delay=0.02, color=BRIGHT_WHITE)
        time.sleep(0.3)
    
    sparkle_thread.join()
    
    # Add some philosophical decoration
    decor_y = quote_y + len(lines) * 2 + 1
    
    # Left decoration
    move_cursor(quote_x, decor_y)
    print(f'{MAGENTA}◈{RESET} {ITALIC}{DIM}"The only thing worse than death is...{RESET}')
    move_cursor(quote_x, decor_y + 1)
    print(f'{MAGENTA}◈{RESET} {ITALIC}{DIM}having to assemble IKEA furniture{RESET}')
    move_cursor(quote_x, decor_y + 2)
    print(f'{MAGENTA}◈{RESET} {ITALIC}{DIM}for eternity."{RESET}')
    
    # Right decoration - neurotic thoughts
    neurotic_x = box_x + box_w - 35
    neurotic_thoughts = [
        "• Did I lock the door?",
        "• Is that a mole?",
        "• Why did I say that in 2003?",
        "• Am I breathing correctly?",
        "• Does my cat resent me?",
        "• Is the stove off?",
        "• What if I'm a simulation?",
        "• Why does my knee click?",
    ]
    
    for i, thought in enumerate(neurotic_thoughts):
        move_cursor(neurotic_x, box_y + 2 + i)
        color = random.choice([BRIGHT_RED, BRIGHT_YELLOW, BRIGHT_MAGENTA, BRIGHT_CYAN])
        print(f'{color}{thought}{RESET}', end='')
        sys.stdout.flush()
        time.sleep(0.15)
    
    # Bottom signature
    sig_y = box_y + box_h + 1
    move_cursor((term_width - 40) // 2, sig_y)
    print(f'{YELLOW}{BOLD}— Woody Allen (probably, maybe, who knows?) {RESET}')
    
    move_cursor((term_width - 50) // 2, sig_y + 1)
    print(f'{DIM}Generated by a neurotic algorithm with existential dread{RESET}')
    
    # Final sparkle burst
    for _ in range(10):
        sx = random.randint(box_x + 1, box_x + box_w - 2)
        sy = random.randint(box_y + 1, box_y + box_h - 2)
        move_cursor(sx, sy)
        c = random.choice(['✦', '✧', '⋆', '✵', '✸', '✹'])
        col = random.choice([BRIGHT_YELLOW, BRIGHT_CYAN, BRIGHT_MAGENTA, BRIGHT_WHITE])
        print(f'{col}{c}{RESET}', end='')
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Move cursor to bottom
    move_cursor(1, term_height)
    show_cursor()
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f'\n{YELLOW}Exiting... my anxiety appreciates the break.{RESET}\n')
    except Exception as e:
        show_cursor()
        print(f'\n{RED}Error: {e}{RESET}\n')