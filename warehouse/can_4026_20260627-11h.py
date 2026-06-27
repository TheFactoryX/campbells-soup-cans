"""
Campbell's Soup Can #4026
Produced: 2026-06-27 11:03:30
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

pythonimport sys
import time
import random

# ANSI color codes
class C:
    R = '\033[91m'    # Red
    G = '\033[92m'    # Green
    Y = '\033[93m'    # Yellow
    B = '\033[94m'    # Blue
    M = '\033[95m'    # Magenta
    C = '\033[96m'    # Cyan
    W = '\033[97m'    # White
    D = '\033[90m'    # Dim
    BD = '\033[1m'    # Bold
    UL = '\033[4m'    # Underline
    BK = '\033[5m'    # Blink
    RS = '\033[0m'    # Reset
    BG_B = '\033[44m' # Blue background
    BG_R = '\033[41m' # Red background
    BG_K = '\033[40m' # Black background

# Woody Allen quote - original, neurotic, existential
QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\n"
    "It involves Russia. And peace. Mostly Russia.\n"
    "My therapist says I have a preoccupation with mortality.\n"
    "I told him, 'Doc, at my age, mortality isn't a preoccupation — it's a roommate.'"
)

# ASCII art frames for a little neurotic character
FRAMES = [
    f"""
{C.D}      @ @      {C.RS}
{C.D}     ( -.- )    {C.RS}
{C.D}     o_(")(")   {C.RS}
""",
    f"""
{C.Y}      @ @      {C.RS}
{C.Y}     ( o.o )    {C.RS}
{C.Y}     o_(")(")   {C.RS}
""",
    f"""
{C.M}      @ @      {C.RS}
{C.M}     ( @.@ )    {C.RS}
{C.M}     o_(")(")   {C.RS}
""",
]

# Neurotic thought bubbles
THOUGHTS = [
    f"{C.D}« Did I lock the door? »{C.RS}",
    f"{C.D}« Is this symptom serious? »{C.RS}",
    f"{C.D}« Why did I say that in 1997? »{C.RS}",
    f"{C.D}« The universe is expanding... into what? »{C.RS}",
    f"{C.D}« I should've been a dentist. »{C.RS}",
]

def clear_screen():
    print('\033[2J\033[H', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, delay=0.02, color=C.W):
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RS}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def typewriter_multiline(lines, delay=0.015, color=C.W):
    for i, line in enumerate(lines):
        move_cursor(12 + i, 4)
        for char in line:
            sys.stdout.write(f"{color}{char}{C.RS}")
            sys.stdout.flush()
            time.sleep(delay)
        print()

def draw_box(width=70, height=18, title=" WOODY ALLEN MODE: ACTIVATED "):
    top = f"{C.C}╔{'═' * (width - 2)}╗{C.RS}"
    title_line = f"{C.C}║{C.BD}{C.Y}{title.center(width - 2)}{C.RS}{C.C}║{C.RS}"
    mid = f"{C.C}╠{'═' * (width - 2)}╣{C.RS}"
    empty = f"{C.C}║{' ' * (width - 2)}║{C.RS}"
    bottom = f"{C.C}╚{'═' * (width - 2)}╝{C.RS}"
    
    lines = [top, title_line, mid] + [empty] * (height - 4) + [bottom]
    for i, line in enumerate(lines):
        move_cursor(i + 1, 5)
        print(line)

def animate_character(frames, cycles=3, delay=0.4):
    for _ in range(cycles):
        for frame in frames:
            move_cursor(5, 55)
            for line in frame.strip().split('\n'):
                move_cursor(5 + frame.strip().split('\n').index(line), 55)
                print(line.ljust(15))
            time.sleep(delay)

def float_thoughts(thoughts, count=8, delay=0.6):
    positions = [(4, 2), (6, 75), (9, 2), (11, 75), (14, 2), (16, 75), (8, 40), (13, 40)]
    for i in range(count):
        thought = random.choice(thoughts)
        y, x = random.choice(positions)
        move_cursor(y, x)
        print(f"{C.D}{C.BK}{thought}{C.RS}")
        time.sleep(delay)
        # Clear it
        move_cursor(y, x)
        print(' ' * len(thought))

def main():
    clear_screen()
    hide_cursor()
    
    # Draw the main box
    draw_box()
    
    # Show the neurotic character animating
    for _ in range(2):
        for frame in FRAMES:
            move_cursor(5, 55)
            for i, line in enumerate(frame.strip().split('\n')):
                move_cursor(5 + i, 55)
                print(line.ljust(15))
            time.sleep(0.5)
    
    # Float some neurotic thoughts
    float_thoughts(THOUGHTS, count=6, delay=0.4)
    
    # Type the quote
    quote_lines = QUOTE.split('\n')
    typewriter_multiline(quote_lines, delay=0.012, color=C.W)
    
    # Final flourish - signature
    time.sleep(0.5)
    move_cursor(18, 30)
    typewriter("— Woody Allen (probably) (definitely neurotic)", delay=0.02, color=C.M)
    
    # Bottom decoration
    move_cursor(20, 5)
    print(f"{C.C}═" * 70 + f"{C.RS}")
    move_cursor(21, 15)
    print(f"{C.D}Existential dread provided free of charge. No refunds. No exchanges.{C.RS}")
    move_cursor(22, 5)
    print(f"{C.C}═" * 70 + f"{C.RS}")
    
    # Return cursor to bottom
    move_cursor(24, 1)
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        show_cursor()
        print(f"\n{C.Y}Interrupted. The universe is indifferent anyway.{C.RS}\n")
    except Exception as e:
        show_cursor()
        print(f"\n{C.R}Error: {e}{C.RS}\n")