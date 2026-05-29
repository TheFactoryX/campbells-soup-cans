"""
Campbell's Soup Can #3815
Produced: 2026-05-29 23:41:25
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'
DIM = '\033[2m'

QUOTE = "Life is full of misery, loneliness, and suffering - and it's all over much too soon."
AUTHOR = "Woody Allen"

# small delay for dramatic effect
def pause(seconds=0.04):
    time.sleep(seconds)

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

# render a single char with random-ish color from set
COLORS = [RED, YELLOW, CYAN, MAGENTA, GREEN]
import itertools
color_cycle = itertools.cycle(COLORS)

def colored_char(c):
    col = next(color_cycle)
    return col + c + RESET

# build a big ASCII art banner for the quote using a simple block-letter style
# but we'll do a "typewriter reveal across the bottom

# let's do a fake binary rain intro
def binary_rain(lines=6, cols=40):
    import random
    for _ in range(lines):
        row = ''.join(random.choice('01') for _ in range(cols))
        pause(0.15)
        sys.stdout.write(DIM + row + RESET + '\n')
    sys.stdout.flush()

# main visual: a big ASCII art "WOODY" in block letters, then the quote in a box
WOODY_ART = r"""
 __      __                  .___             .___
/  \    /  \_____ _______  __| _/______  ____ |   | ____
\   \/\/   /  _ \\__  \  \/ /  |/ __ \ /    \|   |/ __ \
 \        (  <_> )    |>    <|  \  ___/|   |  \  ___/
  \__/\  / \____/____/__/\_ \__|\___  >___|  /\___  >
       \/                  \/        \/     \/     \/
"""

def typewriter(text, delay=0.03, color=WHITE):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        pause(delay)
    sys.stdout.write('\n')

def draw_box(text, width=60, color=CYAN):
    sys.stdout.write(color + '╔' + '═' * width + '╗\n')
    sys.stdout.write('║' + ' ' * width + '║\n')
    # center the text
    padding = (width - len(text)) // 2
    sys.stdout.write('║' + ' ' * padding + BOLD + text + RESET + color + ' ' * (width - padding - len(text)) + '║\n')
    sys.stdout.write('║' + ' ' * width + '║\n')
    sys.stdout.write('╚' + '═' * width + '╝' + RESET + '\n')

def main():
    clear_screen()

    # Phase 1: Binary rain
    sys.stdout.write(BOLD + MAGENTA + "Initializing existential dread...\n" + RESET)
    pause(0.5)
    binary_rain(4, 50)
    pause(0.3)

    # Phase 2: Woody Allen ASCII art
    sys.stdout.write('\n')
    typewriter(WOODY_ART, delay=0.005, color=YELLOW)
    pause(0.5)

    # Phase 3: The quote in a box
    sys.stdout.write('\n')
    draw_box(QUOTE, width=len(QUOTE) + 10, color=CYAN)
    pause(0.3)

    # Phase 4: Author attribution
    author_line = f"— {AUTHOR}"
    padding = (60 - len(author_line)) // 2
    sys.stdout.write(' ' * padding + BOLD + GREEN + author_line + RESET + '\n\n')
    pause(0.3)

    # Phase 5: Philosophical "loading bar" of existential dread
    sys.stdout.write(DIM + "Contemplating the void: [")
    for i in range(30):
        pause(0.08)
        if i % 5 == 0:
            sys.stdout.write(RED + '▓' + RESET)
        else:
            sys.stdout.write(DIM + '░' + RESET)
        sys.stdout.flush()
    sys.stdout.write(DIM + "] 100% - Nothing matters.\n" + RESET)

    # Phase 6: Final colored quote one more time, character by character
    sys.stdout.write('\n' + BOLD + WHITE + "Remember: " + RESET)
    for ch in QUOTE:
        sys.stdout.write(next(color_cycle) + ch + RESET)
        sys.stdout.flush()
        pause(0.04)
    sys.stdout.write('\n\n')

    # Phase 7: Tiny ASCII art of a sad face
    sad_face = r"""
       .-""""""-.
     .'          '.
    /   O      O   \
   :                :
   |    .-------.    |
   |   /         \   |
   |  |  .-. .-.  |  |
   \  |  '-' '-'  |  /
    '-.___________.-'
      /           \
     /  Existential \
    |    Dread      |
    |    Central      |
     \              /
      '-.________.-'
    """
    sys.stdout.write(DIM + sad_face + RESET)
    sys.stdout.write(BOLD + MAGENTA + "   [Press Ctrl+C to escape the void]\n" + RESET)

if __name__ == '__main__':
    main()