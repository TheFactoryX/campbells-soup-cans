"""
Campbell's Soup Can #4263
Produced: 2026-07-19 23:11:39
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
GRAY = '\033[90m'
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

CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'
CLEAR_LINE = '\033[2K'
CLEAR_SCREEN = '\033[2J\033[H'
MOVE_UP = '\033[1A'

WOODY_QUOTE = (
    "I've finally made peace with my mortality. "
    "Mainly by accepting that the universe will "
    "probably outsource my afterlife to a "
    "call center in New Jersey."
)

WOODY_NAME = "— Woody Allen (probably)"

FRAME_TOP = "╔" + "═" * 70 + "╗"
FRAME_BOTTOM = "╚" + "═" * 70 + "╝"
FRAME_SIDE = "║" + " " * 70 + "║"

NEUROTIC_THOUGHTS = [
    "Wait, did I lock the door?",
    "Is that a lump? It's probably a lump.",
    "Why did I say 'you too' when the waiter said 'enjoy your meal'?",
    "Everyone hates me. Statistically impossible, but true.",
    "I should've been a podiatrist. People like their feet.",
    "Death is just nature's way of saying 'your subscription expired.'",
    "My therapist says I have a persecution complex. She would say that.",
    "I'm not paranoid. The universe actually IS watching. And judging.",
]

def typewriter(text, color=WHITE, delay=0.02, newline=True):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    if newline:
        print()

def typewriter_line(text, color=WHITE, delay=0.015):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)

def clear_lines(n):
    for _ in range(n):
        sys.stdout.write(MOVE_UP + CLEAR_LINE)
    sys.stdout.flush()

def animated_frame_reveal():
    print(CLEAR_SCREEN, end='')
    print(CURSOR_HIDE, end='')
    
    colors = [CYAN, BRIGHT_CYAN, BLUE, BRIGHT_BLUE, MAGENTA, BRIGHT_MAGENTA]
    
    # Top border growing
    for i in range(71):
        color = random.choice(colors)
        sys.stdout.write(f"\r{color}╔{'═' * i}{' ' * (70 - i)}╗{RESET}")
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    
    # Side borders with empty content
    for _ in range(5):
        color = random.choice(colors)
        print(f"{color}║{' ' * 70}║{RESET}")
        time.sleep(0.03)
    
    # Bottom border growing
    for i in range(71):
        color = random.choice(colors)
        sys.stdout.write(f"\r{color}╚{'═' * i}{' ' * (70 - i)}╝{RESET}")
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    
    # Move cursor up to fill content
    for _ in range(6):
        sys.stdout.write(MOVE_UP)
    sys.stdout.flush()

def fill_frame_with_quote():
    lines = [
        "",
        f"  {BOLD}{BRIGHT_YELLOW}WOODY ALLEN'S DAILY AFFIRMATION{RESET}",
        "",
        f"  {ITALIC}{CYAN}\"I've finally made peace with my mortality.\"{RESET}",
        f"  {ITALIC}{CYAN}\"Mainly by accepting that the universe will\"{RESET}",
        f"  {ITALIC}{CYAN}\"probably outsource my afterlife to a\"{RESET}",
        f"  {ITALIC}{CYAN}\"call center in New Jersey.\"{RESET}",
        "",
        f"  {DIM}{GRAY}— Woody Allen (probably){RESET}",
        "",
    ]
    
    for i, line in enumerate(lines):
        sys.stdout.write(MOVE_UP)
        sys.stdout.write(CLEAR_LINE)
        color = random.choice([CYAN, BRIGHT_CYAN, BLUE, BRIGHT_BLUE])
        print(f"{color}║{RESET}{line:<70}{color}║{RESET}")
        time.sleep(0.15)

def neurotic_interlude():
    print()
    print(f"  {DIM}{GRAY}[Inner Monologue Activating...]{RESET}")
    time.sleep(0.5)
    
    for thought in random.sample(NEUROTIC_THOUGHTS, 4):
        # Type the thought
        sys.stdout.write(f"  {YELLOW}› {RESET}{ITALIC}{GRAY}")
        for char in thought:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(RESET)
        print()
        time.sleep(0.4)
        
        # Self-correction
        corrections = [
            f"  {DIM}{RED}✗ Irrational.{RESET}",
            f"  {DIM}{RED}✗ Catastrophizing again.{RESET}",
            f"  {DIM}{RED}✗ Take a Xanax, Woody.{RESET}",
            f"  {DIM}{RED}✗ Your mother would be disappointed.{RESET}",
        ]
        print(random.choice(corrections))
        time.sleep(0.3)
        clear_lines(2)

def final_signature():
    print()
    signatures = [
        f"{BRIGHT_MAGENTA}┌{'─' * 50}┐{RESET}",
        f"{BRIGHT_MAGENTA}│{RESET} {BOLD}{YELLOW}Existential dread delivered successfully.{RESET} {BRIGHT_MAGENTA}│{RESET}",
        f"{BRIGHT_MAGENTA}│{RESET} {DIM}{CYAN}Remember: Anxiety is just creativity's shadow.{RESET} {BRIGHT_MAGENTA}│{RESET}",
        f"{BRIGHT_MAGENTA}└{'─' * 50}┘{RESET}",
    ]
    for line in signatures:
        print(line)
        time.sleep(0.1)
    
    print()
    print(f"  {DIM}{GRAY}Press Ctrl+C to spiral into another existential crisis...{RESET}")
    print(CURSOR_SHOW, end='')

def main():
    try:
        animated_frame_reveal()
        fill_frame_with_quote()
        neurotic_interlude()
        final_signature()
        
        # Keep alive for a moment
        time.sleep(2)
        
    except KeyboardInterrupt:
        print(f"\n{CURSOR_SHOW}{YELLOW}Interrupted. Typical. Even my programs have commitment issues.{RESET}")
        sys.exit(0)
    finally:
        print(CURSOR_SHOW, end='')

if __name__ == "__main__":
    main()