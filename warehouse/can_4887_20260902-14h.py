"""
Campbell's Soup Can #4887
Produced: 2026-09-02 14:29:57
Worker: Ling 3.0 Flash Fin (free) (inclusionai/ling-3.0-flash-fin:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ── ANSI Colors ──────────────────────────────────────────────────
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALICS = "\033[3m"
RESET   = "\033[0m"
UNDERLINE = "\033[4m"

# ── Helpers ──────────────────────────────────────────────────────
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.025, color=None, bold=False):
    """Print text character by character with a typewriter effect."""
    style = ""
    if bold:   style += BOLD
    if color:  style += color
    for ch in text:
        sys.stdout.write(style + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def typewriter_line(parts, delay=0.025):
    """Print a line made of multiple (text, color, bold) tuples."""
    for text, color, bold in parts:
        style = ""
        if bold:   style += BOLD
        if color:  style += color
        for ch in text:
            sys.stdout.write(style + ch + RESET)
            sys.stdout.flush()
            time.sleep(delay)
    print()

def flash_dots(count=3, times=2):
    """Flash animated dots."""
    for _ in range(times):
        for i in range(1, count + 1):
            sys.stdout.write(YELLOW + "  " + "." * i + " " + RESET)
            sys.stdout.flush()
            time.sleep(0.4)
            sys.stdout.write("\r                                    \r")
        time.sleep(0.3)

def center(text, width=70):
    return text.center(width)

# ── Main ─────────────────────────────────────────────────────────
def main():
    clear()
    time.sleep(0.3)

    # ── Decorative top bar ────────────────────────────────────────
    print()
    print(CYAN + "╔" + "═" * 68 + "╗")
    print(CYAN + "║" + YELLOW + BOLD + center("  A Woody Allen Production  ", 66) + CYAN + "║")
    print(CYAN + "╚" + "═" * 68 + "╝")
    print()

    # ── Animated title reveal ─────────────────────────────────────
    title = (
        (BLUE + BOLD, "The", False),
        (MAGENTA + BOLD, " Neurotic ", True),
        (CYAN + BOLD, "Thinker's", False),
        (YELLOW + BOLD, " Handbook", False),
    )
    typewriter_line(title, delay=0.04)
    print()

    # ── Animated dots while "thinking" ────────────────────────────
    typewriter(DIM + "  Hmm... let me think about this..." + RESET, delay=0.04, color=DIM)
    flash_dots()
    print()
    time.sleep(0.2)

    # ── Boxed quote ───────────────────────────────────────────────
    quote_width = 64
    print()

    # Top border
    sys.stdout.write(MAGENTA + "╭" + "─" * quote_width + "╮" + RESET + "\n")
    sys.stdout.flush()

    # Quote text in chunks
    quote_lines = [
        "I'm not afraid of death; I just don't want",
        "to be there when it happens. And even then",
        "I'd probably worry about the traffic.",
    ]
    for line in quote_lines:
        padding = quote_width - len(line) - 2
        sys.stdout.write(
            MAGENTA + "│" + RESET + " "
            + WHITE + BOLD + line
            + RESET + " " * padding
            + MAGENTA + "│" + RESET + "\n"
        )
        sys.stdout.flush()
        time.sleep(0.2)

    # Bottom border
    sys.stdout.write(MAGENTA + "╰" + "─" * quote_width + "╯" + RESET + "\n")
    sys.stdout.flush()
    print()

    # ── Attribution line ──────────────────────────────────────────
    typewriter(
        RED + ITALICS + "  — Woody Allen (probably, if he could remember to say it)" + RESET,
        delay=0.03
    )
    print()

    # ── Animated reflection / punchline ───────────────────────────
    time.sleep(0.3)
    print(CYAN + "  " + DIM + "  " + UNDERLINE + "The universe is out to get us." + RESET)
    time.sleep(0.5)
    print(YELLOW + "  " + DIM + "  " + "But so is the parking meter." + RESET)
    time.sleep(0.5)
    print(MAGENTA + "  " + DIM + "  " + "I'm just saying — life's absurd." + RESET)
    time.sleep(0.3)
    print(RED   + "  " + BOLD + "  " + "So why not laugh?" + RESET)
    print()

    # ── Animated closing message ──────────────────────────────────
    time.sleep(0.3)
    typewriter(BOLD + GREEN + "  That's all, folks!  (Go see a shrink.)" + RESET, delay=0.04)
    print()
    print(DIM + center("  Press Enter to exit... ", 70) + DIM, end="")
    sys.stdout.flush()
    try:
        input()
    except EOFError:
        pass

if __name__ == "__main__":
    main()