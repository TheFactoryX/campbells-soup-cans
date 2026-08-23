"""
Campbell's Soup Can #4792
Produced: 2026-08-23 15:36:04
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
======================================================================
 THE NEUROTIC PHILOSOPHER
======================================================================
 A single-file, dependency-free micro-theatre piece that delivers
 exactly ONE (1) Woody-Allen-flavoured philosophical quote, with
 considerably more production value than the thought deserves.

 Best enjoyed in a terminal >= 60 columns wide.
 Run it. Question everything. Blame the interpreter.
======================================================================
"""

import os
import sys
import time
import shutil
import textwrap

# ----------------------------------------------------------------------
# ANSI plumbing (Linux / macOS / Windows Terminal friendly)
# ----------------------------------------------------------------------
if os.name == "nt":
    os.system("")  # ancient incantation that awakens ANSI escapes on Windows

ESC     = "\x1b"
RESET   = ESC + "[0m"
BOLD    = ESC + "[1m"
DIM     = ESC + "[2m"
ITALIC  = ESC + "[3m"
YELLOW  = ESC + "[33m"
MAGENTA = ESC + "[35m"
CYAN    = ESC + "[36m"
WHITE   = ESC + "[37m"
GRAY    = ESC + "[90m"

HIDE_CURSOR = ESC + "[?25l"
SHOW_CURSOR = ESC + "[?25h"


# ----------------------------------------------------------------------
# tiny stagehand utilities
# ----------------------------------------------------------------------
def clear_screen():
    sys.stdout.write(ESC + "[2J" + ESC + "[H")
    sys.stdout.flush()


def term_width():
    return shutil.get_terminal_size((80, 24)).columns


def center(text):
    return text.center(max(term_width(), len(text)))


def pause(seconds):
    time.sleep(seconds)


def type_line(text, delay=0.02, color="", newline=True, center_it=False):
    """Classic typewriter effect."""
    out = sys.stdout
    if center_it:
        text = center(text)
    out.write(color)
    for ch in text:
        out.write(ch)
        out.flush()
        pause(delay)
    out.write(RESET)
    if newline:
        out.write("
")
    out.flush()


# ----------------------------------------------------------------------
# our troubled thinker (built programmatically so he never slouches)
# ----------------------------------------------------------------------
_FIG_CORE = [
    (24, ".-------."),
    (23, "/         \"),
    (22, "|  \\     /  |"),          # worried eyebrows
    (22, "|  (o) (o)  |"),          # enormous therapeutic glasses
    (22, "|     ^     |"),          # a nose that has smelled doom
    (22, "|  \\ ___ /  |"),         # mouth: default position = fretting
    (23, "\\         /"),
    (24, "'-------'"),
    (22, "___|     |___"),
    (21, "/   |     |   \"),
    (20, "/ /| |     | |\\ \"),
    (19, "(_/ |_|     |_| \\_)"),    # hands: permanently wringing
    (24, "(_)   (_)"),
]
FIGURE = [" " * ind + core for ind, core in _FIG_CORE]
MOUTH_ROW = 5

_MOUTH_CORES = [
    "|  \\ ___ /  |",   # mild dread
    "|   \\___/   |",   # active dread
    "|   o O o   |",   # existential gasp
]
MOUTHS = [" " * 22 + core for core in _MOUTH_CORES]

LABELS = [
    "consulting the abyss",
    "phoning my analyst",
    "re-reading my horoscope",
    "asking the universe nicely",
    "overthinking it, twice",
]
SPINNER_FRAMES = ["|", "/", "-", "\"]


def deliberate(total_seconds=3.6):
    """The thinker paces mentally: mouth wiggles, status line rotates."""
    lines_below = len(FIGURE) - MOUTH_ROW
    ticks = int(total_seconds / 0.08)
    for i in range(ticks):
        # wiggle the mouth
        mouth = MOUTHS[(i // 5) % len(MOUTHS)]
        sys.stdout.write(
            ESC + f"[{lines_below}A\r" + CYAN + mouth + RESET + ESC + f"[{lines_below}B"
        )
        # rotate the internal monologue
        label = LABELS[(i // 10) % len(LABELS)]
        frame = SPINNER_FRAMES[i % len(SPINNER_FRAMES)]
        sys.stdout.write("\r" + YELLOW + f"        {frame} {label}...{RESET}   ")
        sys.stdout.flush()
        pause(0.08)
    # restore the original fret and sweep up the status line
    sys.stdout.write(
        ESC + f"[{lines_below}A\r" + CYAN + FIGURE[MOUTH_ROW] + RESET + ESC + f"[{lines_below}B"
    )
    sys.stdout.write("\r" + " " * 70 + "\r")
    sys.stdout.flush()


# ----------------------------------------------------------------------
# the main event
# ----------------------------------------------------------------------
QUOTE = (
    "I'm not afraid of the void \u2014 "
    "I'm afraid the void isn't paying attention. "
    "Nothing stings quite like being ignored by infinity."
)
QUOTE_WIDTH = 50

ATTRIBUTION = "\u2014 a deeply worried man, clutching a sandwich he no longer trusts"

FOOTNOTE = ("* no philosophers were harmed in the making of this thought. "
            "several were mildly inconvenienced.")

WHISPER = ("psst... the void says it WAS looking. "
           "it just didn't want to make things weird.")


def boxed_typewriter(lines, width, border_color=CYAN, ink_color=WHITE, delay=0.018):
    """Reveal the quote character by character inside an elegant box."""
    out = sys.stdout
    pad = " " * max(0, (term_width() - (width + 4)) // 2)
    out.write(pad + border_color + "\u256d" + "\u2500" * (width + 2) + "\u256e" + RESET + "
")
    for ln in lines:
        out.write(pad + border_color + "\u2502 " + RESET)
        out.write(BOLD + ink_color)
        for ch in ln:
            out.write(ch)
            out.flush()
            pause(delay)
        out.write(" " * (width - len(ln)) + RESET)
        out.write(border_color + " \u2502" + RESET + "
")
    out.write(pad + border_color + "\u2570" + "\u2500" * (width + 2) + "\u256f" + RESET + "
")
    out.flush()


def twinkle_fin(repeats=6):
    word = "~  *  ~   f i n .   ~  *  ~"
    for i in range(repeats):
        style = (BOLD + YELLOW) if i % 2 == 0 else (DIM + GRAY)
        sys.stdout.write("\r" + style + center(word) + RESET)
        sys.stdout.flush()
        pause(0.4)
    sys.stdout.write("
")


# ----------------------------------------------------------------------
# curtain up
# ----------------------------------------------------------------------
def main():
    try:
        clear_screen()
        sys.stdout.write(HIDE_CURSOR)

        # ---- title card ------------------------------------------
        pause(0.3)
        type_line("*  *  *", delay=0.05, color=DIM + YELLOW, center_it=True)
        type_line("T H E   N E U R O T I C   P H I L O S O P H E R",
                  delay=0.03, color=BOLD + YELLOW, center_it=True)
        type_line("presents one (1) freshly overthought deep thought",
                  delay=0.008, color=GRAY, center_it=True)
        type_line("*  *  *", delay=0.05, color=DIM + YELLOW, center_it=True)
        pause(0.4)
        print()

        # ---- enter our thinker ------------------------------------
        for ln in FIGURE:
            sys.stdout.write(CYAN + ln + RESET + "
")
            sys.stdout.flush()
            pause(0.07)

        # ---- dramatic deliberation --------------------------------
        deliberate()
        pause(0.3)
        print()
        type_line("Ah. Yes. Here it comes...",
                  delay=0.04, color=DIM + MAGENTA, center_it=True)
        pause(0.5)
        print()

        # ---- THE QUOTE --------------------------------------------
        wrapped = textwrap.wrap(QUOTE, width=QUOTE_WIDTH)
        boxed_typewriter(wrapped, QUOTE_WIDTH)
        print()

        # ---- credits ----------------------------------------------
        type_line(ATTRIBUTION, delay=0.012, color=ITALIC + MAGENTA, center_it=True)
        pause(0.3)
        type_line(FOOTNOTE, delay=0.004, color=DIM + GRAY, center_it=True)
        print()
        pause(0.4)

        # ---- curtain ----------------------------------------------
        twinkle_fin()
        pause(0.3)
        type_line(WHISPER, delay=0.015, color=DIM + GRAY, center_it=True)
        print()

        sys.stdout.write(SHOW_CURSOR)

    except KeyboardInterrupt:
        sys.stdout.write(RESET + SHOW_CURSOR + "
")
        print("
[performance interrupted mid-crisis \u2014 which, frankly, is on brand]")
        sys.exit(130)


if __name__ == "__main__":
    main()