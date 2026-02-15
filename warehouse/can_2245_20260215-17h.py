"""
Campbell's Soup Can #2245
Produced: 2026-02-15 17:43:11
Worker: OpenAI: GPT-5.2 Pro (openai/gpt-5.2-pro)
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
import random
import shutil

ESC = "\x1b["

def c(code: str) -> str:
    return f"{ESC}{code}m"

RESET = c("0")
BOLD = c("1")
DIM = c("2")

FG = {
    "white": c("37"),
    "bright_white": c("97"),
    "cyan": c("36"),
    "bright_cyan": c("96"),
    "magenta": c("35"),
    "bright_magenta": c("95"),
    "yellow": c("33"),
    "bright_yellow": c("93"),
    "blue": c("34"),
    "bright_blue": c("94"),
    "green": c("32"),
    "bright_green": c("92"),
    "red": c("31"),
    "bright_red": c("91"),
}

def clear():
    sys.stdout.write(ESC + "2J" + ESC + "H")

def hide_cursor():
    sys.stdout.write(ESC + "?25l")

def show_cursor():
    sys.stdout.write(ESC + "?25h")

def flush():
    sys.stdout.flush()

def term_size():
    sz = shutil.get_terminal_size((80, 24))
    return sz.columns, sz.lines

def center_line(s, width):
    if len(s) >= width:
        return s[:width]
    pad = (width - len(s)) // 2
    return " " * pad + s

def starfield_animation(duration=1.3, fps=18):
    w, h = term_size()
    h = max(10, h)
    w = max(40, w)

    # A little "existential cosmos" starfield.
    stars = []
    for _ in range(int(w * h * 0.03)):
        stars.append([random.randrange(w), random.randrange(h), random.choice([1, 1, 1, 2])])

    t_end = time.time() + duration
    frame = 0
    while time.time() < t_end:
        clear()
        # Subtle gradient sky using sparse colored dots.
        canvas = [[" "]*w for _ in range(h)]
        for s in stars:
            x, y, sp = s
            if 0 <= x < w and 0 <= y < h:
                canvas[y][x] = random.choice(["·", ".", "✦" if random.random() < 0.05 else "•"])
            s[1] += sp
            if s[1] >= h:
                s[1] = 0
                s[0] = random.randrange(w)
                s[2] = random.choice([1, 1, 1, 2])

        # Add a drifting "question mark comet"
        qx = (frame * 2) % (w + 10) - 5
        qy = h // 3
        if 0 <= qx < w:
            canvas[qy][qx] = "?"
        if 0 <= qx-1 < w:
            canvas[qy][qx-1] = "—"
        if 0 <= qx-2 < w:
            canvas[qy][qx-2] = "—"

        # Print with color
        for y in range(h):
            row = "".join(canvas[y])
            # Color varies slightly by row for visual fun
            if y < h * 0.33:
                col = FG["bright_blue"]
            elif y < h * 0.66:
                col = FG["bright_magenta"]
            else:
                col = FG["bright_cyan"]
            sys.stdout.write(DIM + col + row + RESET + "\n")

        sys.stdout.write(DIM + FG["bright_white"] + center_line("searching for meaning... please hold", w) + RESET)
        flush()
        time.sleep(1 / fps)
        frame += 1

def wrap(text, width):
    words = text.split()
    lines = []
    cur = []
    n = 0
    for w in words:
        add = len(w) + (1 if cur else 0)
        if n + add > width:
            lines.append(" ".join(cur))
            cur = [w]
            n = len(w)
        else:
            cur.append(w)
            n += add
    if cur:
        lines.append(" ".join(cur))
    return lines

def typewriter(s, delay=0.015):
    for ch in s:
        sys.stdout.write(ch)
        flush()
        time.sleep(delay)

def main():
    quote = (
        "I stared into the void for answers, and the void stared back—"
        "then asked if I could keep it down, because it was trying to nap."
    )

    w, h = term_size()
    w = max(60, w)
    h = max(18, h)

    hide_cursor()
    try:
        starfield_animation()

        clear()

        # Cute little neurotic thinker ASCII
        thinker = [
            r"          .-''''-.      ",
            r"         /  .--.  \     ",
            r"        |  /    \  |    ",
            r"        | |  ()  | |    ",
            r"        |  \    /  |    ",
            r"         \  '--'  /     ",
            r"          '-.__.-'      ",
            r"            /||\        ",
            r"           /_||_\       ",
            r"             ||         ",
            r"            /  \        ",
            r"           /____\       ",
        ]

        bubble_width = min(w - 10, 74)
        inner = bubble_width - 4
        lines = wrap(quote, inner)
        top = "+" + "-" * (bubble_width - 2) + "+"
        bot = "+" + "-" * (bubble_width - 2) + "+"

        # Layout
        left_pad = max(2, (w - bubble_width) // 2)
        art_pad = left_pad + 2

        # Header
        hdr = "NEUROTIC COSMOLOGY, IN ONE SENTENCE"
        sys.stdout.write(BOLD + FG["bright_yellow"] + center_line(hdr, w) + RESET + "\n")
        sys.stdout.write(DIM + FG["bright_white"] + center_line("(terminal-safe existential dread)", w) + RESET + "\n\n")

        # Thought bubble
        sys.stdout.write(" " * left_pad + BOLD + FG["bright_cyan"] + top + RESET + "\n")
        for i, ln in enumerate(lines):
            pad = " " * (inner - len(ln))
            # Alternate subtle colors per line
            col = FG["bright_white"] if i % 2 == 0 else FG["bright_magenta"]
            sys.stdout.write(" " * left_pad + BOLD + FG["bright_cyan"] + "| " + RESET)
            sys.stdout.write(BOLD + col)
            # Typewriter only the quote content
            typewriter(ln, delay=0.012)
            sys.stdout.write(RESET + " " * 0 + pad)
            sys.stdout.write(BOLD + FG["bright_cyan"] + " |" + RESET + "\n")
        sys.stdout.write(" " * left_pad + BOLD + FG["bright_cyan"] + bot + RESET + "\n")

        # Bubble tail (thought dots)
        tail = [
            " " * (left_pad + bubble_width // 2) + DIM + FG["bright_cyan"] + "o" + RESET,
            " " * (left_pad + bubble_width // 2 + 2) + DIM + FG["bright_cyan"] + "o" + RESET,
            " " * (left_pad + bubble_width // 2 + 4) + DIM + FG["bright_cyan"] + "o" + RESET,
        ]
        for t in tail:
            sys.stdout.write(t + "\n")

        # Thinker
        for row in thinker:
            sys.stdout.write(" " * art_pad + FG["bright_white"] + row + RESET + "\n")

        # A tiny footer line (no extra quotes)
        sys.stdout.write("\n" + DIM + FG["bright_blue"] + center_line("press Ctrl+C if the universe calls back", w) + RESET + "\n")
        flush()

    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        sys.stdout.write(RESET)
        flush()

if __name__ == "__main__":
    main()