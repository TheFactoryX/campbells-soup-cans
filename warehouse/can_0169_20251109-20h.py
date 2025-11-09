"""
Campbell's Soup Can #169
Produced: 2025-11-09 20:30:56
Worker: Polaris Alpha (openrouter/polaris-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import shutil
import math

# Simple, dependency-free, colorful, slightly neurotic existential gag.
# One quote only. Extra drama included.

# ANSI escape codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
BLINK   = "\033[5m"

FG_RED      = "\033[31m"
FG_GREEN    = "\033[32m"
FG_YELLOW   = "\033[33m"
FG_BLUE     = "\033[34m"
FG_MAGENTA  = "\033[35m"
FG_CYAN     = "\033[36m"
FG_WHITE    = "\033[37m"

FG_BRIGHT_BLACK  = "\033[90m"
FG_BRIGHT_YELLOW = "\033[93m"
FG_BRIGHT_CYAN   = "\033[96m"
FG_BRIGHT_MAGENTA= "\033[95m"

BG_BLUE     = "\033[44m"
BG_BLACK    = "\033[40m"
BG_MAGENTA  = "\033[45m"
BG_CYAN     = "\033[46m"

CLEAR = "\033[2J"
HOME  = "\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

# The single Woody-Allen-style philosophical quote:
QUOTE = (
    "I asked the universe for meaning, and it put me on hold with music,\n"
    "then suggested I leave a message after the absurdity."
)

SIGNATURE = "- Anxious Voice in My Head"

def slow_print(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.flush()

def get_width():
    try:
        return shutil.get_terminal_size((80, 20)).columns
    except:
        return 80

def center_line(line, width):
    return line.center(width)

def wave_color(i, total, base_color, alt_color):
    # gentle sinusoidal swap between two colors
    t = (i / max(1, total)) * math.pi
    return base_color if math.sin(t) > 0 else alt_color

def animate_intro():
    width = get_width()
    banner = "EXISTENTIAL HOLD MUSIC..."
    sys.stdout.write(CLEAR + HOME + HIDE_CURSOR)
    for i in range(18):
        color = wave_color(i, 18, FG_BRIGHT_CYAN, FG_BRIGHT_MAGENTA)
        padding = " " * ((i // 2) % 6)
        line = padding + banner + padding
        sys.stdout.write(HOME)
        sys.stdout.write("\n" * 3)
        sys.stdout.write(center_line(color + BOLD + line + RESET, width) + "\n")
        bar_len = 30
        filled = (i % (bar_len + 1))
        bar = "[" + "#" * filled + "-" * (bar_len - filled) + "]"
        sys.stdout.write("\n")
        sys.stdout.write(center_line(FG_YELLOW + bar + RESET, width))
        sys.stdout.write("\n" * 10)
        sys.stdout.flush()
        time.sleep(0.08)

def draw_boxed_quote():
    width = get_width()
    # Prepare lines (quote already has a newline)
    lines = QUOTE.split("\n")
    max_len = max(len(line) for line in lines + [SIGNATURE])
    box_width = min(max_len + 8, width - 4)
    inner_width = box_width - 4

    # Build top border
    top = FG_BLUE + BOLD + "╔" + "═" * (box_width - 2) + "╗" + RESET
    bottom = FG_BLUE + BOLD + "╚" + "═" * (box_width - 2) + "╝" + RESET

    # Colors for shifting effect
    gradient_colors = [FG_CYAN, FG_BRIGHT_CYAN, FG_BRIGHT_YELLOW, FG_MAGENTA, FG_BRIGHT_MAGENTA]

    def fmt_line(text, idx):
        truncated = text[:inner_width]
        color = gradient_colors[idx % len(gradient_colors)]
        padded = truncated + " " * (inner_width - len(truncated))
        return (
            FG_BLUE + BOLD + "║ " + RESET +
            color + ITALIC + padded + RESET +
            FG_BLUE + BOLD + " ║" + RESET
        )

    sys.stdout.write("\n" * 2)
    sys.stdout.write(center_line(top, width) + "\n")

    # Animated typewriter effect for quote lines
    idx = 0
    for line in lines:
        display_line = " " * inner_width
        # print empty line first
        boxed = fmt_line(display_line, idx)
        sys.stdout.write(center_line(boxed, width) + "\n")
        sys.stdout.flush()
        # overwrite with typing effect
        sys.stdout.write("\033[F")  # move cursor up one line
        # reconstruct with typing
        truncated = line[:inner_width]
        padded = truncated + " " * (inner_width - len(truncated))
        color = gradient_colors[idx % len(gradient_colors)]
        start = FG_BLUE + BOLD + "║ " + RESET + color + ITALIC
        end = RESET + FG_BLUE + BOLD + " ║" + RESET
        sys.stdout.write(center_line(start, width)[:-len(start)-len(end)] + "")  # ensure we stay centered
        sys.stdout.write("\r")  # reset to start of line (within terminal)
        # Simplify: just re-center the full line per char:
        for i, ch in enumerate(padded):
            line_now = padded[:i+1] + " " * (inner_width - i - 1)
            box_line = (
                FG_BLUE + BOLD + "║ " + RESET +
                color + ITALIC + line_now + RESET +
                FG_BLUE + BOLD + " ║" + RESET
            )
            sys.stdout.write("\r" + center_line(box_line, width))
            sys.stdout.flush()
            time.sleep(0.01)
        sys.stdout.write("\n")
        sys.stdout.flush()
        idx += 1

    # Signature line (no typing, but with a little shimmer)
    sign_padded = SIGNATURE[:inner_width]
    sign_padded += " " * (inner_width - len(sign_padded))

    for s in range(3):
        shade = gradient_colors[(idx + s) % len(gradient_colors)]
        line = (
            FG_BLUE + BOLD + "║ " + RESET +
            shade + DIM + sign_padded + RESET +
            FG_BLUE + BOLD + " ║" + RESET
        )
        sys.stdout.write(center_line(line, width) + "\r")
        sys.stdout.flush()
        time.sleep(0.11)
    sys.stdout.write(center_line(line, width) + "\n")

    sys.stdout.write(center_line(bottom, width) + "\n")

def little_epilogue():
    width = get_width()
    text = FG_BRIGHT_BLACK + DIM + "(Please remain on the line while the cosmos continues not answering.)" + RESET
    sys.stdout.write("\n")
    slow_print(center_line(text, width), delay=0.003)
    sys.stdout.write("\n")

def pulsating_ellipsis():
    width = get_width()
    base = "Existence is buffering"
    for i in range(10):
        dots = "." * (i % 4)
        color = wave_color(i, 10, FG_BRIGHT_CYAN, FG_BRIGHT_MAGENTA)
        line = color + base + dots + RESET
        sys.stdout.write("\r" + center_line(line, width))
        sys.stdout.flush()
        time.sleep(0.12)
    sys.stdout.write("\r" + " " * width + "\r")
    sys.stdout.flush()

def main():
    try:
        animate_intro()
        draw_boxed_quote()
        little_epilogue()
        pulsating_ellipsis()
    finally:
        sys.stdout.write(SHOW_CURSOR + RESET + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()