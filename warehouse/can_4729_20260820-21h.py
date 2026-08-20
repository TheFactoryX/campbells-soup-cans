"""
Campbell's Soup Can #4729
Produced: 2026-08-20 21:43:43
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import shutil

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

# A few Woody Allen‑style philosophical one‑liners (original)
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "My brain is my second favorite organ; it keeps trying to quit on me.",
    "The universe is indifferent, which explains why my sock always disappears in the dryer.",
    "I tried to meditate once, but my inner peace kept asking for a refund.",
    "If love is the answer, could you please repeat the question?",
    "Death is nature's way of telling you to slow down… preferably before it catches up.",
    "I'm not lazy, I'm in energy‑saving mode—like a phone on 1% battery.",
    "Honesty is the best policy, but insanity is a better defense."
]

def typewriter_print(text: str, delay: float = 0.04):
    """Print text one character at a time with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def get_terminal_width() -> int:
    try:
        return shutil.get_terminal_size((80, 20)).columns
    except Exception:
        return 80

def make_box(content: str, padding: int = 2, border_color: str = CYAN) -> str:
    """Return a string with the content inside a colored Unicode box."""
    lines = content.split("\n")
    max_len = max(len(line) for line in lines) if lines else 0
    width = max_len + 2 * padding
    horiz = "═" * width
    top = f"╔{horiz}╗"
    bottom = f"╚{horiz}╝"
    boxed = [border_color + top + RESET]
    for line in lines:
        padded = line.ljust(max_len)
        boxed.append(
            f"{border_color}║{RESET}"
            f"{' ' * padding}{padded}{' ' * padding}"
            f"{border_color}║{RESET}"
        )
    boxed.append(border_color + bottom + RESET)
    return "\n".join(boxed)

def main():
    quote = random.choice(QUOTES)
    # Slightly stylized quote: italic effect via ANSI (not widely supported, but we try)
    styled_quote = f"{MAGENTA}{BOLD}> {RESET}{YELLOW}\"{quote}\"{RESET}"
    box = make_box(styled_quote, padding=3, border_color=BLUE)

    # Optional: a tiny Woody Allen‑ish ASCII face above the box
    face = (
        f"{CYAN}"
        r"   _____"
        r"\n  /     \ "
        r"\n |  o o  |"
        r"\n |   ^   |"
        r"\n |  '-'  |"
        r"\n  \_____/ "
        f"{RESET}"
    )

    # Print face
    print(face)
    # Typewriter effect for the box (print line by line)
    for line in box.split("\n"):
        typewriter_print(line, delay=0.02)
    # A final pause before exit
    time.sleep(1)

if __name__ == "__main__":
    main()