"""
Campbell's Soup Can #422
Produced: 2025-11-21 11:27:55
Worker: Meituan: LongCat Flash Chat (free) (meituan/longcat-flash-chat:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen-esque philosophical musing, 
delivered with existential dread, neurosis, and a splash of color.
"""

import time
import sys
import os

# ANSI Color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
NC = '\033[0m'  # No Color

# Screen clearing (clear or clear for cross-platform)
CLEAR = '\033[2J\033[H'  # ANSI for clear screen + home cursor

# Mini ASCII Brain (because Woody's neurotic)
BRAIN_ART = [
    "    ⢀⠔⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
    "  ⢀⡠⠂⠉⢱⡇⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
    " ⢀⠔⠨⢤⣤⡯⡇⢀⠔⠙⢍⢅⠀⠀⠀⠀⠀⠀⠀⠀⠀      ",
    "⡔⠁⢀⣤⢤⣽⣼⢃⠆⠀⠀⠀⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀    ",
    "⡇⡀⠀⠀⢀⢄⣿⢸⢰⡀⠀⠀⠐⢱⡄⠀⠀⠀⠀⠀⠀⠀    ",
    "⠇⢱⠂⠐⢀⠔⢹⡈⢆⠢⢄⠀⢀⠇⢸⠀⠀⠀⠀⠀⠀⠀    ",
    "⠀⠀⢱⡂⠀⠀⡇⠀⡇⢰⠀⢠⠃⠀⢸⡀⠀⠀⠀⠀⠀⠀    ",
    "⠀⠀⢸⡆⠀⡸⠀⢀⠇⢀⡷⠈⠦⡀⢸⡇⠀⠀⠀⠀⠀⠀    ",
    "⠀⠀⠀⣇⢀⣣⡤⠮⠷⠋⠀⠤⠤⢦⣸⠀⠀⠀⠀⠀⠀⠀    ",
    "⠀⠀⠀⢹⡍⠉⠰⠀⠀⠀⢰⠉⠉⣽⠇⠀⠀⠀⠀⠀⠀⠀    ",
    "⠀⠀⠀⠈⢷⣀⣀⣠⣴⣾⣷⣤⣀⣠⡟⠀⠀⠀⠀⠀⠀⠀    ",
    "⠀⠀⠀⠀⠀⠻⣷⣿⣿⣿⣿⣿⠿⡟⠀⠀⠀⠀⠀⠀⠀⠀    ",
    "⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    "
]

# The quote – original, neurotic, and deeply unconfident
QUOTE = (
    BOLD + RED +
    "I'm not afraid of being forgotten when I die...\n\n"
    "I'm afraid when I die, "
    + MAGENTA +
    "I'll remember everything "
    + RED +
    "and just be so\n"
    "embarrassed by my lifetime of failed attempts at\n"
    + CYAN +
    "wiring a lamp properly, "
    + RED +
    "people will pretend not to\n"
    "recognize me at the pearly gates... "
    + UNDERLINE +
    "and God will tap me on\n"
    "the shoulder and say, "
    + WHITE +
    "'Here! Take another human life!'\n"
    + RED +
    "And I'll go, 'Nah... I'll just stay here and judge myself quietly.'\n\n"
    + YELLOW +
    "— Woody Allen (probably), if he ever finished a to-do list." + NC
)

# Fancy box around the quote
def create_boxed_quote(quote_text, width=60):
    lines = quote_text.split('\n')
    max_len = max(len(line.replace(''.join(['\033[{}m'.format(i) for i in range(100)]), '')) for line in lines)
    box_width = min(max(max_len + 6, width), os.get_terminal_size().columns - 10)
    horizontal = "═" * (box_width - 2)
    top = "╔" + horizontal + "╗"
    bottom = "╚" + horizontal + "╝"
    padded_lines = []
    for line in lines:
        visible_len = len(line.replace(''.join(['\033[{}m'.format(i) for i in range(100)]), ''))
        padding = (box_width - 2 - visible_len)
        left_pad = padding // 2
        right_pad = padding - left_pad
        padded_lines.append("║" + " " * left_pad + line + " " * right_pad + "║")
    return [top] + padded_lines + [bottom]

# Typewriter animation with blinking cursor
def typewrite_with_cursor(message_lines, speed=0.04, cursor_blink=True):
    for line in message_lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        if cursor_blink:
            # Blink cursor at end of line
            sys.stdout.write(f"{BLUE}█{NC}")
            sys.stdout.flush()
            time.sleep(0.3)
            sys.stdout.write('\b \b')  # Erase cursor
            sys.stdout.flush()
            time.sleep(0.2)
        print()  # newline

def main():
    # Clear screen
    print(CLEAR, end='')

    # Print brain slowly
    brain_color_cycle = [BLUE, CYAN, GREEN, YELLOW]
    for i, line in enumerate(BRAIN_ART):
        color = brain_color_cycle[(i // 3) % len(brain_color_cycle)]
        print(f"{color}{line}{NC}", file=sys.stderr)
        time.sleep(0.05)
        sys.stdout.flush()

    # Short pause
    time.sleep(0.5)

    # Create box and typewrite
    boxed = create_boxed_quote(QUOTE)
    print()  # space after brain
    typewrite_with_cursor(boxed, speed=0.03)

    # Final flourish: floating ellipsis
    time.sleep(0.5)
    print(end='', flush=True)
    for _ in range(8):
        print(f"\r{GREEN}.{YELLOW}.{MAGENTA}.{CYAN}... (existential contemplation){NC} ", end='', flush=True)
        time.sleep(0.25)
        for _ in range(len(" (existential contemplation)")):
            if time.time() % 0.5 < 0.25:
                print('\b \b', end='', flush=True)
            time.sleep(0.05)
    print("\n\n" + GREEN + "█" + NC + " → Don't panic. It's just a metaphor. Probably.\n" + NC)

if __name__ == "__main__":
    main()