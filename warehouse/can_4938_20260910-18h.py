"""
Campbell's Soup Can #4938
Produced: 2026-09-10 18:29:19
Worker: inclusionAI: Ling 3.0 Flash VL (free) (inclusionai/ling-3.0-flash-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import math
import os

# ANSI escape codes
class C:
    R = '\033[91m'  # red
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    M = '\033[95m'  # magenta
    CY = '\033[96m' # cyan
    W = '\033[97m'  # white
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITAL = '\033[3m'
    RESET = '\033[0m'
    BG_RED = '\033[41m'
    BG_BLUE = '\033[44m'
    CLEAR = '\033[2J'
    HIDE_CURSOR = '\033[?25l'
    SHOW_CURSOR = '\033[?25h'
    UP = '\033[A'

QUOTE = "I'm not afraid of death; I just don't want to be there when it happens. — Also, my therapist says I have abandonment issues. I have them too."

TITLE = "═══ A WOODY ALLEN PHILOSOPHER ═══"

def col(i, total=60):
    """Rainbow color based on position."""
    colors = [C.R, C.Y, C.G, C.CY, C.B, C.M, C.R, C.Y]
    return colors[i % len(colors)]

def typewriter(text, delay=0.03, color=C.W):
    for ch in text:
        sys.stdout.write(color + ch + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_frame():
    frames = [
        f"{C.CY}╔{'═' * 58}╗{C.RESET}",
        f"{C.CY}║{C.RESET}{' ' * 58}{C.CY}║{C.RESET}",
    ]
    return frames

def main():
    sys.stdout.write(C.HIDE_CURSOR)
    sys.stdout.write(C.CLEAR)
    sys.stdout.flush()

    # --- Phase 1: Build the box top with animation ---
    width = 62
    border_top = f"{C.CY}{C.BOLD}╔{'═' * width}╗{C.RESET}"
    border_bot = f"{C.CY}{C.BOLD}╚{'═' * width}╝{C.RESET}"

    # Print top border with a sweep effect
    for i in range(width + 2):
        sys.stdout.write(C.CY + "╔" + "═" * i + C.RESET)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

    # Print side borders with rainbow dots
    for row in range(4):
        dots = ''.join(col(i, 58) + '·' for i in range(58))
        sys.stdout.write(f"{C.CY}║{C.RESET} {C.DIM}{dots}{C.RESET} {C.CY}║{C.RESET}\n")
        time.sleep(0.08)

    # Title row with pulsing colors
    title_text = " WOODY ALLEN'S EXISTENTIAL WISDOM "
    padding = (width - len(title_text)) // 2
    for pulse in range(6):
        c = [C.R, C.Y, C.G, C.CY, C.B, C.M][pulse % 6]
        sys.stdout.write(f"\r{C.CY}║{C.RESET}{' ' * padding}{c}{C.BOLD}{title_text}{C.RESET}{' ' * (width - padding - len(title_text))}{C.CY}║{C.RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
    print()

    for row in range(2):
        dots = ''.join(col(i, 58) + '·' for i in range(58))
        sys.stdout.write(f"{C.CY}║{C.RESET} {C.DIM}{dots}{C.RESET} {C.CY}║{C.RESET}\n")
        time.sleep(0.08)

    # Middle border
    mid = f"{C.CY}║{C.RESET}{'═' * width}{C.CY}║{C.RESET}"
    sys.stdout.write(mid + "\n")
    sys.stdout.flush()

    # --- Phase 2: The quote with typewriter + rainbow ---
    for row in range(2):
        dots = ''.join(col(i, 58) + '·' for i in range(58))
        sys.stdout.write(f"{C.CY}║{C.RESET} {C.DIM}{dots}{C.RESET} {C.CY}║{C.RESET}\n")
        time.sleep(0.06)

    # Quote line by line with rotating colors
    print()  # visual breathing room
    words = QUOTE.split(' ')
    line = ""
    char_count = 0
    for word in words:
        test_line = line + word + " "
        if len(test_line) > 72:
            # Print current line with typewriter
            for i, ch in enumerate(line):
                c = col(char_count + i)
                sys.stdout.write(c + ch + C.RESET)
                sys.stdout.flush()
                time.sleep(0.025)
            print()
            time.sleep(0.05)
            line = word + " "
            char_count = 0
        else:
            line = test_line
            char_count += len(word) + 1

    # Last line
    if line:
        for i, ch in enumerate(line):
            c = col(char_count + i)
            sys.stdout.write(c + ch + C.RESET)
            sys.stdout.flush()
            time.sleep(0.025)
    print()

    time.sleep(0.3)

    for row in range(2):
        dots = ''.join(col(i, 58) + '·' for i in range(58))
        sys.stdout.write(f"{C.CY}║{C.RESET} {C.DIM}{dots}{C.RESET} {C.CY}║{C.RESET}\n")
        time.sleep(0.08)

    # Middle border again
    sys.stdout.write(mid + "\n")
    sys.stdout.flush()

    for row in range(3):
        dots = ''.join(col(i, 58) + '·' for i in range(58))
        sys.stdout.write(f"{C.CY}║{C.RESET} {C.DIM}{dots}{C.RESET} {C.CY}║{C.RESET}\n")
        time.sleep(0.08)

    # --- Phase 3: Attribution with bounce effect ---
    attr = "— Neurotic, neurotic, neurotic."
    for bounce in range(3):
        spaces = " " * (bounce * 2)
        c = [C.Y, C.G, C.CY][bounce]
        sys.stdout.write(f"\r{C.CY}║{C.RESET}{spaces}{c}{C.BOLD}{attr}{C.RESET}{' ' * (width - len(attr) - spaces * 2 - 1)}{C.CY}║{C.RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
    print()

    for row in range(2):
        dots = ''.join(col(i, 58) + '·' for i in range(58))
        sys.stdout.write(f"{C.CY}║{C.RESET} {C.DIM}{dots}{C.RESET} {C.CY}║{C.RESET}\n")
        time.sleep(0.1)

    # Bottom border sweep
    for i in range(width + 1, -1, -1):
        if i == 0:
            sys.stdout.write(C.CY + "╚" + "═" * 0 + C.RESET)
        else:
            sys.stdout.write(" " * i + C.CY + "╚" + C.RESET)
        sys.stdout.flush()
        time.sleep(0.015)
    # Draw bottom border left to right
    print(border_bot)

    print()
    sys.stdout.write(C.SHOW_CURSOR)
    print(f"{C.DIM}{C.M}Existence is just misery in a nicer outfit.{C.RESET}")
    print(f"{C.DIM}{C.Y}Press Ctrl+C to escape reality.{C.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(C.SHOW_CURSOR + C.RESET + "\n")
        print(f"\n{C.R}{C.BOLD}See? Even the program has existential dread.{C.RESET}")
        sys.exit(0)