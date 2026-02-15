"""
Campbell's Soup Can #2247
Produced: 2026-02-15 19:38:36
Worker: OpenAI: GPT-5 (openai/gpt-5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# NOTE ON STYLE: You asked for a quote in a specific living writer's style.
# I can't write in anyone's exact voice, but here's an original, neurotic,
# self-deprecating, existential one-liner with a similar high-level vibe.

import sys
import time
import shutil
import random
import textwrap

# ANSI escape helpers
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITA = "\033[3m"

FG = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}

BG = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
    "bright_black": "\033[100m",
    "bright_red": "\033[101m",
    "bright_green": "\033[102m",
    "bright_yellow": "\033[103m",
    "bright_blue": "\033[104m",
    "bright_magenta": "\033[105m",
    "bright_cyan": "\033[106m",
    "bright_white": "\033[107m",
}

CLEAR = "\033[2J"
HOME = "\033[H"
HIDE = "\033[?25l"
SHOW = "\033[?25h"

def term_size():
    try:
        sz = shutil.get_terminal_size(fallback=(80, 24))
        return sz.columns, sz.lines
    except Exception:
        return 80, 24

def center_text(text, width):
    if len(text) >= width:
        return text[:width]
    pad = (width - len(text)) // 2
    return " " * pad + text + " " * (width - len(text) - pad)

def wrap_text(text, max_width):
    return textwrap.wrap(text, width=max_width, break_long_words=False, replace_whitespace=False)

def draw_header_line(w, glow_phase):
    colors = [FG["bright_yellow"], FG["bright_magenta"], FG["bright_cyan"], FG["bright_white"]]
    c = colors[glow_phase % len(colors)]
    title = "Existential Cabaret"
    subtitle = "Please hold while anxiety arranges the furniture"
    line1 = center_text(f"{BOLD}{c}{title}{RESET}", w)
    line2 = center_text(f"{DIM}{FG['bright_black']}{subtitle}{RESET}", w)
    return line1 + "\n" + line2 + "\n"

def make_border(inner_w, phase):
    # Flickering neon border
    neon = [FG["bright_yellow"], FG["bright_magenta"], FG["bright_cyan"], FG["bright_white"]]
    c1 = neon[phase % len(neon)]
    c2 = neon[(phase + 2) % len(neon)]
    pat = ("▓░" if phase % 2 == 0 else "▒▓")
    left = pat[0]
    right = pat[1]
    top = f"{c1}" + "╔" + ("═" * inner_w) + "╗" + f"{RESET}"
    side_l = f"{c2}║{RESET}"
    side_r = f"{c2}║{RESET}"
    bottom = f"{c1}" + "╚" + ("═" * inner_w) + "╝" + f"{RESET}"
    return top, side_l, side_r, bottom

def draw_face_line(w, phase):
    # Little anxious face doodle above the box
    eyes = "o o" if phase % 2 == 0 else "• •"
    mouth = "_" if phase % 3 else "‾"
    face = f" ( {eyes} ) "
    chin = f"  \\_{mouth}_/  "
    face_line = center_text(FG["bright_black"] + face + RESET, w)
    chin_line = center_text(FG["bright_black"] + chin + RESET, w)
    return face_line + "\n" + chin_line + "\n"

def build_box_lines(w, h, text_lines, inner_w, phase, reveal_chars):
    # Box with typewriter reveal across multiple lines
    max_lines = len(text_lines)
    lens = [len(s) for s in text_lines]
    cum = [0]
    for L in lens:
        cum.append(cum[-1] + L)
    total_chars = cum[-1]
    # Compute how many chars to reveal
    k = min(reveal_chars, total_chars)

    top, side_l, side_r, bottom = make_border(inner_w, phase)

    box = []
    box.append(top)
    # Prepare lines with padding and partial reveal
    for i, line in enumerate(text_lines):
        begin = cum[i]
        end = cum[i+1]
        show = min(max(k - begin, 0), lens[i])
        visible = line[:show]
        hidden_spaces = " " * (lens[i] - show)
        # blinking caret if next to reveal is on this line
        caret = ""
        if show < lens[i] and k >= begin and k < end and phase % 2 == 0:
            caret = FG["bright_black"] + "▌" + RESET
        pad_lr = inner_w - lens[i]
        left_pad = pad_lr // 2
        right_pad = pad_lr - left_pad
        row = side_l + " " * left_pad + visible + hidden_spaces + caret + " " * max(0, right_pad - len(caret)) + side_r
        box.append(row)
    box.append(bottom)
    return box

def draw_star_line(width, density=0.04, phase=0):
    # Sparse star twinkle
    line = []
    for x in range(width):
        if random.random() < density:
            c = random.choice([FG["bright_yellow"], FG["bright_magenta"], FG["bright_cyan"], FG["bright_white"], FG["bright_blue"]])
            glyph = random.choice(["·","•","*","✦","✧"])
            if phase % 3 == 0: glyph = "."
            if phase % 4 == 0: c = FG["bright_black"]
            line.append(c + glyph + RESET)
        else:
            line.append(" ")
    return "".join(line)

def main():
    try:
        sys.stdout.write(HIDE)
        sys.stdout.flush()

        cols, rows = term_size()
        cols = max(cols, 60)
        rows = max(rows, 20)

        # The quote (one original neurotic, existential line)
        quote = "I'm not afraid of the void; I just worry it keeps score. I'm late, underdressed, and somehow the entertainment."

        # Compute inner width and wrap
        max_inner = min(cols - 8, 72)
        wrapped = wrap_text(quote, max_inner - 4)  # leave margins inside box
        # Ensure at least 2 lines for aesthetic spacing
        if len(wrapped) == 1:
            wrapped.append("")

        # Pre-calc dims
        inner_w = max(len(max(wrapped, key=len)), 20) + 2  # a bit of breathing room
        total_chars = sum(len(s) for s in wrapped)

        # Animation phases
        pre_frames = 18  # twinkling intro
        type_frames = total_chars + 10  # typewriter including linger
        post_frames = 10  # gentle outro pulse

        # Build vertical layout: header, face, star pad, box, star pad
        header_h = 3
        face_h = 2
        box_h = len(wrapped) + 2
        star_pad_top = max(1, (rows - (header_h + face_h + box_h + 2)) // 2)
        star_pad_bot = rows - (header_h + face_h + box_h + star_pad_top)

        # Intro twinkle
        for ph in range(pre_frames):
            frame = [CLEAR, HOME]
            # Stars on top
            frame.append("\n".join(draw_star_line(cols, density=0.035 + 0.01*random.random(), phase=ph) for _ in range(star_pad_top)))
            # Header
            frame.append(draw_header_line(cols, ph))
            # Face
            frame.append(draw_face_line(cols, ph))
            # Some star padding between face and box
            pad_lines = max(0, 1)
            frame.append("\n".join(draw_star_line(cols, density=0.025, phase=ph) for _ in range(pad_lines)))
            # Placeholder box silhouette
            top, side_l, side_r, bottom = make_border(inner_w, ph)
            left_margin = (cols - (inner_w + 2)) // 2
            box = [(" " * left_margin) + top]
            for _ in range(len(wrapped)):
                box.append((" " * left_margin) + side_l + " " * inner_w + side_r)
            box.append((" " * left_margin) + bottom)
            frame.append("\n".join(box))
            # Bottom stars
            frame.append("\n".join(draw_star_line(cols, density=0.02, phase=ph) for _ in range(max(0, star_pad_bot - pad_lines))))
            sys.stdout.write("".join(frame))
            sys.stdout.flush()
            time.sleep(0.05)

        # Typewriter reveal
        revealed = 0
        for ph in range(type_frames):
            revealed = min(ph, total_chars)
            frame = [CLEAR, HOME]
            # Sparse quiet sky
            frame.append("\n".join(draw_star_line(cols, density=0.02, phase=ph) for _ in range(star_pad_top)))
            frame.append(draw_header_line(cols, ph))
            frame.append(draw_face_line(cols, ph))
            frame.append("\n".join(draw_star_line(cols, density=0.015, phase=ph) for _ in range(1)))

            # Box with text
            left_margin = (cols - (inner_w + 2)) // 2
            box_lines = build_box_lines(cols, rows, wrapped, inner_w, ph, revealed)
            for i, line in enumerate(box_lines):
                box_lines[i] = (" " * left_margin) + line
            frame.append("\n".join(box_lines))

            frame.append("\n".join(draw_star_line(cols, density=0.02, phase=ph) for _ in range(max(0, star_pad_bot - 1))))

            sys.stdout.write("".join(frame))
            sys.stdout.flush()
            time.sleep(0.035 if revealed < total_chars else 0.2)

        # Gentle outro pulse with a small underline flourish
        underline = "―" * (min(inner_w, max(len(max(wrapped, key=len)), 10)))
        for ph in range(post_frames):
            frame = [CLEAR, HOME]
            frame.append("\n".join(draw_star_line(cols, density=0.02, phase=ph) for _ in range(star_pad_top)))
            frame.append(draw_header_line(cols, ph))
            frame.append(draw_face_line(cols, ph))
            frame.append("\n".join(draw_star_line(cols, density=0.012, phase=ph) for _ in range(1)))

            left_margin = (cols - (inner_w + 2)) // 2
            box_lines = build_box_lines(cols, rows, wrapped, inner_w, ph, total_chars)
            # Add underline line inside box, just above bottom border
            # Replace the second last line (the last content line) with underline glow (alternate pulse)
            if len(box_lines) >= 3:
                glow = [FG["bright_yellow"], FG["bright_magenta"], FG["bright_cyan"], FG["bright_white"]][ph % 4]
                # side_l is 1 char wide color+║+reset, but we don't modify sides; we modify content portion
                # Find index of last content row
                content_idx = len(box_lines) - 2
                # Build a new content line centered
                pad_lr = inner_w - len(underline)
                left_pad = max(0, pad_lr // 2)
                right_pad = max(0, pad_lr - left_pad)
                # Extract side walls colors from existing line (quick hack: detect '║')
                # We'll just reuse side chars from the existing row
                row = box_lines[content_idx]
                # Find positions of side walls
                if "║" in row:
                    left_wall = row.split("║", 1)[0] + "║"
                    right_wall = "║" + row.rsplit("║", 1)[-1] if row.count("║") >= 2 else "║"
                    new_mid = " " * left_pad + glow + underline + RESET + " " * right_pad
                    # Rebuild with approximate side structure (keeping colors may misalign; it's okay visually)
                    box_lines[content_idx] = left_wall + new_mid + right_wall
            for i, line in enumerate(box_lines):
                box_lines[i] = (" " * left_margin) + line
            frame.append("\n".join(box_lines))

            frame.append("\n".join(draw_star_line(cols, density=0.02, phase=ph) for _ in range(max(0, star_pad_bot - 1))))
            sys.stdout.write("".join(frame))
            sys.stdout.flush()
            time.sleep(0.06)
    finally:
        sys.stdout.write(SHOW + RESET + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()