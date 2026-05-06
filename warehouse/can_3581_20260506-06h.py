"""
Campbell's Soup Can #3581
Produced: 2026-05-06 06:45:21
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, colorful, animated showcase of a Woody‑Allen‑style philosophical
quip.  No external libraries are required – just ANSI escape codes,
`time.sleep` and a splash of ASCII art.
"""

import sys
import time
import shutil

# ----------------------------------------------------------------------
# ANSI colour/formatting helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}
BG = {
    "black":  "\033[40m",
    "red":    "\033[41m",
    "green":  "\033[42m",
    "yellow": "\033[43m",
    "blue":   "\033[44m",
    "magenta":"\033[45m",
    "cyan":   "\033[46m",
    "white":  "\033[47m",
}

def color(text: str, *, fg: str = None, bg: str = None, bold: bool = False) -> str:
    """Wrap `text` in ANSI escape sequences."""
    parts = []
    if bold:
        parts.append(BOLD)
    if fg:
        parts.append(FG.get(fg, ""))
    if bg:
        parts.append(BG.get(bg, ""))
    parts.append(text)
    parts.append(RESET)
    return "".join(parts)

# ----------------------------------------------------------------------
# The witty Woody‑Allen‑style quote
# ----------------------------------------------------------------------
QUOTE = (
    "I’m not afraid of death; "
    "I’m just terrified that I’ll miss the final act of the "
    "universe’s absurd sitcom."
)

# ----------------------------------------------------------------------
# Simple animation helpers
# ----------------------------------------------------------------------
def clear_screen():
    """Clear the terminal."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def typewriter(txt: str, delay: float = 0.04):
    """Print `txt` one character at a time (typewriter effect)."""
    for ch in txt:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def bounce_box(lines, *, width=60, cycles=3, speed=0.07):
    """
    Animate a rectangular box that bounces left‑to‑right.
    """
    term_width = shutil.get_terminal_size((80, 20)).columns
    max_offset = max(0, term_width - width - 2)   # 2 for borders

    for _ in range(cycles):
        # left → right
        for offset in range(max_offset + 1):
            draw_box(lines, width=width, offset=offset)
            time.sleep(speed)
        # right → left
        for offset in range(max_offset, -1, -1):
            draw_box(lines, width=width, offset=offset)
            time.sleep(speed)

def draw_box(lines, *, width=60, offset=0):
    """Render the box at a given horizontal offset."""
    clear_screen()
    spacer = " " * offset
    top = spacer + color("╔" + "═" * width + "╗", fg="cyan")
    bottom = spacer + color("╚" + "═" * width + "╝", fg="cyan")
    middle = []
    for line in lines:
        padded = line.center(width)
        middle.append(spacer + color("║", fg="cyan") + padded + color("║", fg="cyan"))
    sys.stdout.write("\n".join([top] + middle + [bottom]))
    sys.stdout.flush()

# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main():
    # Prepare the quote lines with some colour flair
    colored_quote = [
        color("  ", fg="magenta") + color("“", fg="yellow", bold=True) + " " + 
        color(QUOTE, fg="white", bold=True) + " " + 
        color("”", fg="yellow", bold=True)
    ]

    # Show a gentle typewriter intro
    clear_screen()
    intro = color(">>>", fg="green", bold=True) + " A moment of existential contemplation..."
    typewriter(intro, delay=0.03)
    time.sleep(0.6)

    # Animate the quote inside a bouncy cyan box
    bounce_box(colored_quote, width=70, cycles=2, speed=0.04)

    # End with a calming fade‑out
    time.sleep(0.8)
    clear_screen()
    farewell = color("—", fg="red", bold=True) + "  Thanks for watching the universe's sitcom."
    typewriter(farewell, delay=0.03)

if __name__ == "__main__":
    main()