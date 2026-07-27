"""
Campbell's Soup Can #4346
Produced: 2026-07-27 11:38:55
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
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    X = '\033[0m'       # Reset

# The quote - original Woody Allen style
QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\n"
    "It involves Russia. And peace. Mostly Russia.\n\n"
    "My therapist says I have a preoccupation with mortality.\n"
    "I told her, 'Doc, at my age, mortality isn't a preoccupation—\n"
    "it's a roommate who doesn't pay rent and eats all the yogurt.'\n\n"
    "The universe is indifferent. My lower back is hostile.\n"
    "And somewhere, a dentist is judging my flossing technique.\n\n"
    "I don't want to achieve immortality through my work.\n"
    "I want to achieve it through not dying.\n"
    "Failing that, a really good pastrami on rye would suffice."
)

ATTRIBUTION = "— Woody Allen (probably, in an alternate timeline where he writes Python)"

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def typewriter(text, color=C.W, delay=0.02, jitter=0.015):
    """Type text with a typewriter effect."""
    for char in text:
        print(f"{color}{char}{C.X}", end='', flush=True)
        time.sleep(delay + random.uniform(-jitter, jitter))
    print()

def glitch_text(text, color=C.R, intensity=3):
    """Briefly glitch the text."""
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    for _ in range(intensity):
        glitched = ''.join(
            random.choice(glitch_chars) if random.random() < 0.15 else c
            for c in text
        )
        move_cursor(1, 1)
        print(f"{color}{glitched}{C.X}")
        time.sleep(0.05)
    move_cursor(1, 1)
    print(f"{color}{text}{C.X}")

def draw_box(width, height, color=C.C, style='double'):
    """Draw a decorative box."""
    if style == 'double':
        tl, tr, bl, br = '╔', '╗', '╚', '╝'
        h, v = '═', '║'
    elif style == 'single':
        tl, tr, bl, br = '┌', '┐', '└', '┘'
        h, v = '─', '│'
    else:
        tl, tr, bl, br = '╭', '╮', '╰', '╯'
        h, v = '─', '│'
    
    top = f"{color}{tl}{h * (width - 2)}{tr}{C.X}"
    bottom = f"{color}{bl}{h * (width - 2)}{br}{C.X}"
    middle = f"{color}{v}{C.X}{' ' * (width - 2)}{color}{v}{C.X}"
    
    return top, bottom, middle

def neurotic_loader():
    """A neurotic loading animation."""
    thoughts = [
        "Checking if I left the stove on...",
        "Wondering if that mole is new...",
        "Replaying a conversation from 2003...",
        "Calculating probability of spontaneous combustion...",
        "Questioning the nature of reality...",
        "Remembering I need to floss...",
        "Panic attack scheduled for 3pm...",
        "Existential dread loading... ████░░░░ 40%",
    ]
    for i, thought in enumerate(thoughts):
        move_cursor(20, 2)
        print(f"{C.DIM}{C.Y}[{i+1}/8] {thought}{' ' * 20}{C.X}")
        time.sleep(0.4)

def sparkle_animation(width, duration=2):
    """Sparkle effect around the box."""
    sparkles = ['✦', '✧', '⋆', '✩', '✪', '✫', '✬', '✭', '✮', '✯']
    start = time.time()
    while time.time() - start < duration:
        for _ in range(3):
            x = random.randint(2, width - 1)
            y = random.randint(2, 18)
            move_cursor(y, x)
            print(f"{C.Y}{random.choice(sparkles)}{C.X}", end='', flush=True)
        time.sleep(0.15)
        # Clear sparkles
        for _ in range(3):
            x = random.randint(2, width - 1)
            y = random.randint(2, 18)
            move_cursor(y, x)
            print(" ", end='', flush=True)

def breathe_text(text, color=C.M, cycles=2):
    """Make text breathe (fade in/out)."""
    for _ in range(cycles):
        for intensity in [C.DIM, '', C.BOLD]:
            move_cursor(22, 2)
            print(f"{color}{intensity}{text}{C.X}{' ' * 40}")
            time.sleep(0.4)

def main():
    clear_screen()
    hide_cursor()
    
    # Terminal size detection fallback
    width = 78
    height = 24
    
    # Draw the main box
    top, bottom, middle = draw_box(width, height, C.C, 'double')
    
    print(top)
    for _ in range(height - 2):
        print(middle)
    print(bottom)
    
    # Title
    move_cursor(2, (width - 32) // 2)
    print(f"{C.BOLD}{C.Y}═══ WOODY ALLEN WISDOM ENGINE ═══{C.X}")
    
    move_cursor(3, (width - 18) // 2)
    print(f"{C.DIM}{C.M}neurotic.exe v1.0.4{C.X}")
    
    # Decorative corners
    corners = [
        (1, 1, '◈'), (1, width - 2, '◈'),
        (height, 1, '◈'), (height, width - 2, '◈'),
    ]
    for r, c, ch in corners:
        move_cursor(r, c)
        print(f"{C.M}{ch}{C.X}")
    
    # Side decorations
    for i in range(4, height - 2, 3):
        move_cursor(i, 2)
        print(f"{C.DIM}{C.B}░░░{C.X}")
        move_cursor(i, width - 5)
        print(f"{C.DIM}{C.B}░░░{C.X}")
    
    # Neurotic loader
    neurotic_loader()
    
    # Type the quote
    lines = QUOTE.split('\n')
    start_row = 6
    
    for i, line in enumerate(lines):
        move_cursor(start_row + i * 2, 4)
        if line.strip() == "":
            continue
        # Color variation per line
        colors = [C.W, C.C, C.G, C.Y, C.M, C.B]
        typewriter(line, color=colors[i % len(colors)], delay=0.015)
        time.sleep(0.15)
    
    # Attribution with flair
    time.sleep(0.5)
    move_cursor(start_row + len(lines) * 2, 4)
    typewriter(ATTRIBUTION, color=C.DIM + C.C, delay=0.02)
    
    # Sparkle celebration
    sparkle_animation(width, 1.5)
    
    # Breathing footer
    footer = "Press Ctrl+C to escape existence (or just close the terminal)"
    breathe_text(footer, C.Y, 3)
    
    # Final glitch on the title
    move_cursor(2, (width - 32) // 2)
    glitch_text("═══ WOODY ALLEN WISDOM ENGINE ═══", C.R, 2)
    
    # Keep alive for a moment
    time.sleep(1)
    
    show_cursor()
    move_cursor(height + 1, 1)
    print(f"{C.DIM}Session terminated. The universe remains indifferent.{C.X}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f"\n{C.Y}Interrupted. I knew I shouldn't have compiled this.{C.X}\n")
        sys.exit(0)
    except Exception as e:
        show_cursor()
        print(f"\n{C.R}Error: {e}{C.X}")
        print(f"{C.DIM}Even the code has anxiety.{C.X}\n")