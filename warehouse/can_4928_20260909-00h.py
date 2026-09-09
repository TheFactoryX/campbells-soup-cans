"""
Campbell's Soup Can #4928
Produced: 2026-09-09 00:15:40
Worker: Nex AGI: Nex-N2.5-Mini (free) (nex-agi/nex-n2.5-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import sys
import time
import textwrap
import re

QUOTE = "Existence is a cosmic joke, and I'm the nervous little laugh track: anxious, damp, and somehow expected to have opinions."

def ansi_enabled():
    if os.name == "nt":
        try:
            import ctypes
            kernel = ctypes.windll.kernel32
            handle = kernel.GetStdHandle(-11)
            kernel.SetConsoleMode(handle, 7)
            return True
        except Exception:
            return False
    return sys.stdout.isatty()

USE_ANSI = ansi_enabled()
ESC = "\033[" if USE_ANSI else ""
RESET = ESC + "0m"
BOLD = ESC + "1m"
DIM = ESC + "2m"
RED = ESC + "31m"
GREEN = ESC + "32m"
YELLOW = ESC + "33m"
BLUE = ESC + "34m"
CYAN = ESC + "36m"
MAGENTA = ESC + "35m"

def visible_len(text):
    if not USE_ANSI:
        return len(text)
    return len(re.sub(r"\x1b\[[0-9;]*m", "", text))

def clear_screen():
    sys.stdout.write("\033[2J\033[H" if USE_ANSI else "\n\n")
    sys.stdout.flush()

def center(text, width=78):
    pad = max(0, width - visible_len(text))
    left = pad // 2
    right = pad - left
    sys.stdout.write(" " * left + text + " " * right + "\n")
    sys.stdout.flush()

def draw_header(tick):
    sys.stdout.write(BOLD + CYAN + "        PHILOSOPHY.EXE" + RESET + "\n")
    sys.stdout.write("        " + DIM + "loading one existential crisis" + RESET + "\n")
    bar = 36
    pct = (tick % 24) / 24
    filled = int(bar * pct)
    sys.stdout.write("        [" + RED + "=" * filled + DIM + "-" * (bar - filled) + RESET + f"] {pct:.0%}\n")
    sys.stdout.flush()

def draw_thought_bubble():
    art = [
        "             .-~~~~~~~~~~~-.",
        "           /    .-------.   \\",
        "          |    /  ?   ?  \\   |",
        "          |   |    ___    |  |",
        "          |    \\ (___)  /   /",
        "           \\    '-----'   /  /",
        "            '-...........-'",
    ]
    for line in art:
        center(line)
    sys.stdout.flush()

def quote_lines():
    return textwrap.wrap(QUOTE, width=70, break_long_words=True, break_on_hyphens=False)

def draw_quote_frame(lines, shown):
    top = "╔" + "═" * 72 + "╗"
    bottom = "╚" + "═" * 72 + "╝"
    sys.stdout.write(BOLD + BLUE + top + RESET + "\n")
    offset = 0
    for i, line in enumerate(lines):
        take = min(len(line), max(0, shown - offset))
        cursor = ""
        if take < len(line):
            cursor = "▌"
        content = line[:take] + cursor
        offset += len(line)
        pad = max(0, 70 - visible_len(content))
        left = pad // 2
        right = pad - left
        sys.stdout.write("║ " + " " * left + content + " " * right + " ║\n")
    sys.stdout.write(BOLD + BLUE + bottom + RESET + "\n")
    sys.stdout.flush()

def draw_footer(shown, total):
    if shown < total:
        sys.stdout.write(" " * 18 + DIM + "the universe is hesitating..." + RESET + "\n")
    else:
        sys.stdout.write(" " * 18 + GREEN + "one quote served. the void accepts no refunds." + RESET + "\n")
    sys.stdout.flush()

def main():
    lines = quote_lines()
    total = sum(len(line) for line in lines)
    for tick in range(total + 1):
        clear_screen()
        draw_header(tick)
        draw_thought_bubble()
        draw_quote_frame(lines, tick)
        draw_footer(tick, total)
        time.sleep(0.035)

if __name__ == "__main__":
    main()