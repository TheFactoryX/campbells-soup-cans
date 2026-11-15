"""
Campbell's Soup Can #5246
Produced: 2026-11-15 17:42:43
Worker: Particle AI: Particle-1 (free) (particle-ai/particle-1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A brief philosophical transmission.
One quote. Woody Allen energy. Mild visual fanfare.
Pure standard library, no dependencies.
"""

import sys
import time

# ---------------------------------------------------------------- terminal --
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

if sys.platform.startswith("win"):
    try:
        import ctypes
        _k = ctypes.windll.kernel32
        _k.SetConsoleMode(_k.GetStdHandle(-11), 7)  # enable ANSI on Windows
    except Exception:
        pass

E      = "\033["
RESET  = E + "0m"
BOLD   = E + "1m"
DIM    = E + "2m"


def c(n):
    return E + "38;5;%dm" % n


PURPLE = c(141)
PINK   = c(211)
CYAN   = c(81)
GOLD   = c(220)
GREY   = c(245)
LAV    = c(183)
TEAL   = c(79)
ROSE   = c(204)


def w(s=""):
    sys.stdout.write(s)
    sys.stdout.flush()


def hide_cursor():
    w(E + "?25l")


def show_cursor():
    w(E + "?25h")


def clear_line(width=80):
    w("\r" + " " * width + "\r")


# --------------------------------------------------------------- animation --
def type_out(text, color, delay=0.018, bold=True):
    pre = (BOLD if bold else "") + color
    for ch in text:
        w(pre + ch + RESET)
        time.sleep(delay)


def spinner(seconds=2.4):
    frames = ["|", "/", "-", "\\"]
    msgs = [
        "contacting the universe ...",
        "universe is not picking up ...",
        "leaving a vague, anxious voicemail ...",
        "consulting my analyst ...",
        "analyst says it's complicated ...",
        "fine. I'll figure it out myself ...",
    ]
    start = time.time()
    i = 0
    while time.time() - start < seconds:
        msg = msgs[(i // 8) % len(msgs)]
        w("\r   " + CYAN + BOLD + frames[i % 4] + RESET +
          "  " + DIM + LAV + msg + RESET + "      ")
        time.sleep(0.10)
        i += 1
    clear_line(90)


# ------------------------------------------------------------- box drawing --
def hbar(left, right, width, delay=0.006):
    palette = [141, 177, 213, 205, 199, 163, 127]
    w("  " + PURPLE + left + RESET)
    for i in range(width):
        w(c(palette[(i * 2) % len(palette)]) + "─" + RESET)
        time.sleep(delay)
    w(PURPLE + right + RESET + "\n")


def blank_row(width):
    w("  " + PURPLE + "│" + RESET + " " * width + PURPLE + "│" + RESET + "\n")


def text_row(text, width, color, delay=0.018):
    w("  " + PURPLE + "│" + RESET + "   ")
    type_out(text, color, delay)
    w(" " * (width - 3 - len(text)))
    w(PURPLE + "│" + RESET + "\n")


def sig_row(text, width, color, delay=0.020):
    pad = width - len(text) - 3
    w("  " + PURPLE + "│" + RESET + " " * pad)
    type_out(text, color, delay, bold=False)
    w("   " + PURPLE + "│" + RESET + "\n")


# -------------------------------------------------------------------- main --
def main():
    hide_cursor()

    w("\n")
    w("   " + CYAN + "~" * 3 + RESET + "  ")
    type_out("A BRIEF PHILOSOPHICAL TRANSMISSION", PINK, 0.030)
    w("  " + CYAN + "~" * 3 + RESET + "\n\n")
    time.sleep(0.20)

    spinner(2.4)
    w("\n")

    quote = [
        "I'm not afraid of death, exactly.",
        "I'm just afraid of being there when it happens",
        "and having nothing clever to say.",
    ]
    width = max(len(line) for line in quote) + 6

    hbar("╭", "╮", width)
    blank_row(width)

    shades = [LAV, TEAL, GOLD]
    for i, line in enumerate(quote):
        text_row(line, width, shades[i % len(shades)], 0.018)

    blank_row(width)
    sig_row("— W. Allen, more or less", width, GREY, 0.020)
    blank_row(width)

    hbar("╰", "╯", width)

    # little mood readout underneath
    w("\n   ")
    type_out("[ mood: existentially uneasy ]", GREY, 0.012, bold=False)
    w("   ")
    type_out("[ forecast: void, with a chance of dread ]", GREY, 0.012, bold=False)

    w("\n\n   " + DIM + ROSE + "the void has been notified." + RESET + "\n\n")
    time.sleep(0.3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        w(RESET + "\n")