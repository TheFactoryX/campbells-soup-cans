"""
Campbell's Soup Can #4730
Produced: 2026-08-20 22:45:11
Worker: Ox Alpha (stealth/ox-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANNIE HALL-UCINATIONS
~~~~~~~~~~~~~~~~~~~~~
A single-file, deeply neurotic, one-quote philosophical revue.

Pure standard library. No dependencies, no answers, no refunds.
Run it. Question everything. Especially the run instruction.
"""

import re
import sys
import time
import random
import shutil
import textwrap

# ---------------------------------------------------------------------------
#  ANSI plumbing (with a polite fallback for boring, colorless places)
# ---------------------------------------------------------------------------

TTY = sys.stdout.isatty()

RESET, BOLD, DIM, ITALIC = "\033[0m", "\033[1m", "\033[2m", "\033[3m"
YELLOW, CYAN, MAGENTA, WHITE, GRAY = ("\033[93m", "\033[96m",
                                      "\033[95m", "\033[97m", "\033[90m")

ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def paint(text, *codes):
    """Colorize text if we're on a real terminal; otherwise shrug."""
    if not TTY or not codes:
        return text
    return "".join(codes) + text + RESET


def visible_len(text):
    return len(ANSI_RE.sub("", text))


def enable_windows_ansi():
    """Gently persuade older Windows consoles to speak ANSI."""
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass  # the void does not always cooperate


def clear_screen():
    if TTY:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()


def term_width():
    return shutil.get_terminal_size((80, 24)).columns


def center(text):
    return " " * max(0, (term_width() - visible_len(text)) // 2) + text


def nap(seconds):
    time.sleep(seconds if TTY else 0)


def emit_codes(*codes):
    if TTY and codes:
        sys.stdout.write("".join(codes))


def emit_reset():
    if TTY:
        sys.stdout.write(RESET)


def type_chars(text, delay):
    """Type text with organic jitter and dramatic punctuation pauses."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch in ".,;:—?!":
            nap(delay * 7)                      # comedic timing
        else:
            nap(delay * random.uniform(0.7, 1.3))


def type_centered(text, codes=(), delay=0.015, end="
"):
    pad = " " * max(0, (term_width() - len(text)) // 2)
    emit_codes(*codes)
    sys.stdout.write(pad)
    type_chars(text, delay)
    emit_reset()
    sys.stdout.write(end)
    sys.stdout.flush()


# ---------------------------------------------------------------------------
#  The talent
# ---------------------------------------------------------------------------

GLASSES = [
    "    ╭─────────────╮" + " " * 19 + "╭─────────────╮",
    " ───┤   ◉     ◉   ├" + "─" * 19 + "┤   ◉     ◉   ├───",
    "    ╰─────────────╯" + " " * 19 + "╰─────────────╯",
    " " * 25 + "\ \ °  /",
    " " * 26 + "~~~~~",
]

QUOTE = ("I've made peace with the idea that the universe is indifferent. "
         "Indifference I can handle. What keeps me up at 3 a.m. is the "
         "possibility that it's actually paying attention — taking notes — "
         "and grading on a curve I never got to see.")

HIGHLIGHTS = {
    "indifferent": CYAN,
    "indifference": CYAN,
    "3": MAGENTA,
    "a.m": MAGENTA,
    "paying": YELLOW,
    "attention": YELLOW,
    "grading": YELLOW,
    "curve": YELLOW,
}


def word_color(word):
    return HIGHLIGHTS.get(word.strip(".,;:!?—"), WHITE)


def draw_glasses(eye="◉"):
    for line in GLASSES:
        sys.stdout.write("\r\033[K" + center(paint(line.replace("◉", eye), YELLOW)) + "
")
    sys.stdout.flush()


def blink(times=3):
    """The glasses blink. Existence persists. Regrettably."""
    if not TTY:
        return
    for _ in range(times):
        nap(0.45)
        sys.stdout.write("\033[5A")
        draw_glasses("─")
        nap(0.12)
        sys.stdout.write("\033[5A")
        draw_glasses("◉")


def anxious_spinner(phrases, frames=12, delay=0.055):
    """A spinner that looks like it's about to apologize."""
    if not TTY:
        return
    spinner = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    i = 0
    for phrase in phrases:
        for _ in range(frames):
            frame = paint(spinner[i % len(spinner)], MAGENTA, BOLD)
            sys.stdout.write("\r\033[K" + center(frame + "  " + paint(phrase, DIM)))
            sys.stdout.flush()
            i += 1
            nap(delay)
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()


def show_quote(quote):
    """The quote, delivered inside a box (for its own protection)."""
    inner = min(58, max(28, term_width() - 10))
    lines = textwrap.wrap(quote, width=inner)
    width = max(len(line) for line in lines)
    bar = "═" * (width + 2)
    indent = " " * max(0, (term_width() - (width + 4)) // 2)

    print(indent + paint("╔" + bar + "╗", YELLOW, BOLD))

    for line in lines:
        sys.stdout.write(indent + paint("║", YELLOW, BOLD) + " ")
        col = 0
        for word in line.split(" "):
            emit_codes(word_color(word))
            type_chars(word, 0.016)
            emit_reset()
            col += len(word)
            if col < width:
                sys.stdout.write(" ")
                col += 1
        sys.stdout.write(" " * (width - col + 1) + paint("║", YELLOW, BOLD) + "
")
        nap(0.04)

    print(indent + paint("╚" + bar + "╝", YELLOW, BOLD))


def blink_cursor(n=6):
    if not TTY:
        return
    for _ in range(n):
        sys.stdout.write("\r\033[K" + center(paint("▊", YELLOW)))
        sys.stdout.flush()
        nap(0.4)
        sys.stdout.write("\r\033[K" + center(" "))
        sys.stdout.flush()
        nap(0.22)
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()


# ---------------------------------------------------------------------------
#  The show
# ---------------------------------------------------------------------------

def main():
    enable_windows_ansi()
    clear_screen()

    # ---- opening credits (white on black, very serious, very neurotic) ----
    nap(0.4)
    type_centered("A NEUROTIC PICTURE", codes=(DIM,), delay=0.02)
    type_centered("presents", codes=(GRAY, ITALIC), delay=0.03)
    print()
    nap(0.3)
    type_centered("“ANNIE HALL-UCINATIONS”", codes=(BOLD, WHITE), delay=0.03)
    type_centered("a one-quote existential revue", codes=(GRAY, ITALIC), delay=0.012)
    print()
    nap(0.3)
    type_centered("starring", codes=(GRAY, ITALIC), delay=0.03)
    type_centered("ONE EXISTENTIAL QUOTE", codes=(YELLOW,), delay=0.02)
    type_centered("and", codes=(GRAY, ITALIC), delay=0.03)
    type_centered("A MAN IN SOCKS", codes=(CYAN,), delay=0.02)
    nap(0.8)

    # ---- our leading man ----
    print()
    for line in GLASSES:
        print(center(paint(line, YELLOW)))
        nap(0.1)
    blink()
    nap(0.5)
    print()

    # ---- behind the scenes of a single thought ----
    anxious_spinner([
        "silencing the rational mind…",
        "consulting the void… (the void will see you now)",
        "aligning anxieties… 87% aligned",
        "dusting off one (1) philosophical quote…",
    ])
    nap(0.3)
    type_centered("and now, the result of all that thinking:",
                  codes=(GRAY, ITALIC), delay=0.01)
    print()

    # ---- the quote ----
    show_quote(QUOTE)
    nap(0.4)
    print()
    type_centered("— overheard at 3:07 a.m., between a man and his ceiling",
                  codes=(GRAY, ITALIC), delay=0.012)
    print(center(paint("(the ceiling declined to comment.)", DIM, ITALIC)))

    # ---- curtain ----
    nap(0.7)
    print()
    blink_cursor()
    print()
    print(center(paint("— fin —", GRAY, ITALIC)))
    print()
    print(center(paint("(ctrl+c to interrupt your existential crisis — it won't help)", DIM)))
    print(center(paint("(no philosophers were harmed; one ego was mildly bruised)", DIM)))
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print()
        print(center(paint("Interrupted mid-crisis. How fitting.", MAGENTA, BOLD)))
        print(center(paint("Even your keyboard has commitment issues.", MAGENTA, ITALIC)))
        print(center(paint("The quote, like meaning, remains unavailable.", GRAY)))
        print()
        sys.exit(130)