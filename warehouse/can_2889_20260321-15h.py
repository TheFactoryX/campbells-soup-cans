"""
Campbell's Soup Can #2889
Produced: 2026-03-21 15:41:40
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
import shutil

ESC = "\x1b"

def c(code: str) -> str:
    return f"{ESC}[{code}m"

RESET = c("0")
BOLD = c("1")
DIM = c("2")

def fg256(n: int) -> str:
    return f"{ESC}[38;5;{n}m"

def bg256(n: int) -> str:
    return f"{ESC}[48;5;{n}m"

def clear():
    sys.stdout.write(f"{ESC}[2J{ESC}[H")
    sys.stdout.flush()

def write(s: str):
    sys.stdout.write(s)
    sys.stdout.flush()

def sleep(t: float):
    time.sleep(t)

def wrap(text: str, width: int):
    words = text.split()
    lines, cur = [], []
    n = 0
    for w in words:
        if n + (1 if cur else 0) + len(w) <= width:
            if cur:
                cur.append(w)
                n += 1 + len(w)
            else:
                cur.append(w)
                n += len(w)
        else:
            lines.append(" ".join(cur))
            cur = [w]
            n = len(w)
    if cur:
        lines.append(" ".join(cur))
    return lines

def center(s: str, width: int) -> str:
    if len(s) >= width:
        return s
    pad = (width - len(s)) // 2
    return " " * pad + s + " " * (width - len(s) - pad)

def gradient_chars(n: int, start: int = 39, end: int = 213):
    if n <= 1:
        return [start]
    step = (end - start) / (n - 1)
    return [int(start + i * step) for i in range(n)]

def type_line(line: str, delay: float = 0.014, color_seq=None):
    # Print line with a gentle color drift per character (still "one quote"—just dressed up).
    if color_seq is None:
        color_seq = gradient_chars(max(1, len(line)))
    for i, ch in enumerate(line):
        col = color_seq[i % len(color_seq)]
        write(f"{fg256(col)}{ch}{RESET}")
        sleep(delay)

def main():
    quote = (
        "I begged the universe for meaning; it sent me a receipt—"
        "and somehow I'm still the one who has to tip."
    )

    cols = shutil.get_terminal_size((80, 24)).columns
    inner_max = min(64, max(34, cols - 18))
    lines = wrap(quote, inner_max)
    inner_w = max(len(x) for x in lines)
    pad_x = 2

    box_w = inner_w + pad_x * 2
    total_w = box_w + 2  # borders

    # Build a small neurotic philosopher doodle (ASCII-friendly).
    doodle = [
        r"      .-''''-.",
        r"     /  .--.  \ ",
        r"    |  (    )  |",
        r"     \  '--'  /",
        r"      '-.__.-' ",
        r"       /|  |\   ",
        r"      /_|__|_\  ",
    ]

    # Positioning
    left = max(0, (cols - max(total_w, 24)) // 2)
    indent = " " * left

    clear()

    # A subtle "curtain" header line (no extra quotes, just atmosphere).
    header = " " * left + (fg256(90) + DIM + "░" * max(0, min(cols - left, total_w)) + RESET)
    write(header + "\n")
    sleep(0.05)

    # Print doodle above the box
    for row in doodle:
        # Color wobble for the doodle
        color = fg256(33)
        write(indent + color + center(row, max(total_w, len(row))) + RESET + "\n")
    sleep(0.10)

    # Box top
    top = f"┌{'─' * box_w}┐"
    write(indent + fg256(215) + BOLD + top + RESET + "\n")

    # Empty spacer line
    write(indent + fg256(215) + "│" + RESET + " " * box_w + fg256(215) + "│" + RESET + "\n")

    # Quote lines (typing animation)
    for ln in lines:
        ln_pad = ln + " " * (inner_w - len(ln))
        write(indent + fg256(215) + "│" + RESET + " " * pad_x)
        type_line(ln_pad, delay=0.012, color_seq=gradient_chars(len(ln_pad), 81, 207))
        write(" " * pad_x + fg256(215) + "│" + RESET + "\n")

    # Empty spacer line
    write(indent + fg256(215) + "│" + RESET + " " * box_w + fg256(215) + "│" + RESET + "\n")

    # Box bottom
    bottom = f"└{'─' * box_w}┘"
    write(indent + fg256(215) + BOLD + bottom + RESET + "\n")

    # Footer shimmer (still not another quote)
    footer = " " * left + (fg256(90) + DIM + "░" * max(0, min(cols - left, total_w)) + RESET)
    write(footer + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()