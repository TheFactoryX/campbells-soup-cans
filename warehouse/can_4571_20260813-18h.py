"""
Campbell's Soup Can #4571
Produced: 2026-08-13 18:08:28
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
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    X = '\033[0m'
    
    # Bright backgrounds
    BG_R = '\033[101m'
    BG_G = '\033[102m'
    BG_Y = '\033[103m'
    BG_B = '\033[104m'
    BG_M = '\033[105m'
    BG_C = '\033[106m'

# Original Woody Allen-style quote
QUOTE = (
    "I told my analyst I was having an identity crisis, "
    "and he said, 'That'll be $300 — and by the way, "
    "who's asking?'"
)

AUTHOR = "— Woody Allen (probably)"

# ASCII art frames
FRAMES = [
    r"""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║  {quote}  ║
    ║                                                          ║
    ║                        {author}          ║
    ╚══════════════════════════════════════════════════════════╝
    """,
    r"""
     ┌────────────────────────────────────────────────────────┐
     │                                                        │
     │   {quote}   │
     │                                                        │
     │                                    {author}  │
     └────────────────────────────────────────────────────────┘
    """,
    r"""
      ╭────────────────────────────────────────────────────╮
      │                                                    │
      │  {quote}  │
      │                                                    │
      │                                  {author}  │
      ╰────────────────────────────────────────────────────╯
    """,
]

# Woody's face ASCII
WOODY_FACES = [
    r"""
       \   /
        \ /
     .--*--.
    /  (o)(o)  \
   |   ( __ )   |
    \   \__/   /
     '.____.'
    """,
    r"""
       \   /
        \ /
     .--*--.
    /  (-)(-)  \
   |   ( .. )   |
    \   \__/   /
     '.____.'
    """,
    r"""
       \   /
        \ /
     .--*--.
    /  (o)(o)  \
   |   ( >< )   |
    \   \__/   /
     '.____.'
    """,
]

# Neurotic thought bubbles
THOUGHTS = [
    "Wait, did I lock the door?",
    "Is that a symptom? WebMD says yes.",
    "My cholesterol just reading this.",
    "Should've been a dentist. Parents happy.",
    "Existential dread: $0. Therapy: $300/hr.",
    "Am I breathing manually now?",
    "Did I say 'you too' to 'enjoy your meal'?",
]

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.W, delay=0.02, newline=True):
    for ch in text:
        sys.stdout.write(f'{color}{ch}{C.X}')
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def rainbow_text(text):
    colors = [C.R, C.Y, C.G, C.C, C.B, C.M]
    result = ""
    for i, ch in enumerate(text):
        if ch != ' ':
            result += colors[i % len(colors)] + ch + C.X
        else:
            result += ' '
    return result

def glitch_text(text, intensity=0.1):
    glitch_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    result = ""
    for ch in text:
        if ch != ' ' and random.random() < intensity:
            result += C.R + random.choice(glitch_chars) + C.X
        else:
            result += ch
    return result

def animate_woody_face(cycles=3):
    for _ in range(cycles):
        for face in WOODY_FACES:
            clear_screen()
            print(C.Y + face + C.X)
            time.sleep(0.3)

def falling_thoughts():
    """Animate neurotic thoughts falling down"""
    cols = 80
    rows = 20
    thoughts = THOUGHTS.copy()
    random.shuffle(thoughts)
    
    positions = []
    for i, thought in enumerate(thoughts[:5]):
        positions.append({
            'x': random.randint(5, cols - len(thought) - 5),
            'y': -i * 3,
            'text': thought,
            'speed': random.uniform(0.1, 0.3),
            'color': random.choice([C.R, C.Y, C.G, C.C, C.M])
        })
    
    for frame in range(30):
        clear_screen()
        # Draw Woody face at bottom
        print(C.Y + WOODY_FACES[0] + C.X)
        print()
        
        for p in positions:
            if p['y'] < rows:
                move_cursor(p['y'] + 10, p['x'])
                sys.stdout.write(f"{p['color']}{p['text']}{C.X}")
        
        # Update positions
        for p in positions:
            p['y'] += p['speed']
        
        sys.stdout.flush()
        time.sleep(0.1)

def pulse_border(text, cycles=2):
    """Pulse the border colors"""
    frame = FRAMES[0]
    colors = [C.R, C.Y, C.G, C.C, C.B, C.M]
    
    for cycle in range(cycles * 6):
        color = colors[cycle % len(colors)]
        clear_screen()
        print(color + frame.format(quote=text, author=AUTHOR) + C.X)
        time.sleep(0.15)

def matrix_rain_quote():
    """Quote appears like matrix rain"""
    lines = [
        "I told my analyst I was having an identity crisis,",
        "and he said, 'That'll be $300 — and by the way,",
        "who's asking?'",
        "",
        "— Woody Allen (probably)"
    ]
    
    cols = 80
    drops = []
    for i, line in enumerate(lines):
        drops.append({
            'chars': list(line),
            'x': (cols - len(line)) // 2,
            'y': i * 2 + 5,
            'revealed': 0,
            'color': random.choice([C.G, C.C, C.Y, C.M])
        })
    
    for frame in range(60):
        clear_screen()
        
        # Draw Woody
        print(C.Y + WOODY_FACES[frame % len(WOODY_FACES)] + C.X)
        print()
        
        for drop in drops:
            if drop['revealed'] < len(drop['chars']):
                drop['revealed'] += 1
            
            visible = ''.join(drop['chars'][:drop['revealed']])
            move_cursor(drop['y'] + 10, drop['x'])
            sys.stdout.write(f"{drop['color']}{visible}{C.X}")
        
        sys.stdout.flush()
        time.sleep(0.08)
    
    # Final pause
    time.sleep(2)

def typewriter_reveal():
    """Classic typewriter effect with Woody commentary"""
    clear_screen()
    print(C.Y + WOODY_FACES[0] + C.X)
    print()
    
    # Type the quote
    parts = [
        ("I told my analyst ", C.W),
        ("I was having an identity crisis, ", C.Y),
        ("and he said, ", C.W),
        ("'That'll be $300 ", C.R + C.BOLD),
        ("— and by the way, ", C.C),
        ("who's asking?'", C.M + C.BOLD),
    ]
    
    for text, color in parts:
        typewriter(text, color=color, delay=0.04, newline=False)
    
    print()
    print()
    typewriter(AUTHOR, color=C.C + C.DIM, delay=0.06)
    print()
    print()
    
    # Neurotic afterthoughts
    afterthoughts = [
        "    (Note: He doesn't take insurance.)",
        "    (Note: I still don't know who I am.)",
        "    (Note: The $300 was a copay. My deductible is $4,000.)",
        "    (Note: I should've just Googled my symptoms like everyone else.)",
    ]
    
    for thought in afterthoughts:
        typewriter(thought, color=C.DIM + C.B, delay=0.02)
        time.sleep(0.3)

def neon_sign_effect():
    """Quote as a flickering neon sign"""
    lines = [
        "I told my analyst I was having an identity crisis,",
        "and he said, 'That'll be $300 — and by the way,",
        "who's asking?'",
        "",
        "— Woody Allen (probably)"
    ]
    
    neon_colors = [C.R, C.M, C.B, C.C, C.G, C.Y]
    
    for flicker in range(20):
        clear_screen()
        print(C.Y + WOODY_FACES[flicker % len(WOODY_FACES)] + C.X)
        print()
        
        for i, line in enumerate(lines):
            color = neon_colors[(i + flicker) % len(neon_colors)]
            # Random flicker
            if random.random() < 0.1:
                line_display = glitch_text(line, 0.3)
            else:
                line_display = line
            
            # Center it
            padding = (80 - len(line)) // 2
            print(' ' * padding + color + C.BOLD + line_display + C.X)
        
        time.sleep(0.15)
    
    # Steady final version
    clear_screen()
    print(C.Y + WOODY_FACES[0] + C.X)
    print()
    for i, line in enumerate(lines):
        color = neon_colors[i % len(neon_colors)]
        padding = (80 - len(line)) // 2
        print(' ' * padding + color + C.BOLD + line + C.X)

def main():
    hide_cursor()
    try:
        # Randomly pick an animation style
        style = random.randint(1, 5)
        
        if style == 1:
            typewriter_reveal()
        elif style == 2:
            pulse_border(QUOTE)
            time_split = time.sleep
            time_split(1)
            clear_screen()
            print(C.Y + WOODY_FACES[0] + C.X)
            print()
            print(C.C + C.BOLD + " " * 20 + QUOTE + C.X)
            print()
            print(C.DIM + " " * 35 + AUTHOR + C.X)
        elif style == 3:
            matrix_rain_quote()
        elif style == 4:
            neon_sign_effect()
        else:
            falling_thoughts()
            clear_screen()
            print(C.Y + WOODY_FACES[0] + C.X)
            print()
            print(C.W + " " * 15 + QUOTE + C.X)
            print()
            print(C.C + " " * 30 + AUTHOR + C.X)
        
        # Final pause with blinking cursor
        print()
        print(C.DIM + " " * 25 + "Press Ctrl+C to exit (or don't, I'm not your analyst)" + C.X)
        time.sleep(3)
        
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear_screen()
        print(C.G + "Thanks for the session. That'll be $300." + C.X)
        print(C.DIM + "— Your Python Therapist" + C.X)

if __name__ == '__main__':
    main()