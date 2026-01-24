"""
Campbell's Soup Can #1813
Produced: 2026-01-24 08:42:45
Worker: Auto Router (openrouter/auto)
Employment: Paid
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
import itertools
import math
import random

ESC = "\033["
RESET = ESC + "0m"

COLORS = {
    "dim": ESC + "2m",
    "bold": ESC + "1m",
    "italic": ESC + "3m",
    "blink": ESC + "5m",
    "reverse": ESC + "7m",
    "cyan": ESC + "36m",
    "magenta": ESC + "35m",
    "yellow": ESC + "33m",
    "blue": ESC + "34m",
    "white": ESC + "37m",
}


def get_size():
    try:
        size = shutil.get_terminal_size(fallback=(80, 24))
        return size.columns, size.lines
    except Exception:
        return 80, 24


def clear():
    sys.stdout.write(ESC + "2J" + ESC + "H")
    sys.stdout.flush()


def center(text, width):
    if len(text) >= width:
        return text
    pad = (width - len(text)) // 2
    return " " * pad + text


def wrap_text(text, max_width):
    words = text.split()
    lines = []
    current = []
    length = 0
    for w in words:
        if length + len(w) + (1 if current else 0) > max_width:
            lines.append(" ".join(current))
            current = [w]
            length = len(w)
        else:
            current.append(w)
            length += len(w) + (1 if current[:-1] else 0)
    if current:
        lines.append(" ".join(current))
    return lines


def spinner_animation(duration=2.5):
    cols, _ = get_size()
    message = "Calibrating existential anxiety"
    dots_cycle = itertools.cycle(["", ".", "..", "..."])
    spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
    start = time.time()
    while time.time() - start < duration:
        dots = next(dots_cycle)
        spin = next(spinner)
        bar_width = 24
        elapsed = time.time() - start
        progress = min(1.0, elapsed / duration)
        filled = int(bar_width * progress)
        bar = "[" + "█" * filled + " " * (bar_width - filled) + "]"
        line = f"{COLORS['magenta']}{spin} {COLORS['cyan']}{message}{dots}  {COLORS['yellow']}{bar}{RESET}"
        sys.stdout.write("\r" + center(line, cols)[:cols])
        sys.stdout.flush()
        time.sleep(0.06)
    sys.stdout.write("\r" + " " * cols + "\r")
    sys.stdout.flush()


def draw_starfield_frame(t, cols, rows, density=0.015):
    random.seed(int(t * 1000))
    lines = []
    for r in range(rows):
        line_chars = []
        for c in range(cols):
            if random.random() < density:
                star_type = random.random()
                if star_type < 0.33:
                    ch = COLORS["cyan"] + "." + RESET
                elif star_type < 0.66:
                    ch = COLORS["yellow"] + "*" + RESET
                else:
                    ch = COLORS["white"] + "+" + RESET
            else:
                ch = " "
            line_chars.append(ch)
        lines.append("".join(line_chars))
    return "\n".join(lines)


def starfield_animation(duration=1.4):
    cols, rows = get_size()
    rows = max(10, min(rows, 24))
    start = time.time()
    while time.time() - start < duration:
        t = time.time() - start
        clear()
        sys.stdout.write(draw_starfield_frame(t, cols, rows))
        caption = f"{COLORS['dim']}{COLORS['yellow']}∞ The universe, probably looking away politely ∞{RESET}"
        sys.stdout.write("\n" + center(caption, cols) + "\n")
        sys.stdout.flush()
        time.sleep(0.06)


def draw_thought_brain():
    cols, _ = get_size()
    brain = [
        r"           ___      ",
        r"       .-\"   \"-.   ",
        r"     .'  .-. .-.'. ",
        r"    /   ( o| |o ) \ ",
        r"   | .--. '-^-' .-|",
        r"   |(    `-----'  )|",
        r"    \             / ",
        r"     '.         .'  ",
        r"       '-.___.-'    ",
    ]
    bubble = [
        "        (overthinking...)",
        "           o",
        "            o",
    ]
    for i, line in enumerate(brain + bubble):
        color = COLORS["magenta"] if i < len(brain) else COLORS["cyan"]
        sys.stdout.write(center(color + line + RESET, cols) + "\n")


def typewriter(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)


def show_quote_box(quote):
    cols, _ = get_size()
    max_inner = min(cols - 10, 80)
    lines = wrap_text(quote, max_inner)
    inner_width = max(len(l) for l in lines)
    total_width = inner_width + 4

    top = "┏" + "━" * (total_width - 2) + "┓"
    bottom = "┗" + "━" * (total_width - 2) + "┛"

    clear()
    sys.stdout.write("\n" * 2)
    sys.stdout.write(center(COLORS["cyan"] + top + RESET, cols) + "\n")

    for i, line in enumerate(lines):
        pad = inner_width - len(line)
        left = pad // 2
        right = pad - left
        padded = "┃ " + " " * left + line + " " * right + " ┃"
        color = COLORS["yellow"] if i == len(lines) // 2 else COLORS["white"]
        sys.stdout.write(center(color + padded + RESET, cols) + "\n")

    sys.stdout.write(center(COLORS["cyan"] + bottom + RESET, cols) + "\n\n")

    attribution = f"{COLORS['dim']}{COLORS['italic']}— a very worried voice in my head{RESET}"
    sys.stdout.write(center(attribution, cols) + "\n\n")
    sys.stdout.flush()


def main():
    quote = (
        "I tried to find myself through meditation, but all I discovered was that "
        "even in complete silence, I can still interrupt myself."
    )

    clear()
    spinner_animation()
    starfield_animation()
    clear()
    draw_thought_brain()
    time.sleep(1.2)

    cols, _ = get_size()
    sys.stdout.write("\n")
    heading = f"{COLORS['bold']}{COLORS['blue']}One Brief, Neurotic Observation:{RESET}"
    sys.stdout.write(center(heading, cols) + "\n\n")

    # Build the box content as a single string, then type it out for effect
    max_inner = min(cols - 10, 80)
    lines = wrap_text(quote, max_inner)
    inner_width = max(len(l) for l in lines)
    total_width = inner_width + 4
    top = "┏" + "━" * (total_width - 2) + "┓"
    bottom = "┗" + "━" * (total_width - 2) + "┛"

    box_lines = [top]
    for line in lines:
        pad = inner_width - len(line)
        left = pad // 2
        right = pad - left
        padded = "┃ " + " " * left + line + " " * right + " ┃"
        box_lines.append(padded)
    box_lines.append(bottom)

    # Animated printing of the quote box
    sys.stdout.write("\n")
    for idx, line in enumerate(box_lines):
        if idx == 0 or idx == len(box_lines) - 1:
            colored = COLORS["magenta"] + line + RESET
        elif idx == (len(box_lines) // 2):
            colored = COLORS["yellow"] + line + RESET
        else:
            colored = COLORS["white"] + line + RESET
        sys.stdout.write(center("", cols))
        sys.stdout.flush()
        typewriter(center(colored, cols) + "\n", delay=0.0015)

    sys.stdout.write("\n")
    attribution = f"{COLORS['dim']}{COLORS['italic']}— a very worried voice in my head{RESET}"
    typewriter(center(attribution, cols) + "\n", delay=0.01)

    sys.stdout.write("\n")
    faint_note = (
        f"{COLORS['dim']}Tip: if the universe calls, let it go to voicemail.{RESET}"
    )
    sys.stdout.write(center(faint_note, cols) + "\n")

    sys.stdout.write(RESET)
    sys.stdout.flush()


if __name__ == "__main__":
    main()