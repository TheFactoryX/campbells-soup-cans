"""
Campbell's Soup Can #4276
Produced: 2026-07-21 06:41:14
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
A neurotic masterpiece: Woody Allen meets terminal aesthetics.
One quote. Maximum existential dread. Beautiful ANSI colors.
"""

import sys
import time
import random

# ── ANSI Color Palette ──────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
UNDER   = "\033[4m"
BLINK   = "\033[5m"

# Foreground
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
GRAY    = "\033[90m"
BR_RED  = "\033[91m"
BR_GREEN= "\033[92m"
BR_YELLOW="\033[93m"
BR_BLUE = "\033[94m"
BR_MAG  = "\033[95m"
BR_CYAN = "\033[96m"
BR_WHITE= "\033[97m"

# Background
BG_BLACK  = "\033[40m"
BG_RED    = "\033[41m"
BG_GREEN  = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE   = "\033[44m"
BG_MAG    = "\033[45m"
BG_CYAN   = "\033[46m"
BG_WHITE  = "\033[47m"
BG_GRAY   = "\033[100m"

# ── The Quote ───────────────────────────────────────────────────────
QUOTE = (
    "I took a speed-reading course and read 'War and Peace' "
    "in twenty minutes.\n"
    "It involves Russia."
)

ATTRIBUTION = "— Woody Allen (probably, I mean, who's keeping track?)"

# ── ASCII Art Elements ──────────────────────────────────────────────
GLASSES = [
    "    ▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄    ",
    "   ██████████    ██████████   ",
    "  ████████████  ████████████  ",
    " ████████████████████████████ ",
    "  ████████████  ████████████  ",
    "   ██████████    ██████████   ",
    "    ▀▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀    ",
]

BRAIN_FART = [
    "       \\   /       ",
    "        \\ /        ",
    "       ●   ●       ",
    "        \\_/        ",
    "       __|__       ",
    "      /     \\      ",
    "     /  ___  \\     ",
    "    |  /   \\  |    ",
    "    |  \\___/  |    ",
    "     \\       /     ",
    "      \\_____/      ",
]

STARS = "✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦"

# ── Animation Helpers ───────────────────────────────────────────────
def clear_screen():
    print("\033[2J\033[H", end="")

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

def move_cursor(row, col):
    print(f"\033[{row};{col}H", end="")

def typewriter(text, delay=0.03, color=WHITE):
    for char in text:
        print(f"{color}{char}{RESET}", end="", flush=True)
        time.sleep(delay)
    print()

def glitch_text(text, color=BR_RED, iterations=3):
    """Briefly glitch the text for neurotic effect."""
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"
    for _ in range(iterations):
        glitched = "".join(
            random.choice(glitch_chars) if random.random() < 0.1 else c
            for c in text
        )
        print(f"\r{color}{glitched}{RESET}", end="", flush=True)
        time.sleep(0.05)
    print(f"\r{color}{text}{RESET}", end="", flush=True)

# ── Visual Components ───────────────────────────────────────────────
def draw_top_border(width=70):
    print(f"{BR_CYAN}╔{'═' * width}╗{RESET}")

def draw_bottom_border(width=70):
    print(f"{BR_CYAN}╚{'═' * width}╝{RESET}")

def draw_side(text="", width=68, color=WHITE, align="left"):
    if align == "center":
        content = text.center(width)
    elif align == "right":
        content = text.rjust(width)
    else:
        content = text.ljust(width)
    print(f"{BR_CYAN}║{RESET} {color}{content}{RESET} {BR_CYAN}║{RESET}")

def draw_glasses():
    print(f"{BR_YELLOW}")
    for line in GLASSES:
        print(f"        {line}")
    print(f"{RESET}")

def draw_brain_fart():
    print(f"{BR_MAG}")
    for line in BRAIN_FART:
        print(f"           {line}")
    print(f"{RESET}")

# ── Main Sequence ───────────────────────────────────────────────────
def main():
    hide_cursor()
    clear_screen()
    
    width = 70
    
    # Opening: empty space, then glasses fade in
    time.sleep(0.5)
    
    # Draw the frame
    draw_top_border(width)
    
    # Empty lines with neurotic thoughts
    neurotic_thoughts = [
        ("My therapist says I have a preoccupation with mortality.", GRAY, 0.02),
        ("I told her *everyone* has a preoccupation with mortality.", GRAY, 0.02),
        ("She said 'not at 3 AM.' I said 'especially at 3 AM.'", BR_YELLOW, 0.02),
        ("", WHITE, 0),
        ("Also, my left eyelid has been twitching for six years.", BR_RED, 0.02),
        ("Or maybe it's the universe trying to Morse code me.", BR_MAG, 0.02),
        ("Either way, I should probably see a neurologist.", GRAY, 0.02),
        ("But what if the neurologist finds something?", BR_RED, 0.02),
        ("What if they *don't* find something?", BR_RED, 0.02),
        ("Both outcomes are equally terrifying.", BR_RED, 0.02),
        ("", WHITE, 0),
    ]
    
    for thought, color, delay in neurotic_thoughts:
        draw_side(thought, width-2, color, "left")
        if delay:
            time.sleep(0.3)
    
    # The glasses appear
    draw_side("", width-2, WHITE)
    draw_side("", width-2, WHITE)
    for line in GLASSES:
        draw_side(f"    {line}", width-2, BR_YELLOW, "center")
    draw_side("", width-2, WHITE)
    
    # Type the quote
    draw_side("", width-2, WHITE)
    quote_lines = QUOTE.split('\n')
    for i, line in enumerate(quote_lines):
        # Typewriter effect for each line
        prefix = "║ " + " " * 2
        suffix = " " * (width - 2 - len(line) - 2) + " ║"
        print(f"{BR_CYAN}{prefix}{RESET}", end="", flush=True)
        typewriter(line, delay=0.04, color=BR_WHITE)
        # Fix the line ending
        move_cursor(int(sys.stdout.tell() / 80) if hasattr(sys.stdout, 'tell') else 0, 0)
    
    draw_side("", width-2, WHITE)
    draw_side(ATTRIBUTION, width-2, BR_CYAN, "center")
    draw_side("", width-2, WHITE)
    draw_side("", width-2, WHITE)
    
    # Brain fart at bottom
    for line in BRAIN_FART:
        draw_side(f"      {line}", width-2, BR_MAG, "center")
    
    draw_side("", width-2, WHITE)
    draw_side(STARS, width-2, BR_YELLOW, "center")
    draw_bottom_border(width)
    
    # Final neurotic post-script
    print()
    post_scripts = [
        (f"{DIM}...wait, did I leave the stove on?{RESET}", 1.0),
        (f"{DIM}{ITALIC}The stove is a metaphor. The stove is *always* a metaphor.{RESET}", 1.5),
        (f"{BR_RED}{BLINK}★{RESET} {BR_YELLOW}Existential dread delivered successfully.{RESET} {BR_RED}{BLINK}★{RESET}", 0),
    ]
    
    for text, pause in post_scripts:
        print(f"         {text}")
        time.sleep(pause)
    
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f"\n{BR_RED}Interrupted. Just like my peace of mind.{RESET}\n")
        sys.exit(0)