"""
Campbell's Soup Can #114
Produced: 2025-11-07 10:36:34
Worker: Polaris Alpha (openrouter/polaris-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import shutil
import random

# Simple ANSI helpers
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
BLINK = "\033[5m"

FG = {
    "red": "\033[38;5;196m",
    "yellow": "\033[38;5;226m",
    "blue": "\033[38;5;27m",
    "cyan": "\033[38;5;51m",
    "magenta": "\033[38;5;201m",
    "white": "\033[38;5;15m",
    "gray": "\033[38;5;246m",
    "green": "\033[38;5;82m",
    "orange": "\033[38;5;214m",
}

BG = {
    "dark": "\033[48;5;235m",
    "mid": "\033[48;5;238m",
    "bright": "\033[48;5;240m",
    "purple": "\033[48;5;53m",
}

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def slow_print(text, delay=0.03, color="white", style=""):
    for ch in text:
        sys.stdout.write(FG[color] + style + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def center(text, width):
    if len(text) >= width:
        return text
    pad = (width - len(text)) // 2
    return " " * pad + text

def blinking_ellipsis(times=3, delay=0.3):
    for _ in range(times):
        for dots in ["", ".", "..", "..."]:
            sys.stdout.write("\r" + FG["gray"] + ITALIC + "contemplating" + dots + RESET + "   ")
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()

def build_frame(lines, padding=2):
    cols = shutil.get_terminal_size((80, 24)).columns
    max_len = max(len(line) for line in lines) + padding * 2
    width = min(cols - 4, max_len + 4)
    inner_width = width - 4
    top = "╭" + "─" * (width - 2) + "╮"
    bottom = "╰" + "─" * (width - 2) + "╯"
    framed = [top]
    for line in lines:
        line = line[:inner_width]
        pad_total = inner_width - len(line)
        left = pad_total // 2
        right = pad_total - left
        framed.append("│ " + " " * left + line + " " * right + " │")
    framed.append(bottom)
    return framed

def gradient_text(line, colors):
    out = ""
    n = len(line)
    if n == 0:
        return ""
    for i, ch in enumerate(line):
        idx = int(i / max(1, n - 1) * (len(colors) - 1))
        out += colors[idx] + ch
    return out + RESET

def animated_header():
    cols = shutil.get_terminal_size((80, 24)).columns
    title = "NEUROTIC NIGHT THOUGHT"
    title = title.center(len(title) + 2)
    colors = [FG["magenta"], FG["purple"] if "purple" in FG else FG["blue"], FG["cyan"], FG["yellow"], FG["orange"]]
    for i in range(1, len(title) + 1):
        sys.stdout.write("\r")
        piece = title[:i]
        sys.stdout.write(center(gradient_text(piece, colors), cols))
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write("\n\n")
    sys.stdout.flush()

def animated_brain():
    cols = shutil.get_terminal_size((80, 24)).columns
    brain_frames = [
        [
            "          _---_          ",
            "       .-'     `-.       ",
            "      /  .-\"\"-.  \\      ",
            "     /  /  _  _\\  \\     ",
            "    ;   | (_)(_)|   ;    ",
            "    |   |   ..  |   |    ",
            "    ;   |  (__) |   ;    ",
            "     \\  \\      /  /     ",
            "      `-._`--'_.-'       ",
            "           `\"`           ",
        ],
        [
            "          _---_          ",
            "       .-'     `-.       ",
            "      /  .-\"\"-.  \\      ",
            "     /  / (o)(o)\\  \\    ",
            "    ;   |   --  |   ;    ",
            "    |   |  ---- |   |    ",
            "    ;   |  (__) |   ;    ",
            "     \\  \\      /  /     ",
            "      `-._`--'_.-'       ",
            "           `\"`           ",
        ],
    ]
    for i in range(8):
        frame = brain_frames[i % 2]
        sys.stdout.write("\033[s")  # save
        for j, line in enumerate(frame):
            y_offset = j
            sys.stdout.write(f"\033[{4 + y_offset};0H")
            color = FG["magenta"] if i % 2 == 0 else FG["cyan"]
            sys.stdout.write(center(color + line + RESET, cols))
        sys.stdout.flush()
        time.sleep(0.12)
        sys.stdout.write("\033[u")  # restore
    sys.stdout.write("\n" * (len(brain_frames[0]) + 2))
    sys.stdout.flush()

def shake_print(lines, shakes=4, delay=0.04):
    cols = shutil.get_terminal_size((80, 24)).columns
    for s in range(shakes):
        offset = random.randint(-2, 2)
        sys.stdout.write("\033[s")
        for i, line in enumerate(lines):
            padded = center(line, cols)
            if offset > 0:
                padded = " " * offset + padded
            else:
                padded = padded[max(0, -offset):]
            sys.stdout.write(f"\033[{i+1+15};0H" + padded + RESET)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\033[u")
    # final stable print
    for i, line in enumerate(lines):
        sys.stdout.write(center(line, cols) + "\n")
    sys.stdout.flush()

def main():
    clear()
    animated_header()
    animated_brain()

    # Single Woody-Allen-esque philosophical quote
    quote = (
        "I finally made peace with the meaninglessness of the universe—"
        "but now I'm anxious it's going to change its mind just to spite me."
    )

    blinking_ellipsis(times=2, delay=0.25)

    wrapped = []
    width = min(68, shutil.get_terminal_size((80, 24)).columns - 8)
    words = quote.split()
    line = ""
    for w in words:
        if len(line) + len(w) + 1 > width:
            wrapped.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        wrapped.append(line)

    framed = build_frame(wrapped, padding=3)

    colored_framed = []
    border_color = FG["yellow"]
    text_color = FG["white"]
    for i, line_txt in enumerate(framed):
        if i == 0 or i == len(framed) - 1:
            colored_framed.append(border_color + line_txt + RESET)
        else:
            # keep borders colored, text bright
            left = line_txt[:2]
            right = line_txt[-2:]
            middle = line_txt[2:-2]
            colored_framed.append(
                border_color + left + RESET
                + text_color + middle + RESET
                + border_color + right + RESET
            )

    shake_print(colored_framed, shakes=6, delay=0.03)

    sys.stdout.write("\n")
    sys.stdout.flush()
    time.sleep(0.4)

    # Tiny fading signature at the bottom
    cols = shutil.get_terminal_size((80, 24)).columns
    sig = ITALIC + DIM + FG["gray"] + "-- a minor panic in a major cosmos" + RESET
    sys.stdout.write(center(sig, cols) + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()