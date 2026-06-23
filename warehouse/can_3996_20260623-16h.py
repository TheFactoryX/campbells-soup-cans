"""
Campbell's Soup Can #3996
Produced: 2026-06-23 16:42:06
Worker: Z.ai: GLM 5.2 (z-ai/glm-5.2)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic print routine by yours truly.
Runs on anxiety and terminal escape codes.
"""

import sys
import time
import random
import shutil

# ANSI color helpers
def fg(rgb): return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
def bg(rgb): return f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
DIM = "\033[2m"

# Palette
CREAM = (245, 235, 200)
DUSTY = (180, 150, 90)
RUST = (200, 90, 60)
MOSS = (120, 140, 90)
INK = (40, 35, 50)
PAPER = (28, 26, 38)

# The quote — pure existential flop-sweat
QUOTE = (
    "I've spent my entire life searching for meaning, and last Tuesday "
    "I found it behind the refrigerator. It was smaller than I expected, "
    "had a bit of lint on it, and frankly wasn't worth the trip."
)
ATTRIB = "— Woody Allen (probably)"

def typewriter(text, delay=0.018, color=CREAM):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0, 0.012))
    print()

def draw_frame(width):
    # A wobbly hand-drawn-ish frame
    top = "✦" + "·" * (width - 2) + "✦"
    bot = "✧" + "·" * (width - 2) + "✧"
    print(fg(DUSTY) + top + RESET)
    print(fg(DUSTY) + "│" + " " * (width - 2) + "│" + RESET)

def wrap(text, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines

def nervous_cough():
    """Nothing like a little hesitation to sell the bit."""
    for _ in range(random.randint(1, 2)):
        sys.stdout.write(DIM + fg(RUST) + " *cough*  " + RESET)
        sys.stdout.flush()
        time.sleep(0.25)
    print()

def main():
    cols = shutil.get_terminal_size((78, 20)).columns
    width = min(74, cols - 2)

    # Title card
    print()
    print(" " * ((width - 30) // 2) + BOLD + fg(MOSS) + "☕  A QUIET MOMENT OF DREAD  ☕" + RESET)
    print()

    draw_frame(width)

    # Build padded content lines
    quote_lines = wrap(QUOTE, width - 8)
    content = []
    content.append("")  # top padding
    for ln in quote_lines:
        content.append(ln)
    content.append("")
    content.append(ATTRIB)
    content.append("")  # bottom padding

    # Print each line centered within frame
    for line in content:
        left = (width - 2 - len(line)) // 2
        right = (width - 2) - len(line) - left
        if line == ATTRIB:
            inner = fg(DUSTY) + ITALIC + line + RESET
        elif line == "":
            inner = " " * (width - 2)
        else:
            inner = fg(CREAM) + line + RESET
        print(fg(DUSTY) + "│" + RESET + " " * left + inner + " " * right + fg(DUSTY) + "│" + RESET)
        time.sleep(0.12)

    print(fg(DUSTY) + "✧" + "·" * (width - 2) + "✧" + RESET)

    # The "reading aloud" effect
    print()
    time.sleep(0.4)
    nervous_cough()
    time.sleep(0.3)

    # Typewriter reprise in full color
    typewriter(QUOTE, delay=0.02, color=fg(CREAM))
    time.sleep(0.5)
    print("    " + ITALIC + fg(DUSTY) + ATTRIB + RESET)

    # Tiny signature doodle
    print()
    sig = r"""
        \\\///
       ( o o )
    --ooO-( )-Ooo---
       signed,
       a nervous process
"""
    print(DIM + fg(MOSS) + sig + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + DIM + fg(RUST) + "(He fled the room mid-sentence.)" + RESET)
        sys.exit(0)