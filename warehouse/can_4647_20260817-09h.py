"""
Campbell's Soup Can #4647
Produced: 2026-08-17 09:00:51
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

# Cursor control
CLEAR_SCREEN = '\033[2J'
CLEAR_LINE = '\033[2K'
CURSOR_HOME = '\033[H'
CURSOR_UP = '\033[A'
CURSOR_DOWN = '\033[B'
CURSOR_RIGHT = '\033[C'
CURSOR_LEFT = '\033[D'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'
SAVE_CURSOR = '\033[s'
RESTORE_CURSOR = '\033[u'

# Woody Allen glasses ASCII
GLASSES = [
    f"{BRIGHT_BLACK}    .--.     .--.    {RESET}",
    f"{BRIGHT_BLACK}   /    \\   /    \\   {RESET}",
    f"{BRIGHT_BLACK}  |      | |      |  {RESET}",
    f"{BRIGHT_BLACK}  |      | |      |  {RESET}",
    f"{BRIGHT_BLACK}   \\    /   \\    /   {RESET}",
    f"{BRIGHT_BLACK}    `--'     `--'    {RESET}",
]

GLASSES_SMALL = f"{BRIGHT_BLACK}  .--.   .--.  {RESET}"

# The quote - original Woody Allen style
QUOTE = "I don't fear death. I just don't want to be conscious for the Yelp reviews."
ATTRIBUTION = "— Woody Allen (probably)"

def typewriter(text, color=WHITE, delay=0.03, newline=True):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def typewriter_inline(text, color=WHITE, delay=0.03):
    """Print text with typewriter effect without newline."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def print_boxed(text_lines, border_color=CYAN, title="", title_color=YELLOW):
    """Print text in a nice box."""
    max_len = max(len(line) for line in text_lines)
    if title:
        max_len = max(max_len, len(title) + 4)
    
    width = max_len + 4
    
    # Top border
    print(f"{border_color}╔{'═' * width}╗{RESET}")
    
    # Title if provided
    if title:
        padding = (width - len(title) - 2) // 2
        print(f"{border_color}║{' ' * padding}{title_color}{title}{RESET}{border_color}{' ' * (width - padding - len(title))}║{RESET}")
        print(f"{border_color}╠{'═' * width}╣{RESET}")
    
    # Content lines
    for line in text_lines:
        padding = width - len(line) - 2
        print(f"{border_color}║ {line}{' ' * padding}{border_color}║{RESET}")
    
    # Bottom border
    print(f"{border_color}╚{'═' * width}╝{RESET}")

def animate_glasses():
    """Animate the glasses appearing."""
    print(HIDE_CURSOR, end='')
    for i, line in enumerate(GLASSES):
        sys.stdout.write(f"\033[{i+1};1H{line}")
        sys.stdout.flush()
        time.sleep(0.15)
    time.sleep(0.5)
    print(SHOW_CURSOR, end='')

def fade_in_text(text, color=WHITE, steps=10):
    """Fade in text by gradually increasing brightness."""
    colors = [BLACK, BRIGHT_BLACK, DIM + WHITE, WHITE, BOLD + WHITE]
    for i, c in enumerate(colors):
        sys.stdout.write(f"\r{c}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.15)

def pulse_text(text, color=YELLOW, times=3):
    """Make text pulse."""
    for _ in range(times):
        sys.stdout.write(f"\r{BOLD}{color}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{color}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    print()

def main():
    # Clear screen and hide cursor
    print(CLEAR_SCREEN + CURSOR_HOME, end='')
    print(HIDE_CURSOR, end='')
    
    # Print some atmospheric spacing
    print("\n" * 2)
    
    # Animate glasses appearing
    animate_glasses()
    
    print("\n")
    
    # Print a neurotic thought bubble
    thoughts = [
        "Wait, did I lock the door?",
        "Is that a mole? It's definitely a mole.",
        "My therapist says I catastrophize.",
        "But what if catastrophizing is the only rational response to existence?",
        "Also, did I pay the parking meter?",
    ]
    
    for thought in thoughts:
        print(f"  {BRIGHT_BLACK}{ITALIC}{thought}{RESET}")
        time.sleep(0.4)
    
    print("\n")
    
    # Typewriter the main quote
    print(f"  {CYAN}After 40 years of analysis, the breakthrough:{RESET}\n")
    time.sleep(0.5)
    
    # Type the quote word by word for dramatic effect
    words = QUOTE.split()
    print("  ", end='')
    sys.stdout.flush()
    for i, word in enumerate(words):
        color = YELLOW if i == len(words) - 1 else WHITE
        typewriter_inline(word + " ", color, 0.06)
    print()
    
    print()
    
    # Type attribution
    typewriter(f"  {DIM}{ITALIC}{ATTRIBUTION}{RESET}", BRIGHT_BLACK, 0.02)
    
    print("\n")
    
    # Final neurotic postscript
    postscripts = [
        "Anyway, my session's over. Same time Thursday?",
        "Cash only. The void doesn't take Venmo.",
        "And validate my parking? The universe charges $4/hour.",
    ]
    
    for ps in postscripts:
        time.sleep(0.3)
        typewriter(f"  {BRIGHT_BLACK}{ITALIC}{ps}{RESET}", BRIGHT_BLACK, 0.02)
    
    print("\n" * 2)
    
    # Small glasses at bottom
    print(f"         {GLASSES_SMALL}")
    print(f"       {BRIGHT_BLACK}Existential dread sold separately.{RESET}")
    
    print(SHOW_CURSOR, end='')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(SHOW_CURSOR + RESET)
        sys.exit(0)