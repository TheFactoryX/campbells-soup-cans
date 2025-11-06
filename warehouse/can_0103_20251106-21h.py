"""
Campbell's Soup Can #103
Produced: 2025-11-06 21:39:06
Worker: MiniMax: MiniMax M2 (free) (minimax/minimax-m2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody-Allen-esque philosophical witticism with color and animation (no external deps)

import sys
import time
import os

RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"

MAGENTA = "\033[35m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
GREEN   = "\033[32m"
WHITE   = "\033[37m"

def enable_sequencing():
    try:
        import sys
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        else:
            if sys.platform == "win32":
                try:
                    import codecs
                    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
                except Exception:
                    pass
    except Exception:
        pass

def colorize(text, code):
    return f"{code}{text}{RESET}"

def supports_color():
    return (
        hasattr(sys.stdout, "isatty") and
        sys.stdout.isatty() and
        os.environ.get("ANSI_COLORS_DISABLED", "") == ""
    )

def slow_write(s, delay):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def fast_write(s):
    sys.stdout.write(s)

def main():
    enable_sequencing()
    USE_COLOR = supports_color()
    USE_ANIM = USE_COLOR and sys.stdout.isatty() and not bool(os.environ.get("NO_ANIM", ""))

    # Line width and content
    MAX_WIDTH = 70

    quote = (
        "I don't fear death; I fear the elevator's 'Close Door' button—"
        "a placebo that gives me the illusion of control in a universe"
        "that definitely prefers me as a spectator."
    )

    # Box drawing
    EDGE = colorize("│", MAGENTA) if USE_COLOR else "|"
    CORNER_TOP = colorize("╭", MAGENTA) if USE_COLOR else "+"
    CORNER_BOT = colorize("╰", MAGENTA) if USE_COLOR else "+"
    BAR = colorize("─", MAGENTA) if USE_COLOR else "-"

    # Choose a warm color for the quote; add bold to feel neurotic
    QUOTE_COLOR = colorize(BOLD + YELLOW, BOLD + YELLOW) if USE_COLOR else ""

    # Center quote lines inside the box width
    def fit_line(s, width):
        s = s.strip()
        if len(s) > width - 2:
            s = s[:width - 5].rstrip() + " ..."
        return s.center(width - 2)

    # Header flair
    header_left = colorize(" Woody", BLUE)
    header_mid  = colorize(" Allen-esque", GREEN)
    header_right= colorize(" Moment ", CYAN)
    header = f"{header_left}{header_mid}{header_right}"

    top_bar_len = max(len(header), MAX_WIDTH + 2)
    top_bar = BAR * (top_bar_len // len(BAR) if BAR else MAX_WIDTH)
    top = f"{CORNER_TOP}{top_bar}{RESET}"

    # Prepare lines
    lines = [fit_line(quote, MAX_WIDTH)]
    inside = "\n".join(f"{EDGE}{colorize(ln, QUOTE_COLOR)}{EDGE}" for ln in lines)
    bottom = f"{CORNER_BOT}{top_bar}{RESET}"

    # Animate or print
    if USE_ANIM:
        slow_write(top + "\n", 0.015)
        slow_write(header + "\n", 0.03)
        for i, line in enumerate(inside.split("\n")):
            slow_write(line + "\n", 0.017 + (0.003 * (i % 2)))
        slow_write(bottom + "\n", 0.02)
        # The cursor lingers like a guilty conscience
    else:
        fast_write(top + "\n")
        fast_write(header + "\n")
        fast_write(inside + "\n")
        fast_write(bottom + "\n")

if __name__ == "__main__":
    main()