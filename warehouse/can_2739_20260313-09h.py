"""
Campbell's Soup Can #2739
Produced: 2026-03-13 09:56:19
Worker: MiniMax: MiniMax M2 (minimax/minimax-m2)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import threading
import os

# Enable ANSI color codes on Windows 10+
def enable_ansi():
    try:
        if os.name == 'nt':
            import ctypes
            kernel32 = ctypes.windll.kernel32
            h = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
            mode = ctypes.c_uint32()
            kernel32.GetConsoleMode(h, ctypes.byref(mode))
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            kernel32.SetConsoleMode(h, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
    except Exception:
        pass

enable_ansi()

# ANSI helpers
RESET = "\x1b[0m"
BOLD = "\x1b[1m"
DIM = "\x1b[2m"
ITALIC = "\x1b[3m"
BLINK = "\x1b[5m"

def color(idx, bold=False):
    code = 30 + (idx % 8)
    return f"\x1b[{code}m" + (BOLD if bold else "")

SPINNER_STOPS = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

def spin(label, stop_event):
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{label} {SPINNER_STOPS[i % len(SPINNER_STOPS)]}")
        sys.stdout.flush()
        time.sleep(0.07)
        i += 1
    sys.stdout.write("\r" + " " * (len(label) + 2) + "\r")
    sys.stdout.flush()

def type_out(text, cps=38, end_pause=1.4):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        delay = 0.008 if ch in ".,;:!?" else 1.0 / cps
        time.sleep(delay)
    for _ in range(3):
        sys.stdout.write(BLINK + " " + RESET + "\b\b")
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write("\b\b" + "  " + "\b\b")
        sys.stdout.flush()
        time.sleep(0.25)
    time.sleep(end_pause)
    print()

def clear():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass

def boxify(text, width=68):
    # Wrap text to width
    words = text.split()
    lines = []
    line = []
    for w in words:
        if len(" ".join(line + [w])) <= width:
            line.append(w)
        else:
            lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    # Fit lines to width
    fitted = []
    for ln in lines:
        diff = width - len(ln)
        fitted.append(ln + (" " * diff))
    return fitted

def main():
    clear()

    # Top center title
    title = "WOODYS REEL OF ANXIETY"
    pad = max(0, (78 - len(title)) // 2)
    print(DIM + " " * pad + BOLD + title + RESET)

    # The reel itself
    top = color(5) + ".." + "+" + "-" * 72 + "+" + ".." + RESET
    bot = color(5) + ".." + "+" + "-" * 72 + "+" + ".." + RESET
    print(DIM + top + RESET)

    # Seven reels (holes rows)
    holes_row = lambda hue, i: (
        color(hue + i, bold=True) + "::  " * 6 + color(hue + i) + "::  " * 6 + RESET
    )
    for i in range(7):
        print(DIM + "::" + RESET + holes_row(i, i) + DIM + "::" + RESET)

    # The quote, boxed and typed
    quote = (
        "I'm not afraid of death; I just don't want to be in the room when it happens, "
        "preferably with the lights dimmed and a jazz trio playing—preferably not my music."
    )
    lines = boxify(quote, width=68)
    # Frame sides
    for idx, line in enumerate(lines, start=1):
        label = "Clip #42" if idx == 1 else ("Take %d" % idx if idx > 1 else "")
        if label:
            pre = f":: {label} │ "
        else:
            pre = ":: " + " " * 10 + "│ "
        post = " │" + " " * 3
        print(DIM + "::" + RESET, end="")
        print(color(idx) + pre + RESET, end="")
        print(line, end="")
        print(DIM + post + RESET)

    # Reel bottom
    print(DIM + bot + RESET)

    # Animate the reel label and the quote typing
    stop = threading.Event()
    spinner = threading.Thread(target=spin, args=(DIM + "Loading take..." + RESET, stop), daemon=True)
    spinner.start()

    # Short anticipation before the quote
    time.sleep(0.6)

    # Typing the quote itself
    print()
    type_out(color(7, bold=True) + ITALIC + BOLD + quote + RESET)

    # A little epilogue
    stop.set()
    spinner.join()
    time.sleep(0.2)
    print(DIM + "Cut! Print it with existential dread." + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + DIM + "Fine, I'll go contemplate mortality somewhere else." + RESET)