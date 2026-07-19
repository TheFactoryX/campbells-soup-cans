"""
Campbell's Soup Can #4256
Produced: 2026-07-19 13:53:22
Worker: Tencent: Hy3 (free) (tencent/hy3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A single-file, dependency-free Python "experience" that prints one
funny, neurotic, Woody-Allen-style philosophical quote using ANSI colors,
a hand-drawn ASCII box, and a tiny typing animation.
"""

import sys
import time
import shutil

# --- ANSI color helpers -------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
RED = "\033[38;5;196m"
YELLOW = "\033[38;5;227m"
CYAN = "\033[38;5;51m"
MAGENTA = "\033[38;5;201m"
GREEN = "\033[38;5;120m"

def color(text, c):
    return f"{c}{text}{RESET}"

def typing_print(text, delay=0.025, color_code=CYAN):
    """Print text with a neurotic, hesitant typing effect."""
    for ch in text:
        sys.stdout.write(color(ch, color_code))
        sys.stdout.flush()
        # Woody Allen would pause longer on existential words
        if ch in ".,;:-":
            time.sleep(delay * 4)
        else:
            time.sleep(delay)
    sys.stdout.write("\n")

def clear_line():
    sys.stdout.write("\033[2K\r")
    sys.stdout.flush()

def main():
    # Get terminal width (fallback to 80)
    try:
        width = shutil.get_terminal_size().columns
    except Exception:
        width = 80

    quote = (
        "I told my analyst that I’m not afraid of dying — "
        "I’m afraid of being biologically unfinished, like a novel "
        "God put down halfway through the dessert course."
    )
    attribution = "~ possibly Woody Allen (if he were a Python script)"

    box_width = min(width - 4, 72)
    inner_width = box_width - 4

    top = "╔" + "═" * (box_width - 2) + "╗"
    bottom = "╚" + "═" * (box_width - 2) + "╝"
    empty = "║" + " " * (box_width - 2) + "║"

    # Word-wrap the quote to fit inside the box
    words = quote.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= inner_width:
            current = (current + " " + w).strip()
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    # --- Presentation ---------------------------------------------------
    sys.stdout.write("\n")
    sys.stdout.write(color(top, MAGENTA) + "\n")
    sys.stdout.write(color(empty, MAGENTA) + "\n")
    sys.stdout.write(color("║" + " " * ((box_width - 2 - len("EXISTENTIAL MUSINGS")) // 2) +
                           BOLD + YELLOW + "EXISTENTIAL MUSINGS" + RESET +
                           " " * ((box_width - 2 - len("EXISTENTIAL MUSINGS")) // 2) + "║", MAGENTA) + "\n")
    sys.stdout.write(color(empty, MAGENTA) + "\n")

    for line in lines:
        pad = inner_width - len(line)
        sys.stdout.write(color("║  ", MAGENTA))
        # type each line with a delay
        typing_print(line, delay=0.02, color_code=CYAN)
        sys.stdout.write(color(" " * pad + "  ║", MAGENTA) + "\n")
        clear_line()

    sys.stdout.write(color(empty, MAGENTA) + "\n")
    sys.stdout.write(color("║" + " " * (box_width - 2) + "║", MAGENTA) + "\n")
    attr_pad = box_width - 4 - len(attribution)
    sys.stdout.write(color("║  " + ITALIC + DIM + GREEN + attribution + RESET +
                           " " * max(0, attr_pad) + "  ║", MAGENTA) + "\n")
    sys.stdout.write(color(bottom, MAGENTA) + "\n")

    # Final neurotic sign-off
    time.sleep(0.4)
    sys.stdout.write("\n" + color("(...still here. unfortunately.)", RED) + "\n\n")

if __name__ == "__main__":
    main()