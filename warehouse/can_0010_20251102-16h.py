"""
Campbell's Soup Can #10
Produced: 2025-11-02 16:34:23
Worker: MiniMax: MiniMax M2 (free) (minimax/minimax-m2:free)
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
import math

# ANSI color codes (standard 8/16 colors)
COLORS = {
    "RESET": "\x1b[0m",
    "BOLD": "\x1b[1m",
    "DIM": "\x1b[2m",
    "ITALIC": "\x1b[3m",
    "UNDERLINE": "\x1b[4m",
    "BLACK": "\x1b[30m",
    "RED": "\x1b[31m",
    "GREEN": "\x1b[32m",
    "YELLOW": "\x1b[33m",
    "BLUE": "\x1b[34m",
    "MAGENTA": "\x1b[35m",
    "CYAN": "\x1b[36m",
    "WHITE": "\x1b[37m",
}

def colorize(text, fg=None, bold=False, dim=False):
    parts = []
    if bold:
        parts.append(COLORS["BOLD"])
    if dim:
        parts.append(COLORS["DIM"])
    if fg and fg in COLORS:
        parts.append(COLORS[fg])
    parts.append(text)
    parts.append(COLORS["RESET"])
    return "".join(parts)

def gradient(text):
    # Create a multi-color gradient through the ROYGBIV-ish order
    palette = ["RED", "YELLOW", "GREEN", "CYAN", "BLUE", "MAGENTA"]
    n = len(text)
    if n == 0:
        return ""
    out = []
    for i, ch in enumerate(text):
        idx = int((i / max(1, n - 1)) * (len(palette) - 1) + 0.5)
        out.append(colorize(ch, fg=palette[idx], bold=True))
    return "".join(out)

def typewrite(text, delay=0.035, blink_cursor=True, newline=True):
    sys.stdout.flush()
    for i, ch in enumerate(text):
        # Animated color gradient as we type
        sys.stdout.write(colorize(ch, fg=["YELLOW", "MAGENTA", "CYAN", "GREEN"][i % 4], bold=True))
        sys.stdout.flush()
        # Blink a subtle cursor only at the end of the line
        if blink_cursor and i == len(text) - 1:
            # little cursor blink
            for _ in range(2):
                sys.stdout.write(colorize("▌", fg="WHITE", bold=True))
                sys.stdout.flush()
                time.sleep(0.15)
                sys.stdout.write("\b \b")
                sys.stdout.flush()
                time.sleep(0.15)
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")

def clear_line():
    # Move to start of line, clear to end, and return to start
    sys.stdout.write("\x1b[2K\r")

def draw_frame(lines, border_color="CYAN"):
    # Draw a pretty frame around content lines
    # lines: list of strings (already colored)
    width = max(len(strip_ansi(line)) for line in lines) if lines else 0
    top = colorize("╭" + "─" * (width + 2) + "╮", fg=border_color, bold=True)
    bottom = colorize("╰" + "─" * (width + 2) + "╯", fg=border_color, bold=True)
    print(top)
    for line in lines:
        padded = line + " " * max(0, width - len(strip_ansi(line)))
        framed = colorize("│ ", fg=border_color, bold=True) + padded + colorize(" │", fg=border_color, bold=True)
        print(framed)
    print(bottom)

def strip_ansi(s):
    # Simple ANSI strip for width calculation
    return "".join(ch for ch in s if ord(ch) >= 0x20 and ch not in "\x1b")

def stars_background(duration=1.6, density=140):
    # Subtle star field that fades away
    lines, cols = get_terminal_size()
    start = time.time()
    random.seed(42)
    star_count = min(density, max(20, (lines * cols) // 35))
    stars = []
    for _ in range(star_count):
        r = random.random()
        if r < 0.6:
            ch = "."
            fg = "BLUE"
        elif r < 0.85:
            ch = "*"
            fg = "CYAN"
        else:
            ch = "·"
            fg = "WHITE"
        stars.append((random.randint(1, max(1, lines - 2)), random.randint(1, max(1, cols - 2)), ch, fg))

    # Render static stars
    buffer = ["\n"] * lines
    for y, x, ch, fg in stars:
        buffer[y - 1] = buffer[y - 1][: (x - 1)] + colorize(ch, fg=fg, dim=True) + buffer[y - 1][x:]
    sys.stdout.write("".join(buffer))
    sys.stdout.flush()

    # Fade them out
    while time.time() - start < duration:
        time.sleep(0.12)
        sys.stdout.write("\x1b[2J\x1b[H")  # clear screen and home
        sys.stdout.flush()
        time.sleep(duration - (time.time() - start))

def get_terminal_size():
    try:
        return tuple(os.get_terminal_size())
    except Exception:
        return 24, 80

def main():
    quote = "I’m not afraid of death; I just don’t want to be there when it happens—awkward small talk with my subconscious."
    tagline = colorize("A neurotic, existential quip (Woody Allen-adjacent)", fg="MAGENTA", dim=True)
    border = "CYAN"

    print(colorize("\n\n", fg="RESET"))
    stars_background(duration=1.2, density=120)
    time.sleep(0.25)

    draw_frame([tagline], border_color=border)
    time.sleep(0.25)

    print(colorize("\n", fg="RESET") + colorize("“", fg="YELLOW", bold=True) + gradient(quote) + colorize("”", fg="YELLOW", bold=True))
    time.sleep(0.15)
    print(colorize("\n— A Woody-Allen-esque mind in a panic", fg="MAGENTA", italic=True))

if __name__ == "__main__":
    main()