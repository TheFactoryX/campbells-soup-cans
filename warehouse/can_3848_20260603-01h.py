"""
Campbell's Soup Can #3848
Produced: 2026-06-03 01:47:44
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken, missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic, color‑flashed monologue that feels like a Woody Allen screenplay.
"""

import sys
import time
import shutil

# ANSI escape codes for colours and styles
RESET   = "\033[0m"
BOLD    = "\033[1m"
BLINK   = "\033[5m"
# A palette of mood‑matching colours
PALETTE = [
    "\033[38;5;196m",  # bright red
    "\033[38;5;202m",  # orange
    "\033[38;5;226m",  # yellow
    "\033[38;5;118m",  # green
    "\033[38;5;21m",   # blue
    "\033[38;5;93m",   # violet
]

# The quote (by my own imagination, not copyright)
QUOTE = ("I always think, 'Why do I have this existential dread on a Thursday night?'\n"
         "I mean, if I wanted to feel badly about the universe, I'd just watch a sci‑fi film.\n"
         "But no, I have philosophy for free, and I'm a neurotic. — Woody?"

# Build a colourful, animated box
def spin_text(text):
    """Return a cyclical colourized string."""
    t = []
    for i, ch in enumerate(text):
        color = PALETTE[i % len(PALETTE)]
        t.append(f"{color}{ch}{RESET}")
    return "".join(t)

def draw_box(lines, width):
    """Return a list of strings that form a 2‑pixel-wides coloured box around the text."""
    border = "┌" + "─" * (width-2) + "┐"
    bottom = "└" + "─" * (width-2) + "┘"
    box = [border]
    for line in lines:
        padded = line.ljust(width-4)
        box.append(f"│  {padded}  │")
    box.append(bottom)
    return box

def centre(lines, total_width):
    """Left‑pad each line to centre it in `total_width`."""
    return [line.center(total_width) for line in lines]

def main():
    # Split the quote into lines that fit in the terminal
    termwidth, _ = shutil.get_terminal_size(fallback=(80, 24))
    max_text = termwidth - 12  # margin for box and padding

    parts = []
    current = []
    for para in QUOTE.split("\n"):
        words = para.split()
        line = ""
        for w in words:
            if len(line) + len(w) + 1 > max_text:
                parts.append(" ".join(current))
                current = []
            current.append(w)
        if current:
            parts.append(" ".join(current))
            current = []

    # Animate the quoted text
    for i in range(3):  # repeat three times for a simple hand‑wave
        animated_lines = [spin_text(line) for line in parts]
        box = draw_box(animated_lines, termwidth - 4)
        centred = centre(box, termwidth)

        sys.stdout.write("\r" + "\n".join(centred))
        sys.stdout.flush()
        time.sleep(0.6 + i * 0.1)

    # Final pause
    time.sleep(2)

    # Reset terminal
    sys.stdout.write(BOLD + "\n\nAll done. Keep existential dread at a safe distance.\n" + RESET)

if __name__ == "__main__":
    main()