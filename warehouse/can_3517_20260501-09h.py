"""
Campbell's Soup Can #3517
Produced: 2026-05-01 09:57:45
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import random
import sys

# New quotes in Woody Allen's style
quotes = [
    "Life is full of hope, misery, and loneliness — and it’s all over much like a dream.",
    "I don't believe in an afterlife, although I plan to keep my old jokes for the audition.",
    "If you want to make God laugh, tell him about your plans — and if you want to make him cry, tell him mine.",
    "I'm not afraid of death; I just feel violated.",
    "My brain is my second favorite organ, but I don't like to flatter myself.",
    "I have no respect for those who don't weep when they read their own work.",
]

# Pick a quote
quote = random.choice(quotes)

# ANSI color codes
RED   = '\033[91m'
GREEN = '\033[92m'
YELLOW= '\033[93m'
BLUE  = '\033[94m'
CYAN  = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD  = '\033[1m'

# Scroll text char by char
def scroll(text, color=WHITE, delay=0.04):
    sys.stdout.write(color + BOLD)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + '\n')

# Fade background with stars
def fade_stars(duration=6, delay=0.15):
    cols, rows = 50, 3
    for _ in range(duration):
        screen = f'\033[{rows+4}F' # Move cursor up
        screen += '\033[7m'  # Invert
        for _ in range(rows):
            chars = ' * '
            line = ''
            for i in range(cols):
                if random.random() < 0.5:
                    line += random.choice(chars)
                else:
                    line += ' '
            screen += f"{YELLOW}{line}{RESET}\n"
        screen += '\033[0m'
        print(screen, end='')
        time.sleep(delay)
        # Clear lines
        for _ in range(rows + 1):
            print(f'\033[F\033[K', end='', flush=True)
        time.sleep(delay * 0.5)
    for _ in range(rows + 1):
        print('\033[K', end='')
    print(f'\033[{rows+1}F') # Move cursor back to line

# Draw thinking man
man = [
    "     .--./\\.--.     ",
    "    /   \\  /   \\    ",
    "   /    /  \\    \\   ",
    "   '--'    '--'     ",
    "      ( o  o )      ",
    "       ---^---       ",
    "         / \\         ",
    "        /   \\        ",
]

# Animate man thinking
def animated_man(duration=5, delay=0.5):
    msg = "thinking..."
    for i in range(duration):
        print(f'\033[{len(man)+3}F') # Go up to redraw
        for line in man:
            print(CYAN + line + RESET)
        tip = f"{MAGENTA}{msg}{RESET}"
        if i % 2 == 0:
            tip += "  💭"
        else:
            tip += "  🤔"
        print(tip)
        print(f"({i+1}/{duration})")
        time.sleep(delay)

# Draw boxed quote
def make_boxed(q):
    lines = []
    # wrap if needed
    max_w = 70
    while len(q) > max_w:
        idx = q[:max_w].rfind(' ')
        lines.append(q[:idx])
        q = q[idx+1:]
    lines.append(q)
    max_line = max(len(l) for l in lines)
    pad = 4
    box = '+' + '-' * (max_line + 2 * pad - 2) + '+\n'
    box += "|  " + " " * (max_line - 2) + "  |\n"
    for l in lines:
        box += f"|  {l.ljust(max_line-2)}  |\n"
    box += "|  " + " " * (max_line - 2) + "  |\n"
    box += '+' + '-' * (max_line + 2 * pad - 2) + '+'
    return box

# Main visual
if __name__ == '__main__':
    # Fade stars
    fade_stars()
    print()

    # Show man "thinking"
    animated_man()
    time.sleep(0.5)

    # Print the quote in box with colors
    print(GREEN + BOLD)
    boxed = make_boxed(quote)
    scroll(boxed, GREEN)
    print(RESET)

    # Footer
    footer = SYSTEM/"Existence is the problem, not the answer."/"— Woody Allen-ish Bot"
    scroll(footer, MAGENTA)
    print()