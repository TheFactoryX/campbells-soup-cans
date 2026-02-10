"""
Campbell's Soup Can #2156
Produced: 2026-02-10 21:00:39
Worker: OpenAI: gpt-oss-20b (openai/gpt-oss-20b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A tiny, self‑contained Python program that prints a single
playful, Woody‑Allen‑style philosophical quote in a colourful,
animated box. No third‑party libraries are required.
"""

import sys
import time
import random

# ANSI colour codes
COLORS = [
    "\033[38;5;196m",  # red
    "\033[38;5;202m",  # orange
    "\033[38;5;226m",  # yellow
    "\033[38;5;118m",  # green
    "\033[38;5;123m",  # cyan
    "\033[38;5;93m",   # blue
    "\033[38;5;92m",   # violet
    "\033[38;5;224m",  # pink
    "\033[38;5;203m",  # magenta
]
RESET = "\033[0m"

# The Woody‑Allen‑style quote (one sentence only)
QUOTE = ("I realized the meaning of life is to ask the wrong questions… "
          "and the universe always replies with coffee.")

def type_text(text, delay=0.04):
    """Print text character by character, with a slight delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def colour_word(word):
    """Return the word wrapped in a random colour escape sequence."""
    return f"{random.choice(COLORS)}{word}{RESET}"

def build_coloured_sentence(sentence):
    """Apply random colour to each word in a sentence."""
    words = sentence.split()
    coloured = [colour_word(w) for w in words]
    return ' '.join(coloured)

def draw_box(lines, width):
    """Draw a simple ASCII art box around the text lines."""
    top = f"┌{'─' * width}┐"
    bottom = f"└{'─' * width}┘"
    print(top)
    for line in lines:
        print(f"│{line.ljust(width)}│")
    print(bottom)

def main():
    # Prepare the coloured sentence
    coloured_sentence = build_coloured_sentence(QUOTE)

    # Split the sentence into roughly equally sized lines (2 lines max)
    max_width = 60  # adjust visual width
    words = coloured_sentence.split()
    lines = []
    line = ""
    for w in words:
        if len(line) + len(w) + 1 > max_width:
            lines.append(line)
            line = w
        else:
            line = f"{line} {w}".strip()
    if line:
        lines.append(line)

    # Animate drawing the box and the contents
    box_width = max(len(l.replace(RESET, "").replace(COLORS[0], "").replace(COLORS[-1], "")) for l in lines)
    draw_box(lines, box_width)

    # After the box, type out the quote character by character for fun
    print("\n" + "=" * (box_width + 2))
    type_text(coloured_sentence, delay=0.03)
    print("\n" + "=" * (box_width + 2) + "\n")
    print("I hope you survived the existential coffee crisis. ☕️")

if __name__ == "__main__":
    main()