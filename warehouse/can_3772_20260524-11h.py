"""
Campbell's Soup Can #3772
Produced: 2026-05-24 11:42:43
Worker: OpenAI: GPT-5 (openai/gpt-5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Note: The following is an original, playful, neurotic, self-deprecating, existential one-liner,
# capturing a similar vibe—not the exact style—of any specific living writer.

import sys
import time
import shutil
import os
import random

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
CLEAR = "\033[2J\033[H"

def fg256(n):
    return f"\033[38;5;{n}m"

def center_line(s, width):
    if len(s) >= width:
        return s
    pad = (width - len(s)) // 2
    return " " * pad + s

def safe_columns(default=80):
    try:
        return shutil.get_terminal_size((default, 24)).columns
    except:
        return default

def flicker_bulb(width, cycles=6):
    bulb1 = [
        "   .-.",
        "  (   )",
        "   \\_/",
        "  .-|-.",
        " /  |  \\",
        "    |",
        "   / \\"
    ]
    bulb2 = [
        "   .-.",
        "  (   )",
        "   \\_/",
        "  .-+-.",
        " /  |  \\",
        "    |",
        "   / \\"
    ]
    frames = [bulb1, bulb2]
    for i in range(cycles):
        os.system("")  # enable ANSI on some Windows terminals
        sys.stdout.write(CLEAR)
        color = fg256(226) + (BOLD if i % 2 == 0 else DIM)
        jitter = " " * (0 if i % 3 else 1)
        for line in frames[i % 2]:
            sys.stdout.write(center_line(jitter + color + line + RESET, width) + "\n")
        # tiny sparkles
        sparkle_color = fg256(229 if i % 2 == 0 else 220)
        twinkle = jitter + sparkle_color + ("  *" if i % 2 else "   *") + RESET
        sys.stdout.write(center_line(twinkle, width) + "\n")
        sys.stdout.flush()
        time.sleep(0.085 + (0.01 * (i % 2)))
    # Final bright bulb printed, no clear
    sys.stdout.write(CLEAR)
    final_color = fg256(226) + BOLD
    for line in bulb1:
        sys.stdout.write(center_line(final_color + line + RESET, width) + "\n")
    sys.stdout.write(center_line(final_color + "   ★" + RESET, width) + "\n")
    sys.stdout.flush()

def type_char(c, idx):
    palette = [226, 229, 231, 159, 195, 153]  # warm to cool whispers
    color = fg256(palette[idx % len(palette)]) + BOLD
    sys.stdout.write(color + c + RESET)
    sys.stdout.flush()
    if c in ".!?":
        time.sleep(0.14)
    elif c in ",;:":
        time.sleep(0.09)
    elif c == " ":
        time.sleep(0.015)
    else:
        time.sleep(0.02 + random.uniform(-0.006, 0.006))

def draw_quote_box(quote, width):
    # compute inner width, ensuring quote fits even on small terminals
    min_inner = max(len(quote), 40)
    cap = width - 6
    inner = min_inner if cap >= min_inner else len(quote)
    box_w = inner + 2
    indent = max((width - box_w) // 2, 0)
    # colors for box
    border_c = fg256(135) + BOLD
    shade_c = fg256(60) + DIM

    top = "┏" + "━" * inner + "┓"
    mid_blank = "┃" + " " * inner + "┃"
    bottom = "┗" + "━" * inner + "┛"

    # spacer under bulb
    sys.stdout.write("\n")

    sys.stdout.write(" " * indent + border_c + top + RESET + "\n")
    sys.stdout.write(" " * indent + shade_c + mid_blank + RESET + "\n")

    # Prepare the typing line
    left_pad = max((inner - len(quote)) // 2, 0)
    right_pad = inner - left_pad - len(quote)

    # Left border + left padding
    sys.stdout.write(" " * indent + border_c + "┃" + RESET)
    sys.stdout.write(" " * left_pad)

    # Typewriter effect for the quote
    for i, ch in enumerate(quote):
        type_char(ch, i)

    # Right padding + right border + newline
    sys.stdout.write(" " * right_pad + border_c + "┃" + RESET + "\n")

    # A gentle anxious heartbeat line inside the box
    pulse = "┃" + " " * ((inner - 7) // 2) + fg256(81) + DIM + "~ ~" + fg256(45) + " ♥ " + fg256(81) + "~ ~" + RESET
    pulse += " " * (inner - (len(pulse.encode('utf-8')) - 1))  # rough pad; safe fallback
    sys.stdout.write(" " * indent + shade_c + pulse[:inner+1] + border_c + "┃" + RESET + "\n")

    sys.stdout.write(" " * indent + border_c + bottom + RESET + "\n")

def main():
    print(HIDE_CURSOR, end="")
    try:
        width = safe_columns()
        flicker_bulb(width)
        quote = "I asked the void for meaning; it replied 'typing...' and then went for coffee."
        draw_quote_box(quote, width)

        # Little trailing animation: a shy blinking prompt under the box
        blink_y = fg256(244)
        for i in range(10):
            dot = "." if i % 2 == 0 else " "
            sys.stdout.write(blink_y + center_line(" " + dot + "    ", width) + RESET + "\r")
            sys.stdout.flush()
            time.sleep(0.16)
        # Final settle
        sys.stdout.write(" " * width + "\r")
        sys.stdout.flush()
    finally:
        print(SHOW_CURSOR, end="")
        print(RESET, end="")

if __name__ == "__main__":
    main()