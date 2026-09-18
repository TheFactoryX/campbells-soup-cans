"""
Campbell's Soup Can #4985
Produced: 2026-09-18 22:34:39
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes
class C:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_BLUE = '\033[44m'
    BG_YELLOW = '\033[43m'

def paint(text, color):
    return f"{color}{text}{C.RESET}"

def typewrite(text, delay=0.03, color=C.WHITE):
    for char in text:
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(lines, width=None):
    if width is None:
        width = max(len(l) for l in lines) + 4
    h_edge = paint("╔" + "══" * ((width - 2) // 2) + "╗", C.CYAN)
    print(h_edge)
    for line in lines:
        padded = line.center(width - 2)
        print(paint("║ ", C.CYAN) + padded + paint(" ║", C.CYAN))
    print(paint("╚" + "══" * ((width - 2) // 2) + "╝", C.CYAN))

def animate_title():
    titles = [
        paint("~ WOODY ALLEN'S PHILOSOPHICAL ARCHIVES ~", C.YELLOW),
        paint("~ WOODY ALLEN'S PHILOSOPHICAL ARCHIVES ~", C.RED),
        paint("~ WOODY ALLEN'S PHILOSOPHICAL ARCHIVES ~", C.MAGENTA),
        paint("~ WOODY ALLEN'S PHILOSOPHICAL ARCHIVES ~", C.CYAN),
    ]
    for t in titles:
        print(f"\n{t.center(60)}")
        time.sleep(0.15)
    print()

def main():
    print("\n" * 2)
    
    # Decorative top
    print(paint(" " * 15 + "●" * 20, C.RED))
    print(paint(" " * 15 + "✦" * 20, C.YELLOW))
    
    animate_title()
    
    # ASCII art neurotic face
    face = paint(r"""
         _____
        /     \
       | O   O |
       |   >   |
       |  \_/  |
        \_____/
    """, C.MAGENTA)
    print(face.center(60))
    time.sleep(0.3)
    
    # The quote
    quote = (
        'I read a book once. "The Meaning of Life." '
        'Terrible ending. Character was on a yacht, '
        'then — nothing. Just blank pages. '
        'That\'s more like it.'
    )
    
    print(paint("\n    ▶ ", C.GREEN) + paint("THE QUOTE", C.BOLD + C.WHITE))
    print()
    
    # Animated quote with typewriter effect in cyan
    typewrite("    " + quote, delay=0.025, color=C.CYAN)
    
    time.sleep(0.5)
    
    # Attribution with animation
    print()
    typewrite("    — Woody Allen (probably, while overthinking it)", delay=0.04, color=C.YELLOW)
    
    time.sleep(0.3)
    
    # Bottom decorations
    print()
    print(paint(" " * 15 + "●" * 20, C.MAGENTA))
    print(paint(" " * 15 + "✦" * 20, C.CYAN))
    
    # Final box with extra quote
    print()
    draw_box([
        paint("EXISTENTIAL THOUGHT OF THE MOMENT:", C.BOLD + C.RED),
        paint('"I would kill to be immortal,', C.GREEN),
        paint(' but I don\'t want to be there when', C.GREEN),
        paint('  it happens."', C.GREEN),
    ], width=52)
    
    print()
    print(paint("    [ Press Enter to contemplate your existence... ]", C.DIM))
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(paint("\n\n    See? Even interrupting is existential.", C.RED))