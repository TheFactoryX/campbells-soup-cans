"""
Campbell's Soup Can #4993
Produced: 2026-09-20 01:10:23
Worker: inclusionAI: Ling 3.0 Flash VL (free) (inclusionai/ling-3.0-flash-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophical Quote Generator
A visually stunning, animated terminal experience — pure Python, zero dependencies.
"""

import sys
import time
import os
import math
import threading

# ──────────────────────────── ANSI COLOR PALETTE ────────────────────────────

RED      = '\033[91m'
GREEN    = '\033[92m'
YELLOW   = '\033[93m'
BLUE     = '\033[94m'
MAGENTA  = '\033[95m'
CYAN     = '\033[96m'
WHITE    = '\033[97m'
BOLD     = '\033[1m'
DIM      = '\033[2m'
ITALIC   = '\033[3m'
UNDERLINE= '\033[4m'
RESET    = '\033[0m'
BRIGHT_RED    = '\033[1;31m'
BRIGHT_GREEN  = '\033[1;32m'
BRIGHT_YELLOW = '\033[1;33m'
BRIGHT_BLUE   = '\033[1;34m'
BRIGHT_MAGENTA= '\033[1;35m'
BRIGHT_CYAN   = '\033[1;36m'

COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
BRIGHT_COLORS = [BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN]

# ──────────────────────────── QUOTE DATA ────────────────────────────

QUOTE = (
    "\"I'm not afraid of death — "
    "I just don't want to be there "
    "when it happens. "
    "Also, I'm afraid of it. "
    "But mostly the first part.\""
)

AUTHOR = "— Woody Allen, probably, if he remembered"

# ──────────────────────────── ANIMATIONS ────────────────────────────

CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(text, delay=0.03, color=WHITE, bold=False):
    """Print text with a typewriter effect."""
    prefix = BOLD if bold else ''
    for char in text:
        sys.stdout.write(prefix + color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def breathe_text(text, cycles=6, color=BRIGHT_CYAN):
    """Make text pulse by varying intensity using dim/normal swaps."""
    for _ in range(cycles):
        sys.stdout.write(DIM + color + text + RESET + '\n')
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write(BOLD + color + text + RESET + '\n')
        sys.stdout.flush()
        time.sleep(0.15)
    print()

# ──────────────────────────── ASCII ART FRAME ────────────────────────────

def draw_frame(width=62):
    """Draw an animated decorative frame."""
    corners = {
        'tl': BRIGHT_CYAN + '╔', 'tr': BRIGHT_CYAN + '╗',
        'bl': BRIGHT_CYAN + '╚', 'br': BRIGHT_CYAN + '╝',
    }
    h_line = BRIGHT_CYAN + '═'
    v_line = BRIGHT_CYAN + '║'
    
    # Top border
    top = corners['tl'] + h_line * (width - 2) + corners['tr']
    bottom = corners['bl'] + h_line * (width - 2) + corners['br']
    side = v_line + ' ' * (width - 2) + v_line
    
    frame_lines = [top]
    for _ in range(14):
        frame_lines.append(side)
    frame_lines.append(bottom)
    return frame_lines

# ──────────────────────────── SPARKLE ANIMATION ────────────────────────────

def sparkle_banner(width=62):
    """Show a sparkle/decoration line with cycling colors."""
    spark_chars = ['✦', '✧', '⋆', '⋅', '•', '◦']
    for i in range(width - 2):
        char = spark_chars[i % len(spark_chars)]
        color = BRIGHT_COLORS[i % len(BRIGHT_COLORS)]
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

# ──────────────────────────── DECORATIVE ELEMENTS ────────────────────────────

def draw_philosophy_stars(width=62):
    """Draw a line of philosophical stars and dots."""
    line = ""
    for i in range(width - 2):
        if i % 7 == 0:
            line += BRIGHT_MAGENTA + '✦' + RESET
        elif i % 11 == 0:
            line += BRIGHT_YELLOW + '✧' + RESET
        elif i % 13 == 0:
            line += BRIGHT_CYAN + '⋆' + RESET
        else:
            line += '·'
    print(BOLD + line + RESET)

def draw_divider(color=BRIGHT_CYAN, width=62):
    print(color + '│' + '─' * (width - 2) + '│' + RESET)

# ──────────────────────────── MAIN ────────────────────────────

def main():
    # Hide cursor for cleaner animation
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()
    
    try:
        # ── PHASE 1: Title splash ──
        CLEAR()
        title = "★ PHILOSOPHY ★"
        padded = ' ' * 15 + title + ' ' * 15
        
        for color in BRIGHT_COLORS:
            sys.stdout.write('\033[2K')  # clear line
            sys.stdout.write(BOLD + color + padded + RESET + '\n')
            sys.stdout.flush()
            time.sleep(0.1)
        
        time.sleep(0.3)
        
        # ── PHASE 2: Animated sparkle banner ──
        print()
        sparkle_banner()
        time.sleep(0.3)
        
        # ── PHASE 3: Draw the frame top ──
        frame = draw_frame()
        for line in frame[:5]:
            print(BOLD + line + RESET)
            time.sleep(0.05)
        
        time.sleep(0.2)
        
        # ── PHASE 4: Philosophical stars ──
        sys.stdout.write(BOLD + BRIGHT_CYAN + '║' + RESET + ' ')
        draw_philosophy_stars(width=58)
        time.sleep(0.3)
        
        # ── PHASE 5: "Existential Thought of the Moment" header ──
        header = " Existential Thought of the Moment "
        header_padded = header.center(58)
        sys.stdout.write(BOLD + BRIGHT_YELLOW + '║' + RESET + ' ')
        sys.stdout.write(BOLD + BRIGHT_YELLOW + header_padded + RESET + '\n')
        sys.stdout.flush()
        time.sleep(0.4)
        
        draw_divider(BRIGHT_YELLOW, width=60)
        time.sleep(0.2)
        
        # ── PHASE 6: The quote with typewriter + color cycling ──
        # Split quote into lines for nice formatting
        quote_lines = [
            ' "I\'m not afraid of death — ',
            ' I just don\'t want to be there ',
            ' when it happens. Also, I\'m ',
            ' afraid of it. But mostly the ',
            ' first part."',
        ]
        
        time.sleep(0.3)
        
        for i, line in enumerate(quote_lines):
            sys.stdout.write(BOLD + BRIGHT_MAGENTA + '║' + RESET + ' ')
            # Typewrite each line with cycling color prefix
            color = BRIGHT_COLORS[i % len(BRIGHT_COLORS)]
            typewrite(line, delay=0.04, color=WHITE, bold=False)
            time.sleep(0.1)
        
        time.sleep(0.2)
        
        # ── PHASE 7: Author attribution ──
        draw_divider(BRIGHT_MAGENTA, width=60)
        time.sleep(0.2)
        
        author_line = " " + AUTHOR
        # Print author in a breathing animation
        for _ in range(3):
            sys.stdout.write(BOLD + BRIGHT_CYAN + '║' + RESET + ' ')
            sys.stdout.write(DIM + BRIGHT_CYAN + author_line + RESET + '\n')
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write(BOLD + BRIGHT_CYAN + '║' + RESET + ' ')
            sys.stdout.write(BOLD + BRIGHT_CYAN + author_line + RESET + '\n')
            sys.stdout.flush()
            time.sleep(0.2)
        
        time.sleep(0.3)
        
        # ── PHASE 8: Closing thought ──
        closing = " " * 18 + "* existential dread incoming *"
        for _ in range(4):
            sys.stdout.write('\033[2K')
            sys.stdout.write(DIM + GREEN + closing + RESET + '\n')
            sys.stdout.flush()
            time.sleep(0.3)
            CLEAR()
            time.sleep(0.05)
        
        # ── PHASE 9: Bottom frame ──
        # Re-draw the frame as bottom section
        frame = draw_frame()
        
        # Show remaining frame lines as closing
        time.sleep(0.2)
        for i in range(5, len(frame)):
            print(BOLD + frame[i] + RESET)
            time.sleep(0.04)
        
        time.sleep(0.5)
        
        # ── PHASE 10: Final colorful burst ──
        print()
        final_text = " THAT'S EXISTENCE, FOLKS "
        for color in BRIGHT_COLORS * 2:
            sys.stdout.write('\033[2K\r')
            sys.stdout.write(BOLD + color + final_text + RESET)
            sys.stdout.flush()
            time.sleep(0.12)
        
        print()  # newline
        print(BRIGHT_GREEN + BOLD + "\n  Was that profound? Neither did I.\n" + RESET)
        
        # Breathe the final message
        breathe_text("  Was that profound? Neither did I. ", cycles=2, color=BRIGHT_GREEN)
        
    except KeyboardInterrupt:
        print(f"\n{BRIGHT_RED}Even the animation ran away — very Woody.{RESET}")
    finally:
        # Show cursor again
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

if __name__ == "__main__":
    main()