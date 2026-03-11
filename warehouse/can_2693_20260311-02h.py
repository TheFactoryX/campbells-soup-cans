"""
Campbell's Soup Can #2693
Produced: 2026-03-11 02:49:18
Worker: OpenAI: GPT-5.2 (openai/gpt-5.2)
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
import textwrap

CSI = "\x1b["

def esc(*parts: str) -> str:
    return CSI + ";".join(parts) + "m"

RESET = esc("0")
BOLD = esc("1")
DIM = esc("2")

FG = {
    "black": esc("30"),
    "red": esc("31"),
    "green": esc("32"),
    "yellow": esc("33"),
    "blue": esc("34"),
    "magenta": esc("35"),
    "cyan": esc("36"),
    "white": esc("37"),
    "gray": esc("90"),
    "bright_white": esc("97"),
}

def clear():
    sys.stdout.write(CSI + "2J" + CSI + "H")
    sys.stdout.flush()

def term_width(default=80):
    try:
        w = shutil.get_terminal_size((default, 24)).columns
    except Exception:
        w = default
    return max(40, min(120, w))

def typewriter(s: str, delay: float = 0.008):
    if not sys.stdout.isatty():
        sys.stdout.write(s)
        sys.stdout.flush()
        return
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        # Keep it snappy: longer pauses only on punctuation.
        if ch in ".!?":
            time.sleep(delay * 8)
        elif ch in ",;:":
            time.sleep(delay * 4)
        else:
            time.sleep(delay)

def thinking_line(width: int, seconds: float = 1.6):
    if not sys.stdout.isatty():
        return
    msg = "consulting the void"
    start = time.time()
    i = 0
    while time.time() - start < seconds:
        dots = "." * (i % 4)
        pad = " " * max(0, width - len(msg) - len(dots) - 6)
        line = (
            FG["gray"] + DIM + "  " + msg + dots + pad +
            FG["magenta"] + BOLD + " [?!]" +
            RESET
        )
        sys.stdout.write("\r" + line[:width])
        sys.stdout.flush()
        time.sleep(0.12)
        i += 1
    sys.stdout.write("\r" + " " * width + "\r")
    sys.stdout.flush()

def bubble_lines(text: str, width: int):
    inner = max(24, width - 14)
    wrapped = textwrap.wrap(text, width=inner)
    content_width = max(len(line) for line in wrapped) if wrapped else 0

    top = "╭" + "─" * (content_width + 2) + "╮"
    mid = ["│ " + line.ljust(content_width) + " │" for line in wrapped]
    bot = "╰" + "─" * (content_width + 2) + "╯"
    return [top] + mid + [bot]

def main():
    w = term_width()

    quote = (
        "I called the universe looking for meaning, and it put me on hold—"
        "apparently my existence is important to them, but only after the next eternity."
    )

    art = [
        r"           .-''''-.",
        r"         .'  _  _  '.",
        r"        /   (o)(o)   \   ",
        r"       |      __      |  ",
        r"       |    .'__'.    |  ",
        r"        \   \____/   /   ",
        r"         '._      _.'    ",
        r"            '-..-'       ",
        r"          __/  \__       ",
        r"         /  \__/  \      ",
        r"        /___/  \___\     ",
    ]

    clear()

    # Centered, neon-ish header art (no extra "quotes" text—just visuals).
    left_pad = max(0, (w - max(len(line) for line in art)) // 2)
    for i, line in enumerate(art):
        color = FG["cyan"] if i % 2 == 0 else FG["magenta"]
        sys.stdout.write(" " * left_pad + color + BOLD + line + RESET + "\n")

    sys.stdout.write("\n")
    sys.stdout.flush()

    thinking_line(w, seconds=1.7)

    bubble = bubble_lines(quote, w)
    bubble_pad = max(0, (w - len(bubble[0])) // 2)

    # Little "tail" to the bubble, aligned toward the art.
    tail = [
        " " * (bubble_pad + 4) + FG["yellow"] + BOLD + "\\" + RESET,
        " " * (bubble_pad + 3) + FG["yellow"] + BOLD + "\\" + RESET,
        " " * (bubble_pad + 2) + FG["yellow"] + BOLD + "\\" + RESET,
    ]

    # Print bubble with a subtle color frame and typewriter effect.
    frame = FG["yellow"] + BOLD
    textc = FG["bright_white"]

    out = []
    for idx, line in enumerate(bubble):
        if idx == 0 or idx == len(bubble) - 1:
            out.append(" " * bubble_pad + frame + line + RESET)
        else:
            # Color the borders, keep text bright.
            if line.startswith("│ ") and line.endswith(" │"):
                inner = line[2:-2]
                out.append(
                    " " * bubble_pad + frame + "│ " + RESET +
                    textc + inner + RESET +
                    frame + " │" + RESET
                )
            else:
                out.append(" " * bubble_pad + textc + line + RESET)

    # Print tail + bubble.
    for t in tail:
        typewriter(t + "\n", delay=0.004)
    typewriter("\n", delay=0.001)
    for line in out:
        typewriter(line + "\n", delay=0.004)

if __name__ == "__main__":
    main()