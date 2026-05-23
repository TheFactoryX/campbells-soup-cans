"""
Campbell's Soup Can #3763
Produced: 2026-05-23 17:17:21
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
A tiny, colorful showcase of a Woody‑Allen‑style philosophical quip.
Run it in a terminal that understands ANSI escape codes.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# Configuration – tweak these to change the look
# ----------------------------------------------------------------------
QUOTE = (
    "I think the meaning of life is to find out why we keep"
    " insisting on putting pineapples on pizza while we"
    " simultaneously fear the meaning of our own existence."
)

# Color palette (ANSI 256‑color codes)
FG_COLORS = [196, 202, 220, 46, 51, 93, 129, 201]   # bright rainbow
BG_COLOR  = 233                                        # dark gray background
TEXT_COLOR = 15                                        # bright white

# Animation settings
TYPE_SPEED = 0.04      # seconds per character
BOX_PADDING = 2        # spaces around the text inside the box
BOX_BORDER = "█"       # Unicode block for a thick border

# ----------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------
def colored(text: str, fg: int = None, bg: int = None, style: int = 0) -> str:
    """Return text wrapped in ANSI codes for given foreground/background."""
    seq = []
    if style:
        seq.append(str(style))
    if fg is not None:
        seq.append(f"38;5;{fg}")
    if bg is not None:
        seq.append(f"48;5;{bg}")
    prefix = f"\033[{';'.join(seq)}m" if seq else ""
    suffix = "\033[0m"
    return f"{prefix}{text}{suffix}"

def type_out(s: str, color_cycle):
    """Print the string with a typing animation, cycling through colors."""
    for ch in s:
        sys.stdout.write(colored(ch, fg=next(color_cycle), bg=BG_COLOR))
        sys.stdout.flush()
        time.sleep(TYPE_SPEED)
    sys.stdout.write("\n")

def make_box(lines):
    """Wrap given lines (list of strings) in a Unicode box."""
    max_len = max(len(line) for line in lines)
    horiz = BOX_BORDER * (max_len + BOX_PADDING * 2 + 2)
    top = f"{BOX_BORDER}{horiz}{BOX_BORDER}"
    bottom = top
    boxed = [top]
    for line in lines:
        padded = " " * BOX_PADDING + line.ljust(max_len) + " " * BOX_PADDING
        boxed.append(f"{BOX_BORDER}{padded}{BOX_BORDER}")
    boxed.append(bottom)
    return boxed

def rainbow_cycle():
    """Infinite generator yielding colors from FG_COLORS cyclically."""
    return itertools.cycle(FG_COLORS)

# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main():
    # Clear the screen and set a dark background
    sys.stdout.write("\033[2J\033[H")          # clear screen, move cursor home
    sys.stdout.write(colored(" " * 80, bg=BG_COLOR))  # paint background line

    # Prepare the animated quote
    color_gen = rainbow_cycle()
    type_out("\n".join(["", ""],), color_gen)   # just a little vertical spacing

    # Break the quote into manageable chunks for the box
    words = QUOTE.split()
    lines = []
    line = ""
    for w in words:
        if len(line) + len(w) + 1 > 60:
            lines.append(line)
            line = w
        else:
            line = f"{line} {w}" if line else w
    if line:
        lines.append(line)

    # Build the box and animate its appearance line‑by‑line
    boxed = make_box(lines)
    for i, line in enumerate(boxed):
        # Fade‑in style: increase brightness as we go down
        intensity = 236 + i  # a range of dark to lighter gray backgrounds
        sys.stdout.write(colored(line + "\n", fg=TEXT_COLOR, bg=intensity))
        sys.stdout.flush()
        time.sleep(0.1)

    # Final flourish: flash the border colors a couple of times
    for _ in range(3):
        flash = colored(BOX_BORDER * (len(boxed[0])-2), fg=next(color_gen))
        sys.stdout.write("\033[{}A".format(len(boxed)))   # move cursor up
        sys.stdout.write("\033[{}B".format(1))           # down to border line
        sys.stdout.write(flash + "\n")
        sys.stdout.flush()
        time.sleep(0.2)

    # Keep the screen for a moment before exiting
    time.sleep(2)

if __name__ == "__main__":
    main()