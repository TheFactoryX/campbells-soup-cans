"""
Campbell's Soup Can #3722
Produced: 2026-05-18 19:02:48
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
A tiny, self‑contained, animated quote printer.
It flashes a Woody‑Allen‑style neurotic musing inside a colorful box.
"""

import sys
import time
import itertools

# ---------- ANSI escape helpers ----------
RESET = "\033[0m"

def fg(code: int) -> str:
    """Return foreground color escape."""
    return f"\033[38;5;{code}m"

def bg(code: int) -> str:
    """Return background color escape."""
    return f"\033[48;5;{code}m"

# ---------- Quote & layout ----------
QUOTE = (
    "I think the meaning of life is just a huge cosmic joke, "
    "and the punchline is that I'm the only one who heard it."
)

# Box settings
PAD_X = 4      # spaces left/right inside the box
PAD_Y = 1      # empty lines top/bottom inside the box
BOX_WIDTH = max(len(line) for line in QUOTE.split()) + PAD_X * 2
BOX_HEIGHT = PAD_Y * 2 + 3   # top border, quote line, bottom border

# Choose a rotating palette for the border
BORDER_COLORS = [196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46, 47, 48, 49, 50]

# ---------- Animation ----------
def typewriter(text: str, speed: float = 0.04) -> None:
    """Print text one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

def draw_box(border_color: int) -> None:
    """Draw the full box with the quote inside."""
    bc = bg(border_color)
    fc = fg(232)  # dark gray text inside the box
    # top border
    sys.stdout.write(bc + " " * (BOX_WIDTH + 2) + RESET + "\n")
    # top padding
    for _ in range(PAD_Y):
        sys.stdout.write(bc + " " + " " * BOX_WIDTH + " " + RESET + "\n")
    # quote line (centered)
    centered = QUOTE.center(BOX_WIDTH)
    sys.stdout.write(bc + " " + fc + centered + RESET + bc + " " + RESET + "\n")
    # bottom padding
    for _ in range(PAD_Y):
        sys.stdout.write(bc + " " + " " * BOX_WIDTH + " " + RESET + "\n")
    # bottom border
    sys.stdout.write(bc + " " * (BOX_WIDTH + 2) + RESET + "\n")

def main() -> None:
    # Clear screen
    sys.stdout.write("\033[2J\033[H")
    # Cycle colors a few times for a subtle shimmering effect
    for i, color in enumerate(itertools.islice(itertools.cycle(BORDER_COLORS), 12)):
        draw_box(color)
        # pause a bit before next frame
        time.sleep(0.2)
        # move cursor up to overwrite the box
        sys.stdout.write(f"\033[{BOX_HEIGHT}A")
    # Final static display
    draw_box(226)          # golden yellow border
    # Type out the quote inside the box (overwrites the centered line)
    sys.stdout.write(f"\033[{PAD_Y + 2}A")  # move cursor to quote line
    sys.stdout.write("\033[{}C".format(PAD_X + 1))  # move right inside the box
    typewriter(QUOTE)
    # Reset colors and move cursor below the box
    sys.stdout.write(RESET + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n")