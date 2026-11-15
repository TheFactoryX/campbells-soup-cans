"""
Campbell's Soup Can #5245
Produced: 2026-11-15 10:55:04
Worker: StepFun: Step 5 Preview (stepfun/step-5-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
The Quantum Woody Allen Experience
A single-file, pure-Python, dependency-free philosophical panic attack.
"""

import sys
import time
import shutil
import random

# ────────────────────────────────────────────────────────────────
# ANSI Colour Palette & Control Codes
# ────────────────────────────────────────────────────────────────
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
BLINK = "\033[5m"

FORE = {
    "black":   "\033[30m",
    "red":     "\033[31m",
    "green":   "\033[32m",
    "yellow":  "\033[33m",
    "blue":    "\033[34m",
    "magenta": "\033[35m",
    "cyan":    "\033[36m",
    "white":   "\033[37m",
    "gray":    "\033[90m",
    "bred":    "\033[91m",
    "bgreen":  "\033[92m",
    "byellow": "\033[93m",
    "bblue":   "\033[94m",
    "bmagenta": "\033[95m",
    "bcyan":   "\033[96m",
    "bwhite":  "\033[97m",
}


def col(text: str, color: str = "white", bold: bool = False) -> str:
    """Wrap text in an ANSI colour code."""
    prefix = FORE.get(color, FORE["white"])
    if bold:
        prefix += BOLD
    return f"{prefix}{text}{RESET}"


def cursor_up(n: int = 1) -> str:
    return f"\033[{n}A"


def cursor_down(n: int = 1) -> str:
    return f"\033[{n}B"


def cursor_forward(n: int) -> str:
    return f"\033[{n}C"


def cursor_back(n: int) -> str:
    return f"\033[{n}D"


def clear_screen() -> str:
    return "\033c"


def hide_cursor() -> str:
    return "\033[?25l"


def show_cursor() -> str:
    return "\033[?25h"


# ────────────────────────────────────────────────────────────────
# The Quote (Woody Allen-esque neurosis)
# ────────────────────────────────────────────────────────────────
QUOTE = (
    "I don't suffer from existential dread; "
    "I enjoy it—"
)
PUNCHLINE = (
    "it's the only thing that pays attention to me."
)


def print_centered(text: str, width: int = 80) -> None:
    """Print a line of text centered within a terminal width."""
    lines = text.split("\n")
    for line in lines:
        pad = max(0, (width - len(line)) // 2)
        sys.stdout.write(" " * pad + line + "\n")


def type_text(text: str, color: str = "bwhite", delay: float = 0.035) -> None:
    """Simulate a neurotic typist with a typewriter effect."""
    sys.stdout.write(FORE[color])
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        # Woody Allen-style stutter: occasional longer pause after punctuation
        if ch in ",;—":
            time.sleep(delay * 3)
        elif ch in ".?!":
            time.sleep(delay * 5)
        else:
            time.sleep(delay)
    sys.stdout.write(RESET)


def draw_breathing_brain(frames: int = 6) -> None:
    """A tiny, pulsing ASCII brain to symbolize the anxiety."""
    brain_states = [
        r"""
      (\-.
      / _`>
     (_)(
        """,
        r"""
      (\-.
      / _`>   ~
     (_)(    ~
        """,
        r"""
      (\-.
      / _`>   ~ ~
     (_)(    ~ ~
        """,
    ]
    for i in range(frames):
        sys.stdout.write(clear_screen() + hide_cursor())
        offset = i % 3
        print_centered(col("Contemplating the Void…", "gray"))
        print("\n" * 2)
        print_centered(col(brain_states[offset], "byellow"))
        time.sleep(0.35)
    sys.stdout.write(clear_screen())


def draw_progress_bar(steps: int = 30) -> None:
    """A comically over-engineered loading bar for existential dread."""
    print_centered(col("Loading Neuroses…", "bcyan"))
    for i in range(steps + 1):
        filled = i
        empty = steps - i
        bar = "█" * filled + "░" * empty
        sys.stdout.write("\r" + " " * 40 + "\r")
        sys.stdout.write(f"  [{col(bar, 'bmagenta')}] {i * 100 // steps}%")
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\n")
    sys.stdout.write(col("  ✓ Anxiety levels optimal.\n", "bgreen"))


def draw_ascii_frame(text_lines: list) -> None:
    """Wrap a block of text in a crude ASCII box."""
    width = max(len(line) for line in text_lines) + 4
    top = "╔" + "═" * width + "╗"
    bot = "╚" + "═" * width + "╝"
    print(col(top, "bblue"))
    for line in text_lines:
        pad = width - len(line) - 2
        print(col("║ ", "bblue") + line + " " * pad + col(" ║", "bblue"))
    print(col(bot, "bblue"))


def main() -> None:
    """Run the full theatrical experience."""
    try:
        # 1. Clear screen and hide cursor for clean animation
        sys.stdout.write(clear_screen() + hide_cursor())

        # 2. Pulsing brain intro
        draw_breathing_brain(frames=9)

        # 3. Loading bar to build tension
        draw_progress_bar(steps=25)

        # 4. The main event
        sys.stdout.write("\n" * 2)
        draw_ascii_frame([
            col("WOODY ALLEN PRESENTS:", "byellow"),
            "",
            col("A Brief Meditation on Mortality", "bcyan"),
            col("and Why You Should Call Your Mother", "bcyan"),
        ])
        sys.stdout.write("\n" * 2)

        # 5. Type the quote
        type_text(QUOTE, color="bwhite", delay=0.04)
        sys.stdout.write("\n")

        # 6. Pause for dramatic effect
        time.sleep(0.6)

        # 7. Punchline in a different style
        type_text("   " + PUNCHLINE, color="bmagenta", delay=0.045)
        sys.stdout.write("\n" * 2)

        # 8. Final blinking cursor for existential suspension
        for _ in range(3):
            sys.stdout.write("\r" + " " * 60 + "\r")
            sys.stdout.write(col("— still thinking…", "gray") + " " + col("_", "bred", bold=True) + BLINK)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\r" + " " * 60 + "\r")
            sys.stdout.write(col("— still thinking…", "gray") + " " + col("_", "bred", bold=True))
            sys.stdout.flush()
            time.sleep(0.3)
        sys.stdout.write("\n" * 2)
        sys.stdout.write(RESET)

    finally:
        # Always restore the cursor so the user isn't stuck in the dark
        sys.stdout.write(show_cursor() + RESET)


if __name__ == "__main__":
    main()