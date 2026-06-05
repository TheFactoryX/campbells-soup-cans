"""
Campbell's Soup Can #3861
Produced: 2026-06-05 04:47:12
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
FG_CYAN = "\033[36m"
FG_MAG  = "\033[35m"
BG_BLACK= "\033[40m"

# Woody Allen‑style quote (original)
quote = (
    "I’m not afraid of death; I just don’t want to be the punchline "
    "of a joke nobody bothered to set up."
)

def typewriter(text, delay=0.03, color=FG_CYAN):
    """Print text character‑by‑character with a slight pause."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def make_box(lines, pad=2):
    """Return a list of strings forming a colored box around the lines."""
    max_len = max(len(line) for line in lines)
    width   = max_len + 2 * pad
    horiz   = FG_MAG + BOLD + "╔" + "═" * width + "╗" + RESET
    bottom  = FG_MAG + BOLD + "╚" + "═" * width + "╝" + RESET
    boxed   = [horiz]
    for line in lines:
        spaced = " " * pad + line + " " * (width - pad - len(line) - pad)
        boxed.append(FG_MAG + BOLD + "║" + RESET + spaced + FG_MAG + BOLD + "║" + RESET)
    boxed.append(bottom)
    return boxed

def main():
    # Split quote into manageable chunks for the box (wrap at 60 chars)
    wrapped = []
    current = ""
    for word in quote.split():
        if len(current) + len(word) + 1 > 60:
            wrapped.append(current)
            current = word
        else:
            current = f"{current} {word}" if current else word
    if current:
        wrapped.append(current)

    # Print box with typewriter effect line by line
    for line in make_box(wrapped):
        # Animate the border instantly, then type the inner content
        if line.startswith(FG_MAG + BOLD + "║"):
            # It's a content line: strip the border chars and type the middle part
            inner = line[len(FG_MAG + BOLD + "║"): -len(FG_MAG + BOLD + "║")]
            sys.stdout.write(FG_MAG + BOLD + "║" + RESET)
            typewriter(inner, delay=0.04, color=FG_CYAN)
            sys.stdout.write(FG_MAG + BOLD + "║" + RESET + "\n")
        else:
            # Border lines: just print them
            print(line)
            time.sleep(0.1)

if __name__ == "__main__":
    main()