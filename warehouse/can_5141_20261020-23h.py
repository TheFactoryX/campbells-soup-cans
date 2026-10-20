"""
Campbell's Soup Can #5141
Produced: 2026-10-20 23:53:11
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic dispatch from the void — Woody Allen style.
Pure Python, zero dependencies, maximum existential dread.
"""

import sys
import time
import random

# ─── ANSI PALETTE ──────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
BLINK   = "\033[5m"

# foreground
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
GRAY    = "\033[90m"
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"

# background
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"
BG_GRAY    = "\033[100m"

# ─── THE QUOTE ─────────────────────────────────────────────────
QUOTE = (
    "I told my analyst I was having an identity crisis; "
    "he said, 'That’ll be $300 — and by the way, who’s asking?'"
)

ATTRIBUTION = "— Woody Allen (probably, I mean, who really knows?)"

# ─── ASCII ART FRAMES ──────────────────────────────────────────
TOP_LEFT     = "┌"
TOP_RIGHT    = "┐"
BOTTOM_LEFT  = "└"
BOTTOM_RIGHT = "┘"
HORIZONTAL   = "─"
VERTICAL     = "│"

NEUROTIC_DUDE = r"""
      \   /
       \ /
    ┌───────┐
    │  @ @  │   <-- that's me, dissociating
    │  \_/  │
    └───────┘
       | |
      /   \
"""

THOUGHT_BUBBLE = r"""
    .--.
   /    \
  |  💭  |
   \    /
    '--'
"""

# ─── UTILITIES ─────────────────────────────────────────────────
def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def move_cursor(row, col):
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()

def typewriter(text, delay=0.02, color=WHITE, end="", flush=True):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        if flush:
            sys.stdout.flush()
        time.sleep(delay)
    if end:
        sys.stdout.write(end)
        sys.stdout.flush()

def random_glitch_char():
    return random.choice("░▒▓█▄▀▌▐▬◆◇◈◉○●◎◍◌")

def glitch_line(width, color=RED):
    return "".join(f"{color}{random_glitch_char()}{RESET}" for _ in range(width))

# ─── MAIN ANIMATION ────────────────────────────────────────────
def main():
    hide_cursor()
    clear_screen()
    
    try:
        # ─── INTRO: STATIC NOISE ──────────────────────────────
        for _ in range(3):
            for row in range(1, 8):
                move_cursor(row, 1)
                sys.stdout.write(glitch_line(70, random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])))
                sys.stdout.flush()
                time.sleep(0.03)
            time.sleep(0.1)
        
        clear_screen()
        
        # ─── DRAW THE NEUROTIC DUDE ───────────────────────────
        move_cursor(2, 2)
        for line in NEUROTIC_DUDE.strip().split("\n"):
            typewriter(line, delay=0.005, color=BRIGHT_CYAN)
            move_cursor(move_cursor.__defaults__[0] if False else 0, 0)  # dummy
            # manually track
            sys.stdout.write("\n")
            sys.stdout.flush()
        
        # ─── THOUGHT BUBBLE APPEARS ───────────────────────────
        time.sleep(0.3)
        move_cursor(10, 15)
        for line in THOUGHT_BUBBLE.strip().split("\n"):
            typewriter(line, delay=0.01, color=BRIGHT_YELLOW)
            sys.stdout.write("\n")
            sys.stdout.flush()
        
        # ─── QUOTE BOX ────────────────────────────────────────
        quote_lines = []
        words = QUOTE.split()
        line = ""
        max_width = 54
        for w in words:
            if len(line) + len(w) + 1 > max_width:
                quote_lines.append(line)
                line = w
            else:
                line += (" " + line) if line else w
        if line:
            quote_lines.append(line)
        
        box_w = max(len(l) for l in quote_lines) + 4
        box_h = len(quote_lines) + 2
        start_row = 14
        start_col = 10
        
        # top border
        move_cursor(start_row, start_col)
        typewriter(TOP_LEFT + HORIZONTAL * (box_w - 2) + TOP_RIGHT, delay=0.005, color=BRIGHT_MAGENTA)
        
        # content lines
        for i, qline in enumerate(quote_lines):
            move_cursor(start_row + 1 + i, start_col)
            padding = " " * (box_w - 4 - len(qline))
            typewriter(VERTICAL + " " + qline + padding + " " + VERTICAL, delay=0.015, color=BRIGHT_WHITE)
        
        # bottom border
        move_cursor(start_row + box_h - 1, start_col)
        typewriter(BOTTOM_LEFT + HORIZONTAL * (box_w - 2) + BOTTOM_RIGHT, delay=0.005, color=BRIGHT_MAGENTA)
        
        # ─── ATTRIBUTION ──────────────────────────────────────
        time.sleep(0.4)
        attr_row = start_row + box_h + 1
        move_cursor(attr_row, start_col + 2)
        typewriter(ATTRIBUTION, delay=0.02, color=GRAY + ITALIC)
        
        # ─── FINAL GLITTER ────────────────────────────────────
        time.sleep(0.5)
        for _ in range(20):
            r = random.randint(1, 22)
            c = random.randint(1, 70)
            move_cursor(r, c)
            sys.stdout.write(f"{random.choice([BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN])}{random_glitch_char()}{RESET}")
            sys.stdout.flush()
            time.sleep(0.02)
        
        # ─── HOLD ─────────────────────────────────────────────
        move_cursor(24, 1)
        sys.stdout.write(f"{DIM}Press Ctrl+C to escape existence...{RESET}\n")
        sys.stdout.flush()
        
        # keep alive
        while True:
            time.sleep(1)
            # subtle breathing glow on the quote
            move_cursor(start_row + 1, start_col + 1)
            sys.stdout.write(f"{BRIGHT_WHITE if random.random() > 0.5 else WHITE}{quote_lines[0]}{RESET}")
            sys.stdout.flush()
            
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear_screen()
        # parting thought
        print(f"{ITALIC}{GRAY}")
        print("The universe is indifferent. Your analyst's yacht, however, is not.")
        print(f"{RESET}")

if __name__ == "__main__":
    main()