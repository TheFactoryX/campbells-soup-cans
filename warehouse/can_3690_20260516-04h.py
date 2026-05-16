"""
Campbell's Soup Can #3690
Produced: 2026-05-16 04:02:44
Worker: OpenAI: GPT-5 (openai/gpt-5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Note: This program evokes a neurotic, self-deprecating, existential comedic voice rather than any specific living writer's exact phrasing or wording.

import sys
import time
import shutil
import textwrap
import os

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
HIDE = "\033[?25l"
SHOW = "\033[?25h"
CLEAR = "\033[2J\033[H"

BRIGHT_WHITE = "\033[97m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_BLUE = "\033[94m"
GRAY = "\033[90m"

BORDER_CYCLE = [BRIGHT_CYAN, BRIGHT_MAGENTA, BRIGHT_BLUE]

QUOTE = "I tried to schedule meaning, but the universe marked it 'tentative' -- so I RSVP'd 'maybe' and spent the evening catastrophizing eternity."

def term_size():
    cols, rows = shutil.get_terminal_size(fallback=(80, 24))
    return max(60, cols), max(20, rows)

def wrap_quote(text, width):
    # Avoid breaking words awkwardly
    return textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)

def draw_bubble(content_lines, cont_w, left_pad, border_color, text_color=BRIGHT_WHITE):
    out = []
    top = "╭" + "─"*cont_w + "╮"
    bottom = "╰" + "─"*cont_w + "╯"
    out.append(" " * left_pad + border_color + top + RESET)
    for line in content_lines:
        pad = cont_w - len(line)
        out.append(" " * left_pad + border_color + "│" + RESET + text_color + line + " " * pad + RESET + border_color + "│" + RESET)
    out.append(" " * left_pad + border_color + bottom + RESET)
    return out

def head_art():
    # A charmingly worried little face on a minimalist body.
    return [
        "     .-''''-.",
        "    /  .--.  \\",
        "   |  (o  o)  |",
        "   |    ..    |",
        "   |  \\____/  |",
        "    \\        /",
        "     '-.__.-' ",
        "        ||    ",
        "       _||_   ",
        "      /____\\  ",
    ]

def draw_head(left_pad, color=BRIGHT_YELLOW):
    h = head_art()
    return [(" " * left_pad) + color + line + RESET for line in h]

def lerp(a, b, t):
    return a + (b - a) * t

def build_frame(partial_text, cols, rows, frame_i):
    # Layout parameters
    cont_w = min(max(46, int(cols * 0.6)), cols - 6)  # inner bubble width
    bubble_left = (cols - (cont_w + 2)) // 2
    border_color = BORDER_CYCLE[frame_i % len(BORDER_CYCLE)]
    text_color = BRIGHT_WHITE

    # Wrap the typed portion
    lines = wrap_quote(partial_text, cont_w)
    if not lines:
        lines = [""]

    # Make bubble
    bubble_block = draw_bubble(lines, cont_w, bubble_left, border_color, text_color)

    # Head placement strategy:
    head = head_art()
    head_w = max(len(x) for x in head)
    # Try to place the head a bit left of the bubble; if not enough space, put it on the right
    prefer_left_x = bubble_left - head_w - 4
    if prefer_left_x >= 0:
        head_left = prefer_left_x
        tail_from = (bubble_left + 4, len(bubble_block) + 1)  # start under bubble near left corner
        tail_to = (head_left + head_w - 4, len(bubble_block) + 2)  # toward head top-right
    else:
        head_left = bubble_left + cont_w + 6
        if head_left + head_w > cols:
            head_left = max(0, cols - head_w)
        tail_from = (bubble_left + cont_w - 6, len(bubble_block) + 1)
        tail_to = (min(cols-2, head_left + 3), len(bubble_block) + 2)

    # Tail rendering (bubbly dotted line)
    tail_lines = []
    tail_steps = 4
    bubble_char_choices = ["·", "•", "o", "•"]
    dot = bubble_char_choices[frame_i % len(bubble_char_choices)]
    for i in range(tail_steps):
        t = (i + 1) / (tail_steps + 1)
        x = int(round(lerp(tail_from[0], tail_to[0], t)))
        # A tiny vertical jitter for nervousness
        v_shift = (i + frame_i) % 2
        line = " " * max(0, x) + border_color + dot + RESET
        tail_lines.append((v_shift, line))

    # Compose full frame
    frame = []
    # Top margin
    top_margin = max(0, (rows - (len(bubble_block) + tail_steps + len(head) + 3)) // 3)
    frame.extend([""] * top_margin)

    # A dim little title that flickers
    title = "Existential Popcorn"
    neon = BORDER_CYCLE[(frame_i + 1) % len(BORDER_CYCLE)] + BOLD + title + RESET
    title_pad = max(0, (cols - len(title)) // 2)
    glow = GRAY + ("." * ((frame_i % 3) + 1)) + RESET
    frame.append(" " * title_pad + neon + " " + glow)

    # Bubble
    frame.extend(bubble_block)

    # Tail
    for i, (v, line) in enumerate(tail_lines):
        frame.append((" " * 0) + (" " * 0) + " " * 0 + (" " * 0) + (" " * 0) + (" " * 0))  # ensure a line exists
        frame.append(line if v == 1 else " " + line)

    # Head
    head_block = draw_head(head_left, BRIGHT_YELLOW)
    frame.extend(head_block)

    # Add a dainty shadow under the head for depth
    shadow_w = head_w - 2
    shadow_left = max(0, head_left + 1)
    shadow = " " * shadow_left + GRAY + DIM + "_" * max(1, shadow_w) + RESET
    frame.append(shadow)

    # Ensure frame doesn't exceed terminal height (best effort)
    if len(frame) > rows:
        frame = frame[:rows]
    # Pad to full height for clean clearing
    if len(frame) < rows:
        frame.extend([""] * (rows - len(frame)))
    return frame

def main():
    # Try enabling ANSI on Windows terminals
    if os.name == "nt":
        os.system("")

    cols, rows = term_size()
    sys.stdout.write(HIDE)
    sys.stdout.flush()

    try:
        # Intro shimmer
        for i in range(8):
            sys.stdout.write(CLEAR)
            frame = build_frame("", cols, rows, i)
            sys.stdout.write("\n".join(frame) + RESET)
            sys.stdout.flush()
            time.sleep(0.05)

        # Typewriter animation
        delay = 0.02
        typed = ""
        for i, ch in enumerate(QUOTE):
            typed += ch
            sys.stdout.write(CLEAR)
            frame = build_frame(typed, cols, rows, i + 8)
            sys.stdout.write("\n".join(frame) + RESET)
            sys.stdout.flush()
            time.sleep(delay)

        # A brief satisfied pause (as satisfied as anxiety allows)
        for j in range(18):
            sys.stdout.write(CLEAR)
            frame = build_frame(typed, cols, rows, j + len(QUOTE) + 8)
            sys.stdout.write("\n".join(frame) + RESET)
            sys.stdout.flush()
            time.sleep(0.04)

    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(RESET + SHOW + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()