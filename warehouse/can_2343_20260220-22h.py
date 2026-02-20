"""
Campbell's Soup Can #2343
Produced: 2026-02-20 22:47:28
Worker: OpenAI: GPT-5.2 Pro (openai/gpt-5.2-pro)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import sys
import time
import shutil

# ---------- ANSI helpers ----------
CSI = "\033["
RESET = CSI + "0m"

def esc(code: str) -> str:
    return CSI + code

def supports_ansi() -> bool:
    if os.name == "nt":
        # Modern Windows terminals usually support ANSI; best-effort.
        return True
    return sys.stdout.isatty()

ANSI = supports_ansi()

def color(s, code):
    return f"{esc(code)}{s}{RESET}" if ANSI else s

def clear():
    if not sys.stdout.isatty():
        return
    sys.stdout.write(esc("2J") + esc("H"))
    sys.stdout.flush()

def term_width(default=80):
    try:
        return shutil.get_terminal_size((default, 24)).columns
    except Exception:
        return default

def center_line(s, width):
    if len(s) >= width:
        return s
    pad = (width - len(s)) // 2
    return (" " * pad) + s

def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()

# ---------- Art / Layout ----------
QUOTE = "“I tried to find the meaning of life, but it kept asking for my ID and a co-pay.”"

def make_box_lines(text, width):
    inner = min(max(38, len(text) + 6), max(38, width - 6))
    inner = max(inner, len(text) + 4)
    top = "╭" + "─" * (inner - 2) + "╮"
    bot = "╰" + "─" * (inner - 2) + "╯"

    # Simple wrap (though quote is single line)
    line = "│ " + text.ljust(inner - 4) + " │"
    return [top, line, bot], inner

def spiral_frames(width):
    # Pure-symbol frames (no extra words).
    # Use a small "existential thought bubble" drifting.
    frames = []
    glyphs = ["·", "•", "○", "◌", "◍", "◎", "◉", "●"]
    for i in range(16):
        g = glyphs[i % len(glyphs)]
        x = int((width - 20) * (i / 15)) if width > 30 else 0
        line1 = " " * x + f"      {g}   {g}      "
        line2 = " " * x + f"   {g}    {g}    {g}   "
        line3 = " " * x + f"      {g}   {g}      "
        frames.append([line1, line2, line3])
    return frames

def type_in_box(box_lines, inner_width, width, delay=0.018):
    # box_lines has top, content placeholder, bottom. We'll type inside.
    top, content, bot = box_lines
    # Find content boundaries for typing
    # content: "│ " + padded + " │"
    prefix = "│ "
    suffix = " │"
    available = inner_width - len(prefix) - len(suffix)

    typed = ""
    target = QUOTE
    padded_target = target.ljust(available)

    # Print top once, then rewrite content line progressively.
    write(center_line(top, width) + "\n")

    for i in range(len(padded_target) + 1):
        typed = padded_target[:i]
        rest = " " * (available - len(typed))
        line = prefix + typed + rest + suffix

        # Color accents: frame + quote (subtle gradient-ish by segments)
        if ANSI:
            frame_c = "38;5;45"   # cyan-ish
            quote_c = "38;5;228"  # warm yellow
            bar = lambda s: f"{esc(frame_c+'m')}{s}{RESET}"
            q = lambda s: f"{esc(quote_c+'m')}{s}{RESET}"
            colored_line = bar("│ ") + q(typed) + rest + bar(" │")
            write(center_line(colored_line, width) + "\r\n" if i == 0 else esc("1A") + "\r" + center_line(colored_line, width) + "\n")
        else:
            write(center_line(line, width) + "\r\n" if i == 0 else esc("1A") + "\r" + center_line(line, width) + "\n")

        if i < len(padded_target):
            time.sleep(delay)

    write(center_line(bot, width) + "\n")

def main():
    no_anim = os.environ.get("NO_ANIM", "").strip().lower() in {"1", "true", "yes", "on"} or (not sys.stdout.isatty())
    width = term_width()

    box_lines, inner_width = make_box_lines(QUOTE, width)
    # Colorize box top/bottom
    if ANSI:
        frame_c = "38;5;45"
        box_lines = [
            color(box_lines[0], frame_c),
            box_lines[1],  # content line is handled by typewriter function
            color(box_lines[2], frame_c),
        ]

    if not no_anim:
        clear()
        frames = spiral_frames(width)
        for k in range(10):
            clear()
            f = frames[(k * 2) % len(frames)]
            # Add a tiny "stick figure" pondering (no words)
            stick = [
                r"        .-.",
                r"       (o o)",
                r"       | O |",
                r"       |   |",
                r"       '~~~'",
            ]
            # Colorize subtlely
            if ANSI:
                f_col = [color(line, "38;5;33") for line in f]
                stick_col = [color(line, "38;5;240") for line in stick]
            else:
                f_col, stick_col = f, stick

            for line in f_col:
                write(center_line(line, width) + "\n")
            write("\n")
            for line in stick_col:
                write(center_line(line, width) + "\n")

            time.sleep(0.06)

        clear()

    # Print final with typewriter effect (quote appears once)
    if no_anim:
        # Static, still colorful.
        top, content, bot = box_lines
        if ANSI:
            frame_c = "38;5;45"
            quote_c = "38;5;228"
            top = color("╭" + "─" * (inner_width - 2) + "╮", frame_c)
            bot = color("╰" + "─" * (inner_width - 2) + "╯", frame_c)
            inner = inner_width - 4
            line = "│ " + color(QUOTE.ljust(inner), quote_c) + " │"
            line = color("│ ", frame_c) + color(QUOTE.ljust(inner), quote_c) + color(" │", frame_c)
            write(center_line(top, width) + "\n")
            write(center_line(line, width) + "\n")
            write(center_line(bot, width) + "\n")
        else:
            inner = inner_width - 4
            write(center_line("╭" + "─" * (inner_width - 2) + "╮", width) + "\n")
            write(center_line("│ " + QUOTE.ljust(inner) + " │", width) + "\n")
            write(center_line("╰" + "─" * (inner_width - 2) + "╯", width) + "\n")
    else:
        type_in_box(box_lines, inner_width, width)

if __name__ == "__main__":
    main()