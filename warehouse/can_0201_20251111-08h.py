"""
Campbell's Soup Can #201
Produced: 2025-11-11 08:41:39
Worker: MiniMax: MiniMax M2 (free) (minimax/minimax-m2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import shutil

# ANSI color codes
RESET = "\x1b[0m"
BOLD = "\x1b[1m"
FAINT = "\x1b[2m"
ITALIC = "\x1b[3m"
UNDERLINE = "\x1b[4m"

YELLOW = "\x1b[38;5;226m"
CYAN = "\x1b[38;5;51m"
MAGENTA = "\x1b[38;5;201m"
GREEN = "\x1b[38;5;46m"
WHITE = "\x1b[38;5;15m"
ORANGE = "\x1b[38;5;208m"
GRAY = "\x1b[38;5;8m"

def clear_line(n=1):
    for _ in range(n):
        sys.stdout.write("\x1b[2K\x1b[1G")
        sys.stdout.flush()

def move_cursor_up(n=1):
    sys.stdout.write(f"\x1b[{n}A")
    sys.stdout.flush()

def size():
    try:
        return shutil.get_terminal_size((80, 24))
    except Exception:
        return shutil.os_terminal_size((80, 24))

def color(text, code):
    return f"{code}{text}{RESET}"

def pad_to_width(s, width):
    return s + " " * max(0, width - len(s))

def center_text(s, width):
    return " " * max(0, (width - len(s)) // 2) + s

def print_shadow_row(width, left=" ", right=" ", fill=" ", shadow_color=GRAY):
    full = left + fill * width + right
    print(color(full, shadow_color))

def print_box_line(content, width, edge_color=YELLOW, text_color=WHITE):
    sys.stdout.write(color("+", edge_color))
    sys.stdout.write(color(pad_to_width(content, width), text_color))
    sys.stdout.write(color("+" + "\n", edge_color))
    sys.stdout.flush()

def spinner(duration=2.0, message=" Wrestling with existence ", frames=None, rate=0.12):
    if frames is None:
        frames = ["⏳", "loading", "loading.", "loading..", "loading..."]
    start = time.time()
    idx = 0
    width, _ = size()
    border = "+" + "-" * (width - 2) + "+"
    while time.time() - start < duration:
        clear_line(1)
        sys.stdout.write(color(border, ORANGE) + "\n")
        text = f" {message} {frames[idx % len(frames)]} "
        text = text[: max(0, width - 2)]
        sys.stdout.write(color("|", ORANGE))
        sys.stdout.write(color(text.ljust(width - 2), FAINT + YELLOW))
        sys.stdout.write(color("|\n", ORANGE))
        sys.stdout.write(color(border, ORANGE))
        sys.stdout.flush()
        idx += 1
        time.sleep(rate)
    clear_line(3)
    sys.stdout.flush()

def main():
    # Woody Allen–style funny philosophical quote (original)
    quote = (
        "I don't believe in an afterlife; even so, I'm taking night classes."
    )
    author = "— Woody Allen"

    # Get terminal size for a nice fit
    term_width, term_height = size()
    # Keep a comfortable margin
    box_width = min(max(50, term_width - 8), 100)
    # Frame paddings inside the box
    inner = 2
    inner_width = box_width - (inner * 2) - 2  # accounting for the two vertical edges

    # Build the framed, colored output
    top_border = "+" + "-" * (box_width - 2) + "+"
    bottom_border = top_border

    # Shadow row for a tiny 3D effect (only if we have room)
    if box_width + 2 <= term_width:
        shadow_prefix = " "
    else:
        shadow_prefix = ""

    # Print top border
    print(color(top_border, YELLOW))

    # Title row
    title = " A Woodyesqueexistential aside "
    print_box_line(center_text(title, box_width - 2), box_width, edge_color=YELLOW, text_color=ITALIC + CYAN)

    # Divider row
    print(color("|" + "-" * (box_width - 2) + "|", YELLOW))

    # Quote text row(s) - break into chunks that fit the inner width
    quote_words = quote.split()
    lines = []
    current = ""
    for w in quote_words:
        if len(current) + 1 + len(w) <= inner_width:
            current = (current + " " + w).strip()
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    for ln in lines:
        padded = center_text(ln, inner_width)
        sys.stdout.write(color("|", YELLOW))
        sys.stdout.write(color(" " * inner, GRAY))
        sys.stdout.write(color(padded, WHITE))
        sys.stdout.write(color(" " * inner, GRAY))
        sys.stdout.write(color("|\n", YELLOW))
        sys.stdout.flush()

    # Spacer row
    print(color("|" + " " * (box_width - 2) + "|", YELLOW))

    # Author row (centered, italic, green)
    author_text = author.strip()
    author_padded = center_text(author_text, inner_width)
    sys.stdout.write(color("|", YELLOW))
    sys.stdout.write(color(" " * inner, GRAY))
    sys.stdout.write(color(author_padded, ITALIC + GREEN))
    sys.stdout.write(color(" " * inner, GRAY))
    sys.stdout.write(color("|\n", YELLOW))
    sys.stdout.flush()

    # Bottom border
    print(color(bottom_border, YELLOW))

    # Optional tiny shadow for a playful touch
    if box_width + 2 <= term_width:
        print_shadow_row(box_width, left=" ", right=" ", fill=" ", shadow_color=GRAY)

if __name__ == "__main__":
    # A tiny pre-quote animation for whimsy
    spinner(duration=1.4, message=" Polishing punchline ")
    main()