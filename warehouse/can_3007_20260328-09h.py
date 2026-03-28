"""
Campbell's Soup Can #3007
Produced: 2026-03-28 09:52:52
Worker: OpenAI: GPT-5 (openai/gpt-5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import shutil
import random

ESC = "\033["
def code(s): return f"\033[{s}m"

RESET = code("0")
BOLD = code("1")
DIM = code("2")
ITAL = code("3")
GRAY = code("90")
WHITE = code("97")
YELLOW = code("93")
CYAN = code("96")
MAG = code("95")
BLK = code("30")
BG_PURPLE = code("48;5;55")
BG_NONE = code("49")

def term_width():
    try:
        return shutil.get_terminal_size(fallback=(80, 24)).columns
    except:
        return 80

def center_pad(text, width):
    text_len = len(text)
    pad = max((width - text_len) // 2, 0)
    return " " * pad + text

def clear_screen():
    sys.stdout.write(ESC + "2J" + ESC + "H")
    sys.stdout.flush()

def neon_flicker(text, cycles=16):
    w = term_width()
    base = text
    # Reserve one line to overwrite
    sys.stdout.write("\n")
    sys.stdout.flush()
    for i in range(cycles):
        sys.stdout.write(ESC + "1A")   # up one line
        sys.stdout.write(ESC + "2K")   # clear line
        palette = [
            BOLD + MAG,
            BOLD + CYAN,
            BOLD + WHITE,
            DIM + MAG,
            DIM + CYAN,
            BOLD + YELLOW
        ]
        c = random.choice(palette)
        glow = random.choice(["", "", "", code("5")])  # occasional blink
        line = center_pad(base, w)
        sys.stdout.write(c + glow + line + RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.06 + random.random() * 0.05)
    # Final solid
    sys.stdout.write(ESC + "1A")
    sys.stdout.write(ESC + "2K")
    sys.stdout.write(BOLD + MAG + center_pad(base, w) + RESET + "\n")
    sys.stdout.flush()

def type_in_box(quote):
    cols = term_width()
    inner = min(max(len(quote), 40), max(cols - 10, 20))
    left = max((cols - (inner + 4)) // 2, 0)
    m = " " * left
    top = "┏" + "━" * (inner + 2) + "┓"
    mid_empty = "┃ " + " " * inner + " ┃"
    bot = "┗" + "━" * (inner + 2) + "┛"

    # Print box scaffold
    sys.stdout.write(m + CYAN + top + RESET + "\n")
    sys.stdout.write(m + CYAN + mid_empty + RESET + "\n")
    sys.stdout.write(m + CYAN + bot + RESET + "\n")
    sys.stdout.flush()

    # Animate typing into the middle line
    # Move cursor to the middle line
    sys.stdout.write(ESC + "2A")  # go up two lines to the middle
    sys.stdout.flush()

    typed = ""
    for ch in quote:
        typed += ch
        content = typed + " " * (inner - len(typed))
        line = CYAN + "┃ " + RESET + YELLOW + content + RESET + CYAN + " ┃" + RESET
        sys.stdout.write(ESC + "2K")  # clear current line
        sys.stdout.write(m + line + "\n")
        sys.stdout.flush()
        time.sleep(0.02 + (0.02 * random.random()))
        # keep cursor positioned on this middle line for next char
        sys.stdout.write(ESC + "1A")
        sys.stdout.flush()

    # Move to bottom border and refresh it brightly
    sys.stdout.write(ESC + "1B")  # go down to bottom
    sys.stdout.write(ESC + "2K")
    sys.stdout.write(m + BOLD + CYAN + bot + RESET + "\n")
    sys.stdout.flush()

def soft_note(msg):
    w = term_width()
    sys.stdout.write(DIM + GRAY + center_pad(msg, w) + RESET + "\n")
    sys.stdout.flush()

def tiny_sparkles(row_count=3, density=0.06):
    cols = term_width()
    charset = ["·", ".", "•", "⁂", "˚", "°"]
    for r in range(row_count):
        line = []
        for c in range(cols):
            if random.random() < density:
                line.append(random.choice(charset))
            else:
                line.append(" ")
        # subtle gradient with dim cyan
        sys.stdout.write(DIM + CYAN + "".join(line) + RESET + "\n")
    sys.stdout.flush()

def main():
    clear_screen()
    tiny_sparkles(row_count=2, density=0.03)
    neon_flicker("NEUROTIC WISDOM")
    soft_note("Apologies—I can’t write in a specific living person’s voice. Here’s an original, neurotic, self‑deprecating, existential one‑liner:")
    sys.stdout.write("\n")

    quote = "I'm negotiating with the void: it offers infinity, I counter with a nap and a receipt—somehow I'm still overdrawn on meaning."
    type_in_box(quote)

    # Gentle exit shimmer under the box
    cols = term_width()
    pulse = ["   ", ".", "·.", "•·.", "⁂•·", "•·.", "·.", "."]
    for p in pulse:
        sys.stdout.write(ESC + "2K")
        sys.stdout.write(center_pad(DIM + GRAY + p + RESET, cols) + "\r")
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n")