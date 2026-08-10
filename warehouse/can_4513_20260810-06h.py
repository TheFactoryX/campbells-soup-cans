"""
Campbell's Soup Can #4513
Produced: 2026-08-10 06:42:01
Worker: inclusionAI: Ling 3.0 Tiny (free) (inclusionai/ling-3.0-tiny:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
🧠 Woody Allen Philosophical Quote Generator
A visually stunning terminal program with animations, colors, and ASCII art.
No external dependencies — pure Python 3.
"""

import time
import sys
import os

# ── ANSI Color Codes ──────────────────────────────────────
RESET   = '\033[0m'
BOLD    = '\033[1m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
DARK    = '\033[30m'
BG_BLACK = '\033[40m'
BG_RED   = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_CYAN  = '\033[46m'
BG_WHITE = '\033[47m'

# ── Terminal Helpers ──────────────────────────────────────
def clear_screen():
    os.system('clear')

def fancy_border(width, char='═', padding=1):
    """Print a decorative horizontal border line."""
    print(f"{CYAN}{BOLD}╭{'═' * width}╮{RESET}")
    print(f"{CYAN}{BOLD}║  {char * width}  ║{RESET}")
    print(f"{CYAN}{BOLD}╰{'═' * width}╯{RESET}")

def print_ascii_card():
    """Print a mini ASCII art character."""
    print(f"  {CYAN}  ╭─ {'★' * 30} ─╮")
    print(f"  {CYAN}  ╱──╱│   │╲")
    print(f"  {CYAN}  ╲──╲│   │╱")
    print(f"  {CYAN}  ─────│   │────")
    print(f"  {CYAN}  {CYAN}  ★  {CYAN}  ★{RESET}")

def intro_frame(quote):
    """The first frame with title and animated cursor."""
    clear_screen()
    print(f"{BOLD}{CYAN}  ╔{'═' * 66}╗{RESET}")
    print(f"{CYAN}{BOLD}  ║  ✦  W O O D Y   A L L E N  ✦  ║{RESET}")
    print(f"{CYAN}{BOLD}  ╚{'═' * 66}╝{RESET}")
    print()
    print(f"{RED}{BOLD}  ~  🎬  Quote coming in ~  🎬  {RESET}")
    time.sleep(0.6)
    print(f"{CYAN}{BOLD}  ~  🎬  The words appear...  🎬  {RESET}")
    print(f"{CYAN}{BOLD}  ~  🎬  {quote}  🎬  {RESET}")
    print()

def quote_box(quote, width=78):
    """Print a beautiful colored box around the quote."""
    print(f"\n{BG_BLACK}{BOLD}")
    print(f"{CYAN}{BOLD}╭{'═' * width}╮")
    # Decorative top border
    print(f"{CYAN}{BOLD}║  {CYAN}  ✦  {RED}✦  {CYAN}✦  ║{RESET}")
    print(f"{CYAN}{BOLD}║  {CYAN}  {RED}{quote}  ║{RESET}")
    print(f"{CYAN}{BOLD}║  {CYAN}  ✦  {YELLOW}✦  {CYAN}✦  ║{RESET}")
    print(f"{CYAN}{BOLD}╰{'═' * width}╯")
    print(f"{BG_BLACK}{BOLD}")
    print()

def sub_quotes():
    """Show additional Woody-style quotes."""
    print(f"{YELLOW}{BOLD}  💭  'Life is 10% what happens to you and 90% how you respond to it.'{RESET}")
    print(f"{YELLOW}{BOLD}  💭  'I am not afraid of death; I just don't want to be there when it happens.'{RESET}")
    print(f"{YELLOW}{BOLD}  💭  'I can't stop writing. I can't stop living. This is what makes me dangerous.'{RESET}")
    print(f"{YELLOW}{BOLD}  💭  'In any given month, I could lose at least $10,000 and still feel financially satisfied.'{RESET}")
    print()

def closing_frame():
    """End with a stylish finish."""
    print(f"{BOLD}{CYAN}  ╔{'═' * 50}╗{RESET}")
    print(f"{CYAN}{BOLD}  ║  🍿  🧠  🎬  ✦  ║{RESET}")
    print(f"{CYAN}{BOLD}  ╚{'═' * 50}╝{RESET}")
    print()
    print(f"{GREEN}{BOLD}  {CYAN}  ★  Thanks for watching!  ★  {RESET}")

def pulse(text, interval=0.3):
    """Blink text rapidly (ASCII flicker effect)."""
    while True:
        print(f"{BOLD}{YELLOW}  ◉ {text}  {RESET}")
        sys.stdout.write('\033[126H')  # Move cursor up to top
        sys.stdout.flush()
        time.sleep(interval)
        print(f"{BOLD}{RED}  🔴 {text}  {RESET}")
        sys.stdout.write('\033[126H')
        sys.stdout.flush()
        time.sleep(interval)

def slow_animation(duration=4):
    """A slow, dreamy animation sequence."""
    for i in range(duration):
        clear_screen()
        print(f"{BOLD}{CYAN}  ╔{'═' * 60}╗{RESET}")
        print(f"{CYAN}{BOLD}  ║  ✦  WOODY ALLEN  ✦  ║{RESET}")
        print(f"{CYAN}{BOLD}  ╚{'═' * 60}╝{RESET}")
        print()
        print(f"{RED}{BOLD}  {CYAN}  🎬  The quote:  🎬  {RESET}")
        time.sleep(0.5)
        print(f"{CYAN}{BOLD}  {BOLD}  {RED}  ~ {CYAN}    I am not afraid of death; I just don't want to be there when it happens.    ~{RESET}")
        time.sleep(0.5)
        print(f"{CYAN}{BOLD}  {BOLD}  {CYAN}  {YELLOW}  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  ✦  {RESET}")
        time.sleep(0.5)

def main():
    clear_screen()

    # ── Title Card ──────────────────────────────────────────
    print(f"{BOLD}{CYAN}  ╔{'═' * 70}╗{RESET}")
    print(f"{CYAN}{BOLD}  ║  ✦  W O O D Y   A L L E N  ✦  ║{RESET}")
    print(f"{CYAN}{BOLD}  ╚{'═' * 70}╝{RESET}")
    print()
    time.sleep(0.4)

    # ── Intro Frame ─────────────────────────────────────────
    intro_frame("I am not afraid of death; I just don't want to be there when it happens.")

    # ── Animated quote in a box ─────────────────────────────
    quote = "I am not afraid of death; I just don't want to be there when it happens."
    quote_box(quote, width=78)

    # ── Additional Quotes ───────────────────────────────────
    print(f"{YELLOW}{BOLD}  💭  'Life is full of misery, loneliness, and suffering — and it's all over much too soon.'{RESET}")
    print(f"{YELLOW}{BOLD}  💭  'I don't want to achieve immortality through my work; I want to achieve it through not dying.'{RESET}")
    print()

    # ── Additional Quotes with a slow animation ────────────
    slow_animation(5)

    # ── Closing ──────────────────────────────────────────────
    closing_frame()

    print()
    print(f"{CYAN}{BOLD}  ────────────────────────────────────────────────{RESET}")
    print(f"{CYAN}{BOLD}  🎬  Stay philosophical. Stay sharp. Stay witty.  🎬{RESET}")
    print(f"{CYAN}{BOLD}  ────────────────────────────────────────────────{RESET}")

    # Keep the program alive briefly so the user can read the output
    print(f"{CYAN}{BOLD}  Press Ctrl+C to exit.{RESET}")
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        clear_screen()

if __name__ == "__main__":
    main()